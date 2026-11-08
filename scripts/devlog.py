#!/usr/bin/env python3
"""dev-log 파이프라인.

PR 하나를 받아 (1) 변경점을 요약해 마크다운 기록을 만들고 (2) INDEX를 갱신하고
(3) 노션 페이지에 블록을 붙이고 (4) X에 1줄 요약을 올립니다.

`scan` 은 한 발 더 나아가 내 계정의 모든 레포(소유 + 기여)에서 최근 머지된 PR을 찾아
아직 기록되지 않은 것만 위 파이프라인에 태웁니다. 정기 실행(cron)이 이것을 씁니다.

표준 라이브러리만 씁니다. 설치할 패키지가 없습니다.

    python3 scripts/devlog.py entry  --repo Team-B1ND/dodamdodam-web --pr 223
    python3 scripts/devlog.py entry  --from-json fixture.json --dry-run
    python3 scripts/devlog.py scan   --days 14 --dry-run
    python3 scripts/devlog.py scan   --days 14 --publish all
    python3 scripts/devlog.py notion --file logs/2026/2026-11-08-pr-223.md
    python3 scripts/devlog.py tweet  --file logs/2026/2026-11-08-pr-223.md

환경 변수
    GITHUB_TOKEN     PR을 읽을 때 (없으면 익명, 공개 레포만)
    DEVLOG_USER      (선택) 스캔 대상 계정. 기본값은 GITHUB_REPOSITORY_OWNER → 토큰 주인
    LLM_API_KEY      (선택) 요약을 LLM으로. 없으면 diff 기반 자동 요약
    LLM_MODEL        (선택) 기본 gemini-2.0-flash
    NOTION_TOKEN     Notion 내부 통합 토큰
    NOTION_PAGE_ID   기록을 붙일 페이지 id
    X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET
    GITHUB_STEP_SUMMARY  (있으면) 스캔 결과 요약을 Actions 화면에 남긴다
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs"
INDEX_FILE = LOG_DIR / "INDEX.md"
GITHUB_API = "https://api.github.com"
MAX_FILES = 300
MAX_PATCH_CHARS = 24000

# ---------------------------------------------------------------- 공통 유틸


def env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name, "").strip()
    return value or default


def http_json(method: str, url: str, token: str | None = None, body=None, headers=None):
    """JSON 요청 한 번. (status, parsed) 를 돌려준다. 실패는 예외."""
    data = None
    hdrs = {"Accept": "application/json", "User-Agent": "dev-log-pipeline"}
    if body is not None:
        data = json.dumps(body).encode()
        hdrs["Content-Type"] = "application/json"
    if token:
        hdrs["Authorization"] = f"Bearer {token}"
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8", "replace")
            return resp.status, (json.loads(raw) if raw.strip() else {})
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"{method} {url} → HTTP {exc.code}: {raw[:400]}") from None


def github_api(path: str, token: str | None = None, method: str = "GET", body=None):
    status, payload = http_json(method, GITHUB_API + path, token, body,
                                {"Accept": "application/vnd.github+json",
                                 "X-GitHub-Api-Version": "2022-11-28"})
    return payload


def slugify(text: str, limit: int = 40) -> str:
    text = unicodedata.normalize("NFKC", text).strip()
    text = re.sub(r"^(feat|fix|refactor|chore|docs|style|test|build|perf|merge|design|hotfix)"
                  r"(\([^)]*\))?\s*:?\s*", "", text, flags=re.I)
    text = re.sub(r"^[a-z]+/#?\d+-", "", text, flags=re.I)     # feature/#222-change-password
    text = re.sub(r"[^0-9A-Za-z가-힣]+", "-", text).strip("-").lower()
    return (text[:limit].rstrip("-") or "entry")


# ---------------------------------------------------------------- GitHub에서 PR 읽기


def fetch_pr(repo: str, number: str, token: str | None) -> dict:
    pr = github_api(f"/repos/{repo}/pulls/{number}", token)
    files, page = [], 1
    while len(files) < MAX_FILES:
        batch = github_api(f"/repos/{repo}/pulls/{number}/files?per_page=100&page={page}", token)
        if not batch:
            break
        files.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    commits = github_api(f"/repos/{repo}/pulls/{number}/commits?per_page=100", token)
    return {
        "repo": repo,
        "number": str(pr.get("number", number)),
        "title": pr.get("title") or "",
        "body": pr.get("body") or "",
        "url": pr.get("html_url") or f"https://github.com/{repo}/pull/{number}",
        "author": (pr.get("user") or {}).get("login") or "",
        "merged_at": pr.get("merged_at") or "",
        "base": (pr.get("base") or {}).get("ref") or "",
        "head": (pr.get("head") or {}).get("ref") or "",
        "additions": pr.get("additions", 0),
        "deletions": pr.get("deletions", 0),
        "changed_files": pr.get("changed_files", len(files)),
        "files": [{"filename": f.get("filename", ""),
                   "status": f.get("status", ""),
                   "additions": f.get("additions", 0),
                   "deletions": f.get("deletions", 0),
                   "patch": f.get("patch") or ""} for f in files],
        "commits": [{"sha": (c.get("sha") or "")[:7],
                     "message": ((c.get("commit") or {}).get("message") or "").splitlines()[0][:160]}
                    for c in commits],
    }


# ---------------------------------------------------------------- 여러 레포 스캔

# develop→main 처럼 머지 커밋만 있는 PR은 기록 가치가 낮아 기본으로 건너뛴다.
TRIVIAL_TITLE = re.compile(r"^(merge\b|develop$|dev$|main$|master$|release$|revert\b)", re.I)


def is_trivial_merge(title: str) -> bool:
    text = re.sub(r"^\[[^\]]*\]\s*", "", title or "").strip().lower()
    return bool(TRIVIAL_TITLE.match(text))


def resolve_login(token: str | None) -> str:
    """스캔 대상 계정. Actions 설치 토큰은 /user 를 못 읽으므로 환경변수를 먼저 본다."""
    for name in ("DEVLOG_USER", "GITHUB_REPOSITORY_OWNER"):
        value = env(name)
        if value and not value.endswith("[bot]"):
            return value
    try:
        payload = github_api("/user", token)
        if payload.get("login"):
            return payload["login"]
    except RuntimeError:
        pass
    try:
        payload = github_api("/installation/repositories?per_page=1", token)
        repos = payload.get("repositories") or []
        if repos:
            owner = (repos[0].get("owner") or {}).get("login")
            if owner:
                return owner
    except RuntimeError:
        pass
    raise RuntimeError("GitHub 로그인을 확인하지 못했습니다. --user lee090626 처럼 지정해 주세요.")


def _paged(path_template: str, token: str | None, limit: int = 500) -> list[dict]:
    """{page} 자리에 페이지 번호를 넣어 목록을 끝까지 읽는다."""
    items: list[dict] = []
    page = 1
    while len(items) < limit:
        payload = github_api(path_template.format(page=page), token)
        batch = payload.get("repositories") if isinstance(payload, dict) else payload
        batch = batch or []
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


def list_owned_repos(login: str, token: str | None) -> list[str]:
    """계정이 소유한 레포. 설치 토큰이면 /user/repos 가 막혀 대체 경로를 쓴다."""
    templates = (
        "/user/repos?affiliation=owner&per_page=100&sort=pushed&page={page}",
        f"/users/{login}/repos?per_page=100&type=owner&page={{page}}",
        "/installation/repositories?per_page=100&page={page}",
    )
    for template in templates:
        try:
            repos = _paged(template, token)
        except RuntimeError:
            continue
        names = sorted({repo["full_name"] for repo in repos
                        if (repo.get("owner") or {}).get("login") == login
                        and not repo.get("archived") and repo.get("full_name")})
        if names:
            return names
    return []


def search_merged_prs(login: str, since: str, token: str | None, limit: int = 300) -> list[dict]:
    """내가 author 인 머지 PR 전체 (소유·기여 레포 무관)."""
    query = urllib.parse.quote(f"is:pr is:merged author:{login} merged:>={since}", safe="")
    items: list[dict] = []
    page = 1
    while len(items) < limit:
        payload = github_api(
            f"/search/issues?q={query}&per_page=100&page={page}&sort=updated&order=asc", token)
        batch = payload.get("items") or []
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    found = []
    for item in items:
        repo = (item.get("repository_url") or "").split("/repos/")[-1]
        if "/" not in repo:
            continue
        found.append({"repo": repo, "number": str(item.get("number")),
                      "title": item.get("title") or "", "url": item.get("html_url") or "",
                      "merged_at": item.get("closed_at") or ""})
    return found


def repo_merged_prs(repo: str, login: str, since: str, token: str | None) -> list[dict]:
    """레포 하나의 최근 머지 PR 중 내가 author 인 것 (검색 API 보완·대체)."""
    pulls = github_api(
        f"/repos/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page=100", token)
    found = []
    for pull in pulls or []:
        merged_at = pull.get("merged_at") or ""
        if not merged_at or merged_at[:10] < since:
            continue
        if login and (pull.get("user") or {}).get("login") != login:
            continue
        found.append({"repo": repo, "number": str(pull.get("number")),
                      "title": pull.get("title") or "", "url": pull.get("html_url") or "",
                      "merged_at": merged_at})
    return found


def collect_merged_prs(login: str, since: str, token: str | None, owned: list[str]):
    """검색 API + 소유 레포 직접 조회를 합쳐 중복을 제거한다."""
    found: dict[tuple[str, str], dict] = {}
    problems: list[str] = []
    try:
        for pr in search_merged_prs(login, since, token):
            found[(pr["repo"].lower(), pr["number"])] = pr
    except RuntimeError as exc:
        problems.append(f"검색 API 실패: {exc}")
    for repo in owned:
        try:
            for pr in repo_merged_prs(repo, login, since, token):
                found.setdefault((pr["repo"].lower(), pr["number"]), pr)
        except RuntimeError as exc:
            problems.append(f"{repo} 조회 실패: {exc}")
    return sorted(found.values(), key=lambda pr: pr.get("merged_at") or ""), problems


def existing_entries() -> set[tuple[str, str]]:
    """이미 기록된 (레포, PR번호). front-matter 의 project/pr 또는 source URL 로 판별."""
    known: set[tuple[str, str]] = set()
    if not LOG_DIR.exists():
        return known
    for path in LOG_DIR.rglob("*.md"):
        if path.name == "INDEX.md":
            continue
        try:
            head = path.read_text(encoding="utf-8")[:4000]
        except OSError:
            continue
        project = re.search(r"^project:\s*(.+)$", head, re.M)
        source = re.search(r"^source:\s*(\S+)$", head, re.M)
        number = re.search(r"^pr:\s*(\d+)\s*$", head, re.M)
        repo = project.group(1).strip() if project else ""
        num = number.group(1) if number else ""
        if (not repo or not num) and source:
            match = re.search(r"github\.com/([^/]+/[^/]+)/pull/(\d+)", source.group(1))
            if match:
                repo = repo or match.group(1)
                num = num or match.group(2)
        if repo and num:
            known.add((repo.lower(), num))
    return known


def entry_path(date: str, number: str, title: str, repo: str) -> Path:
    """저장 경로. 같은 날 같은 번호의 다른 레포 PR과 부딪히면 레포 이름을 덧붙인다."""
    year_dir = LOG_DIR / date[:4]
    stem = f"{date}-pr-{number}-{slugify(title)}"
    candidate = year_dir / f"{stem}.md"
    if candidate.exists():
        head = candidate.read_text(encoding="utf-8")[:4000]
        project = re.search(r"^project:\s*(.+)$", head, re.M)
        number_in = re.search(r"^pr:\s*(\d+)\s*$", head, re.M)
        same = (project and number_in
                and project.group(1).strip().lower() == repo.lower()
                and number_in.group(1) == str(number))
        if not same:
            candidate = year_dir / f"{stem}-{slugify(repo.split('/')[-1], 24)}.md"
    return candidate


# ---------------------------------------------------------------- 기술 판별

EXT_TECH = {
    ".ts": "TypeScript", ".tsx": "React", ".js": "JavaScript", ".jsx": "React",
    ".java": "Java", ".kt": "Kotlin", ".py": "Python", ".go": "Go", ".rs": "Rust",
    ".css": "CSS", ".scss": "SCSS", ".html": "HTML", ".vue": "Vue", ".svelte": "Svelte",
    ".sql": "SQL", ".sh": "Shell", ".yml": "GitHub Actions", ".yaml": "GitHub Actions",
    ".json": "JSON", ".md": "문서",
}
PATH_TECH = [
    ("package.json", "npm"), ("vite.config", "Vite"), ("next.config", "Next.js"),
    ("tsconfig", "TypeScript"), ("tailwind", "Tailwind"), ("dockerfile", "Docker"),
    ("build.gradle", "Gradle"), ("pom.xml", "Maven"), ("application.yml", "Spring Boot"),
    ("@testing-library", "Testing Library"), ("vitest", "Vitest"), ("jest", "Jest"),
]


def detect_tech(files: list[dict]) -> list[str]:
    found: list[str] = []
    for f in files:
        name = f["filename"].lower()
        for key, tech in PATH_TECH:
            if key in name:
                found.append(tech)
        ext = os.path.splitext(name)[1]
        tech = EXT_TECH.get(ext)
        if tech and tech not in ("문서", "JSON"):
            found.append(tech)
    seen, ordered = set(), []
    for tech in found:
        if tech not in seen:
            seen.add(tech)
            ordered.append(tech)
    return ordered[:8]


def file_groups(files: list[dict], limit: int = 8) -> list[str]:
    """변경이 큰 파일부터 사람이 읽을 수 있는 한 줄로."""
    rows = sorted(files, key=lambda f: -(f["additions"] + f["deletions"]))[:limit]
    lines = []
    for f in rows:
        status = {"added": "추가", "removed": "삭제", "renamed": "이름변경"}.get(f["status"], "수정")
        lines.append(f"`{f['filename']}` — {status} +{f['additions']} / -{f['deletions']}")
    return lines


# ---------------------------------------------------------------- 요약 (LLM 또는 자동)


def llm_available() -> bool:
    return bool(env("LLM_API_KEY"))


def llm_summary(pr: dict, tech: list[str]) -> dict | None:
    """LLM으로 문제/원인/해결/포인트를 뽑는다. 실패하면 None → 자동 요약으로 폴백."""
    key = env("LLM_API_KEY")
    if not key:
        return None
    model = env("LLM_MODEL", "gemini-2.0-flash")
    patch_text = []
    budget = MAX_PATCH_CHARS
    for f in pr["files"]:
        if not f["patch"]:
            continue
        chunk = f"### {f['filename']}\n{f['patch']}\n"
        if len(chunk) > budget:
            chunk = chunk[:budget] + "\n…(생략)\n"
        patch_text.append(chunk)
        budget -= len(chunk)
        if budget <= 0:
            break
    prompt = f"""너는 시니어 프론트엔드 개발자의 이력서 작성을 돕는다.
아래 PR을 읽고, 채용 담당자가 읽을 기록으로 정리해라. 사실만 쓰고 추측은 쓰지 마라.

저장소: {pr['repo']}
PR 제목: {pr['title']}
PR 본문:
{(pr['body'] or '(없음)')[:3000]}

변경 파일:
{chr(10).join(f"- {f['filename']} ({f['status']}, +{f['additions']}/-{f['deletions']})" for f in pr['files'][:40])}

커밋:
{chr(10).join(f"- {c['message']}" for c in pr['commits'][:20])}

diff:
{''.join(patch_text)}

다음 JSON만 출력해라(설명 문장 없이):
{{
  "title": "무엇을 했는지 한 줄 (한국어, 60자 이내)",
  "overview": "이 변경이 무엇이고 왜 필요했는지 2~3문장",
  "features": ["이번 변경이 만든/고친 동작 2~4개"],
  "problem": "해결한 문제. 증상 기준으로",
  "cause": "원인. 코드/구조/설정 중 어느 경계에서 어긋났는지. 근거가 diff에 없으면 \"diff에서 확인되지 않음\"",
  "solution": "어떻게 풀었는지. 무엇을 바꿨고 무엇을 고정했는지",
  "lesson": "다음에 같은 상황에서 다르게 할 것 한 문장",
  "achievements": ["측정 가능한 결과 1~3개"]
}}"""
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{urllib.parse.quote(model)}:generateContent?key={urllib.parse.quote(key)}")
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"}}
    try:
        _, payload = http_json("POST", url, None, body)
        text = payload["candidates"][0]["content"]["parts"][0]["text"]
        text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
        data = json.loads(text)
        return data if isinstance(data, dict) else None
    except Exception as exc:                                  # noqa: BLE001
        print(f"[devlog] LLM 요약 실패, 자동 요약으로 대체: {exc}", file=sys.stderr)
        return None


CONVENTIONAL = r"^(feat|fix|refactor|chore|docs|style|test|build|perf|merge|design|hotfix|release)(\([^)]*\))?[:/]?\s*"


def human_title(pr: dict) -> str:
    """PR 제목이 `fix/#217-team-detail-dark-back` 같은 슬러그면 커밋 제목을 쓴다."""
    title = re.sub(r"\[[^\]]*\]", "", pr["title"] or "").strip()
    has_korean = bool(re.search(r"[가-힣]", title))
    if not has_korean or not re.search(r"\s", title):
        for commit in pr.get("commits", []):
            msg = commit["message"].strip()
            if msg and not re.match(r"^merge", msg, re.I):
                cleaned = re.sub(CONVENTIONAL, "", msg, flags=re.I).strip()
                if cleaned:
                    return cleaned
    return re.sub(CONVENTIONAL, "", title, flags=re.I).strip() or pr["title"]


def clean_body(body: str) -> str:
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"<[^>]+>", "", body)
    return body.replace("\r\n", "\n").replace("\r", "\n")


def auto_summary(pr: dict, tech: list[str]) -> dict:
    """키가 없거나 LLM이 실패했을 때: diff와 PR 본문에서 사실만 뽑는다."""
    body = clean_body(pr["body"] or "").strip()
    first_para = ""
    for block in re.split(r"\n\s*\n", body):
        cleaned = re.sub(r"^[#>*\-\s]+", "", block).strip()
        if len(cleaned) < 40:
            continue
        if cleaned.startswith(("- [", "|", "```")):
            continue
        first_para = re.sub(r"\s+", " ", cleaned)[:600]
        break
    commits = [c["message"] for c in pr["commits"]
               if not re.match(r"^merge", c["message"], re.I)][:4]
    return {
        "title": human_title(pr)[:90],
        "overview": (f"{pr['repo']}의 변경입니다. 파일 {pr['changed_files']}개 "
                     f"(+{pr['additions']}/-{pr['deletions']}), 커밋 {len(pr['commits'])}개. "
                     "아래 '문제'는 PR 본문에서 그대로 발췌했습니다."),
        "features": commits,
        "problem": first_para or "PR 본문에 문제 설명이 없습니다. 아래 변경 파일과 커밋으로 확인합니다.",
        "cause": "**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)",
        "solution": "변경 파일: " + ", ".join(f["filename"] for f in pr["files"][:6]),
        "lesson": "",
        "achievements": [f"변경 파일 {pr['changed_files']}개, +{pr['additions']} / -{pr['deletions']}",
                         f"커밋 {len(pr['commits'])}개"],
        "_auto": True,
    }


# ---------------------------------------------------------------- 마크다운 렌더


def render_entry(pr: dict, summary: dict, tech: list[str], date: str, generated: str) -> str:
    title = summary.get("title") or pr["title"]
    files_line = file_groups(pr["files"], 10)
    commits = pr["commits"][:10]
    features = [f for f in summary.get("features", []) if f]
    achievements = [a for a in summary.get("achievements", []) if a]
    tags = ", ".join(tech) if tech else ""

    parts: list[str] = []
    parts.append("---")
    parts.append(f"project: {pr['repo']}")
    parts.append(f"source: {pr['url']}")
    parts.append(f"date: {date}")
    parts.append(f"pr: {pr['number']}")
    parts.append(f"author: {pr['author']}")
    parts.append(f"tags: [{tags}]")
    parts.append(f"generated: {generated}")
    if pr.get("merged_at"):
        parts.append(f"merged_at: {pr['merged_at']}")
    parts.append("---")
    parts.append("")
    parts.append(f"# {title}")
    parts.append("")
    parts.append("## 개요")
    parts.append("")
    parts.append(summary.get("overview") or "")
    parts.append("")
    if features:
        parts.append("## 주요 기능 / 변경 사항")
        parts.append("")
        for item in features:
            parts.append(f"- {item}")
        parts.append("")
    parts.append("## 사용 기술")
    parts.append("")
    parts.append(" · ".join(f"`{t}`" for t in tech) if tech else "- (diff에서 판별되지 않음)")
    parts.append("")
    if files_line:
        parts.append("## 변경 파일")
        parts.append("")
        for line in files_line:
            parts.append(f"- {line}")
        parts.append("")
    parts.append("## 트러블슈팅")
    parts.append("")
    parts.append("### 1. " + (title if not summary.get("_auto") else "이번 변경에서 해결한 것"))
    parts.append("")
    parts.append("**문제**")
    parts.append(summary.get("problem") or "")
    parts.append("")
    parts.append("**원인**")
    parts.append(summary.get("cause") or "")
    parts.append("")
    parts.append("**해결**")
    parts.append(summary.get("solution") or "")
    parts.append("")
    if summary.get("lesson"):
        parts.append("**배운 점**")
        parts.append(summary["lesson"])
        parts.append("")
    if commits:
        parts.append("## 커밋")
        parts.append("")
        for c in commits:
            parts.append(f"- `{c['sha']}` {c['message']}")
        parts.append("")
    parts.append("## 성과 및 배운 점")
    parts.append("")
    for a in achievements or ["(기록 없음)"]:
        parts.append(f"- {a}")
    parts.append("")
    if generated == "auto":
        parts.append("---")
        parts.append("")
        parts.append(f"> 자동 생성: PR [{pr['repo']}#{pr['number']}]({pr['url']}) · "
                     f"`scripts/devlog.py entry`")
        parts.append("")
    return "\n".join(parts)


# ---------------------------------------------------------------- INDEX 갱신


def update_index(date: str, project: str, label: str, rel_path: str) -> None:
    """INDEX.md 표의 마지막 행 뒤에 한 줄 추가한다."""
    if not INDEX_FILE.exists():
        return
    lines = INDEX_FILE.read_text(encoding="utf-8").splitlines()
    entry = (f"| {date} | {project.split('/')[-1]} | {label} | "
             f"[{Path(rel_path).name}]({rel_path}) |")
    last_row = max((i for i, line in enumerate(lines) if line.strip().startswith("|")), default=None)
    if last_row is None:
        lines += ["", "| 날짜 | 프로젝트 | 구분 | 기록 |",
                  "| --- | --- | --- | --- |", entry]
    else:
        lines.insert(last_row + 1, entry)
    INDEX_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- entry 커맨드


def build_entry(pr: dict, no_llm: bool = False, date: str | None = None) -> tuple[str, str, str]:
    """(markdown, 날짜, 제목). LLM 키가 없거나 실패하면 자동 요약으로."""
    date = date or (pr.get("merged_at") or "")[:10] or time.strftime("%Y-%m-%d")
    tech = detect_tech(pr["files"])
    summary = None if no_llm else llm_summary(pr, tech)
    if not summary:
        summary = auto_summary(pr, tech)
    return (render_entry(pr, summary, tech, date, "auto"), date,
            summary.get("title") or pr["title"])


def save_entry(path: Path, markdown: str, date: str, repo: str, number: str) -> None:
    """파일을 쓰고 INDEX에 한 줄 붙인다."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown, encoding="utf-8")
    update_index(date, repo, f"PR #{number} · 자동", path.relative_to(LOG_DIR).as_posix())


def cmd_entry(args) -> int:
    token = env("GITHUB_TOKEN")
    if args.from_json:
        pr = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
    else:
        if not args.repo or not args.pr:
            print("--repo 와 --pr 이 필요합니다.", file=sys.stderr)
            return 2
        pr = fetch_pr(args.repo, str(args.pr), token)

    markdown, date, title = build_entry(pr, no_llm=args.no_llm, date=args.date)
    target = entry_path(date, pr["number"], title, pr["repo"])

    if args.dry_run:
        print(markdown)
        print(f"\n[dry-run] 저장 예정 경로: {target.relative_to(ROOT)}", file=sys.stderr)
        return 0

    if target.exists():
        print(f"[devlog] 이미 기록되어 있습니다: {target.relative_to(ROOT)}")
        return 0

    save_entry(target, markdown, date, pr["repo"], pr["number"])
    print(f"[devlog] 기록 생성: {target.relative_to(ROOT)}")
    return 0


# ---------------------------------------------------------------- scan 커맨드


def write_step_summary(lines: list[str]) -> None:
    """Actions 화면($GITHUB_STEP_SUMMARY)에 남길 요약. 없으면 조용히 넘진다."""
    path = env("GITHUB_STEP_SUMMARY")
    if not path:
        return
    try:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    except OSError:
        pass


def cmd_scan(args) -> int:
    """내 모든 레포에서 최근 머지된 PR을 찾아, 아직 기록되지 않은 것만 기록·전파한다."""
    token = env("GITHUB_TOKEN")
    login = args.user or resolve_login(token)
    days = max(int(args.days), 1)
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    publish = (args.publish or "none").lower()
    if publish not in ("all", "notion", "x", "none"):
        print(f"--publish 는 all | notion | x | none 중 하나입니다. (받은 값: {publish})", file=sys.stderr)
        return 2
    do_notion = publish in ("all", "notion")
    do_x = publish in ("all", "x")

    owned = list_owned_repos(login, token)
    prs, problems = collect_merged_prs(login, since, token, owned)
    known = existing_entries()
    by_repo: dict[str, int] = {}
    for pr in prs:
        by_repo[pr["repo"]] = by_repo.get(pr["repo"], 0) + 1

    pending: list[dict] = []
    already, merges = 0, 0
    for pr in prs:
        if (pr["repo"].lower(), pr["number"]) in known:
            already += 1
            continue
        if not args.include_merges and is_trivial_merge(pr["title"]):
            merges += 1
            continue
        pending.append(pr)

    overflow = pending[args.limit:]
    if overflow:
        pending = pending[:args.limit]

    print(f"[devlog] 대상: {login} · 최근 {days}일 (merged >= {since})")
    print(f"[devlog] 소유 레포 {len(owned)}개 · 머지 PR {len(prs)}건 → 기록 대상 {len(pending)}건 "
          f"(이미 기록 {already} · 머지커밋 {merges}"
          + (f" · 상한 넘어 다음으로 {len(overflow)}" if overflow else "") + ")")
    if by_repo:
        ordered = sorted(by_repo.items(), key=lambda item: (-item[1], item[0]))
        print("[devlog] 기여 레포: " + ", ".join(f"{name}({count})" for name, count in ordered))
    for pr in pending:
        print(f"  · {pr['repo']}#{pr['number']} ({pr['merged_at'][:10]}) {pr['title'][:70]}")

    created: list[Path] = []
    failures: list[str] = []
    notes: list[str] = []
    published = {"notion": 0, "x": 0}

    for index, pr in enumerate(pending, 1):
        label = f"{pr['repo']}#{pr['number']}"
        try:
            detail = fetch_pr(pr["repo"], pr["number"], token)
        except RuntimeError as exc:
            failures.append(f"{label} PR 조회 실패: {exc}")
            print(f"[devlog] {label} 조회 실패: {exc}", file=sys.stderr)
            continue
        markdown, date, title = build_entry(detail, no_llm=args.no_llm)
        target = entry_path(date, detail["number"], title, detail["repo"])
        if args.dry_run:
            if index == 1:
                print(f"\n[dry-run] {label} → {target.relative_to(ROOT)}")
                print(markdown)
            continue
        save_entry(target, markdown, date, detail["repo"], detail["number"])
        created.append(target)
        print(f"[devlog] 기록 생성: {target.relative_to(ROOT)}")
        if do_notion:
            try:
                ok, message = publish_notion(target)
                print(message)
                published["notion"] += 1 if ok else 0
            except RuntimeError as exc:
                problems.append(f"{label} 노션 전파 실패: {exc}")
        if do_x:
            if published["x"] >= args.max_publish:
                notes.append(f"{label}: X 전파 상한({args.max_publish}건)에 걸려 트윗 없이 기록만 남김")
                continue
            try:
                ok, message = publish_tweet(target)
                print(message)
                published["x"] += 1 if ok else 0
            except RuntimeError as exc:
                problems.append(f"{label} X 전파 실패: {exc}")

    if args.dry_run:
        print(f"\n[dry-run] 예정 {len(pending)}건. 파일·노션·X 모두 쓰지 않았습니다.")
    else:
        print(f"[devlog] 스캔 완료: 기록 {len(created)}건 · 노션 {published['notion']}건 "
              f"· X {published['x']}건")
    for problem in problems:
        print(f"[devlog] 경고: {problem}", file=sys.stderr)
    for note in notes:
        print(f"[devlog] 참고: {note}")
    for failure in failures:
        print(f"[devlog] 실패: {failure}", file=sys.stderr)

    lines = ["### dev-log scan", "",
             f"- 계정: `{login}` · 최근 {days}일",
             f"- 소유 레포 {len(owned)}개 · 머지 PR {len(prs)}건",
             f"- 새 기록 {len(created)}건 · 노션 {published['notion']}건 · X {published['x']}건"]
    if by_repo:
        lines.append("- 기여 레포: " + ", ".join(
            f"{name} ({count})" for name, count in
            sorted(by_repo.items(), key=lambda item: (-item[1], item[0]))))
    if args.dry_run:
        lines.insert(2, "- 모드: dry-run (아무것도 쓰지 않음)")
    if pending:
        lines += ["", "| PR | 머지일 | 제목 |", "| --- | --- | --- |"]
        for pr in pending:
            lines.append(f"| {pr['repo']}#{pr['number']} | {pr['merged_at'][:10]} "
                         f"| {pr['title'][:80].replace('|', '/')} |")
    for failure in failures:
        lines.append(f"\n- ⚠️ {failure}")
    write_step_summary(lines)
    return 1 if failures else 0


# ---------------------------------------------------------------- 노션


def md_to_blocks(markdown: str, limit: int = 90) -> list[dict]:
    """간단한 마크다운 → Notion 블록. 지원: h1~h3, 문단, 불릿, 번호, 구분선, 코드블록."""
    blocks: list[dict] = []
    in_code, code_buf = False, []
    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                blocks.append({"object": "block", "type": "code", "code": {
                    "rich_text": [rt("\n".join(code_buf)[:1900])], "language": "plain text"}})
                in_code, code_buf = False, []
            else:
                in_code = True
            continue
        if in_code:
            code_buf.append(raw)
            continue
        if not line or line in ("---", "***"):
            continue
        if line.startswith("# "):
            continue  # 제목은 페이지 제목/헤딩으로 따로 처리
        m = re.match(r"^(#{2,4})\s+(.*)$", line)
        if m:
            kind = {2: "heading_2", 3: "heading_3", 4: "heading_3"}[len(m.group(1))]
            blocks.append({"object": "block", "type": kind,
                           kind: {"rich_text": [rt(m.group(2))]}})
            continue
        if line.startswith("- "):
            blocks.append({"object": "block", "type": "bulleted_list_item",
                           "bulleted_list_item": {"rich_text": [rt(line[2:])]}})
            continue
        m = re.match(r"^\d+\.\s+(.*)$", line)
        if m:
            blocks.append({"object": "block", "type": "numbered_list_item",
                           "numbered_list_item": {"rich_text": [rt(m.group(1))]}})
            continue
        blocks.append({"object": "block", "type": "paragraph", "paragraph": {"rich_text": [rt(line)]}})
        if len(blocks) >= limit:
            break
    return blocks[:limit]


def rt(text: str) -> dict:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", text)
    return {"type": "text", "text": {"content": text[:2000]}}


def read_entry(path: Path) -> tuple[dict, str, str]:
    """(front-matter, 제목, 본문)"""
    raw = path.read_text(encoding="utf-8")
    meta = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            for line in raw[3:end].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = raw[end + 4:]
    title_match = re.search(r"^#\s+(.*)$", body, flags=re.M)
    title = title_match.group(1).strip() if title_match else path.stem
    return meta, title, body


def publish_notion(path: Path, page_id: str | None = None,
                   dry_run: bool = False) -> tuple[bool, str]:
    """기록 파일을 노션 페이지 아래에 블록으로 붙인다. (전파함?, 메시지)"""
    token = env("NOTION_TOKEN")
    page_id = page_id or env("NOTION_PAGE_ID")
    meta, title, body = read_entry(path)
    blocks = [{"object": "block", "type": "heading_1", "heading_1": {"rich_text": [rt(title)]}},
              {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [rt(
                  f"{meta.get('project', '')} · PR #{meta.get('pr', '')} · {meta.get('date', '')} · "
                  f"{meta.get('source', '')}")]}},
              {"object": "block", "type": "divider", "divider": {}}]
    blocks += md_to_blocks(body, limit=80)
    if dry_run:
        return False, f"[dry-run] 블록 {len(blocks)}개를 {page_id or 'NOTION_PAGE_ID'}에 추가 예정"
    if not token or not page_id:
        return False, "[devlog] NOTION_TOKEN 또는 NOTION_PAGE_ID 가 없어 노션 전파를 건너뜁니다."
    status, _ = http_json(
        "PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children", token,
        {"children": blocks},
        {"Notion-Version": "2022-06-28"})
    return True, f"[devlog] 노션 블록 {len(blocks)}개 추가 (HTTP {status})"


def cmd_notion(args) -> int:
    ok, message = publish_notion(Path(args.file), args.page_id, args.dry_run)
    print(message, file=sys.stdout if ok else sys.stderr)
    return 0


# ---------------------------------------------------------------- X


def oauth1_header(method: str, url: str, consumer_key: str, consumer_secret: str,
                  token: str, token_secret: str, extra_params: dict | None = None) -> str:
    """OAuth 1.0a HMAC-SHA1 Authorization 헤더 (X API v2 트윗 작성용)."""
    import base64
    import hashlib
    import hmac
    import secrets

    oauth = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_token": token,
        "oauth_version": "1.0",
    }
    enc = lambda s: urllib.parse.quote(str(s), safe="~")              # noqa: E731
    params = {**oauth, **(extra_params or {})}
    param_str = "&".join(f"{enc(k)}={enc(v)}" for k, v in sorted(params.items()))
    base_url = url.split("?")[0]
    base = "&".join([method.upper(), enc(base_url), enc(param_str)])
    signing_key = f"{enc(consumer_secret)}&{enc(token_secret)}"
    signature = base64.b64encode(
        hmac.new(signing_key.encode(), base.encode(), hashlib.sha1).digest()).decode()
    oauth["oauth_signature"] = signature
    return "OAuth " + ", ".join(f'{enc(k)}="{enc(v)}"' for k, v in sorted(oauth.items()))


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def build_tweet(meta: dict, title: str, body: str, max_len: int = 275) -> str:
    """1줄 요약: 제목 + (배운 점 또는 첫 성과) + 링크 + 해시태그."""
    point = ""
    if meta.get("generated") != "auto":
        m = re.search(r"\*\*배운 점\*\*\s*\n+(.+)", body)
        if m:
            point = strip_md(m.group(1))
        else:
            section = re.search(r"##\s*성과 및 배운 점\s*\n+(.+?)(?:\n##|\Z)", body, flags=re.S)
            if section:
                bullet = re.search(r"^-\s+(.+)$", section.group(1), flags=re.M)
                if bullet:
                    point = strip_md(bullet.group(1))
    title = strip_md(title)
    url = meta.get("source", "")
    if not url.startswith("http"):
        url = ""
    tail = (f"\n{url}" if url else "") + "\n#BuildInPublic #DevLog"
    head = title + (f"\n{point}" if point else "")
    if len(head) + len(tail) > max_len:
        room = max_len - len(tail) - 1
        head = head[:room].rstrip() + "…"
    return head + tail


def publish_tweet(path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """기록을 X 1줄 요약으로 올린다. (전파함?, 메시지·본문)"""
    meta, title, body = read_entry(path)
    text = build_tweet(meta, title, body)
    if dry_run:
        return False, text
    keys = {k: env(k) for k in ("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_SECRET")}
    if not all(keys.values()):
        return False, "[devlog] X 시크릿이 없어 트윗을 건너뜁니다."
    url = "https://api.x.com/2/tweets"
    auth = oauth1_header("POST", url, keys["X_API_KEY"], keys["X_API_SECRET"],
                         keys["X_ACCESS_TOKEN"], keys["X_ACCESS_SECRET"])
    status, payload = http_json("POST", url, None, {"text": text}, {"Authorization": auth})
    return True, f"[devlog] 트윗 전송 (HTTP {status}) {payload.get('data', {}).get('id', '')}"


def cmd_tweet(args) -> int:
    ok, message = publish_tweet(Path(args.file), args.dry_run)
    print(message, file=sys.stdout if ok else sys.stderr)
    return 0


# ---------------------------------------------------------------- main


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="devlog", description="dev-log 파이프라인")
    sub = parser.add_subparsers(dest="command", required=True)

    p_entry = sub.add_parser("entry", help="PR을 기록으로 만든다")
    p_entry.add_argument("--repo", help="owner/name")
    p_entry.add_argument("--pr", help="PR 번호")
    p_entry.add_argument("--from-json", help="미리 받아둔 PR JSON으로 생성 (네트워크 없이)")
    p_entry.add_argument("--date", help="기록 날짜 (기본: 머지일)")
    p_entry.add_argument("--no-llm", action="store_true", help="LLM 없이 자동 요약만")
    p_entry.add_argument("--dry-run", action="store_true", help="파일을 쓰지 않고 출력만")
    p_entry.set_defaults(func=cmd_entry)

    p_scan = sub.add_parser("scan", help="모든 레포의 최근 머지 PR을 찾아 기록한다")
    p_scan.add_argument("--days", type=int, default=14, help="최근 N일 (기본 14)")
    p_scan.add_argument("--user", help="스캔할 GitHub 계정 (기본: DEVLOG_USER → 저장소 소유자)")
    p_scan.add_argument("--limit", type=int, default=25, help="한 번에 기록할 최대 PR 수 (기본 25)")
    p_scan.add_argument("--publish", default="none",
                        help="전파 채널: all | notion | x | none (기본 none)")
    p_scan.add_argument("--max-publish", type=int, default=5,
                        help="한 번에 X에 올릴 최대 건수 (기본 5)")
    p_scan.add_argument("--include-merges", action="store_true",
                        help="develop→main 같은 머지 PR도 기록")
    p_scan.add_argument("--no-llm", action="store_true", help="LLM 없이 자동 요약만")
    p_scan.add_argument("--dry-run", action="store_true",
                        help="파일·노션·X에 쓰지 않고 미리보기만")
    p_scan.set_defaults(func=cmd_scan)

    p_notion = sub.add_parser("notion", help="기록을 노션 페이지에 붙인다")
    p_notion.add_argument("--file", required=True)
    p_notion.add_argument("--page-id")
    p_notion.add_argument("--dry-run", action="store_true")
    p_notion.set_defaults(func=cmd_notion)

    p_tweet = sub.add_parser("tweet", help="기록을 X에 1줄로 올린다")
    p_tweet.add_argument("--file", required=True)
    p_tweet.add_argument("--dry-run", action="store_true")
    p_tweet.set_defaults(func=cmd_tweet)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

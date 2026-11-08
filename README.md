# dev-log

> 커밋과 PR을 분석해 **트러블슈팅과 배운 점**을 자동으로 쌓는 개발 자산 아카이브

이 저장소는 "개발이 끝나고 나중에 포트폴리오를 쓰려면 다 까먹는다"는 문제를 없애기 위한 기록 저장소입니다.
평소처럼 코드를 짜고 PR을 머지하면, GitHub Actions가 변경점(diff)과 커밋 이력을 읽어
**어떤 문제를 만났고, 원인이 무엇이었고, 어떻게 풀었는지**를 이 저장소의 마크다운으로 남깁니다.

노션과 X(트위터)는 같은 파이프라인의 출력 채널입니다. 한 번의 머지로

- **GitHub** — `logs/{연도}/` 아래 날짜별 마크다운 (영구 보존, 검색 가능, 포트폴리오 원본)
- **Notion** — `🚀 개발 트러블슈팅 & Dev Log` 페이지에 같은 내용 요약
- **X (@antifreezew9)** — 1줄 요약 트윗 (Build in Public)

세 곳에 동시에 쌓입니다.

> 노션 미러: `포트폴리오 > 🚀 개발 트러블슈팅 & Dev Log` (같은 내용의 요약본이 쌓이는 곳)

---

## 기록 포맷

기존 포트폴리오(Orato · figma-token)에 쓰던 형식을 그대로 씁니다. 자동 생성 기록도 같은 뼈대를 따릅니다.

```
개요            →  이 변경이 무엇을 하는지 한 문단
주요 기능        →  이번 변경이 만든/고친 동작
사용 기술        →  실제로 손댄 기술 (diff에서 판별)
트러블슈팅       →  문제 / 원인 / 해결  (이 저장소의 핵심)
성과 및 배운 점   →  남는 결과와 다음에 다르게 할 것
```

자동 생성 기록에는 앞에 메타데이터가 붙습니다.

```yaml
---
project: Team-B1ND/dodamdodam-web
source: https://github.com/Team-B1ND/dodamdodam-web/pull/223
date: 2026-11-08
pr: 223
author: lee090626
tags: [React, TypeScript]
generated: auto            # auto = 파이프라인 생성, manual = 직접 작성
---
```

파일 이름은 `logs/{연도}/{YYYY-MM-DD}-{슬러그}.md`이고, 전체 목록은 [logs/INDEX.md](logs/INDEX.md)에 자동으로 추가됩니다.

---

## 파이프라인 구조

```
[프로젝트 레포]  PR merged  (또는 Actions에서 수동 실행)
        │
        │  repository_dispatch  (templates/target-repo-workflow.yml)
        ▼
[dev-log / .github/workflows/auto-devlog.yml]   ← templates/auto-devlog.yml 을 옮겨서 활성화
        │
        ├─ 1. PR 메타데이터 · 파일별 diff · 커밋 수집   (scripts/devlog.py entry)
        ├─ 2. 문제 / 원인 / 해결 / 포인트 요약          (LLM 키가 있으면 LLM, 없으면 diff 기반 자동 요약)
        ├─ 3. logs/{연도}/{날짜}-{슬러그}.md 작성 + INDEX 갱신 → 커밋 & push
        ├─ 4. Notion '개발 트러블슈팅 & Dev Log' 페이지에 블록 추가  (scripts/devlog.py notion)
        └─ 5. X 1줄 요약 트윗                                      (scripts/devlog.py tweet)
```

3번은 항상 실행되고, 4·5번은 해당 시크릿이 등록되어 있을 때만 실행됩니다(없으면 조용히 건너뜀).

---

## 폴더 구조

```
.
├── README.md
├── logs/
│   ├── INDEX.md                  # 전체 기록 목록 (자동 갱신)
│   └── 2026/
│       ├── orato.md              # Orato — AI 발표 피드백 서비스
│       ├── figma-token.md        # figma-token — 디자인 토큰 변환 도구
│       ├── part-trip.md          # PartTrip — 여행 플래너 웹
│       ├── hanggi-pick.md        # 한끼픽 — 학식 리뷰 REST API
│       └── aid-kit.md            # 도담도담 aid-kit — 버그 분석
├── templates/
│   ├── auto-devlog.yml           # ★ 이 파일을 .github/workflows/ 로 옮기면 파이프라인 활성화
│   ├── entry-template.md         # 기록 포맷 (수동 작성용)
│   └── target-repo-workflow.yml  # 프로젝트 레포에 붙이는 트리거 워크플로우
├── scripts/
│   └── devlog.py                 # 분석 · 기록 · 노션 · X (표준 라이브러리만 사용)
└── (활성화 후) .github/workflows/auto-devlog.yml
```

---

## 이미 쌓인 자산

노션에 흩어져 있던 기존 트러블슈팅 기록을 이 저장소로 옮겨 왔습니다. 자동 파이프라인이 만들어내는 기록의 기준선입니다.

| 프로젝트 | 성격 | 트러블슈팅 | 기록 |
| --- | --- | --- | --- |
| Orato | 학교 팀 프로젝트 · 프론트엔드 | 3건 | [logs/2026/orato.md](logs/2026/orato.md) |
| figma-token | 개인 프로젝트 · Core/Plugin/CLI/npm 배포 | 3건 | [logs/2026/figma-token.md](logs/2026/figma-token.md) |
| PartTrip | 팀 프로젝트 · 웹 파트 단독 담당 | 8건 | [logs/2026/part-trip.md](logs/2026/part-trip.md) |
| 한끼픽 | 팀 프로젝트 · Spring Boot REST API | 4건 | [logs/2026/hanggi-pick.md](logs/2026/hanggi-pick.md) |
| aid-kit | 도담도담 앱 내부 패키지 버그 분석 | 3건 | [logs/2026/aid-kit.md](logs/2026/aid-kit.md) |

전체 목록: [logs/INDEX.md](logs/INDEX.md)

---

## 자동화 붙이는 법

### 0. 워크플로우 파일을 `.github/workflows/`로 옮기기

`templates/auto-devlog.yml`을 `.github/workflows/auto-devlog.yml`로 옮기면 파이프라인이 켜집니다.
GitHub 웹에서 **Add file → Create new file** → 파일 이름 `.github/workflows/auto-devlog.yml` → `templates/auto-devlog.yml` 내용 붙여넣기 → Commit.
(이 저장소를 만든 도구가 GitHub Actions 파일 쓰기 권한을 가지고 있지 않아서, 이 한 파일만 손으로 옮겨야 합니다. 한 번만 하면 됩니다.)

### 1. 이 저장소의 Actions 권한 켜기

`Settings → Actions → General → Workflow permissions`에서 **Read and write permissions**를 선택합니다.
(워크플로우가 기록을 커밋해야 하므로 필요)

### 2. 감시할 프로젝트 레포에 트리거 한 장 붙이기

`templates/target-repo-workflow.yml`을 프로젝트 레포의 `.github/workflows/devlog-dispatch.yml`로 복사하고,
그 레포 `Settings → Secrets and variables → Actions`에 `DEVLOG_DISPATCH_TOKEN`(dev-log에 `contents: write`가 있는 PAT)을 등록합니다.

```yaml
# .github/workflows/devlog-dispatch.yml  (감시할 레포 쪽)
on:
  pull_request:
    types: [closed]
jobs:
  dispatch:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.DEVLOG_DISPATCH_TOKEN }}
          repository: lee090626/dev-log
          event-type: devlog
          client-payload: |
            {"source_repo":"${{ github.repository }}","pr_number":"${{ github.event.pull_request.number }}"}
```

### 3. (선택) 노션 · X 연결

아래 시크릿을 `Settings → Secrets and variables → Actions`에 넣으면 4·5단계가 켜집니다. 없으면 마크다운 기록만 남고 나머지는 건너뜁니다.

| 시크릿 | 무엇 | 어디서 |
| --- | --- | --- |
| `NOTION_TOKEN` | Notion 내부 통합 토큰 (`ntn_...`) | notion.so/my-integrations 에서 통합 생성 → 대상 페이지에 `Connections`로 초대 |
| `NOTION_PAGE_ID` | 기록을 붙일 페이지 id (기본값: `🚀 개발 트러블슈팅 & Dev Log`) | 페이지 URL의 32자리 |
| `X_API_KEY` / `X_API_SECRET` | X 앱 Consumer Key / Secret | developer.x.com → App → Keys and tokens |
| `X_ACCESS_TOKEN` / `X_ACCESS_SECRET` | 같은 앱의 Access Token / Secret (`Read and write` 권한) | developer.x.com |
| `LLM_API_KEY` | (선택) 요약을 LLM으로. 없으면 diff 기반 자동 요약 | Gemini API 키 등 |
| `LLM_MODEL` | (선택) 기본 `gemini-2.0-flash` | |
| `DEVLOG_GITHUB_TOKEN` | (선택) 다른 레포의 비공개 PR까지 읽을 때 쓰는 PAT | 없으면 `github.token` 사용 |

---

## 수동 실행

Actions 탭에서 **auto-devlog → Run workflow**를 누르고 `source_repo`(예: `Team-B1ND/dodamdodam-web`)와 `pr_number`(예: `223`)를 넣으면 그 PR 하나가 기록으로 만들어집니다.

로컬에서도 같은 스크립트를 씁니다.

```bash
export GITHUB_TOKEN=<repo 읽기 권한 토큰>

# 1) PR 하나를 기록으로
python3 scripts/devlog.py entry --repo Team-B1ND/dodamdodam-web --pr 223

# 2) diff 없이 바로 보고 싶을 때 (dry-run: 파일을 쓰지 않고 콘솔에만)
python3 scripts/devlog.py entry --repo Team-B1ND/dodamdodam-web --pr 223 --dry-run

# 3) 만들어진 기록을 노션 / X로
python3 scripts/devlog.py notion --file logs/2026/2026-11-08-pr-223.md
python3 scripts/devlog.py tweet  --file logs/2026/2026-11-08-pr-223.md
```

`scripts/devlog.py`는 **표준 라이브러리만** 씁니다(설치할 패키지 없음).

---

## 검증 상태

솔직하게 적어 둡니다.

- `entry` (수집 → 요약 → 마크다운 생성 → INDEX 갱신): **실제 머지된 PR 1건으로 실행해 검증 완료**
  (예: `Team-B1ND/dodamdodam-web#218` → `logs/2026/2026-10-28-pr-218-*.md` 생성, INDEX 한 줄 추가 확인)
- `notion` · `tweet`: 코드는 완성되어 있으나 **토큰이 없어 실제 호출은 아직 검증하지 못했습니다.**
  첫 실행 시 Actions 로그로 결과를 확인하고, 필요하면 `--dry-run`으로 본문만 먼저 봅니다.
- LLM 요약은 키가 없을 때를 대비해 **diff 기반 자동 요약으로 항상 동작**합니다.

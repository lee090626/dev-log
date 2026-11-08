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

그리고 **매일 밤 23:00(KST)** 정기 스캔이 돌아, 내 계정의 **모든 레포**(소유 + 기여)에서 그날까지 머지된 PR 중 아직 기록되지 않은 것을 자동으로 찾아 같은 파이프라인에 태웁니다. 머지를 깜빡해도 기록이 비지 않습니다.

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
[정기 스캔]  매일 23:00 KST (cron)
        │
        │  내 레포 전체에서 최근 14일 머지 PR 조회 → 이미 기록된 것 제외
        ▼
[프로젝트 레포]  PR merged  (또는 Actions에서 수동 실행)
        │
        │  repository_dispatch  (templates/target-repo-workflow.yml)
        ▼
[dev-log / .github/workflows/auto-devlog.yml]   ← templates/auto-devlog.yml 을 옮겨서 활성화
        │
        ├─ 1. PR 메타데이터 · 파일별 diff · 커밋 수집   (scripts/devlog.py entry / scan)
        ├─ 2. 문제 / 원인 / 해결 / 포인트 요약          (LLM 키가 있으면 LLM, 없으면 diff 기반 자동 요약)
        ├─ 3. logs/{연도}/{날짜}-{슬러그}.md 작성 + INDEX 갱신 → 커밋 & push
        ├─ 4. Notion '개발 트러블슈팅 & Dev Log' 페이지에 블록 추가  (scripts/devlog.py notion)
        └─ 5. X 1줄 요약 트윗                                      (scripts/devlog.py tweet)
```

3번은 항상 실행되고, 4·5번은 해당 시크릿이 등록되어 있을 때만 실행됩니다(없으면 조용히 건너뜀).

---

## 전체 레포 자동 스캔

`scan` 은 PR 하나가 아니라 **내 계정 전체**를 훑습니다.

1. 소유 레포 목록 + 검색 API(`is:pr is:merged author:lee090626 merged:>=YYYY-MM-DD`)로 최근 N일(기본 14일) 머지 PR을 모읍니다. 검색 API가 막히면 소유 레포를 하나씩 직접 조회해 보완합니다.
2. `logs/` 의 front-matter(`project` + `pr`)와 대조해 **이미 기록된 PR은 건너뜁니다.** (여러 번 돌아도 중복이 생기지 않음)
3. 남은 PR만 `entry` 와 같은 경로로 기록하고, `--publish` 에 따라 노션·X로 전파합니다.

```bash
python3 scripts/devlog.py scan --days 14 --dry-run          # 무엇이 기록될지 미리보기 (아무것도 쓰지 않음)
python3 scripts/devlog.py scan --days 14                    # 기록만 (파일 + INDEX)
python3 scripts/devlog.py scan --days 14 --publish all      # 기록 + 노션 + X
```

| 옵션 | 기본값 | 의미 |
| --- | --- | --- |
| `--days N` | 14 | 최근 N일 안에 머지된 PR만 |
| `--publish` | `none` | `all` / `notion` / `x` / `none` |
| `--limit N` | 25 | 한 번에 기록할 최대 PR 수 (나머지는 다음 실행) |
| `--max-publish N` | 5 | 한 번에 X에 올릴 최대 건수 — 밀린 기록이 한꺼번에 트윗되는 것을 막음 |
| `--include-merges` | 꺼짐 | `merge: develop` 같은 머지 커밋만 있는 PR도 기록 |
| `--user` | 저장소 소유자 | 스캔할 계정 (다른 계정으로 돌려볼 때) |

기본으로 `merge: develop`, `Develop`, `develop` 처럼 머지 커밋만 있는 PR은 건너뜁니다. develop→main 머지가 기록으로 쌓이면 내용이 비어서입니다.

> **스캔이 다른 레포까지 보려면 `DEVLOG_GITHUB_TOKEN` 이 필요합니다.** GitHub Actions의 기본 `github.token` 은 이 저장소(dev-log)만 읽을 수 있습니다. 그 토큰만으로 스캔하면 조직 레포(B1ND·PartTrip 등)의 PR은 **한 건도 보이지 않습니다.**

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

### 0. 워크플로우 파일을 `.github/workflows/`로 옮기기 (유일하게 손으로 해야 하는 단계)

`templates/auto-devlog.yml`을 `.github/workflows/auto-devlog.yml`로 옮기면 파이프라인(정기 스캔 포함)이 켜집니다. GitHub App 토큰에는 Actions 파일 쓰기 권한이 없어 이 한 파일만 직접 옮겨야 합니다.

1. <https://github.com/lee090626/dev-log/edit/main/.github/workflows/auto-devlog.yml> 를 연다 (없으면 같은 경로로 **Add file → Create new file**).
2. <https://raw.githubusercontent.com/lee090626/dev-log/main/templates/auto-devlog.yml> 내용을 전부 복사해 그대로 붙여넣는다.
3. **Commit changes** → main에 커밋.
4. Actions 탭 → **auto-devlog** → **Run workflow** (mode: `scan`) 으로 한 번 돌려 확인.

템플릿이 바뀌면(예: 스캔 옵션이 늘어나면) 같은 방법으로 다시 붙여넣으면 됩니다. 이 저장소를 만든 도구는 `templates/` 만 고칠 수 있습니다.

### 1. 이 저장소의 Actions 권한 켜기

`Settings → Actions → General → Workflow permissions`에서 **Read and write permissions**를 선택합니다.
(워크플로우가 기록을 커밋해야 하므로 필요)

### 2. (선택) 감시할 프로젝트 레포에 트리거 한 장 붙이기

정기 스캔이 매일 알아서 찾아가므로 **이 단계는 이제 선택**입니다. 머지되자마자 바로 기록되고 싶은 레포에만 붙이면 됩니다.

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
| `DEVLOG_GITHUB_TOKEN` | **스캔에 필요** — 내 다른 레포(비공개 포함)의 PR까지 읽는 PAT | Settings → Developer settings → Personal access tokens (classic, `repo` + `read:org`) |

---

## 수동 실행

### Actions 탭에서

Actions 탭 → **auto-devlog** → **Run workflow**

- **mode `scan`** (기본): 최근 `days`일 머지 PR을 전부 훑어 새것만 기록. `days` 기본 14.
- **mode `single`**: PR 하나만 기록. `source_repo`(예: `Team-B1ND/dodamdodam-web`)와 `pr_number`(예: `223`)를 넣습니다.
- `publish` 로 이번 실행의 전파 채널을 고릅니다(`all` / `notion` / `x` / `none`).

### 로컬에서

```bash
export GITHUB_TOKEN=<repo 읽기 권한 토큰>

# 0) 내 모든 레포에서 최근 14일 머지 PR 중 기록 안 된 것 찾기 (dry-run: 아무것도 쓰지 않음)
python3 scripts/devlog.py scan --days 14 --dry-run

# 0-1) 실제로 기록 + INDEX 갱신 (노션·X는 안 씀)
python3 scripts/devlog.py scan --days 14

# 0-2) 기록 + 노션 + X (X는 한 번에 최대 5건)
python3 scripts/devlog.py scan --days 14 --publish all --max-publish 5

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
- `scan`: **실제 계정 데이터로 검증 완료** (2026-11-08, 익명 토큰=공개 레포만)
  - `scan --days 14 --dry-run`: 소유 레포 8개 · 머지 PR 2건 → `merge: develop` 1건 제외 → 1건(`dodamdodam-web#218`) 기록 예정 확인
  - 실제 기록 실행: 파일 1건 생성 + INDEX 한 줄 추가 확인, 같은 명령 재실행 시 **기록 대상 0건**(중복 방지 동작)
  - `--include-merges`: 머지 커밋 PR(`#221`)까지 대상에 들어오는 것 확인
  - 비공개 레포는 익명 토큰에서 안 보였습니다. Actions에서는 `DEVLOG_GITHUB_TOKEN` 으로 볼 수 있습니다.
- `notion` · `tweet`: 코드는 완성되어 있으나 **토큰이 없어 실제 호출은 아직 검증하지 못했습니다.**
  첫 실행 시 Actions 로그로 결과를 확인하고, 필요하면 `--dry-run`으로 본문만 먼저 봅니다.
- LLM 요약은 키가 없을 때를 대비해 **diff 기반 자동 요약으로 항상 동작**합니다.

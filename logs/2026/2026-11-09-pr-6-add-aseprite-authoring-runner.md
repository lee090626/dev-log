---
project: lee090626/pixelrefinery-tools
source: https://github.com/lee090626/pixelrefinery-tools/pull/6
date: 2026-11-09
pr: 6
author: lee090626
tags: [Python]
generated: auto
merged_at: 2026-11-09T01:25:56Z
private: true
---

# add Aseprite authoring runner

## 개요

lee090626/pixelrefinery-tools의 변경입니다. 파일 9개 (+715/-72), 커밋 9개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: add Aseprite authoring runner
- feat: add Aseprite Update workflow
- Bind Update reviews to Aseprite artifacts
- docs: verify Aseprite Update workflow

## 사용 기술

`Python`

## 변경 파일

- `PixelRefinery/engine/generation/update.py` — 수정 +205 / -59
- `PixelRefinery/tests/integration/test_ashenbriar_update.py` — 수정 +163 / -9
- `PixelRefinery/engine/aseprite.py` — 추가 +131 / -0
- `PixelRefinery/tests/unit/test_aseprite_runner.py` — 추가 +115 / -0
- `PixelRefinery/tools/aseprite/README.md` — 추가 +54 / -0
- `PixelRefinery/tools/aseprite/build_animation.lua` — 추가 +23 / -0
- `PixelRefinery/tools/aseprite/edit_pixels.lua` — 추가 +17 / -0
- `README.md` — 수정 +3 / -3
- `PixelRefinery/tools/refinery.py` — 수정 +4 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Aseprite를 PixelRefinery의 픽셀 아트 제작·편집·내보내기 경로에 연결했습니다. Lua runner는 안전한 새 후보 경로, 입력 복사, 출력 해시를 확인합니다. Update edit/animate는 편집 가능한 Aseprite 문서와 PNG 후보를 만들고, review evidence에는 문서·시트·메타데이터 해시를 묶어 변경 시 재검수를 요구합니다. 프레임별 밀리초 반올림 시간표와 실제 effective_fps도 기록합니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: PixelRefinery/engine/aseprite.py, PixelRefinery/engine/generation/update.py, PixelRefinery/tests/integration/test_ashenbriar_update.py, PixelRefinery/tests/unit/test_aseprite_runner.py, PixelRefinery/tools/aseprite/README.md, PixelRefinery/tools/aseprite/build_animation.lua

## 커밋

- `72d36f5` feat: add Aseprite authoring runner
- `41e06ed` Merge commit '72d36f52f6c7ffdb8b6970b70b8d127de652c2f5' into feature/#1-aseprite-workflow
- `e85ebd8` feat: add Aseprite Update workflow
- `3c4add7` Merge branch 't3/replace-libresprite-aseprite' into feature/#1-aseprite-workflow
- `2e141fd` Bind Update reviews to Aseprite artifacts
- `b7e4af6` Merge branch 't3/bind-aseprite-review-artifacts' into feature/#1-aseprite-workflow
- `02b8e84` docs: verify Aseprite Update workflow
- `3e45804` Merge branch 't3/document-aseprite-workflow' into feature/#1-aseprite-workflow
- `c93cd58` fix: verify effective Aseprite animation timing

## 성과 및 배운 점

- 변경 파일 9개, +715 / -72
- 커밋 9개

---

> 자동 생성: PR [lee090626/pixelrefinery-tools#6](https://github.com/lee090626/pixelrefinery-tools/pull/6) · `scripts/devlog.py entry`

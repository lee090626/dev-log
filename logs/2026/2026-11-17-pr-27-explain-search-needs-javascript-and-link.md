---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/27
date: 2026-11-17
pr: 27
author: lee090626
tags: [React]
generated: auto
merged_at: 2026-11-17T01:24:30Z
---

# Explain search needs JavaScript and link to browsable pages

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+4/-0), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Explain search needs JavaScript and link to browsable pages

## 사용 기술

`React`

## 변경 파일

- `app/search/page.tsx` — 수정 +4 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Fixes #24. Search results are computed in the browser (static export, no server), so with JavaScript off the page now shows a `` notice linking to the home page and /themes. Checked /search?q=부산: JS off shows the notice; JS on shows no notice and the same 156 results.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/search/page.tsx

## 커밋

- `7a1dcea` Explain search needs JavaScript and link to browsable pages

## 성과 및 배운 점

- 변경 파일 1개, +4 / -0
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#27](https://github.com/lee090626/travel-discovery/pull/27) · `scripts/devlog.py entry`

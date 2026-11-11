---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/7
date: 2026-11-11
pr: 7
author: lee090626
tags: [CSS, React]
generated: auto
merged_at: 2026-11-11T04:39:08Z
---

# 디자인 v2 적용: 뽈뽈이 포즈, Pretendard, 카드/필 리디자인

## 개요

lee090626/travel-discovery의 변경입니다. 파일 16개 (+525/-218), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Implement design v2: mascot poses, Pretendard body font, card and pill redesign, show-more lists

## 사용 기술

`CSS` · `React`

## 변경 파일

- `app/globals.css` — 수정 +389 / -131
- `components/travel-ui.tsx` — 수정 +64 / -36
- `app/regions/[region]/page.tsx` — 수정 +9 / -20
- `app/page.tsx` — 수정 +7 / -13
- `app/regions/[region]/[theme]/page.tsx` — 수정 +11 / -9
- `components/show-more.tsx` — 추가 +20 / -0
- `components/search-results.tsx` — 수정 +10 / -4
- `app/places/[id]/page.tsx` — 수정 +5 / -4
- `app/regions/page.tsx` — 수정 +3 / -1
- `app/search/page.tsx` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
캔버스 디자인(Main/Regions/RegionDetail/Place/Search/NotFound)을 코드에 반영했습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/globals.css, app/page.tsx, app/places/[id]/page.tsx, app/regions/[region]/[theme]/page.tsx, app/regions/[region]/page.tsx, app/regions/page.tsx

## 커밋

- `6d40133` Implement design v2: mascot poses, Pretendard body font, card and pill redesign, show-more lists

## 성과 및 배운 점

- 변경 파일 16개, +525 / -218
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#7](https://github.com/lee090626/travel-discovery/pull/7) · `scripts/devlog.py entry`

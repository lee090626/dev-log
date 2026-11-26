---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/30
date: 2026-11-26
pr: 30
author: lee090626
tags: [React, TypeScript]
generated: auto
merged_at: 2026-11-26T03:09:32Z
---

# 월별 행사 페이지 (/events/YYYY-MM)

## 개요

lee090626/travel-discovery의 변경입니다. 파일 6개 (+117/-6), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Add monthly event pages

## 사용 기술

`React` · `TypeScript`

## 변경 파일

- `app/events/[month]/page.tsx` — 추가 +47 / -0
- `lib/travel.ts` — 수정 +32 / -0
- `app/events/page.tsx` — 수정 +15 / -3
- `lib/travel.test.ts` — 수정 +17 / -1
- `app/sitemap.ts` — 수정 +5 / -1
- `docs/glossary.md` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 - `/events/YYYY-MM`: 빌드일 기준 이번 달부터 세 달, 그 달에 열리는 진행 중·예정 행사를 지역별로 정리. 행사가 2건 미만인 달은 페이지를 만들지 않음(`MIN_LISTED_MONTH_EVENTS`). - `/events`에 월별 링크, 사이트맵에 월별 페이지 추가.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/events/[month]/page.tsx, app/events/page.tsx, app/sitemap.ts, docs/glossary.md, lib/travel.test.ts, lib/travel.ts

## 커밋

- `e5fbaf7` Add monthly event pages

## 성과 및 배운 점

- 변경 파일 6개, +117 / -6
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#30](https://github.com/lee090626/travel-discovery/pull/30) · `scripts/devlog.py entry`

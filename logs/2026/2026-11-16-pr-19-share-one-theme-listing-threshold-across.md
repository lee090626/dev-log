---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/19
date: 2026-11-16
pr: 19
author: lee090626
tags: [TypeScript, React]
generated: auto
merged_at: 2026-11-16T14:36:07Z
---

# Share one theme listing threshold across pages, sitemap and llms.txt

## 개요

lee090626/travel-discovery의 변경입니다. 파일 8개 (+27/-24), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Share one theme listing threshold across pages, sitemap and llms.txt

## 사용 기술

`TypeScript` · `React`

## 변경 파일

- `app/themes/[theme]/page.tsx` — 수정 +5 / -5
- `app/regions/[region]/[theme]/page.tsx` — 수정 +4 / -5
- `app/sitemap.ts` — 수정 +3 / -5
- `lib/travel.ts` — 수정 +7 / -0
- `app/llms.txt/route.ts` — 수정 +2 / -3
- `app/page.tsx` — 수정 +2 / -2
- `app/regions/[region]/page.tsx` — 수정 +2 / -2
- `app/themes/page.tsx` — 수정 +2 / -2

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
문제 "장소가 2곳 이상인 테마만 목록 페이지로 노출한다"는 규칙이 9곳에 `>= 2`, `< 2`로 따로 적혀 있었습니다. 홈, 테마 목록과 상세, 지역 상세, 지역×테마 상세, 사이트맵 2곳, llms.txt가 그 위치입니다. 한 곳만 바꾸면 사이트맵에는 있는데 페이지는 404이거나, 페이지는 있는데 사이트맵에 빠지는 불일치가 생길 수 있었습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/llms.txt/route.ts, app/page.tsx, app/regions/[region]/[theme]/page.tsx, app/regions/[region]/page.tsx, app/sitemap.ts, app/themes/[theme]/page.tsx

## 커밋

- `cdb55f1` Share one theme listing threshold across pages, sitemap and llms.txt

## 성과 및 배운 점

- 변경 파일 8개, +27 / -24
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#19](https://github.com/lee090626/travel-discovery/pull/19) · `scripts/devlog.py entry`

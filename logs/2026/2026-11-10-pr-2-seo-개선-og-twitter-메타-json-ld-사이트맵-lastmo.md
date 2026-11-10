---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/2
date: 2026-11-10
pr: 2
author: lee090626
tags: [React, TypeScript]
generated: auto
merged_at: 2026-11-10T12:36:09Z
---

# SEO 개선: OG/Twitter 메타, JSON-LD, 사이트맵 lastmod

## 개요

lee090626/travel-discovery의 변경입니다. 파일 5개 (+82/-32), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Add Open Graph, JSON-LD and sitemap lastmod for SEO

## 사용 기술

`React` · `TypeScript`

## 변경 파일

- `lib/seo.tsx` — 추가 +49 / -0
- `app/places/[id]/page.tsx` — 수정 +30 / -2
- `lib/seo.ts` — 삭제 +0 / -29
- `app/sitemap.ts` — 수정 +2 / -1
- `app/layout.tsx` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 - `pageMetadata`: Open Graph·Twitter 카드 추가 (모든 페이지). 장소 페이지는 관광공사 대표 이미지를 og:image로 사용. - 장소 페이지 title을 `장소명 - 지역 여행 정보`로 변경해 지역 검색어 포함. - 장소 페이지 JSON-LD: `TouristAttraction`(행사는 `Event`, 시작·종료일 포함) + `BreadcrumbList`. - 사이트맵 장소 URL에 TourAPI `modifiedtime` 기반 `lastmod` 추가. - `lib/seo.ts` → `lib/seo.tsx` (JsonLd 컴포넌트 포함).

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/layout.tsx, app/places/[id]/page.tsx, app/sitemap.ts, lib/seo.ts, lib/seo.tsx

## 커밋

- `688c5fc` Add Open Graph, JSON-LD and sitemap lastmod for SEO

## 성과 및 배운 점

- 변경 파일 5개, +82 / -32
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#2](https://github.com/lee090626/travel-discovery/pull/2) · `scripts/devlog.py entry`

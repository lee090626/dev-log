---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/3
date: 2026-11-10
pr: 3
author: lee090626
tags: [CSS, TypeScript, React]
generated: auto
merged_at: 2026-11-10T12:44:07Z
---

# AEO·GEO 최적화: FAQ, 구조화 데이터 확장, AI 크롤러 허용, llms.txt

## 개요

lee090626/travel-discovery의 변경입니다. 파일 7개 (+127/-3), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Add FAQ, ItemList/WebSite JSON-LD, AI crawler rules and llms.txt

## 사용 기술

`CSS` · `TypeScript` · `React`

## 변경 파일

- `app/llms.txt/route.ts` — 추가 +37 / -0
- `lib/seo.tsx` — 수정 +31 / -0
- `app/regions/[region]/page.tsx` — 수정 +19 / -1
- `app/globals.css` — 수정 +15 / -0
- `app/places/[id]/page.tsx` — 수정 +11 / -1
- `app/page.tsx` — 수정 +10 / -0
- `app/robots.ts` — 수정 +4 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 **AEO (답변 엔진)** - 장소 페이지에 '자주 묻는 질문' 섹션 + `FAQPage` JSON-LD. 위치·행사 기간·테마·문의처·홈페이지를 실제 데이터로만 생성 (없는 정보는 질문도 만들지 않음). - 지역 페이지 `ItemList`(장소 목록) + `BreadcrumbList` JSON-LD. - 홈 `WebSite` + `SearchAction`(/search?q=) JSON-LD.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/globals.css, app/llms.txt/route.ts, app/page.tsx, app/places/[id]/page.tsx, app/regions/[region]/page.tsx, app/robots.ts

## 커밋

- `1806c5b` Add FAQ, ItemList/WebSite JSON-LD, AI crawler rules and llms.txt

## 성과 및 배운 점

- 변경 파일 7개, +127 / -3
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#3](https://github.com/lee090626/travel-discovery/pull/3) · `scripts/devlog.py entry`

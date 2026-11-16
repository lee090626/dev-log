---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/18
date: 2026-11-16
pr: 18
author: lee090626
tags: [React]
generated: auto
merged_at: 2026-11-16T14:28:59Z
---

# Show the search form while search results load

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+3/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Show the search form while search results load

## 사용 기술

`React`

## 변경 파일

- `app/search/page.tsx` — 수정 +3 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
문제 검색 페이지는 `useSearchParams`를 쓰는 `SearchResults`를 ``로 감싸고 있었습니다. 그래서 정적 HTML(`out/search.html`)에 검색 폼이 없었고(`role="search"` 0개), 하이드레이션 전까지 검색창 자리가 비어 있었습니다. 자바스크립트가 꺼진 환경에서는 검색창 자체가 보이지 않았습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/search/page.tsx

## 커밋

- `a3b7b1d` Show the search form while search results load

## 성과 및 배운 점

- 변경 파일 1개, +3 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#18](https://github.com/lee090626/travel-discovery/pull/18) · `scripts/devlog.py entry`

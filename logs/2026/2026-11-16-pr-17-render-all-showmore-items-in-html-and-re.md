---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/17
date: 2026-11-16
pr: 17
author: lee090626
tags: [React]
generated: auto
merged_at: 2026-11-16T14:22:49Z
---

# Render all ShowMore items in HTML and remember expansion per page

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+29/-3), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Render all ShowMore items in HTML and remember expansion per page

## 사용 기술

`React`

## 변경 파일

- `components/show-more.tsx` — 수정 +29 / -3

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
문제 `ShowMore`가 펼친 개수만큼만 렌더링해서, 정적 HTML에는 장소 링크가 12개만 들어갔습니다. 서울 지역 페이지는 장소가 163곳인데 HTML 링크는 12개였습니다. 자바스크립트를 실행하지 않는 크롤러(네이버 등)는 나머지 장소 페이지로 가는 링크를 볼 수 없었습니다. 또 상세 페이지에 갔다가 뒤로 오면 펼친 상태가 12개로 초기화됐습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: components/show-more.tsx

## 커밋

- `e4bc0e0` Render all ShowMore items in HTML and remember expansion per page

## 성과 및 배운 점

- 변경 파일 1개, +29 / -3
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#17](https://github.com/lee090626/travel-discovery/pull/17) · `scripts/devlog.py entry`

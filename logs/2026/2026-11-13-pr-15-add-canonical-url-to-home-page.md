---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/15
date: 2026-11-13
pr: 15
author: lee090626
tags: [React]
generated: auto
merged_at: 2026-11-13T11:38:00Z
---

# Add canonical URL to home page

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+5/-0), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Add canonical URL to home page

## 사용 기술

`React`

## 변경 파일

- `app/page.tsx` — 수정 +5 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 - 메인 페이지에 `canonical` 링크를 추가했습니다. 하위 페이지는 `pageMetadata`로 이미 canonical을 갖고 있었고, 메인만 빠져 있었습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: app/page.tsx

## 커밋

- `52d322c` Add canonical URL to home page

## 성과 및 배운 점

- 변경 파일 1개, +5 / -0
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#15](https://github.com/lee090626/travel-discovery/pull/15) · `scripts/devlog.py entry`

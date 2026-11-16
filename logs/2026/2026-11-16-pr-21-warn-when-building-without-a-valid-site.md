---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/21
date: 2026-11-16
pr: 21
author: lee090626
tags: [React, TypeScript, Next.js]
generated: auto
merged_at: 2026-11-16T14:49:49Z
---

# Warn when building without a valid SITE_URL

## 개요

lee090626/travel-discovery의 변경입니다. 파일 3개 (+21/-12), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Warn when building without a valid SITE_URL

## 사용 기술

`React` · `TypeScript` · `Next.js`

## 변경 파일

- `lib/seo.tsx` — 수정 +2 / -12
- `lib/site-origin.ts` — 추가 +13 / -0
- `next.config.ts` — 수정 +6 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
문제 `SITE_URL`이 없거나 https 주소가 아니면 빌드가 조용히 색인 차단 모드로 바뀌었습니다. 이 모드에서는 사이트 전체에 `noindex`가 붙고, 사이트맵이 비고, canonical이 사라집니다. 배포 환경변수 하나만 빠져도 사이트가 검색에서 통째로 빠질 수 있었고, 그걸 알려주는 신호가 없었습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: lib/seo.tsx, lib/site-origin.ts, next.config.ts

## 커밋

- `de23744` Warn when building without a valid SITE_URL

## 성과 및 배운 점

- 변경 파일 3개, +21 / -12
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#21](https://github.com/lee090626/travel-discovery/pull/21) · `scripts/devlog.py entry`

---
project: TEAM-DSLIVE/daeso-live-web
source: https://github.com/TEAM-DSLIVE/daeso-live-web/pull/3
date: 2026-09-15
pr: 3
author: lee090626
tags: [TypeScript, React]
generated: auto
merged_at: 2026-09-15T03:17:38Z
---

# proxy API requests for AID deployment

## 개요

TEAM-DSLIVE/daeso-live-web의 변경입니다. 파일 9개 (+129/-43), 커밋 4개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- fix: proxy API requests for AID deployment
- fix: read AID token from WebView URL
- fix: use the AID WebView token query
- fix: route AID API traffic through CORS proxy

## 사용 기술

`TypeScript` · `React`

## 변경 파일

- `api/proxy.ts` — 추가 +61 / -0
- `src/app/session.tsx` — 수정 +19 / -41
- `src/shared/api.ts` — 수정 +13 / -2
- `test/model.test.mjs` — 수정 +12 / -0
- `.env.example` — 추가 +10 / -0
- `src/app/aid-auth.ts` — 추가 +4 / -0
- `src/shared/api-base.ts` — 추가 +4 / -0
- `src/vite-env.d.ts` — 수정 +3 / -0
- `vercel.json` — 추가 +3 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
PR #2 merge 이후의 후속 프론트 배포 수정입니다. - Vercel API proxy로 /api/v1/* HTTP 요청의 cross-origin 문제를 우회 - host-only VITE_SERVER_URL도 HTTPS base URL로 정규화 - AID WebView의 URL token을 읽어 기존 POST /api/v1/auth/login 계약으로 전달 - token은 주소에서 즉시 제거하고 메모리에만 유지 - AID release용 HTTP proxy와 백엔드 WebSocket 주소를 분리

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .env.example, api/proxy.ts, src/app/aid-auth.ts, src/app/session.tsx, src/shared/api-base.ts, src/shared/api.ts

## 커밋

- `1f32c9a` fix: proxy API requests for AID deployment
- `92e2a06` fix: read AID token from WebView URL
- `5c66e8e` fix: use the AID WebView token query
- `885d505` fix: route AID API traffic through CORS proxy

## 성과 및 배운 점

- 변경 파일 9개, +129 / -43
- 커밋 4개

---

> 자동 생성: PR [TEAM-DSLIVE/daeso-live-web#3](https://github.com/TEAM-DSLIVE/daeso-live-web/pull/3) · `scripts/devlog.py entry`

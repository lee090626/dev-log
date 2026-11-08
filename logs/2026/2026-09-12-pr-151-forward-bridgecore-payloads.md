---
project: Team-B1ND/dodam-framework
source: https://github.com/Team-B1ND/dodam-framework/pull/151
date: 2026-09-12
pr: 151
author: lee090626
tags: [TypeScript]
generated: auto
merged_at: 2026-09-12T06:22:03Z
---

# forward BridgeCore payloads

## 개요

Team-B1ND/dodam-framework의 변경입니다. 파일 3개 (+7/-5), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- fix: forward BridgeCore payloads

## 사용 기술

`TypeScript`

## 변경 파일

- `packages/aid-kit/src/bridge-kit/core/models/BridgeCore.ts` — 수정 +5 / -3
- `packages/aid-kit/src/bridge-kit/core/types/app.ts` — 수정 +1 / -1
- `packages/aid-kit/src/bridge-kit/shared/types/enums/error.ts` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
BridgeCore가 미니앱 요청 payload를 앱 handler에 전달하도록 수정했습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: packages/aid-kit/src/bridge-kit/core/models/BridgeCore.ts, packages/aid-kit/src/bridge-kit/core/types/app.ts, packages/aid-kit/src/bridge-kit/shared/types/enums/error.ts

## 커밋

- `c29f1a7` fix: forward BridgeCore payloads

## 성과 및 배운 점

- 변경 파일 3개, +7 / -5
- 커밋 1개

---

> 자동 생성: PR [Team-B1ND/dodam-framework#151](https://github.com/Team-B1ND/dodam-framework/pull/151) · `scripts/devlog.py entry`

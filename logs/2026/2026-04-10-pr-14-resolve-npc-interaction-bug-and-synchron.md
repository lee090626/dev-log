---
project: lee090626/Project-A
source: https://github.com/lee090626/Project-A/pull/14
date: 2026-04-10
pr: 14
author: lee090626
tags: [React, TypeScript]
generated: auto
merged_at: 2026-04-10T09:44:43Z
---

# resolve NPC interaction bug and synchronize UI state

## 개요

lee090626/Project-A의 변경입니다. 파일 5개 (+90/-44), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- fix: resolve NPC interaction bug and synchronize UI state

## 사용 기술

`React` · `TypeScript`

## 변경 파일

- `src/features/game/ecs/systems/interactionSystem.ts` — 수정 +54 / -40
- `src/shared/lib/store.ts` — 수정 +15 / -0
- `src/features/game/components/GameOverlay.tsx` — 수정 +12 / -0
- `src/features/game/hooks/useGameWorker.ts` — 수정 +8 / -4
- `src/features/game/ecs/systems/GameLoop.ts` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
📝 버그 수정 내역 - NPC 중심점 좌표 수식 보정 (y - h/2 -> y + h/2) - 상호작용 사거리 최적화 및 완화 - 워커와 메인 스레드 간 UI 상태(Prompt) 실시간 동기화 (SYNC_UI) - GameOverlay에 상호작용 안내창 렌더링 추가 - 모달창이 오버레이에 정상적으로 뜨도록 OPEN_MODAL 브릿지 구현

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: src/features/game/components/GameOverlay.tsx, src/features/game/ecs/systems/GameLoop.ts, src/features/game/ecs/systems/interactionSystem.ts, src/features/game/hooks/useGameWorker.ts, src/shared/lib/store.ts

## 커밋

- `3c08a7b` fix: resolve NPC interaction bug and synchronize UI state

## 성과 및 배운 점

- 변경 파일 5개, +90 / -44
- 커밋 1개

---

> 자동 생성: PR [lee090626/Project-A#14](https://github.com/lee090626/Project-A/pull/14) · `scripts/devlog.py entry`

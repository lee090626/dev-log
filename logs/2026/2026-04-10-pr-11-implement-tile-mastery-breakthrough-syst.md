---
project: lee090626/Project-A
source: https://github.com/lee090626/Project-A/pull/11
date: 2026-04-10
pr: 11
author: lee090626
tags: [TypeScript, React]
generated: auto
merged_at: 2026-04-10T08:56:31Z
---

# implement tile mastery breakthrough system and add perks for Dirt tiles

## 개요

lee090626/Project-A의 변경입니다. 파일 8개 (+144/-1), 커밋 2개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: implement tile mastery breakthrough system and add perks for Dirt tiles
- fix: add missing PlayerStats fields in world/model.ts to resolve build error

## 사용 기술

`TypeScript` · `React`

## 변경 파일

- `src/shared/config/masteryPerks.ts` — 추가 +51 / -0
- `src/features/game/ecs/systems/miningSystem.ts` — 수정 +33 / -0
- `src/widgets/status/StatusWindow.tsx` — 수정 +26 / -0
- `src/features/game/ecs/systems/physicsSystem.ts` — 수정 +13 / -1
- `src/entities/player/model.ts` — 수정 +12 / -0
- `src/entities/world/model.ts` — 수정 +5 / -0
- `src/shared/types/game.ts` — 수정 +3 / -0
- `src/shared/lib/saveManager.ts` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
📝 구현 개요 마스터리 레벨 50, 100, 150, 200 구간에서 해금되는 돌파 특성 시스템을 구현했습니다. 우선적으로 흙(Dirt) 타일의 특성 트리를 완성하였으며, 다른 타일로 확장 가능한 기반 구조(Config, Stats, Save Migration)를 마련했습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: src/entities/player/model.ts, src/entities/world/model.ts, src/features/game/ecs/systems/miningSystem.ts, src/features/game/ecs/systems/physicsSystem.ts, src/shared/config/masteryPerks.ts, src/shared/lib/saveManager.ts

## 커밋

- `45b0b27` feat: implement tile mastery breakthrough system and add perks for Dirt tiles
- `88c97b0` fix: add missing PlayerStats fields in world/model.ts to resolve build error

## 성과 및 배운 점

- 변경 파일 8개, +144 / -1
- 커밋 2개

---

> 자동 생성: PR [lee090626/Project-A#11](https://github.com/lee090626/Project-A/pull/11) · `scripts/devlog.py entry`

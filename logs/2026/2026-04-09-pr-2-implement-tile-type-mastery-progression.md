---
project: lee090626/Project-A
source: https://github.com/lee090626/Project-A/pull/2
date: 2026-04-09
pr: 2
author: lee090626
tags: [CSS, React, TypeScript]
generated: auto
merged_at: 2026-04-09T13:57:33Z
---

# implement tile-type mastery progression system and overhaul status window UI

## 개요

lee090626/Project-A의 변경입니다. 파일 18개 (+327/-73), 커밋 3개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: implement tile-type mastery progression system and overhaul status window UI
- fix: resolve build errors related to missing tileMastery stats and CSS font face rules
- fix: resolve slottedRunes null safety error in ActionSystem and fix CSS font import order

## 사용 기술

`CSS` · `React` · `TypeScript`

## 변경 파일

- `src/widgets/status/StatusWindow.tsx` — 수정 +82 / -25
- `public/game-init-data.json` — 추가 +89 / -0
- `.github/ISSUE_TEMPLATE/bug_report.md` — 추가 +34 / -0
- `src/features/game/ecs/systems/miningSystem.ts` — 수정 +14 / -12
- `.github/ISSUE_TEMPLATE/feature_request.md` — 추가 +22 / -0
- `.github/PULL_REQUEST_TEMPLATE.md` — 추가 +22 / -0
- `src/shared/lib/masteryUtils.ts` — 수정 +14 / -7
- `src/shared/types/game.ts` — 수정 +11 / -8
- `src/widgets/inventory/Inventory.tsx` — 수정 +8 / -8
- `docs/AI_DEVELOPMENT_GUIDE.md` — 수정 +13 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
주요 변경 사항 - 기존 드릴 기반 숙련도를 제거하고 타일 종류별 숙련도 시스템 도입 - 채굴 시스템(miningSystem.ts)에서 타일 XP 획득 로직 구현 - 데미지 계산기(miningCalculator.ts)에 타일 마법 배수 반영 - 상태창(StatusWindow.tsx) UI 전면 개편 (가로형 전체 너비 마스터리 그리드) - 세이브 시스템 하위 호환성 보정 추가

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/ISSUE_TEMPLATE/bug_report.md, .github/ISSUE_TEMPLATE/feature_request.md, .github/PULL_REQUEST_TEMPLATE.md, docs/AI_DEVELOPMENT_GUIDE.md, public/game-init-data.json, src/app/globals.css

## 커밋

- `c4ffacb` feat: implement tile-type mastery progression system and overhaul status window UI
- `57bd810` fix: resolve build errors related to missing tileMastery stats and CSS font face rules
- `528b0d8` fix: resolve slottedRunes null safety error in ActionSystem and fix CSS font import order

## 성과 및 배운 점

- 변경 파일 18개, +327 / -73
- 커밋 3개

---

> 자동 생성: PR [lee090626/Project-A#2](https://github.com/lee090626/Project-A/pull/2) · `scripts/devlog.py entry`

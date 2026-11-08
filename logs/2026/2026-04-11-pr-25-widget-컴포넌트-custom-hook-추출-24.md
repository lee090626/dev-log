---
project: lee090626/Project-A
source: https://github.com/lee090626/Project-A/pull/25
date: 2026-04-11
pr: 25
author: lee090626
tags: [React, TypeScript]
generated: auto
merged_at: 2026-04-11T09:47:58Z
---

# Widget 컴포넌트 Custom Hook 추출 (#24)

## 개요

lee090626/Project-A의 변경입니다. 파일 4개 (+313/-154), 커밋 2개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- refactor: StatusWindow 스탯 계산 로직을 useStatusStats Hook으로 분리
- refactor: Shop 가챠 연출 로직을 useGachaAnimation Hook으로 분리

## 사용 기술

`React` · `TypeScript`

## 변경 파일

- `src/widgets/status/useStatusStats.ts` — 추가 +152 / -0
- `src/widgets/shop/useGachaAnimation.ts` — 추가 +127 / -0
- `src/widgets/status/StatusWindow.tsx` — 수정 +19 / -86
- `src/widgets/shop/Shop.tsx` — 수정 +15 / -68

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
1. StatusWindow: useStatusStats Hook 추출 - 80줄의 인라인 스탯 계산 로직(공격력, 크리티컬, 이동속도, 행운 등)과 Breakdown 정의를 `useStatusStats` Custom Hook으로 분리 - `useMemo`로 감싸 불필요한 재계산을 방지 - **599줄 → 531줄** (약 -11%)

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: src/widgets/shop/Shop.tsx, src/widgets/shop/useGachaAnimation.ts, src/widgets/status/StatusWindow.tsx, src/widgets/status/useStatusStats.ts

## 커밋

- `3563e92` refactor: StatusWindow 스탯 계산 로직을 useStatusStats Hook으로 분리
- `fe69e55` refactor: Shop 가챠 연출 로직을 useGachaAnimation Hook으로 분리

## 성과 및 배운 점

- 변경 파일 4개, +313 / -154
- 커밋 2개

---

> 자동 생성: PR [lee090626/Project-A#25](https://github.com/lee090626/Project-A/pull/25) · `scripts/devlog.py entry`

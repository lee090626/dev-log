---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/26
date: 2026-11-16
pr: 26
author: lee090626
tags: [React]
generated: auto
merged_at: 2026-11-16T23:49:52Z
---

# Show every ShowMore item when JavaScript is off

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+3/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Show every ShowMore item when JavaScript is off

## 사용 기술

`React`

## 변경 파일

- `components/show-more.tsx` — 수정 +3 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Fixes #23. A `` style un-hides the items past the first 12 and hides the dead button. Checked on /regions/seoul: JS off shows 164 items and no button; JS on is unchanged (12 items + button).

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: components/show-more.tsx

## 커밋

- `aef0ada` Show every ShowMore item when JavaScript is off

## 성과 및 배운 점

- 변경 파일 1개, +3 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#26](https://github.com/lee090626/travel-discovery/pull/26) · `scripts/devlog.py entry`

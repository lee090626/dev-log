---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/14
date: 2026-11-11
pr: 14
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-11T01:12:06Z
---

# Reference App 세 작업 확장과 변경·실패·복구 테스트

## 개요

lee090626/synthetix의 변경입니다. 파일 4개 (+336/-113), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: Reference App에 T1·T3 연결, 세 작업의 변경·실패·복구 테스트

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/tests/policy_change.rs` — 수정 +292 / -110
- `examples/policy-calculator/main.ax` — 수정 +23 / -1
- `examples/policy-calculator/policy.ax` — 수정 +14 / -0
- `examples/policy-calculator/README.md` — 수정 +7 / -2

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 - `examples/policy-calculator`: `base_amount`(T1, 단가×수량)와 `items_total`(T3, 네 항목 합계) 계약 추가. 앱에서 T1 또는 T3 결과가 `total`에 들어가고, 정책 버튼(T2/C1)이 그 값에 적용됨. 입력은 모두 persist. - `crates/axiom-cli/tests/policy_change.rs`: 시나리오 하나 → 세 작업 시나리오로 일반화

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/tests/policy_change.rs, examples/policy-calculator/README.md, examples/policy-calculator/main.ax, examples/policy-calculator/policy.ax

## 커밋

- `3e17f69` feat: Reference App에 T1·T3 연결, 세 작업의 변경·실패·복구 테스트

## 성과 및 배운 점

- 변경 파일 4개, +336 / -113
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#14](https://github.com/lee090626/synthetix/pull/14) · `scripts/devlog.py entry`

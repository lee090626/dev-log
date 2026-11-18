---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/156
date: 2026-11-18
pr: 156
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-18T08:25:16Z
---

# promise 반례 + axiom check --report JSON (3.0 C1)

## 개요

lee090626/synthetix의 변경입니다. 파일 3개 (+127/-5), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: promise 반례, axiom check --report JSON

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/src/main.rs` — 수정 +75 / -3
- `crates/axiom-cli/src/web.rs` — 수정 +42 / -2
- `docs/writing-specs.md` — 수정 +10 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
틀린 promise: 답만 정하는 규칙으로 후보를 찾고, promise 하나씩 `verify` → 첫 반례를 `promise 2 does not hold for total=294896131 (answer 268087391)`로 출력 (실패할 때만 추가 비용) - `axiom check --report check.json`: `{ok}` 또는 `{ok:false, error:{message, file, rule, line, promise, inputs, answer, hint}}`. 메시지 원문은 그대로, 아는 부분만 필드로 (기존 --report 방식과 같음) - 문서 추가

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/main.rs, crates/axiom-cli/src/web.rs, docs/writing-specs.md

## 커밋

- `029c299` feat: promise 반례, axiom check --report JSON

## 성과 및 배운 점

- 변경 파일 3개, +127 / -5
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#156](https://github.com/lee090626/synthetix/pull/156) · `scripts/devlog.py entry`

---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/130
date: 2026-11-18
pr: 130
author: lee090626
tags: [JavaScript, Rust]
generated: auto
merged_at: 2026-11-18T01:02:57Z
---

# 모임 정산 A~E — 예/아니오, settle, 송금 목록·복사·기록, group-settle 예제

## 개요

lee090626/synthetix의 변경입니다. 파일 14개 (+550/-8), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 모임 정산 — 예/아니오 입력, settle, 송금 목록·복사·기록, group-settle 예제

## 사용 기술

`JavaScript` · `Rust`

## 변경 파일

- `crates/axiom-parser/src/simple.rs` — 수정 +171 / -4
- `crates/axiom-cli/tests/group_settle.rs` — 추가 +123 / -0
- `crates/axiom-cli/tests/settle_property.rs` — 추가 +60 / -0
- `crates/axiom-cli/src/runtime.js` — 수정 +43 / -0
- `examples/group-settle/main.ax` — 추가 +33 / -0
- `crates/axiom-parser/src/parser.rs` — 수정 +24 / -0
- `examples/group-settle/rules.ax` — 추가 +24 / -0
- `examples/group-settle/README.md` — 추가 +23 / -0
- `crates/axiom-cli/src/web.rs` — 수정 +14 / -0
- `docs/writing-specs.md` — 수정 +14 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
읽기 시험 안 함:** 이 PR의 새 문법(`= yes/no`, `settle(owe)`, `show transfers(sends, names)`)과 예제 규칙은 Claude가 정했고 사용자 읽기 시험을 거치지 않았습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/runtime.js, crates/axiom-cli/src/web.rs, crates/axiom-cli/tests/group_settle.rs, crates/axiom-cli/tests/settle_property.rs, crates/axiom-parser/src/ast.rs, crates/axiom-parser/src/parser.rs

## 커밋

- `583bd8d` feat: 모임 정산 — 예/아니오 입력, settle, 송금 목록·복사·기록, group-settle 예제

## 성과 및 배운 점

- 변경 파일 14개, +550 / -8
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#130](https://github.com/lee090626/synthetix/pull/130) · `scripts/devlog.py entry`

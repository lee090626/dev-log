---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/141
date: 2026-11-18
pr: 141
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-18T05:51:45Z
---

# 규칙 파일에서 settle 쓰기, TS settle(owe) 내보내기

## 개요

lee090626/synthetix의 변경입니다. 파일 4개 (+72/-6), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 규칙 파일의 use settle for N, TS settle(owe) 내보내기

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/src/js.rs` — 수정 +37 / -0
- `crates/axiom-parser/src/simple.rs` — 수정 +20 / -1
- `crates/axiom-cli/tests/js_emit.rs` — 수정 +11 / -5
- `docs/writing-specs.md` — 수정 +4 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
규칙 파일에 `use settle for N` (2~16): settle_N_i_j와 보조 정리를 증명해 넣음 - `--emit js`: `settle(owe: number[]): number[]` (길이로 N 선택) - 정산 함수 줄 단위 묶음(settle_4_1 등)은 더 이상 만들지 않음

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/js.rs, crates/axiom-cli/tests/js_emit.rs, crates/axiom-parser/src/simple.rs, docs/writing-specs.md

## 커밋

- `c180100` feat: 규칙 파일의 use settle for N, TS settle(owe) 내보내기

## 성과 및 배운 점

- 변경 파일 4개, +72 / -6
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#141](https://github.com/lee090626/synthetix/pull/141) · `scripts/devlog.py entry`

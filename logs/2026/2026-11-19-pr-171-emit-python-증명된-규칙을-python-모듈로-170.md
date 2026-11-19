---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/171
date: 2026-11-19
pr: 171
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-19T02:09:12Z
---

# --emit python: 증명된 규칙을 Python 모듈로 (#170)

## 개요

lee090626/synthetix의 변경입니다. 파일 6개 (+490/-5), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: --emit python (#170)

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/src/py.rs` — 추가 +279 / -0
- `crates/axiom-cli/tests/py_emit.rs` — 추가 +189 / -0
- `crates/axiom-cli/src/web.rs` — 수정 +10 / -1
- `docs/writing-specs.md` — 수정 +8 / -2
- `crates/axiom-cli/src/main.rs` — 수정 +3 / -1
- `examples/invoice/README.md` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`axiom build --emit python` → `dist/contracts.py` (표준 라이브러리만) - 연산마다 32비트(`with big numbers`는 64비트)로 잘라 `Expr::try_eval_bits`와 같은 의미. 부호 있는 나눗셈은 0 방향 버림, 0으로 나누기·overflow는 `AxiomError` - 입력 검사: 정수 범위·`bool` 구분은 `TypeError`, `need` 위반은 `AxiomError` - 목록 규칙·`settle` 래퍼는 JS/Rust와 같은 규칙(`list_parts`, `param_groups`, `settle_sizes` 재사용) - 문서·invoice README 갱신

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/main.rs, crates/axiom-cli/src/py.rs, crates/axiom-cli/src/web.rs, crates/axiom-cli/tests/py_emit.rs, docs/writing-specs.md, examples/invoice/README.md

## 커밋

- `138a4e0` feat: --emit python (#170)

## 성과 및 배운 점

- 변경 파일 6개, +490 / -5
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#171](https://github.com/lee090626/synthetix/pull/171) · `scripts/devlog.py entry`

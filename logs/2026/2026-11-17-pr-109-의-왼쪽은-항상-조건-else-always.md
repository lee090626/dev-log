---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/109
date: 2026-11-17
pr: 109
author: lee090626
tags: [Rust, JavaScript]
generated: auto
merged_at: 2026-11-17T11:42:42Z
---

# !: ->의 왼쪽은 항상 조건, else, always

## 개요

lee090626/synthetix의 변경입니다. 파일 13개 (+178/-119), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat(syntax)!: ->의 왼쪽은 항상 조건, else, always

## 사용 기술

`Rust` · `JavaScript`

## 변경 파일

- `crates/axiom-parser/src/simple.rs` — 수정 +114 / -63
- `crates/axiom-cli/tests/simple_differential.rs` — 수정 +20 / -20
- `docs/writing-specs.md` — 수정 +12 / -10
- `crates/axiom-verify/src/lib.rs` — 수정 +9 / -9
- `crates/axiom-cli/tests/simple_page.rs` — 수정 +5 / -5
- `editors/vscode/extension.js` — 수정 +7 / -1
- `examples/policy-calculator/policy.ax` — 수정 +4 / -4
- `editors/vscode/snippets/axiom.json` — 수정 +2 / -2
- `README.md` — 수정 +1 / -1
- `docs/limitations.md` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
왜 읽기 시험에서 조건 없는 `-> value`를 문법을 모르면 읽을 수 없었습니다. `->`가 두 가지 뜻(조건이면 답 / 그냥 답)으로 쓰여서입니다. 사용자가 고른 ①안을 적용합니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: README.md, crates/axiom-cli/tests/simple_differential.rs, crates/axiom-cli/tests/simple_page.rs, crates/axiom-parser/src/simple.rs, crates/axiom-verify/src/lib.rs, docs/limitations.md

## 커밋

- `0b1acdf` feat(syntax)!: ->의 왼쪽은 항상 조건, else, always

## 성과 및 배운 점

- 변경 파일 13개, +178 / -119
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#109](https://github.com/lee090626/synthetix/pull/109) · `scripts/devlog.py entry`

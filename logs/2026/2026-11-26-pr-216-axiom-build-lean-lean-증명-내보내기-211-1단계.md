---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/216
date: 2026-11-26
pr: 216
author: lee090626
tags: [GitHub Actions, Rust]
generated: auto
merged_at: 2026-11-26T00:28:22Z
---

# axiom build --lean — Lean 증명 내보내기 (#211 1단계)

## 개요

lee090626/synthetix의 변경입니다. 파일 7개 (+666/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: axiom build --lean으로 규칙 증명을 Lean bv_decide로 검사 (#211 1단계)

## 사용 기술

`GitHub Actions` · `Rust`

## 변경 파일

- `crates/axiom-verify/src/lean.rs` — 추가 +548 / -0
- `crates/axiom-cli/tests/lean_export.rs` — 추가 +45 / -0
- `crates/axiom-cli/src/main.rs` — 수정 +42 / -0
- `proofs/lean/generated/fit_price.lean` — 추가 +14 / -0
- `proofs/lean/generated/web_counter.lean` — 추가 +14 / -0
- `.github/workflows/ci.yml` — 수정 +2 / -1
- `crates/axiom-verify/src/lib.rs` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Part of #211 (M1 Lean 백엔드). #211은 열어 둡니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml, crates/axiom-cli/src/main.rs, crates/axiom-cli/tests/lean_export.rs, crates/axiom-verify/src/lean.rs, crates/axiom-verify/src/lib.rs, proofs/lean/generated/fit_price.lean

## 커밋

- `9352d3a` feat: axiom build --lean으로 규칙 증명을 Lean bv_decide로 검사 (#211 1단계)

## 성과 및 배운 점

- 변경 파일 7개, +666 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#216](https://github.com/lee090626/synthetix/pull/216) · `scripts/devlog.py entry`

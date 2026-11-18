---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/147
date: 2026-11-18
pr: 147
author: lee090626
tags: [GitHub Actions, Rust]
generated: auto
merged_at: 2026-11-18T06:35:36Z
---

# proof: settle 후 모두 0원 — Lean 증명

## 개요

lee090626/synthetix의 변경입니다. 파일 7개 (+215/-55), 커밋 3개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- proof: settle 후 모두 0원을 Lean으로 증명 (인원 수 무관)
- settle: Z3 증명 대신 Lean 일반정리를 근거로 (인원 상한 21)
- fix: settle fn에 문법상 필요한 ensures 한 줄

## 사용 기술

`GitHub Actions` · `Rust`

## 변경 파일

- `proofs/lean/Settle.lean` — 추가 +176 / -0
- `crates/axiom-parser/src/simple.rs` — 수정 +13 / -47
- `.github/workflows/ci.yml` — 수정 +15 / -0
- `docs/writing-specs.md` — 수정 +7 / -5
- `docs/limitations.md` — 수정 +2 / -2
- `examples/group-settle/README.md` — 수정 +1 / -1
- `proofs/lean/lean-toolchain` — 추가 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
원칙: **내장 기능은 Lean으로 한 번 증명, 사용자 규칙은 Z3로 매번 자동 증명.**

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml, crates/axiom-parser/src/simple.rs, docs/limitations.md, docs/writing-specs.md, examples/group-settle/README.md, proofs/lean/Settle.lean

## 커밋

- `143768e` proof: settle 후 모두 0원을 Lean으로 증명 (인원 수 무관)
- `a31d464` settle: Z3 증명 대신 Lean 일반정리를 근거로 (인원 상한 21)
- `98fc26a` fix: settle fn에 문법상 필요한 ensures 한 줄

## 성과 및 배운 점

- 변경 파일 7개, +215 / -55
- 커밋 3개

---

> 자동 생성: PR [lee090626/synthetix#147](https://github.com/lee090626/synthetix/pull/147) · `scripts/devlog.py entry`

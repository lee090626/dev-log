---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/197
date: 2026-11-24
pr: 197
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-24T10:21:46Z
---

# 나눈 몫의 합 약속 sum(answer) <= total (#196)

## 개요

lee090626/synthetix의 변경입니다. 파일 5개 (+73/-2), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 나눈 몫의 합 약속 share sum(answer) <= total (#196)

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-parser/src/lists.rs` — 수정 +44 / -1
- `proofs/lean/Lists.lean` — 수정 +23 / -0
- `docs/writing-specs.md` — 수정 +4 / -1
- `examples/any-length/README.md` — 수정 +1 / -0
- `examples/any-length/rules.ax` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`always -> total * weights / sum(weights)`인 목록 답에서 `promise sum(answer) <= y`를 증명한다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-parser/src/lists.rs, docs/writing-specs.md, examples/any-length/README.md, examples/any-length/rules.ax, proofs/lean/Lists.lean

## 커밋

- `63719d0` feat: 나눈 몫의 합 약속 share sum(answer) <= total (#196)

## 성과 및 배운 점

- 변경 파일 5개, +73 / -2
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#197](https://github.com/lee090626/synthetix/pull/197) · `scripts/devlog.py entry`

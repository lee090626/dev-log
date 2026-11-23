---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/193
date: 2026-11-23
pr: 193
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-23T07:51:39Z
---

# 합 사이 관계 sum(a - b) = sum(a) - sum(b) (#192)

## 개요

lee090626/synthetix의 변경입니다. 파일 5개 (+209/-26), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 합 사이 관계 sum(a - b) = sum(a) - sum(b) (#192)

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-parser/src/lists.rs` — 수정 +165 / -22
- `proofs/lean/Lists.lean` — 수정 +27 / -0
- `docs/writing-specs.md` — 수정 +7 / -4
- `examples/any-length/rules.ax` — 수정 +9 / -0
- `examples/any-length/README.md` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 - `sum(식)`의 항목 식이 목록 항목·입력·숫자의 `+ - *`(곱 하나에 목록 항목 최대 하나)이면, core가 그 합을 목록별 합으로 나타낸 관계를 전제함. 예: `sum(paid - 2 * share + fee)` → `sum1 + 2 * sum3 is 1 * sum2 + n * fee`. - 뺄 항은 반대편으로 옮겨 덧셈만 씀 → 부호 없는 규칙에서도 조건식이 정의됨. - 필요한 `sum(paid)`이 없으면 범위에 맞을 때 내부 입력으로 추가(넘치면 관계 없이 기존대로). - 근거(Lean, `proofs/lean/Lists.lean`): `sum_add`, `sum_mul`, `sum_const`, `sum_emod`. `+ - *`는 2^w 나머지를 보존하므로 넘침과 무관하게 참. - `/`나 목록끼리 곱은 관계 없음(기존 동작). - 예제 `net`(4개 언어 차등 테스트가 검사), 문서 한계 문단 갱신.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-parser/src/lists.rs, docs/writing-specs.md, examples/any-length/README.md, examples/any-length/rules.ax, proofs/lean/Lists.lean

## 커밋

- `e677f68` feat: 합 사이 관계 sum(a - b) = sum(a) - sum(b) (#192)

## 성과 및 배운 점

- 변경 파일 5개, +209 / -26
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#193](https://github.com/lee090626/synthetix/pull/193) · `scripts/devlog.py entry`

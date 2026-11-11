---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/23
date: 2026-11-11
pr: 23
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-11T06:10:32Z
---

# develop → main: 내부 계획 문서 추적 제외

## 개요

lee090626/synthetix의 변경입니다. 파일 7개 (+7/-438), 커밋 4개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- docs: 로드맵을 저장소 추적에서 제외
- docs: 내부 계획 문서를 저장소 추적에서 제외

## 사용 기술

`Rust`

## 변경 파일

- `docs/roadmap.md` — 삭제 +0 / -197
- `docs/architecture.md` — 삭제 +0 / -190
- `docs/first-product/requirements.md` — 삭제 +0 / -47
- `.gitignore` — 수정 +5 / -0
- `README.md` — 수정 +0 / -2
- `crates/axiom-cli/tests/policy_change.rs` — 수정 +1 / -1
- `examples/policy-calculator/README.md` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
20 로드맵 추적 제외 (#19) - #22 requirements.md, architecture.md 추적 제외 (#21)

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .gitignore, README.md, crates/axiom-cli/tests/policy_change.rs, docs/architecture.md, docs/first-product/requirements.md, docs/roadmap.md

## 커밋

- `23fd2e5` docs: 로드맵을 저장소 추적에서 제외
- `868c6fe` Merge pull request #20 from lee090626/docs/untrack-roadmap
- `8697b9e` docs: 내부 계획 문서를 저장소 추적에서 제외
- `afb00d6` Merge pull request #22 from lee090626/docs/untrack-internal

## 성과 및 배운 점

- 변경 파일 7개, +7 / -438
- 커밋 4개

---

> 자동 생성: PR [lee090626/synthetix#23](https://github.com/lee090626/synthetix/pull/23) · `scripts/devlog.py entry`

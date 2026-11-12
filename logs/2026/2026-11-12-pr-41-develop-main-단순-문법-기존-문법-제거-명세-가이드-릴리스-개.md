---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/41
date: 2026-11-12
pr: 41
author: lee090626
tags: [GitHub Actions, Rust]
generated: auto
merged_at: 2026-11-12T02:43:30Z
---

# develop → main: 단순 문법, 기존 문법 제거, 명세 가이드, 릴리스 개선

## 개요

lee090626/synthetix의 변경입니다. 파일 73개 (+1041/-229), 커밋 6개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- docs: 명세 작성 가이드
- feat: 읽기 쉬운 단순 문법 추가
- feat: 화면 단순 문법, 기존 문법 제거, 뺄셈 검사 개선

## 사용 기술

`GitHub Actions` · `Rust`

## 변경 파일

- `crates/axiom-parser/src/simple.rs` — 추가 +738 / -0
- `README.md` — 수정 +28 / -87
- `docs/writing-specs.md` — 추가 +104 / -0
- `examples/policy-calculator/main.ax` — 수정 +21 / -39
- `examples/policy-calculator/policy.ax` — 수정 +30 / -27
- `crates/axiom-synth/src/lib.rs` — 수정 +17 / -17
- `docs/limitations.md` — 수정 +11 / -15
- `.github/workflows/release.yml` — 수정 +10 / -7
- `crates/axiom-parser/src/lib.rs` — 수정 +17 / -0
- `crates/axiom-verify/src/lib.rs` — 수정 +7 / -7

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
PR 본문에 문제 설명이 없습니다. 아래 변경 파일과 커밋으로 확인합니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .cargo/config.toml, .github/workflows/release.yml, README.md, crates/axiom-application/src/lib.rs, crates/axiom-cli/src/main.rs, crates/axiom-cli/src/web.rs

## 커밋

- `ce89348` docs: 명세 작성 가이드
- `8628822` Merge pull request #36 from lee090626/docs/writing-specs
- `462f7d6` feat: 읽기 쉬운 단순 문법 추가
- `7a0e7d4` Merge pull request #38 from lee090626/feat/simple-syntax
- `dd69e30` feat: 화면 단순 문법, 기존 문법 제거, 뺄셈 검사 개선
- `305cf99` Merge pull request #40 from lee090626/feat/simple-only

## 성과 및 배운 점

- 변경 파일 73개, +1041 / -229
- 커밋 6개

---

> 자동 생성: PR [lee090626/synthetix#41](https://github.com/lee090626/synthetix/pull/41) · `scripts/devlog.py entry`

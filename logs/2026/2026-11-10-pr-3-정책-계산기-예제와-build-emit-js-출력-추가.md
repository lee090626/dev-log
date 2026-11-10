---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/3
date: 2026-11-10
pr: 3
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-10T03:06:40Z
private: true
---

# 정책 계산기 예제와 build --emit js 출력 추가

## 개요

lee090626/synthetix의 변경입니다. 파일 7개 (+422/-1), 커밋 2개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 정책 계산기 브라우저 세로 흐름 예제 추가
- feat: build --emit js로 검증된 후보를 JavaScript와 d.ts로 출력

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/src/js.rs` — 추가 +211 / -0
- `crates/axiom-cli/tests/js_emit.rs` — 추가 +129 / -0
- `crates/axiom-cli/src/main.rs` — 수정 +26 / -1
- `examples/policy-calculator/main.ax` — 추가 +22 / -0
- `examples/policy-calculator/policy.ax` — 추가 +16 / -0
- `examples/policy-calculator/README.md` — 추가 +15 / -0
- `examples/policy-calculator/synthetix.toml` — 추가 +3 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
첫 제품 로드맵의 다음 목표(브라우저 세로 흐름)를 위한 두 가지 변경입니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/js.rs, crates/axiom-cli/src/main.rs, crates/axiom-cli/tests/js_emit.rs, examples/policy-calculator/README.md, examples/policy-calculator/main.ax, examples/policy-calculator/policy.ax

## 커밋

- `cf7fe6b` feat: 정책 계산기 브라우저 세로 흐름 예제 추가
- `becbedf` feat: build --emit js로 검증된 후보를 JavaScript와 d.ts로 출력

## 성과 및 배운 점

- 변경 파일 7개, +422 / -1
- 커밋 2개

---

> 자동 생성: PR [lee090626/synthetix#3](https://github.com/lee090626/synthetix/pull/3) · `scripts/devlog.py entry`

---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/59
date: 2026-11-12
pr: 59
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-12T08:01:18Z
---

# ci: 테스트 최적화 빌드와 nextest 병렬 실행

## 개요

lee090626/synthetix의 변경입니다. 파일 2개 (+14/-3), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: 테스트 최적화 빌드와 nextest 병렬 실행

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/ci.yml` — 수정 +7 / -3
- `Cargo.toml` — 수정 +7 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`[profile.test] opt-level=1`, 의존성(z3 등) `opt-level=2`: 로컬 simple_differential 50.0s → 6.6s - CI: `cargo nextest`로 테스트 바이너리 병렬 실행, doctest는 `cargo test --doc`으로 별도 실행 - fmt 검사를 캐시 복원 전으로 이동

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml, Cargo.toml

## 커밋

- `9ed579d` ci: 테스트 최적화 빌드와 nextest 병렬 실행

## 성과 및 배운 점

- 변경 파일 2개, +14 / -3
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#59](https://github.com/lee090626/synthetix/pull/59) · `scripts/devlog.py entry`

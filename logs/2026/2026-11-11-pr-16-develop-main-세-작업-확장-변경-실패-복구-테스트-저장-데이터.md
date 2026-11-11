---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/16
date: 2026-11-11
pr: 16
author: lee090626
tags: [GitHub Actions, Rust]
generated: auto
merged_at: 2026-11-11T02:04:02Z
---

# develop → main: 세 작업 확장, 변경·실패·복구 테스트, 저장 데이터 보존

## 개요

lee090626/synthetix의 변경입니다. 파일 6개 (+447/-9), 커밋 8개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- test: C1 정책 변경·실패·복구 흐름 통합 테스트
- feat: Reference App에 T1·T3 연결, 세 작업의 변경·실패·복구 테스트
- fix: 저장 상태 로드 실패 시 저장 중단, dev 빌드 상태 확인이 실행 오류를 지우지 않게
- ci: main에서도 rust-cache 저장

## 사용 기술

`GitHub Actions` · `Rust`

## 변경 파일

- `crates/axiom-cli/tests/policy_change.rs` — 추가 +361 / -0
- `crates/axiom-cli/src/web.rs` — 수정 +37 / -5
- `examples/policy-calculator/main.ax` — 수정 +23 / -1
- `examples/policy-calculator/policy.ax` — 수정 +14 / -0
- `examples/policy-calculator/README.md` — 수정 +11 / -2
- `.github/workflows/ci.yml` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
11 C1 정책 변경·실패·복구 통합 테스트 - #14 Reference App 세 작업(T1·T2/C1·T3) 확장, 세 작업의 변경·실패·복구 테스트 (#12) - #15 저장 상태 로드 실패 시 저장 중단, dev 빌드 상태 확인이 실행 오류를 지우지 않게 (#13)

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml, crates/axiom-cli/src/web.rs, crates/axiom-cli/tests/policy_change.rs, examples/policy-calculator/README.md, examples/policy-calculator/main.ax, examples/policy-calculator/policy.ax

## 커밋

- `24c389a` test: C1 정책 변경·실패·복구 흐름 통합 테스트
- `f13b4b8` Merge pull request #11 from lee090626/test/policy-change
- `3e17f69` feat: Reference App에 T1·T3 연결, 세 작업의 변경·실패·복구 테스트
- `974b599` Merge pull request #14 from lee090626/feat/12-three-tasks
- `baec1bc` fix: 저장 상태 로드 실패 시 저장 중단, dev 빌드 상태 확인이 실행 오류를 지우지 않게
- `2eaca66` Merge pull request #15 from lee090626/test/13-browser-persistence
- `3ed7996` ci: main에서도 rust-cache 저장
- `111cf29` Merge pull request #18 from lee090626/ci/main-cache

## 성과 및 배운 점

- 변경 파일 6개, +447 / -9
- 커밋 8개

---

> 자동 생성: PR [lee090626/synthetix#16](https://github.com/lee090626/synthetix/pull/16) · `scripts/devlog.py entry`

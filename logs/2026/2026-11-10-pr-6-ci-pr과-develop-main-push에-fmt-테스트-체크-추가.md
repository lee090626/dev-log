---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/6
date: 2026-11-10
pr: 6
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-10T08:39:00Z
---

# ci: PR과 develop/main push에 fmt·테스트 체크 추가

## 개요

lee090626/synthetix의 변경입니다. 파일 1개 (+33/-0), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: PR과 develop/main push에 fmt·테스트 체크 추가

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/ci.yml` — 추가 +33 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`.github/workflows/ci.yml`을 추가합니다. 모든 PR과 `develop`/`main` push에서 `cargo fmt --all -- --check`와 `cargo test --locked --workspace`를 실행합니다(ubuntu, Rust·Z3 빌드 캐시 사용).

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml

## 커밋

- `88477e1` ci: PR과 develop/main push에 fmt·테스트 체크 추가

## 성과 및 배운 점

- 변경 파일 1개, +33 / -0
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#6](https://github.com/lee090626/synthetix/pull/6) · `scripts/devlog.py entry`

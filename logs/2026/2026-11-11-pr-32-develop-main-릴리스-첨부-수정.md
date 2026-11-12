---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/32
date: 2026-11-11
pr: 32
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-11T23:41:02Z
---

# develop → main: 릴리스 첨부 수정

## 개요

lee090626/synthetix의 변경입니다. 파일 1개 (+12/-1), 커밋 4개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: 릴리스에 CLI와 VSIX 아티팩트만 첨부
- ci: 릴리스 테스트가 CI 캐시를 재사용

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/release.yml` — 수정 +12 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
PR 본문에 문제 설명이 없습니다. 아래 변경 파일과 커밋으로 확인합니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/release.yml

## 커밋

- `5696469` ci: 릴리스에 CLI와 VSIX 아티팩트만 첨부
- `2cdf6e0` Merge pull request #31 from lee090626/ci/release-assets
- `e5fe256` ci: 릴리스 테스트가 CI 캐시를 재사용
- `7b6e937` Merge pull request #34 from lee090626/ci/release-cache

## 성과 및 배운 점

- 변경 파일 1개, +12 / -1
- 커밋 4개

---

> 자동 생성: PR [lee090626/synthetix#32](https://github.com/lee090626/synthetix/pull/32) · `scripts/devlog.py entry`

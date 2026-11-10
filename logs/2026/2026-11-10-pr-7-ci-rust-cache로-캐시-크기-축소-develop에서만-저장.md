---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/7
date: 2026-11-10
pr: 7
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-10T11:01:10Z
---

# ci: rust-cache로 캐시 크기 축소, develop에서만 저장

## 개요

lee090626/synthetix의 변경입니다. 파일 1개 (+7/-8), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: rust-cache로 캐시 크기 축소, develop에서만 저장

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/ci.yml` — 수정 +7 / -8

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`actions/cache`(target 전체, 2.68GiB)를 `Swatinem/rust-cache@v2`로 바꿉니다. 워크스페이스 크레이트 산출물을 빼고 의존성(Z3 포함) 빌드 결과만 캐시합니다. - `CARGO_INCREMENTAL=0`, `CARGO_PROFILE_DEV_DEBUG=0`으로 CI 빌드의 증분 산출물과 디버그 정보를 끕니다. - 캐시 저장은 `develop` push에서만 합니다. PR은 `develop` 캐시를 읽기만 해서 브랜치별 중복 캐시가 쌓이지 않습니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml

## 커밋

- `402f80e` ci: rust-cache로 캐시 크기 축소, develop에서만 저장

## 성과 및 배운 점

- 변경 파일 1개, +7 / -8
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#7](https://github.com/lee090626/synthetix/pull/7) · `scripts/devlog.py entry`

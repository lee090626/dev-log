---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/67
date: 2026-11-14
pr: 67
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-14T10:26:42Z
---

# ci: npm 배포를 Trusted Publishing(OIDC)으로 전환

## 개요

lee090626/synthetix의 변경입니다. 파일 2개 (+9/-10), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: npm 배포를 Trusted Publishing(OIDC)으로 전환

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/release.yml` — 수정 +5 / -7
- `docs/setup.md` — 수정 +4 / -3

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`publish-npm`: `NPM_TOKEN` 제거, npm 11(Trusted Publishing 지원)로 OIDC 배포. provenance는 자동 생성 - `docs/setup.md`: Trusted Publisher 설정 안내

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/release.yml, docs/setup.md

## 커밋

- `ef3adff` ci: npm 배포를 Trusted Publishing(OIDC)으로 전환

## 성과 및 배운 점

- 변경 파일 2개, +9 / -10
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#67](https://github.com/lee090626/synthetix/pull/67) · `scripts/devlog.py entry`

---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/75
date: 2026-11-14
pr: 75
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-14T13:46:55Z
---

# ci: Open VSX 배포 추가

## 개요

lee090626/synthetix의 변경입니다. 파일 2개 (+23/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: Open VSX 배포 추가

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/release.yml` — 수정 +20 / -0
- `docs/setup.md` — 수정 +3 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
태그마다 `npx ovsx publish`로 Open VSX에 .vsix 배포. OIDC trusted publishing 사용, 첫 버전만 `OVSX_PAT` 필요.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/release.yml, docs/setup.md

## 커밋

- `3c28497` ci: Open VSX 배포 추가

## 성과 및 배운 점

- 변경 파일 2개, +23 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#75](https://github.com/lee090626/synthetix/pull/75) · `scripts/devlog.py entry`

---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/73
date: 2026-11-14
pr: 73
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-14T13:28:39Z
---

# ci: VSCE_PAT 없으면 Marketplace 배포 건너뛰기

## 개요

lee090626/synthetix의 변경입니다. 파일 2개 (+6/-5), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: VSCE_PAT 없으면 Marketplace 배포 건너뛰기

## 사용 기술

`GitHub Actions`

## 변경 파일

- `docs/setup.md` — 수정 +4 / -3
- `.github/workflows/release.yml` — 수정 +2 / -2

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Marketplace는 큰 업데이트 때 수동 업로드. secret 없으면 notice만 남기고 성공 처리.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/release.yml, docs/setup.md

## 커밋

- `365aa86` ci: VSCE_PAT 없으면 Marketplace 배포 건너뛰기

## 성과 및 배운 점

- 변경 파일 2개, +6 / -5
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#73](https://github.com/lee090626/synthetix/pull/73) · `scripts/devlog.py entry`

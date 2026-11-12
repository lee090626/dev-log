---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/31
date: 2026-11-11
pr: 31
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-11T23:16:57Z
---

# ci: 릴리스에 CLI와 VSIX 아티팩트만 첨부

## 개요

lee090626/synthetix의 변경입니다. 파일 1개 (+5/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: 릴리스에 CLI와 VSIX 아티팩트만 첨부

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/release.yml` — 수정 +5 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Create GitHub Release가 모든 아티팩트(pattern "*")를 받아 증거 폴더까지 업로드하다 실패. cli-*와 synthetix-vscode만 받도록 변경. 첨부 목록은 v0.14.0과 동일(13개).

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/release.yml

## 커밋

- `5696469` ci: 릴리스에 CLI와 VSIX 아티팩트만 첨부

## 성과 및 배운 점

- 변경 파일 1개, +5 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#31](https://github.com/lee090626/synthetix/pull/31) · `scripts/devlog.py entry`

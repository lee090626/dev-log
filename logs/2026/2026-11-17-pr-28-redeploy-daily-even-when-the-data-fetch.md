---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/28
date: 2026-11-17
pr: 28
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-17T01:33:28Z
---

# Redeploy daily even when the data fetch fails

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+3/-2), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Redeploy daily even when the data fetch fails

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/refresh-travel-data.yml` — 수정 +3 / -2

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
Fixes #25. Expired events are filtered at build time, so a failed fetch used to leave ended events on the site until the next successful run. The rebuild step now runs with `always()`: it rebuilds from the previous snapshot. The commit step is still skipped on failure, and the run still shows as failed. YAML lint passes; the change takes effect at the next scheduled run.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/refresh-travel-data.yml

## 커밋

- `0af3bea` Redeploy daily even when the data fetch fails

## 성과 및 배운 점

- 변경 파일 1개, +3 / -2
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#28](https://github.com/lee090626/travel-discovery/pull/28) · `scripts/devlog.py entry`

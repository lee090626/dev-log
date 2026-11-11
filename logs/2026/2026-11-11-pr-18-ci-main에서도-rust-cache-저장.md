---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/18
date: 2026-11-11
pr: 18
author: lee090626
tags: [GitHub Actions]
generated: auto
merged_at: 2026-11-11T01:42:20Z
---

# ci: main에서도 rust-cache 저장

## 개요

lee090626/synthetix의 변경입니다. 파일 1개 (+1/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: main에서도 rust-cache 저장

## 사용 기술

`GitHub Actions`

## 변경 파일

- `.github/workflows/ci.yml` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
PR은 대상·기본 브랜치(main) 캐시만 읽을 수 있습니다. 지금은 캐시를 develop에서만 저장해서, develop→main PR과 main push가 매번 캐시 없이 약 19분 걸렸습니다. `save-if`에 main을 추가합니다. 캐시가 하나 늘어나 총 약 2.6GiB가 됩니다(한도 10GB).

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml

## 커밋

- `3ed7996` ci: main에서도 rust-cache 저장

## 성과 및 배운 점

- 변경 파일 1개, +1 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#18](https://github.com/lee090626/synthetix/pull/18) · `scripts/devlog.py entry`

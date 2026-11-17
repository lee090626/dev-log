---
project: lee090626/travel-discovery
source: https://github.com/lee090626/travel-discovery/pull/22
date: 2026-11-16
pr: 22
author: lee090626
tags: []
generated: auto
merged_at: 2026-11-16T23:41:25Z
---

# Point domain docs at docs/glossary.md

## 개요

lee090626/travel-discovery의 변경입니다. 파일 1개 (+1/-0), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- Point domain docs at docs/glossary.md

## 사용 기술

- (diff에서 판별되지 않음)

## 변경 파일

- `docs/agents/domain.md` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
docs/agents/domain.md told agents to read a root `GLOSSARY.md`, which does not exist (root `*.md` is gitignored, so the glossary lives at `docs/glossary.md`). Because the guide says to proceed silently when the file is missing, agents skipped the glossary, and a glossary created at the root would never be committed.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: docs/agents/domain.md

## 커밋

- `6a36fbf` Point domain docs at docs/glossary.md

## 성과 및 배운 점

- 변경 파일 1개, +1 / -0
- 커밋 1개

---

> 자동 생성: PR [lee090626/travel-discovery#22](https://github.com/lee090626/travel-discovery/pull/22) · `scripts/devlog.py entry`

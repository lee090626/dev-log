---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/29
date: 2026-11-11
pr: 29
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-11T11:25:23Z
---

# develop → main: axiom new, 한계 문서

## 개요

lee090626/synthetix의 변경입니다. 파일 4개 (+110/-2), 커밋 4개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: axiom new 프로젝트 시작 명령 추가
- docs: 지원 범위와 알려진 한계 문서

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/src/main.rs` — 수정 +40 / -0
- `docs/limitations.md` — 추가 +38 / -0
- `crates/axiom-cli/tests/new_project.rs` — 추가 +30 / -0
- `docs/setup.md` — 수정 +2 / -2

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
PR 본문에 문제 설명이 없습니다. 아래 변경 파일과 커밋으로 확인합니다.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/main.rs, crates/axiom-cli/tests/new_project.rs, docs/limitations.md, docs/setup.md

## 커밋

- `b50e958` feat: axiom new 프로젝트 시작 명령 추가
- `f8b8607` docs: 지원 범위와 알려진 한계 문서
- `af88bdc` Merge pull request #27 from lee090626/feat/axiom-new
- `6bc4499` Merge pull request #28 from lee090626/docs/limitations

## 성과 및 배운 점

- 변경 파일 4개, +110 / -2
- 커밋 4개

---

> 자동 생성: PR [lee090626/synthetix#29](https://github.com/lee090626/synthetix/pull/29) · `scripts/devlog.py entry`

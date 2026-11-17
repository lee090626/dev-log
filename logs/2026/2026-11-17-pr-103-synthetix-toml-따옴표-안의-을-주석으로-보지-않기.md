---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/103
date: 2026-11-17
pr: 103
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-17T10:34:46Z
---

# synthetix.toml 따옴표 안의 #을 주석으로 보지 않기

## 개요

lee090626/synthetix의 변경입니다. 파일 1개 (+26/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- fix(project): synthetix.toml 따옴표 안의 #을 주석으로 보지 않기

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-project/src/lib.rs` — 수정 +26 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 `parse_config`가 따옴표 밖의 `#`부터만 주석으로 지웁니다. `entry = "a#b.ax"`가 `"a`로 잘리던 문제.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-project/src/lib.rs

## 커밋

- `5501116` fix(project): synthetix.toml 따옴표 안의 #을 주석으로 보지 않기

## 성과 및 배운 점

- 변경 파일 1개, +26 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#103](https://github.com/lee090626/synthetix/pull/103) · `scripts/devlog.py entry`

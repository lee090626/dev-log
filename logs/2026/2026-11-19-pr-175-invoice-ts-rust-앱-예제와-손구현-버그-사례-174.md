---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/175
date: 2026-11-19
pr: 175
author: lee090626
tags: [Rust, TypeScript]
generated: auto
merged_at: 2026-11-19T02:57:11Z
---

# invoice: TS·Rust 앱 예제와 손구현 버그 사례 (#174)

## 개요

lee090626/synthetix의 변경입니다. 파일 3개 (+114/-0), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- docs: invoice TS·Rust 앱 예제와 손구현 버그 사례 (#174)

## 사용 기술

`Rust` · `TypeScript`

## 변경 파일

- `examples/invoice/README.md` — 수정 +77 / -0
- `examples/invoice/app/main.rs` — 추가 +20 / -0
- `examples/invoice/app/main.ts` — 추가 +17 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`examples/invoice/app/main.ts`, `main.rs`: 같은 청구서를 `--emit js`/`--emit rust` 출력으로 계산 (빌드 도구·외부 의존성 없음) - README: 실행법·결과, 손구현 버그 3가지(일할 나누기 먼저 3원, 수수료 따로 떼기 1원, 부가세 10% 빼기)와 `axiom check`가 찾은 실제 반례

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: examples/invoice/README.md, examples/invoice/app/main.rs, examples/invoice/app/main.ts

## 커밋

- `93d9dfc` docs: invoice TS·Rust 앱 예제와 손구현 버그 사례 (#174)

## 성과 및 배운 점

- 변경 파일 3개, +114 / -0
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#175](https://github.com/lee090626/synthetix/pull/175) · `scripts/devlog.py entry`

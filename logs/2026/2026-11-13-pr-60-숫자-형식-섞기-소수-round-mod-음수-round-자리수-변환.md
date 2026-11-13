---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/60
date: 2026-11-13
pr: 60
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-13T04:00:18Z
---

# 숫자 형식 섞기 — 소수 round·mod, 음수 round, 자리수 변환

## 개요

lee090626/synthetix의 변경입니다. 파일 5개 (+149/-114), 커밋 2개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 숫자 형식 섞기 — 소수 round·mod, 음수 round, 자리수 변환
- style: cargo fmt

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-parser/src/simple.rs` — 수정 +129 / -65
- `crates/axiom-project/src/lib.rs` — 수정 +5 / -37
- `docs/writing-specs.md` — 수정 +11 / -7
- `docs/limitations.md` — 수정 +3 / -4
- `crates/axiom-cli/src/web.rs` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
소수 규칙: `round(10.01 / 3)` = 3.34(마지막 자리 반올림), `7.50 mod 2` = 1.50 - 음수 규칙: `round`는 0에서 먼 쪽으로 반올림(`round(-7 / 2)` = -4) - 같은 파일의 자리수가 다른 규칙 호출: 입력은 상대 자리수로, 답은 내 자리수로 변환(줄일 때 버림) - 페이지 `show`/조건: 자리수가 다른 값은 가장 많은 자리로 맞춤 - 남은 제한: 버튼 인자와 다른 파일 규칙 호출은 여전히 같은 자리수 필요 - 로드맵: 키워드 개수 제한 폐지

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/web.rs, crates/axiom-parser/src/simple.rs, crates/axiom-project/src/lib.rs, docs/limitations.md, docs/writing-specs.md

## 커밋

- `78abb7e` feat: 숫자 형식 섞기 — 소수 round·mod, 음수 round, 자리수 변환
- `3ff693c` style: cargo fmt

## 성과 및 배운 점

- 변경 파일 5개, +149 / -114
- 커밋 2개

---

> 자동 생성: PR [lee090626/synthetix#60](https://github.com/lee090626/synthetix/pull/60) · `scripts/devlog.py entry`

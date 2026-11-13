---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/65
date: 2026-11-13
pr: 65
author: lee090626
tags: [Rust, JavaScript]
generated: auto
merged_at: 2026-11-13T06:25:37Z
---

# 페이지 문법 ask ... for, when ... is clicked 블록

## 개요

lee090626/synthetix의 변경입니다. 파일 10개 (+266/-123), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 페이지 문법 ask ... for, when ... is clicked 블록

## 사용 기술

`Rust` · `JavaScript`

## 변경 파일

- `crates/axiom-parser/src/simple.rs` — 수정 +150 / -36
- `crates/axiom-project/src/lib.rs` — 수정 +46 / -40
- `examples/policy-calculator/main.ax` — 수정 +17 / -13
- `docs/writing-specs.md` — 수정 +20 / -9
- `crates/axiom-cli/tests/simple_page.rs` — 수정 +15 / -10
- `editors/vscode/snippets/axiom.json` — 수정 +7 / -6
- `README.md` — 수정 +5 / -4
- `editors/vscode/extension.js` — 수정 +3 / -3
- `examples/web-counter/main.ax` — 수정 +2 / -1
- `editors/vscode/syntaxes/axiom.tmLanguage.json` — 수정 +1 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
값 하나는 기존 button으로, 여러 개는 기존 reducer(원자적, 순서대로 새 값 사용)로 변환 — 런타임 변경 없음 - reducer 갱신에도 소수 자리수 검사 적용 - 옛 `ask name "Label"`, `button ... ->`는 새 형태를 안내하는 오류 - 예제·문서·README·VSCode(자동완성, 스니펫, hover, 문법 강조)·테스트 갱신

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: README.md, crates/axiom-cli/tests/simple_page.rs, crates/axiom-parser/src/simple.rs, crates/axiom-project/src/lib.rs, docs/writing-specs.md, editors/vscode/extension.js

## 커밋

- `b3ea5bb` feat: 페이지 문법 ask ... for, when ... is clicked 블록

## 성과 및 배운 점

- 변경 파일 10개, +266 / -123
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#65](https://github.com/lee090626/synthetix/pull/65) · `scripts/devlog.py entry`

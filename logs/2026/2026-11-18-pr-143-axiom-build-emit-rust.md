---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/143
date: 2026-11-18
pr: 143
author: lee090626
tags: [Rust]
generated: auto
merged_at: 2026-11-18T05:57:54Z
---

# axiom build --emit rust

## 개요

lee090626/synthetix의 변경입니다. 파일 6개 (+430/-58), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: axiom build --emit rust

## 사용 기술

`Rust`

## 변경 파일

- `crates/axiom-cli/src/rs.rs` — 추가 +231 / -0
- `crates/axiom-cli/tests/rust_emit.rs` — 추가 +108 / -0
- `crates/axiom-cli/src/web.rs` — 수정 +39 / -30
- `crates/axiom-cli/src/js.rs` — 수정 +36 / -21
- `crates/axiom-cli/src/main.rs` — 수정 +10 / -6
- `docs/writing-specs.md` — 수정 +6 / -1

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
프로젝트 빌드에 `--emit rust` → `dist/contracts.rs` (외부 crate 없음, `mod contracts;`로 사용) - 각 규칙 `Result`, need 위반·0 나눗셈은 Err. 목록 답 규칙은 `[T; N]` 배열, `settle(&owe) -> Vec` - AMI 의미(u32 wrapping)를 그대로 출력. 증명은 AMI에 대한 것이고 Rust 출력은 차등 테스트로 확인 (js와 같은 방식) - web.rs의 `emit_js: bool` → `Emit` enum, 안 낸 라이브러리 파일은 삭제 - js.rs의 목록/settle 감지를 공유 함수로 분리

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: crates/axiom-cli/src/js.rs, crates/axiom-cli/src/main.rs, crates/axiom-cli/src/rs.rs, crates/axiom-cli/src/web.rs, crates/axiom-cli/tests/rust_emit.rs, docs/writing-specs.md

## 커밋

- `a171227` feat: axiom build --emit rust

## 성과 및 배운 점

- 변경 파일 6개, +430 / -58
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#143](https://github.com/lee090626/synthetix/pull/143) · `scripts/devlog.py entry`

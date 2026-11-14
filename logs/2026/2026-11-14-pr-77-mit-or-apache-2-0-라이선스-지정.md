---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/77
date: 2026-11-14
pr: 77
author: lee090626
tags: [npm]
generated: auto
merged_at: 2026-11-14T14:51:23Z
---

# MIT OR Apache-2.0 라이선스 지정

## 개요

lee090626/synthetix의 변경입니다. 파일 14개 (+261/-1), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- chore: MIT OR Apache-2.0 라이선스 지정

## 사용 기술

`npm`

## 변경 파일

- `LICENSE-APACHE` — 추가 +202 / -0
- `editors/vscode/LICENSE` — 추가 +24 / -0
- `LICENSE-MIT` — 추가 +21 / -0
- `README.md` — 수정 +4 / -0
- `npm/synthetix-cli/package.json` — 수정 +1 / -1
- `crates/axiom-ami/Cargo.toml` — 수정 +1 / -0
- `crates/axiom-application/Cargo.toml` — 수정 +1 / -0
- `crates/axiom-cli/Cargo.toml` — 수정 +1 / -0
- `crates/axiom-parser/Cargo.toml` — 수정 +1 / -0
- `crates/axiom-project/Cargo.toml` — 수정 +1 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
LICENSE-MIT, LICENSE-APACHE 추가. crate, npm, VSCode 확장의 license 필드 지정. 확장 폴더에도 LICENSE를 둬 vsce가 묻지 않게 함.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: LICENSE-APACHE, LICENSE-MIT, README.md, crates/axiom-ami/Cargo.toml, crates/axiom-application/Cargo.toml, crates/axiom-cli/Cargo.toml

## 커밋

- `695ab07` chore: MIT OR Apache-2.0 라이선스 지정

## 성과 및 배운 점

- 변경 파일 14개, +261 / -1
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#77](https://github.com/lee090626/synthetix/pull/77) · `scripts/devlog.py entry`

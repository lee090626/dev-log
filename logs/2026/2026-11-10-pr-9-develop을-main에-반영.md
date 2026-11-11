---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/9
date: 2026-11-10
pr: 9
author: lee090626
tags: [GitHub Actions, Rust]
generated: auto
merged_at: 2026-11-10T23:15:39Z
---

# develop을 main에 반영

## 개요

lee090626/synthetix의 변경입니다. 파일 10개 (+716/-13), 커밋 17개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat: 정책 계산기 브라우저 세로 흐름 예제 추가
- feat: build --emit js로 검증된 후보를 JavaScript와 d.ts로 출력
- chore: graphify 산출물을 저장소 ignore에 추가
- feat: 프로젝트 빌드에 --emit js 연결

## 사용 기술

`GitHub Actions` · `Rust`

## 변경 파일

- `crates/axiom-cli/src/js.rs` — 추가 +241 / -0
- `crates/axiom-cli/src/web.rs` — 수정 +177 / -9
- `crates/axiom-cli/tests/js_emit.rs` — 추가 +173 / -0
- `crates/axiom-cli/src/main.rs` — 수정 +32 / -4
- `.github/workflows/ci.yml` — 추가 +32 / -0
- `examples/policy-calculator/main.ax` — 추가 +22 / -0
- `examples/policy-calculator/README.md` — 추가 +17 / -0
- `examples/policy-calculator/policy.ax` — 추가 +16 / -0
- `.gitignore` — 수정 +3 / -0
- `examples/policy-calculator/synthetix.toml` — 추가 +3 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
3 정책 계산기 예제와 `build --emit js` - #4 프로젝트 빌드에 `--emit js` 연결 - #5 `graphify-out/` ignore - #6 CI(fmt + workspace tests) - #7 rust-cache로 CI 캐시 축소 - #8 정적 빌드 실패 시 이전 검증 산출물 제거

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/ci.yml, .gitignore, crates/axiom-cli/src/js.rs, crates/axiom-cli/src/main.rs, crates/axiom-cli/src/web.rs, crates/axiom-cli/tests/js_emit.rs

## 커밋

- `8e7c9ab` feat: 정책 계산기 브라우저 세로 흐름 예제 추가
- `e70470e` feat: build --emit js로 검증된 후보를 JavaScript와 d.ts로 출력
- `8c13139` Merge pull request #3 from lee090626/feat/policy-calculator-slice
- `003ac7b` chore: graphify 산출물을 저장소 ignore에 추가
- `295afe9` feat: 프로젝트 빌드에 --emit js 연결
- `88477e1` ci: PR과 develop/main push에 fmt·테스트 체크 추가
- `1ac0e9d` Merge pull request #6 from lee090626/ci/pr-checks
- `aa80581` Merge develop into feat/project-emit-js
- `9cc5700` Merge develop into chore/gitignore-graphify
- `bc820e4` Merge pull request #4 from lee090626/feat/project-emit-js

## 성과 및 배운 점

- 변경 파일 10개, +716 / -13
- 커밋 17개

---

> 자동 생성: PR [lee090626/synthetix#9](https://github.com/lee090626/synthetix/pull/9) · `scripts/devlog.py entry`

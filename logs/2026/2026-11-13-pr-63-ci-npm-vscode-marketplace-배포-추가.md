---
project: lee090626/synthetix
source: https://github.com/lee090626/synthetix/pull/63
date: 2026-11-13
pr: 63
author: lee090626
tags: [GitHub Actions, JavaScript, npm]
generated: auto
merged_at: 2026-11-13T04:18:25Z
---

# ci: npm·VSCode Marketplace 배포 추가

## 개요

lee090626/synthetix의 변경입니다. 파일 5개 (+157/-0), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- ci: npm·VSCode Marketplace 배포 추가

## 사용 기술

`GitHub Actions` · `JavaScript` · `npm`

## 변경 파일

- `.github/workflows/release.yml` — 수정 +57 / -0
- `scripts/npm-packages.cjs` — 추가 +48 / -0
- `npm/synthetix-cli/package.json` — 추가 +25 / -0
- `npm/synthetix-cli/bin/axiom.js` — 추가 +19 / -0
- `docs/setup.md` — 수정 +8 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
`release.yml`: 태그에서 `publish-npm`(플랫폼 패키지 4개 → `synthetix-cli` 런처 순서, provenance), `publish-vsix`(`vsce publish`) job 추가. secret이 없으면 명확한 오류로 실패 - `npm/synthetix-cli`: 플랫폼 패키지를 찾아 네이티브 `axiom`을 실행하는 런처(esbuild 방식 optionalDependencies) - `scripts/npm-packages.cjs`: 릴리스 바이너리로 패키지 생성 - `docs/setup.md`: 설치법·필요 secrets

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .github/workflows/release.yml, docs/setup.md, npm/synthetix-cli/bin/axiom.js, npm/synthetix-cli/package.json, scripts/npm-packages.cjs

## 커밋

- `2d7a45c` ci: npm·VSCode Marketplace 배포 추가

## 성과 및 배운 점

- 변경 파일 5개, +157 / -0
- 커밋 1개

---

> 자동 생성: PR [lee090626/synthetix#63](https://github.com/lee090626/synthetix/pull/63) · `scripts/devlog.py entry`

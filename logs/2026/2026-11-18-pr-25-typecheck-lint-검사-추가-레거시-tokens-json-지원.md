---
project: lee090626/Figma-Token-Exporter
source: https://github.com/lee090626/Figma-Token-Exporter/pull/25
date: 2026-11-18
pr: 25
author: lee090626
tags: [npm, TypeScript, HTML, GitHub Actions]
generated: auto
merged_at: 2026-11-18T12:53:13Z
---

# typecheck·lint 검사 추가, 레거시 tokens.json 지원, .env 미로딩

## 개요

lee090626/Figma-Token-Exporter의 변경입니다. 파일 18개 (+626/-48), 커밋 1개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- chore: typecheck·lint 검사 추가, 레거시 tokens.json 지원, .env 미로딩

## 사용 기술

`npm` · `TypeScript` · `HTML` · `GitHub Actions`

## 변경 파일

- `pnpm-lock.yaml` — 수정 +440 / -7
- `packages/core/src/index.ts` — 수정 +44 / -1
- `packages/plugin/src/ui.html` — 수정 +21 / -18
- `.dependency-cruiser.cjs` — 추가 +30 / -0
- `packages/core/src/index.test.ts` — 수정 +28 / -1
- `biome.json` — 추가 +21 / -0
- `packages/cli/src/exportTokens.ts` — 수정 +9 / -5
- `packages/cli/src/sync.ts` — 수정 +7 / -5
- `package.json` — 수정 +5 / -1
- `packages/cli/package.json` — 수정 +3 / -3

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
변경 - `pnpm typecheck`: 패키지별 `tsc --noEmit` (core·cli tsconfig 추가) - `pnpm lint`: Biome recommended + dependency-cruiser (core → cli/plugin import 금지, 순환 금지, src의 devDependency 런타임 import 금지) - 기존 Biome 위반 34건 수정 (동작 변경 없음) - CLI가 예전 Plugin 형식(hex 색상 문자열, `type: "number"`, 모든 mode 포함)도 읽음. collection마다 처음 나온 mode만 쓰고, number는 이름·collection으로 분류하며 분류 불가 시 오류 - CLI가 `.env`를 읽지 않음 (`dotenv` 제거). 토큰은 셸 환경변수나 옵션으로 전달

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: .dependency-cruiser.cjs, README.md, biome.json, package.json, packages/cli/package.json, packages/cli/src/exportTokens.ts

## 커밋

- `4133fb0` chore: typecheck·lint 검사 추가, 레거시 tokens.json 지원, .env 미로딩

## 성과 및 배운 점

- 변경 파일 18개, +626 / -48
- 커밋 1개

---

> 자동 생성: PR [lee090626/Figma-Token-Exporter#25](https://github.com/lee090626/Figma-Token-Exporter/pull/25) · `scripts/devlog.py entry`

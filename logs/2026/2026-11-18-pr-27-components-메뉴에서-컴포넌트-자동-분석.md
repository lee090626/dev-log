---
project: lee090626/Figma-Token-Exporter
source: https://github.com/lee090626/Figma-Token-Exporter/pull/27
date: 2026-11-18
pr: 27
author: lee090626
tags: [TypeScript, HTML]
generated: auto
merged_at: 2026-11-18T12:54:08Z
---

# Components 메뉴에서 컴포넌트 자동 분석

## 개요

lee090626/Figma-Token-Exporter의 변경입니다. 파일 3개 (+265/-40), 커밋 5개. 아래 '문제'는 PR 본문에서 그대로 발췌했습니다.

## 주요 기능 / 변경 사항

- feat(plugin): Component·Component Set을 선택 없이 자동 분석하는 Components 메뉴 추가
- feat(plugin): Components 화면을 Tokens처럼 보드와 블롭 카드로 표시
- feat(plugin): Components 다운로드를 상단 파일 버튼으로 이동
- style(plugin): 앱 색감을 딸기우유 톤으로 변경 (라이트·다크)

## 사용 기술

`TypeScript` · `HTML`

## 변경 파일

- `packages/plugin/src/ui.html` — 수정 +152 / -18
- `packages/plugin/src/code.ts` — 수정 +47 / -22
- `packages/plugin/src/ui.test.ts` — 수정 +66 / -0

## 트러블슈팅

### 1. 이번 변경에서 해결한 것

**문제**
26 위에 쌓인 PR입니다. #25 → #26 → 이 PR 순서로 머지하세요.

**원인**
**diff에서 자동으로 판별하지 못했습니다.** (LLM 키가 없어 자동 요약으로 기록됨 — 직접 보완)

**해결**
변경 파일: packages/plugin/src/code.ts, packages/plugin/src/ui.html, packages/plugin/src/ui.test.ts

## 커밋

- `e12d66b` feat(plugin): Component·Component Set을 선택 없이 자동 분석하는 Components 메뉴 추가
- `7efa238` feat(plugin): Components 화면을 Tokens처럼 보드와 블롭 카드로 표시
- `3ecbf9e` feat(plugin): Components 다운로드를 상단 파일 버튼으로 이동
- `f5c62b0` style(plugin): 앱 색감을 딸기우유 톤으로 변경 (라이트·다크)
- `095f663` feat(plugin): 좌상단 핸들로도 창 크기 조절

## 성과 및 배운 점

- 변경 파일 3개, +265 / -40
- 커밋 5개

---

> 자동 생성: PR [lee090626/Figma-Token-Exporter#27](https://github.com/lee090626/Figma-Token-Exporter/pull/27) · `scripts/devlog.py entry`

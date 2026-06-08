# TIL 학습 운영 규칙

이 저장소는 공개 가능한 기술 자료를 GitHub Issue와 댓글로 정리하는 공개 학습 기록이다.

## 사용자 언어

본문, 댓글, 템플릿 설명은 한국어로 쓴다.

다음 항목은 고유명사이므로 영어를 유지할 수 있다.

| 유지 가능 | 예시 |
|---|---|
| 제품명 | Gajae-Code, GitHub, TypeScript |
| 명령어 | `deep-interview`, `ralplan`, `ultragoal` |
| 라벨 값 | `project`, `in-progress`, `advanced` |
| 원문 인용 | README나 release note의 짧은 원문 |

## 표현 원칙

공개 여부와 무관하게 특정 대상의 방식을 그대로 가져온다는 인상을 주는 표현을 쓰지 않는다.

자료를 다룰 때는 다음 표현을 쓴다.

| 상황 | 쓸 표현 |
|---|---|
| 배울 지점 | 참고할 점, 분석할 점 |
| 내 시스템에 쓸 수 있는 지점 | 적용 가능 요소, 도입 후보 |
| 지금 쓰지 않을 지점 | 보류할 요소, 추가 확인 필요 |
| 직접 확인할 지점 | 재현 실험, 구현 확인 |

## 스킬

### Study Gate (`/study-gate`)

자료를 게시해도 되는지 먼저 점검한다.

- 위치: `.claude/skills/study-gate.md`
- 사용 시점: 이슈 생성 전 내부 점검
- 다음 단계: `/study-scan`, `/study-analysis`, `/study-to-issue`

### Study Scan (`/study-scan`)

자료를 깊게 다룰 가치가 있는지 빠르게 판별한다.

- 위치: `.claude/skills/study-scan.md`
- 사용 시점: 논문, 개념, 프로젝트, 릴리스, 글, 영상의 초기 판별

### Study Analysis (`/study-analysis`)

게시 적합성 점검을 통과한 자료를 6단계로 분석한다.

- 위치: `.claude/skills/study-analysis.md`
- 사용 시점: 이슈 생성 전 깊은 분석

### Study to Issue (`/study-to-issue`)

분석 결과를 GitHub Issue로 바꾼다.

- 위치: `.claude/skills/study-to-issue.md`
- 사용 시점: 검색과 연결이 가능한 학습 단위를 만들 때

### Study Explain (`/study-explain`)

어려운 본문을 쉬운 설명 댓글로 다시 쓴다.

- 위치: `.claude/skills/study-explain.md`
- 사용 시점: 이슈 생성 직후
- 원칙: 본문만 만들고 끝내지 않는다.

## Workflow

```text
Discover -> Check -> Scan -> Analyze -> Document -> Explain -> Connect -> Close
```

| 단계 | 하는 일 | 산출물 |
|---|---|---|
| Discover | 자료를 찾는다 | source 후보 |
| Check | 게시 적합성을 점검한다 | 진행, 문구 정리, 비게시, 보류 |
| Scan | 우선순위를 정한다 | 빠른 판별 |
| Analyze | 깊게 분석한다 | 분석문 |
| Document | 이슈로 고정한다 | Study Issue |
| Explain | 쉬운 댓글을 붙인다 | Explanation Comment |
| Connect | 관련 자료와 연결한다 | 관련 이슈 링크 |
| Close | 이해 완료 시 닫는다 | 완료 표시 |

## 게시 적합성 점검

이 저장소는 public이다. 출처를 직접 걸 수 있는 기술 자료만 올린다.

| 내부 결과 | 처리 |
|---|---|
| 진행 | 이슈 작성 |
| 문구 정리 | 제목, 본문, 댓글을 중립적으로 정리한 뒤 작성 |
| 비게시 | 이 저장소에 올리지 않음 |
| 보류 | 이슈를 만들지 않음 |

의심되면 공개 이슈를 만들지 말고 먼저 확인을 받는다.

## Issue 규칙

### 강제 품질 게이트

새 이슈나 기존 이슈 수정은 다음 조건을 통과해야 완료로 본다.

| 항목 | 기준 |
|---|---|
| 본문 시작 | 반드시 `## 출처`로 시작 |
| 본문 길이 | 일반 학습 이슈는 3,500자 이상. 원자료 접근이 막힌 경우에는 차단 사유와 확인 필요 항목을 명시 |
| 댓글 길이 | 쉬운 설명 댓글은 900자 이상 |
| 필수 본문 섹션 | 출처, Issue Metadata, TL;DR, 학습 질문, 문제의식, 구조 분해, 근거, 비판적 분석, 분석 관점, 적용 가능 요소, 보류할 요소, 관련 이슈, Action Items |
| 원자료 우선 | LinkedIn, Threads, 블로그, 영상 공유글은 포인터로 보고 원자료를 먼저 찾음 |
| 연결 | 관련 이슈가 있으면 `#N`으로 연결. 없으면 `없음` 또는 `확인 필요`로 명시 |
| 금지 표현 | 내부 채널명, 내부 판정문, 특정 대상의 방식을 그대로 가져온다는 인상을 주는 표현 |

대량 생성은 금지한다. 여러 후보를 한 번에 처리하더라도 각 항목은 위 게이트를 개별 통과해야 한다.

### Labels

- `paper`: 논문 리뷰
- `concept`: 개념 학습
- `project`: 오픈소스 프로젝트 또는 공개 제품 분석
- `release`: 릴리스 노트 분석
- `in-progress`: 학습 중
- `needs-revisit`: 재검토 필요
- `foundational`: 기초 개념
- `advanced`: 심화 주제

### 제목 Prefix

- `[Paper]`: 논문
- `[Concept]`: 개념
- `[Project]`: 오픈소스 프로젝트 또는 공개 제품
- `[Release]`: 릴리스 노트 또는 changelog
- `[Production]`: 공개 production system 또는 운영 패턴

### 연결

- 관련 이슈는 `#N`으로 연결한다.
- 같은 주제의 자료는 서로 cross-link한다.
- 대기 자료는 `resources/reading-list.md`에 남긴다.

## 분석 관점

자료를 볼 때 항상 다음을 확인한다.

| 관점 | 질문 |
|---|---|
| 기법 분류 | write, select, compress, isolate, evaluate, orchestrate, govern 중 무엇인가 |
| 구성요소 | prompt, input, retrieved docs, memory, tool output, state, evidence, handoff 중 무엇을 다루는가 |
| 운영 적용성 | 실제 작업에 안전하게 쓸 수 있는가 |
| 연결 지점 | agent, RAG, memory, CLI, MCP, LSP, browser, CI, GitHub, review workflow와 어떻게 연결되는가 |
| 적용 가능 요소 | 내 시스템에 검토할 만한 원칙이나 구조는 무엇인가 |
| 보류할 요소 | 아직 위험하거나, 성숙하지 않았거나, 맥락이 맞지 않는 것은 무엇인가 |

## 저장소 구조

```text
til/
├── CLAUDE.md
├── README.md
├── .claude/
│   └── skills/
│       ├── study-gate.md
│       ├── study-scan.md
│       ├── study-analysis.md
│       ├── study-to-issue.md
│       └── study-explain.md
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── paper-review.md
│       ├── concept-study.md
│       └── project-analysis.md
└── resources/
    └── reading-list.md
```

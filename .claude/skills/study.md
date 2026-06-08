# Study Skill

모든 학습 자료를 하나의 입구에서 받아 source lock, 분석, publish gate를 강제한다.

## 사용법

```text
/study <url-or-message>
```

## 공개 진입점

사용자는 이 스킬만 호출한다.

에이전트는 `study-gate`, `study-scan`, `study-analysis`, `study-to-issue`, `study-explain`를 사용자에게 직접 호출하라고 안내하지 않는다.

## 내부 workflow

```text
Normalize -> Study Kernel -> Publish Gate
```

| 단계 | 하는 일 | 중단 조건 |
|---|---|---|
| Normalize | canonical source, source type, artifact, route를 고정 | source lock 없음 |
| Study Kernel | source type에 맞는 분석과 이슈 본문을 작성 | 타입 불명확 |
| Publish Gate | public 여부, 이슈, 댓글, related, reading-list, validator 확인 | 검증 실패 |

## Normalize

| 입력 | 처리 |
|---|---|
| YouTube | 안정적인 digest artifact가 있어야 다음 단계로 간다 |
| LinkedIn, Threads | repo, 논문, 제품, 공식 문서 같은 원자료를 먼저 찾는다 |
| GitHub repo | README, docs, code, examples를 확인한다 |
| 논문 | paper URL, PDF, code, project page를 확인한다 |
| 제품 | 화면, docs, pricing, API, data boundary를 확인한다 |
| 아이디어 | 공개 원자료가 없으면 public issue를 만들지 않는다 |

## Study Kernel

| source type | 처리 |
|---|---|
| paper | paper review 흐름으로 분석 |
| github repo | project analysis 흐름으로 분석 |
| product | project 또는 production 분석 |
| concept, blog, opinion | concept study 흐름으로 분석 |
| YouTube digest artifact | artifact를 원자료로 보고 concept 또는 project 분석 |

## Publish Gate

공개 이슈에는 내부 판단 경로를 쓰지 않는다.

| 조건 | 기준 |
|---|---|
| 본문 | `## 출처`로 시작하고 필수 섹션을 포함 |
| 댓글 | 쉬운 설명 댓글 포함 |
| 연결 | 관련 이슈나 `확인 필요` 표시 |
| 원장 | `resources/reading-list.md` 갱신 |
| 검증 | `scripts/validate-study-issues.py --repo myeolkoreaseoul/til --limit 100` 통과 |

## 금지

| 금지 | 이유 |
|---|---|
| source lock 없이 이슈 작성 | 원자료가 흔들림 |
| YouTube를 digest artifact 없이 이슈화 | 자막과 요약 근거가 고정되지 않음 |
| LinkedIn feed text만으로 단정 | 원자료와 의견이 섞임 |
| 게시 적합성 판단문을 공개 이슈에 작성 | 공개 표면 오염 |
| 검증 실패 후 완료 보고 | workflow 강제력 상실 |

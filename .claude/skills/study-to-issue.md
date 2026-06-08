# Study to Issue Skill

분석 결과를 GitHub Issue로 바꾼다.

## 사용법

```text
/study-to-issue <source_url_or_artifact>
```

## 순서

1. `/study-gate`로 내부 게시 적합성을 점검한다.
2. 게시가 부적합하면 여기서 멈춘다.
3. `/study-scan`으로 우선순위를 본다.
4. `/study-analysis`로 분석한다.
5. 공개 이슈 본문으로 변환한다.
6. `gh`로 이슈를 만든다.
7. `/study-explain`으로 쉬운 설명 댓글을 붙인다.

## 제목 형식

```text
[Paper] {짧은 제목} ({저자}, {연도})
[Concept] {개념명}
[Project] {프로젝트명}: {분석 초점}
[Release] {프로젝트명} {버전}: {분석 초점}
[Production] {시스템 또는 제품}: {운영 패턴}
```

## Labels

자동으로 붙인다.

- 종류: `paper`, `concept`, `project`
- 상태: `in-progress`
- 난이도: `foundational` 또는 `advanced`
- 선택: `release`

## 공개 이슈 본문 템플릿

```markdown
## 출처
- **제목**:
- **종류**:
- **작성자/소유자**:
- **주요 링크**:
- **보조 링크**:

## 요약
[2-3문장]

## 문제의식
[핵심 문제]

## 작동 방식

### 직관
[쉬운 설명]

### 핵심 기술 포인트
[핵심 기여 또는 패턴]

### 근거
| 출처 | 확인한 내용 |
|---|---|
| | |

## 분석 관점
- **기법 분류**:
- **다루는 구성요소**:
- **운영 적용성**:
- **연결 지점**:

## 강점
1.
2.

## 약점
1.
2.

## 적용 가능 요소
- [ ]

## 보류할 요소
- [ ]

## 관련 이슈
- 관련:

## 다음 행동
- [ ] 원자료를 읽는다.
- [ ] 구현 또는 예시를 확인한다.
- [ ] 로컬 실험 여부를 결정한다.

---
**읽기 상태**: [ ] 1차 확인 [ ] 깊은 분석 [ ] 로컬 실험
**확신도**: 높음 / 중간 / 낮음
```

## CLI 명령

```bash
gh issue create \
  --repo myeolkoreaseoul/til \
  --title "[Project] {title}" \
  --label "project,in-progress,advanced" \
  --body-file <body-file>
```

## 생성 후 할 일

1. 쉬운 설명 댓글을 추가한다.
2. 대기 자료라면 `resources/reading-list.md`를 갱신한다.
3. 관련 이슈가 있으면 서로 연결한다.

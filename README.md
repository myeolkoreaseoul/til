# til

배우고 만들면서 알아낸 것을 GitHub Issue로 정리한다.

주제는 회계, 정산, 세무, 규정 자동화, AI 에이전트, 데이터다.

## 운영 방식

이 저장소는 공개 가능한 기술 자료만 다룬다.

학습 흐름은 다음과 같다.

```text
Normalize -> Study Kernel -> Publish Gate
```

| 단계 | 산출물 |
|---|---|
| Normalize | source lock |
| Study Kernel | 분석문, GitHub Issue 본문, 쉬운 설명 댓글 |
| Publish Gate | related 연결, reading-list 갱신, 검증 통과 |

새 자료는 `/study <url-or-message>` 하나로만 처리한다.

세부 규칙은 `CLAUDE.md`와 `.claude/skills/study.md`를 따른다.

## 검증

이슈를 만들기 전에는 local packet을 먼저 검사한다.

```bash
scripts/validate-study-issues.py --title "<title>" --body-file issue-body.md --comment-file explanation-comment.md
```

공개 이슈 발행은 wrapper로만 한다.

```bash
scripts/publish-study-issue.py --title "<title>" --body-file issue-body.md --comment-file explanation-comment.md --approved-by-user
```

이슈를 만들거나 고친 뒤에는 아래 명령이 통과해야 완료로 본다.

```bash
scripts/validate-study-issues.py --repo myeolkoreaseoul/til --limit 100
```

검증은 본문 시작, 필수 섹션, 본문 길이, 쉬운 설명 댓글 길이, 공개 저장소에 남기면 안 되는 표현을 확인한다.

## 표현 원칙

문서는 한국어로 쓴다.

공개 여부와 무관하게 특정 대상의 방식을 그대로 가져온다는 인상을 주는 표현을 쓰지 않는다.

기술 자료를 다룰 때는 `참고`, `분석`, `도입 후보`, `적용 가능 요소`, `보류할 요소`처럼 중립적인 표현을 쓴다.

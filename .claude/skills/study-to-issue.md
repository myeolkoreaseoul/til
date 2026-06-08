# Study to Issue Skill

Convert a study analysis into a GitHub issue.

## Usage

```text
/study-to-issue <source_url_or_artifact>
```

## Process

1. Run `/study-gate`.
2. Stop unless the decision is `PUBLIC APPROVED` or `PUBLIC WITH CARE`.
3. Run `/study-scan`.
4. Run `/study-analysis`.
5. Transform the result into GitHub issue format.
6. Create the issue with `gh`.
7. Run `/study-explain` and add the explanation as a comment.

## Title Format

```text
[Paper] {Short Title} ({Author}, {Year})
[Concept] {Concept Name}
[Project] {Project Name}: {Study Focus}
[Release] {Project Name} {Version}: {Study Focus}
[Production] {System or Product}: {Production Pattern}
```

## Labels

Auto-assign:

- Type: `paper`, `concept`, or `project`
- Status: `in-progress`
- Gate: `public-approved`
- Difficulty: `foundational` or `advanced`
- Optional content label: `release`

## Body Template

```markdown
## Public/Private Gate
- **Decision**:
- **Reason**:
- **Publication Target**:

## Source
- **Title**:
- **Type**:
- **Author/Owner**:
- **Primary Link**:
- **Supporting Links**:

## TL;DR
[2-3 sentence summary]

## Problem
[Core problem in 1-2 sentences]

## How It Works

### Intuition
[Simple explanation]

### Key Technical Insight
[Main technical contribution or pattern]

### Evidence
| Source | Evidence |
|---|---|
| | |

## Study Lens
- **Technique Category**:
- **Context Components**:
- **Production Readiness**:
- **Integration Points**:

## Strengths
1.
2.

## Weaknesses
1.
2.

## What I Can Copy
- [ ]

## What I Should Skip
- [ ]

## Related Issues
- Related to:

## Action Items
- [ ] Read source README or paper.
- [ ] Inspect implementation or example.
- [ ] Decide whether to try it in a local project.

---
**Reading Status**: [ ] 1st pass [ ] Deep read [ ] Tried locally
**Confidence**: High / Medium / Low
```

## CLI Command

```bash
gh issue create \
  --repo myeolkoreaseoul/til \
  --title "[Project] {title}" \
  --label "project,in-progress,public-approved,advanced" \
  --body-file <body-file>
```

## Post-Creation

1. Add a beginner-friendly explanation comment.
2. Update `resources/reading-list.md` if the source should stay queued.
3. Link related issues bidirectionally when related issues exist.

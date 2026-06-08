# Study Scan Skill

Quick source triage to decide if a source is worth a full study issue.

## Usage

```text
/study-scan <source_url_or_artifact>
```

## Quick Scan Protocol

### Step 1: 30-Second Overview

Read only:

- Title
- Summary, abstract, release heading, or README opening
- Section headings
- Figures, tables, or changelog bullets
- Repository metadata when relevant

### Step 2: Triage Questions

Answer with YES, NO, or MAYBE.

| Question | Answer | Notes |
|---|---|---|
| Is this relevant to AI agents, automation, software operations, accounting, tax, or regulation work. | | |
| Is there a novel contribution or useful pattern. | | |
| Is code, paper, docs, or release evidence available. | | |
| Is the author, venue, project, or artifact credible enough to study. | | |
| Is this useful for current systems or future practice. | | |

### Step 3: Categorize

Place in one category.

- **MUST STUDY**: High relevance, novel, and directly applicable.
- **SHOULD STUDY**: Useful pattern or reference.
- **SKIM**: Background knowledge, not urgent.
- **SKIP**: Not relevant enough or not safe enough.

### Step 4: Priority Score

Calculate priority from 1 to 10.

```text
Relevance (0-4):
Novelty (0-3):
Practical applicability (0-3):
TOTAL:
```

## Output Format

```markdown
# Study Scan: [Title]

**Quick Verdict**: [MUST STUDY / SHOULD STUDY / SKIM / SKIP]
**Priority Score**: X/10
**Time Investment**: [estimated hours]

## 30-Second Summary
[2 sentences max]

## Relevance
[1 sentence on why this matters]

## Evidence
- Source:
- Code/docs:
- Release/paper:

## Decision
[Study now / queue for later / skip]

## If Studying, Focus On
- Section or artifact:
- Reason:
```

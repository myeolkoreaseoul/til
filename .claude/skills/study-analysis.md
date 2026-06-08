# Study Analysis Skill

Deep analysis for public technical sources.

## Usage

```text
/study-analysis <source_url_or_artifact>
```

## Analysis Framework

Follow this 6-level extraction framework.

### Level 1: Metadata Extraction

Extract:

- **Title**
- **Author or project owner**
- **Source type**
- **Published or updated date**
- **Links**: source, repository, release, docs, paper, demo, package
- **Keywords**

### Level 2: Problem Definition

Answer:

1. **Core Problem**: What specific problem does this solve.
2. **Motivation**: Why this problem matters now.
3. **Gap**: What existing approaches fail to do.
4. **Study Question**: What I am trying to learn from it.

### Level 3: Methodology or Architecture

Extract in layers:

#### 3.1 Intuitive Explanation

Explain the core idea without jargon.

#### 3.2 Technical Approach

Describe architecture, workflow, algorithms, contracts, or implementation patterns.

#### 3.3 Implementation Details

Capture install path, commands, configuration, runtime boundary, dependencies, and project gates when available.

### Level 4: Evidence and Results

Extract:

| Component | What to Extract |
|---|---|
| Source evidence | README, release notes, docs, code, examples |
| Changes or features | What changed or what exists |
| Claims | What the source claims |
| Verification path | How to verify or try it |
| Failure cases | What the source warns about |

### Level 5: Critical Analysis

Analyze:

#### 5.1 Strengths

What does this do well.

#### 5.2 Weaknesses

What is missing, risky, immature, or unclear.

#### 5.3 Study Lens

Classify:

- Technique category: write, select, compress, isolate, evaluate, orchestrate, govern
- Components: prompt, user input, memory, tool output, state, evidence, handoff
- Production readiness
- Integration points

#### 5.4 Questions and Concerns

What to ask, test, or watch later.

### Level 6: Actionable Takeaways

Extract:

- Key quotes or short source claims, without overquoting
- Related issues
- What to copy
- What to skip
- Follow-up actions

## Output Template

```markdown
# [Study Title]

## Metadata
- **Source Type**:
- **Author/Owner**:
- **Published/Updated**:
- **Links**:

## TL;DR
[2-3 sentence summary]

## Problem Definition
**Core Problem**:
**Motivation**:
**Gap**:
**Study Question**:

## How It Works

### Intuition
[simple explanation]

### Technical Approach
[architecture, workflow, contracts, implementation]

### Implementation Notes
[commands, configs, boundaries, dependencies]

## Evidence
| Source | Evidence |
|---|---|
| | |

## Critical Analysis

### Strengths
1.
2.

### Weaknesses
1.
2.

### Study Lens
- **Technique Category**:
- **Components**:
- **Production Readiness**:
- **Integration Points**:

## What to Copy
- [ ]

## What to Skip
- [ ]

## Questions
- [ ]

## Connections
- Related to:

## Action Items
- [ ]
```

## Quality Checklist

- [ ] All 6 levels are covered.
- [ ] Source URLs are included.
- [ ] Public/private gate has passed.
- [ ] Actionable takeaways are specific.
- [ ] Related issues are linked when available.

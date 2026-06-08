# TIL Study Guidelines

This repository is for studying public technical materials through issues, comments, labels, and links.

## Custom Skills

### Study Gate (`/study-gate`)

Classify whether a source can be documented in this public repository.

- Location: `.claude/skills/study-gate.md`
- Use for: Public/private decision before creating any issue
- Required before: `/study-scan`, `/study-analysis`, `/study-to-issue`

### Study Scan (`/study-scan`)

Quick triage to decide whether a source is worth a full study issue.

- Location: `.claude/skills/study-scan.md`
- Use for: Initial screening of papers, concepts, projects, releases, posts, and videos

### Study Analysis (`/study-analysis`)

Deep analysis of an approved source with a 6-level extraction framework.

- Location: `.claude/skills/study-analysis.md`
- Use for: Comprehensive study before issue creation

### Study to Issue (`/study-to-issue`)

Convert a study analysis into a GitHub issue.

- Location: `.claude/skills/study-to-issue.md`
- Use for: Creating searchable study issues

### Study Explain (`/study-explain`)

Simplify a study issue with analogies, diagrams, step-by-step walkthroughs, and misconceptions.

- Location: `.claude/skills/study-explain.md`
- Use for: Adding beginner-friendly explanation comments
- Runs after: `/study-to-issue`

## Workflow

1. **Discover**: Find a public technical source from GitHub, papers, product docs, release notes, technical posts, or videos.
2. **Gate**: `/study-gate` to classify public/private handling.
3. **Scan**: `/study-scan` to triage value and priority.
4. **Analyze**: `/study-analysis` for deep reading.
5. **Document**: `/study-to-issue` to create a GitHub issue.
6. **Explain**: `/study-explain` to add a beginner-friendly comment.
7. **Connect**: Link related issues together.
8. **Close**: Mark the issue closed when understanding is complete.

## Public/Private Gate

This repo is public. Never publish private, copied, sensitive, or person-specific workflow absorption notes here.

| Decision | Use this repo when | Do not use this repo when |
|---|---|---|
| Public | Source is public, technical, citeable, and safe to summarize | Source includes private chats, paid content, personal imitation, client work, secrets, or controversial copying |
| Private | Source is useful but not safe to publish | Public issue would reveal internal intent, private workflow, credentials, client information, or another person's non-public operating style |

When in doubt, stop at the gate and ask for approval before publishing.

## Issue Conventions

### Labels

- `paper`: Academic paper review
- `concept`: Conceptual learning
- `project`: Open source project or product analysis
- `release`: Release note analysis
- `public-approved`: Passed public publishing gate
- `private-required`: Must not be published here
- `in-progress`: Currently studying
- `needs-revisit`: Needs another look
- `foundational`: Core or basic concept
- `advanced`: Cutting-edge or complex topic

### Title Prefixes

- `[Paper]`: Academic paper
- `[Concept]`: Conceptual learning unit
- `[Project]`: Open source project or product
- `[Release]`: Release note or changelog
- `[Production]`: Production system or public production pattern

### Linking

- Use `#N` to reference related issues.
- Cross-link related materials.
- Update `resources/reading-list.md` when a source is queued or documented.

## Study Focus Areas

When analyzing any material, always consider:

1. **Technique Category**: Write, select, compress, isolate, evaluate, orchestrate, or govern.
2. **Context Components**: System prompt, user input, retrieved docs, memory, tool outputs, state, evidence, or handoff.
3. **Production Readiness**: Can this be used safely in real work.
4. **Integration Points**: Agents, RAG, memory, CLI, MCP, LSP, browser, CI, GitHub, or review workflows.
5. **What to Copy**: What can be reused in my own systems.
6. **What to Skip**: What is unsafe, premature, too specific, or not worth copying.

## Repository Structure

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

# Study Gate Skill

Classify whether a source can be documented in this public repository.

## Usage

```text
/study-gate <source_url_or_message>
```

Run this before scan, analysis, issue creation, or comment publication.

## Gate Protocol

### Step 1: Source Identity

Extract:

- Source URL or artifact path
- Source type: paper, GitHub repo, release, product doc, post, video, private chat, internal note, or client work
- Author or publisher
- Publication status: public, restricted, paid, private, or unknown

### Step 2: Risk Questions

Answer with YES, NO, or UNKNOWN.

| Question | Answer | Notes |
|---|---|---|
| Is the source publicly accessible. | | |
| Is the source technical or educational. | | |
| Can the source be cited directly. | | |
| Does the source include private chat, client data, secrets, or credentials. | | |
| Would publishing reveal an internal imitation or copying intent. | | |
| Would publishing create avoidable personal or reputational risk. | | |

### Step 3: Decision

Place in one category.

- **PUBLIC APPROVED**: Public, citeable, technical, and safe.
- **PUBLIC WITH CARE**: Public source, but wording must avoid private intent or sensitive framing.
- **PRIVATE REQUIRED**: Useful but unsafe for public issue.
- **SKIP**: Not worth documenting or not enough source evidence.

### Step 4: Publication Rule

- `PUBLIC APPROVED`: issue may be created in this repo.
- `PUBLIC WITH CARE`: issue may be created only after removing private context from title, body, labels, and comments.
- `PRIVATE REQUIRED`: do not create an issue in this repo. Use a private repo or private document.
- `SKIP`: do not create an issue.

## Output Format

```markdown
# Study Gate: [Source]

**Decision**: [PUBLIC APPROVED / PUBLIC WITH CARE / PRIVATE REQUIRED / SKIP]
**Reason**: [one sentence]
**Publication Target**: [public til / private repo / no publication]

## Source Identity
- **Type**:
- **Author/Publisher**:
- **URL**:
- **Public Status**:

## Risk Check
| Question | Answer | Notes |
|---|---|---|
| Publicly accessible | | |
| Citeable | | |
| Private or sensitive content | | |
| Internal copying intent exposed | | |
| Reputational risk | | |

## Required Edits Before Publishing
- [ ] Remove private channel names.
- [ ] Remove internal agent names unless technically relevant and public.
- [ ] Cite public source URLs only.
- [ ] Keep commentary about what to copy framed as technical learning.
```

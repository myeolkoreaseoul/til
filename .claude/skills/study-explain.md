# Study Explain Skill

Explain a study issue so a beginner can understand it.

## Usage

```text
/study-explain <issue_number>
```

Read the issue and add one explanation comment.

## Explanation Framework

### 1. Glossary

Extract technical terms and define them with plain analogies.

```markdown
## Glossary

| Term | Plain Meaning | Everyday Analogy |
|---|---|---|
| Context window | Text the model can see at once | A desk with limited space |
```

### 2. Easy Explanation

Explain each core concept simply.

```markdown
## Easy Explanation

### What is [concept].

**One-line summary**: [10 words or fewer]

**Analogy**:
[3-4 sentences]

**Why it helps**:
[problem solved]
```

### 3. Visual Diagram

Use ASCII diagrams.

```markdown
## Visual Diagram

### Before
[problem state]

### After
[improved state]

### Flow
[step-by-step arrows]
```

### 4. Step-by-Step Walkthrough

Break down the process.

```markdown
## Step-by-Step

**Scenario**: [concrete example]

**Step 1: [action]**
- What happens:
- Why:
- Example:
```

### 5. Why It Matters

Explain what becomes possible and where it can be used.

### 6. Common Misconceptions

Separate wrong interpretations from correct ones.

### 7. Connections

Connect the idea to known concepts or related issues.

### 8. One-Page Summary

End with a boxed ASCII summary.

## Output Format

```markdown
# [Study Title] Easy Explanation

> This comment explains the study issue in simpler terms.

[sections above]

---
This explanation was generated with `/study-explain`.
```

## Quality Checklist

- [ ] All important terms are explained.
- [ ] Analogies are practical and not decorative.
- [ ] ASCII diagram is readable.
- [ ] Step-by-step section includes why each step exists.
- [ ] Misconceptions are explicit.
- [ ] Summary is short enough to scan.

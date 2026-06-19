---
name: story-writer
description: Use when Abu wants user stories, BDD scenarios, acceptance paths, or testable product slices derived from an approved spec. Keeps stories distinct from specs and plans, and makes each story traceable to spec requirements and acceptance criteria.
---

# Story Writer

Use this skill after or alongside a spec, before implementation planning.

## Core Rule

Stories are user-facing or behavior-facing slices. They are not the whole spec and not the implementation plan.

## Required Inputs

Prefer these inputs:

- Approved or draft spec.
- Target user roles.
- Acceptance criteria.
- Known constraints and non-goals.

If no spec exists, either create a minimal story draft from the idea or recommend `spec-writer` first.

## Process

1. Identify actors, workflows, and observable outcomes.
2. Derive stories from spec requirements.
3. Keep each story independently testable.
4. Add BDD-style scenarios only where they clarify behavior.
5. Link each story back to spec sections or requirement IDs when available.
6. Record edge cases and excluded behavior.
7. Stop before implementation planning.

## Output

Use this structure:

```markdown
# Stories: <feature or project>

## Traceability

## Story 1: <title>

As a <user>,
I want <capability>,
so that <outcome>.

### Acceptance Criteria

### Scenarios

### Notes

## Open Questions
```

When creating a file, default to:

```text
<project-root>/.thoughts/stories/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

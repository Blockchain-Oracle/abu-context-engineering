---
name: spec-writer
description: Use when Abu wants to turn an idea, research brief, hackathon concept, bug area, or product requirement into a clear implementation-ready spec. Produces what/why/done requirements, constraints, non-goals, acceptance criteria, and research references without writing the implementation plan.
---

# Spec Writer

Use this skill after reality research and before planning or implementation.

## Core Rule

A spec defines what should exist, why it matters, and how done will be recognized. It does not define the implementation sequence unless the user explicitly asks for planning.

## Required Inputs

Prefer these inputs:

- Idea or problem statement.
- Reality research brief.
- Quality profile when available.
- Existing product/domain constraints.
- Target users and success criteria.

If research is missing and the topic is unclear, recommend `reality-research` first.

## Process

1. Restate the objective in concrete terms.
2. Separate goals from non-goals.
3. Capture current reality and constraints from cited research.
4. Define functional requirements.
5. Define acceptance criteria that can be verified later.
6. Identify stories needed to validate the spec, but do not expand them unless asked or using `story-writer`.
7. List open questions and risky assumptions.
8. Stop before implementation planning.

## Output

Use this structure:

```markdown
# Spec: <feature or project>

## Objective

## Background And Current Reality

## Users

## Goals

## Non-goals

## Requirements

## Acceptance Criteria

## Constraints

## Stories Needed

## Open Questions

## Source References
```

When creating a file, default to:

```text
<project-root>/.thoughts/specs/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

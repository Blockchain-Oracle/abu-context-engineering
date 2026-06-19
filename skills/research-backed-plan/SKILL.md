---
name: research-backed-plan
description: Use when Abu wants an implementation plan based on completed research, quality profile, spec, and stories. Produces phased, verifiable steps with tests and checkpoints, and refuses to plan from vague assumptions when required research or specs are missing.
---

# Research-backed Plan

Use this skill after research, quality profile, spec, and stories are available or intentionally waived.

## Core Rule

The plan explains how to build. It must trace back to research, spec requirements, stories, and quality gates. Do not invent facts to fill missing research.

## Required Inputs

Prefer these inputs:

- Reality research brief.
- Project quality profile.
- Spec.
- Stories or acceptance criteria.
- Current repo state when implementation will happen in an existing codebase.

If a critical input is missing, state the gap and either request it or mark the assumption explicitly.

## Process

1. Summarize the accepted inputs.
2. List assumptions and open questions.
3. Define implementation phases.
4. For each phase, include:
   - Goal.
   - Files or areas likely affected.
   - Tests or checks.
   - Acceptance criteria covered.
   - Stop condition.
5. Include a verification-audit checkpoint before completion.
6. Do not begin implementation unless the user asks to execute the plan.

## Output

Use this structure:

```markdown
# Plan: <feature or project>

## Inputs

## Assumptions

## Open Questions

## Phase 1: <name>

### Goal

### Work

### Checks

### Acceptance Criteria Covered

### Stop Condition

## Verification Checkpoint

## Handoff Notes
```

When creating a file, default to:

```text
<project-root>/.thoughts/plans/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

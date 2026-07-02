---
name: research-backed-plan
description: Use when Abu wants an implementation plan based on completed research, quality profile, spec, and stories. Produces phased, verifiable steps with tests and checkpoints, and refuses to plan from vague assumptions when required research or specs are missing.
---

# Research-backed Plan

Use this skill after research, quality profile, spec, and stories are available or intentionally waived.

If a high-fidelity prototype exists, use this skill only after prototype discovery and prototype reintegration are complete and accepted, unless Abu explicitly waives that gate.

## Core Rule

The plan explains how to build. It must trace back to research, spec requirements, stories, and quality gates. Do not invent facts to fill missing research.

## Required Inputs

Prefer these inputs:

- Reality research brief.
- Project quality profile.
- Spec.
- Stories or acceptance criteria.
- Prototype discovery report, when a prototype exists.
- Prototype reintegration report, when a prototype exists.
- Current repo state when implementation will happen in an existing codebase.

If a critical input is missing, state the gap and either request it or mark the assumption explicitly.

## Prototype Gate Rule

When a prototype exists, refuse to plan broad implementation if there is no accepted prototype reintegration report.

The plan must not silently carry prototype mocks into real implementation. For each integration-dependent phase, state whether the path is:

- real MVP integration,
- simulated demo-only with visible labeling,
- deferred and not claimed,
- blocked.

If Abu says no mocks should remain in real integration, treat mock-backed behavior as a blocker unless it is explicitly limited to local development/test fixtures and excluded from the judged product path.

## Process

1. Summarize the accepted inputs.
2. List assumptions and open questions.
3. If a prototype exists, summarize the reintegration gate decision and no-shipping-mock decisions.
4. Define implementation phases.
5. For each phase, include:
   - Goal.
   - Files or areas likely affected.
   - Real integration path.
   - Mock/simulation policy.
   - Tests or checks.
   - Acceptance criteria covered.
   - Stop condition.
6. Include a verification-audit checkpoint before completion.
7. Do not begin implementation unless the user asks to execute the plan.

## Output

Use this structure:

```markdown
# Plan: <feature or project>

## Inputs

## Assumptions

## Open Questions

## Prototype Reintegration Gate

## Phase 1: <name>

### Goal

### Work

### Real Integration Path

### Mock/Simulation Policy

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

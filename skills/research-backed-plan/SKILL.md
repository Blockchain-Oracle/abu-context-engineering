---
name: research-backed-plan
description: Use when Abu wants an implementation plan based on completed research, quality profile, spec, stories, and (when UI is in scope) the accepted design document. Produces phased, verifiable steps with tests and checkpoints, includes the mandatory Integration Reality Matrix (every integration-bearing surface classified REAL_MVP / REAL_LATER / SIMULATED_DEMO_ONLY / OUT_OF_SCOPE / BLOCKED — absorbed from the retired prototype-reintegration skill), drafts in Plan Mode with research enabled when the harness provides it, and refuses to plan from vague assumptions when required research or specs are missing.
---

# Research-backed Plan

Use this skill after research, quality profile, spec, and stories are available or intentionally waived. When UI work is in scope, plan after the design document is accepted.

Draft the plan with research enabled: re-read the corpus, and go back online (docs, vendor pages, live probes) whenever a load-bearing fact needs re-verifying — plans inherit the reality-research discipline. When the harness provides a plan mode, draft there.

## Core Rule

The plan explains how to build. It must trace back to research, spec requirements, stories, and quality gates. Do not invent facts to fill missing research.

## Required Inputs

Prefer these inputs:

- Reality research brief.
- Project quality profile.
- Spec.
- Stories or acceptance criteria.
- Product surface map and design document, when UI is in scope.
- The running design/coverage-audit.md, when implementation has already produced screens.
- Legacy prototype discovery/reintegration reports, when the project predates pipeline v0.8.0.
- Current repo state when implementation will happen in an existing codebase.

If a critical input is missing, state the gap and either request it or mark the assumption explicitly.

## Integration Reality Matrix (required)

Before phases are cut, inventory every integration-bearing product surface — APIs, SDKs, MCP servers, wallets, x402/payment paths, auth, databases, storage, agents, external services — and classify each:

- `REAL_MVP`: must be real in MVP; name the concrete tool/API/SDK and its verified capability source.
- `REAL_LATER`: deferred; the product must visibly avoid claiming it.
- `SIMULATED_DEMO_ONLY`: allowed only with explicit in-UI labeling; no product claim may depend on it.
- `OUT_OF_SCOPE`: not part of the accepted product; matches a spec non-goal.
- `BLOCKED`: cannot proceed without more research or an Abu decision; attach the unblocking action and the fallback.

No mock ships silently. For hackathon/submission work, judged proof paths default to `REAL_MVP`; a `BLOCKED` surface on a judged path blocks the affected phase (and only that phase) until resolved. If Abu says no mocks should remain, treat mock-backed behavior as a blocker unless it is explicitly limited to local development/test fixtures and excluded from the judged product path.

## Process

1. Summarize the accepted inputs.
2. List assumptions and open questions.
3. Build the Integration Reality Matrix and resolve or flag every BLOCKED surface.
4. Define implementation phases (UI phases land screens in batches of 3-4, each gated by `screen-batch-audit`).
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

## Integration Reality Matrix

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

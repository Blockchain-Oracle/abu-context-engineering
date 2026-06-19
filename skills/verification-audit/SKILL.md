---
name: verification-audit
description: Use when Abu wants proof that implementation matches the accepted spec, stories, plan, designer brief, and project quality profile before calling work done or opening/merging a PR. Produces a traceability audit with evidence, commands, missing coverage, deviations, and a pass/fail verdict. This is distinct from code review.
---

# Verification Audit

Use this skill after implementation and before claiming completion.

## Core Rule

Verification audit proves traceability. It is not a PR review. Do not approve work because it looks plausible; approve only when spec, stories, plan, code, tests, and commands line up.

## Inputs To Gather

Prefer these inputs:

- Spec.
- Stories and acceptance criteria.
- Designer brief when UI/prototype work is in scope.
- Research-backed plan.
- Project quality profile.
- Changed files or diff.
- Test/build/lint/typecheck output.
- Known deviations or intentionally skipped work.

If key artifacts are missing, mark the audit incomplete and explain what cannot be verified.

## Process

1. List the artifacts checked.
2. Extract requirements and acceptance criteria.
3. Map each requirement to implementation evidence.
4. Map each acceptance criterion to test, command output, screenshot, or manual verification evidence.
5. Compare implementation against the plan and record deviations.
6. Run or cite required quality gates when feasible.
7. Separate blocking gaps from acceptable follow-ups.
8. Give a clear verdict.

## Verdicts

- Pass: requirements satisfied, required gates pass, deviations are justified.
- Conditional pass: usable with explicit non-blocking follow-ups.
- Fail: missing required behavior, failing gates, unverified acceptance criteria, or unexplained deviations.
- Incomplete: required artifacts or evidence are missing.

## Output

Use this structure:

```markdown
# Verification Audit: <feature or project>

## Verdict

## Artifacts Checked

## Requirement Traceability

## Acceptance Criteria Coverage

## Quality Gates

## Deviations From Plan

## Gaps And Risks

## Follow-ups

## Evidence Log
```

When creating a file, default to:

```text
<project-root>/.thoughts/verification/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

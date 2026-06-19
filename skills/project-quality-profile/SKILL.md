---
name: project-quality-profile
description: Use when starting or onboarding a project to decide stack-specific quality gates, CI/CD, local hooks, lint, format, test, build, commit message rules, file length limits, and verification commands. Inspects the actual project before recommending guardrails and avoids one-size-fits-all enforcement.
---

# Project Quality Profile

Use this skill before implementation or when creating/updating repo AGENTS.md, hooks, or CI.

## Core Rule

Inspect the project before choosing guardrails. A web app, smart contract repo, Python service, Codex plugin, and monorepo need different checks.

The helper script is not the research. It only collects signals. Use it as evidence alongside manifests, existing docs, CI files, package scripts, test layout, and source tree inspection.

## Process

1. Identify the project root and inspect files with fast tools such as `rg --files`.
2. Run `scripts/detect-project-stack.py <project-root>` from this plugin when useful, then verify its result against actual project files.
3. Identify existing commands from manifests and docs before inventing commands.
4. Choose quality gates by stack:
   - Format/lint.
   - Typecheck or static analysis.
   - Unit/integration tests.
   - Build/package.
   - Security checks where appropriate.
   - File length guardrail: target 200 source lines, warn above 200, hard fail above 300 unless generated or explicitly justified.
   - Commit message enforcement when the repo uses conventional commits.
5. Separate local hooks from CI gates. Hooks are fast feedback; CI is the final gate.
6. Produce a profile, not code changes, unless the user asks to implement it.

## Output

Use this structure:

```markdown
# Project Quality Profile: <project>

## Detected Stack

## Existing Commands

## Required Local Checks

## Required CI Gates

## Suggested Hooks

## File Size Policy

Default recommendation:

- Target: 200 source lines.
- Warning: above 200 source lines.
- Hard cap: above 300 source lines.
- Exclusions: generated files, build output, vendored code, fixtures, lockfiles, and framework output.
- Escape hatch: allow larger files only with a written reason in the quality profile or PR.

## Commit Policy

## AGENTS.md Notes

## Open Questions
```

When creating a file, default to:

```text
<project-root>/.thoughts/quality/YYYY-MM-DD-project-quality-profile.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

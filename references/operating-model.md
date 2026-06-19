# Abu Context Engineering Operating Model

## Objective

Create a Codex-native workflow that turns an idea into verified software through accumulated context instead of repeated rediscovery.

The workflow is:

```text
idea
-> raw sources
-> domain wiki
-> reality research
-> quality profile
-> spec
-> stories
-> designer brief
-> high-fidelity mocked prototype
-> prototype discovery
-> spec/story/quality deltas accepted
-> plan
-> implementation loop
-> verification audit
-> PR/code review
-> handoff and wiki update
```

## Non-goals

- Do not make AGENTS.md a large process manual.
- Do not replace hooks, linters, tests, or CI with prompt instructions.
- Do not let research documents propose implementation unless the user explicitly asks for solutions.
- Do not assume one folder structure or one CI profile fits every project.
- Do not treat specs and stories as the same artifact.

## Artifact Boundaries

`AGENTS.md` is the small always-on router. It should mention project commands, project conventions, and which skills to use. It should not contain full workflows.

Skills are reusable workflows. They teach Codex how to perform a task such as reality research, quality profiling, domain wiki maintenance, planning, or verification.

Hooks and CI are deterministic enforcement. Mechanical rules such as file length, lint, formatting, typecheck, tests, and commit message style belong there.

The domain wiki is persistent knowledge. It compounds across sessions and should cite raw sources.

Specs define what should be built, why it matters, and what done means.

Stories describe user-facing slices or BDD-style acceptance paths derived from a spec.

Designer briefs package project context for a design/prototype agent. They should explain the product, users, flows, screens, states, domain details, inspirations, and prototype scope. They should ask for a high-fidelity mocked prototype: production-quality UX and visuals with mocked data and mocked integrations. They should not prescribe colors, fonts, or exact visual style unless brand rules or user instructions require it.

Prototype discovery audits the designer's output after it exists. It extracts newly revealed requirements, hidden data needs, routes, auth rules, API contracts, schema candidates, states, and implementation implications. It writes a discovery report first; specs, stories, and plans should be updated after review instead of letting the prototype silently replace the source of truth.

Plans define how to implement approved specs, stories, and accepted prototype-discovery deltas.

Verification audits prove traceability from spec to stories to plan to code to tests. They are not the same as PR review.

PR/code review looks for bugs, maintainability risks, security issues, and missing tests.

Handoffs preserve current state for resuming work without re-reading the full conversation.

## Default Storage

Use this layout unless the user or project gives a better one:

```text
<project-root>/.thoughts/
  raw/
  wiki/
  research/
  quality/
  specs/
  stories/
  design/
  prototype-discovery/
  plans/
  verification/
  handoffs/
```

Raw sources are immutable. Wiki files are maintained by the agent. Specs, stories, design briefs, prototype discovery reports, plans, verification, and handoffs are project artifacts.

## First Plugin Scope

The first usable version implements:

- `reality-research`
- `project-quality-profile`
- `domain-wiki`
- `spec-writer`
- `story-writer`
- `designer-brief`
- `prototype-discovery`
- `research-backed-plan`
- `agents-md-author`
- `verification-audit`
- `handoff-compaction`
- `scripts/check-file-lengths.py`
- `scripts/detect-project-stack.py`

The core workflow is now covered. Future optional skills should be added only when repeated friction proves they are worth keeping always available.

## Quality Rule Placement

Use prose instructions only for intent. Use deterministic tooling for enforcement.

Examples:

- File length: target 200 source lines, warn above 200, hard fail above 300 unless generated or explicitly justified. Enforce with skill guidance plus `scripts/check-file-lengths.py`, local hooks, and CI.
- Commit messages: commitlint or equivalent hook plus CI.
- JS/TS formatting/linting: Biome or ESLint based on project profile.
- Smart contracts: Foundry, Hardhat, Slither, or other tools based on project profile.
- Python: Ruff, mypy/pyright, pytest based on project profile.

The numbers are heuristics, not a law. Prefer cohesive modules over mechanical splitting. Generated files, build outputs, vendored code, fixtures, and framework output should be excluded from file-length checks.

## Research Discipline

Reality research documents current reality only. It may include verified facts, relevant source excerpts, inferences, unknowns, and questions. It must not contain proposed implementation steps unless the user explicitly requests a solution pass.

## Decision Checkpoints

Use explicit checkpoints:

1. Research accepted.
2. Quality profile accepted.
3. Spec accepted.
4. Stories accepted.
5. Designer brief accepted when UI/prototype work is in scope.
6. Prototype discovery accepted when a prototype exists.
7. Spec/story/quality deltas accepted when prototype discovery finds gaps.
8. Plan accepted.
9. Implementation verified.
10. Handoff written.

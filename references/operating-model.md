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
-> product surface map
-> design document (tokens + laws; one living sample screen only when taste needs deciding)
-> goal prompt refreshed when useful
-> plan (Plan Mode with research enabled; includes the integration reality matrix)
-> implementation loop (screens land in batches, audited against map + design doc; spec/story deltas accepted as they arise)
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

Goal prompts are execution controls. They tell an agent what objective Abu is setting now, which artifacts to inspect, which Context Engineering gates must be followed, and when to pause for Abu. A goal prompt is not a replacement for research, specs, stories, plans, implementation, verification, or handoff.

Specs define what should be built, why it matters, and what done means.

Stories describe user-facing slices or BDD-style acceptance paths derived from a spec. Stories are not frozen: planning and the implementation loop's screen batch audits may propose story deltas as the product gets built and seen, and those deltas must be accepted at a checkpoint rather than applied silently.

Product surface maps make the concrete product surface explicit before a design document: full screen inventory, navigation flow, per-screen required states (loading, empty, error, success, and product-specific states), on-screen data shapes, and generated artifacts. They exist because design direction written from stories alone delegates dozens of micro-decisions to imagination. They stay on the product surface — no database schema, API design, or code architecture.

Design documents replace the prototype stage entirely (locked with Abu 2026-07-23, second design postmortem on x402arc; verified against 2026 practice — spec-driven agent workflows plan from documents and iterate design in the real codebase, because "prototypes stop being mere mockups; they become previews of production"). Design is aesthetics and aesthetics keep changing; what the pipeline needs before planning is a contract, not screens. The design document is that contract: the product's LAWS (fixed vocabulary, honesty rules, jargon bans), the visual language as TOKENS (palette per theme, type roles, spacing, motion rules, signature elements and their semantics), per-surface direction (default sentence → hard constraints → the trap), the accessibility bar, and named anti-references. It is written in-repo by the context-holding agent from the whole corpus, consuming the product surface map as the source of truth for screens, states, and data shapes. **Taste protocol:** when the visual language is genuinely undecided, build at most ONE living sample screen on the product's demo-critical spine and iterate it with the user in fast rounds; once accepted, extract its tokens into the design document and archive the sample as direction evidence. The sample is a taste instrument, never a coverage artifact — coverage happens in the implementation loop, on production screens. The context-custody rule stands: no external, context-poor design environment by default; commissioning a human designer is an optional mode, and then the design document is their brief and their work returns in audited batches, never one full-surface drop.

Screen batch audits keep design verification continuous during implementation. Screens land in batches of 3-4 real, production screens; each batch is audited against the product surface map and the design document (required states, canonical data verbatim, copy laws, token fidelity, accessibility) before the next batch starts, and findings append to one running `design/coverage-audit.md` as proposed deltas — specs and stories are updated after review, never silently. This is the same continuous-gate discipline every text stage already uses, applied to the built product instead of a throwaway artifact.

Plans define how to implement approved specs, stories, the accepted design document, and the plan's own integration reality matrix: before tasks are cut, every integration-bearing product surface (APIs, wallets, payments, auth, storage, MCP servers, agents, external services) is classified as real-for-MVP, real-later with a visible non-shipping limitation, simulated-demo-only with explicit labeling, out of scope, or blocked pending research or a user decision. No mock ships silently; a blocked judged-path surface blocks the plan. Plans are drafted with research enabled — the planning agent re-reads the corpus and goes back online whenever reality needs re-verifying — and in Plan Mode when the harness provides it.

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
  prototype-reintegration/
  goals/
  plans/
  verification/
  handoffs/
```

Raw sources are immutable. Wiki files are maintained by the agent. Specs, stories, design documents, coverage-audit logs, plans, verification, and handoffs are project artifacts. The design document, direction evidence (archived sample screens), and the running `coverage-audit.md` live under `design/`; the `prototype-discovery/` and `prototype-reintegration/` directories exist only in legacy projects and in the optional external-designer mode.

## First Plugin Scope

The first usable version implements:

- `reality-research`
- `project-quality-profile`
- `domain-wiki`
- `spec-writer`
- `story-writer`
- `product-surface-map`
- `design-document` (absorbed `designer-brief`)
- `screen-batch-audit` (absorbed `prototype-discovery`; `prototype-reintegration` folded into `research-backed-plan`)
- `goal-writer`
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
5. Product surface map accepted when UI work is in scope.
6. Design document accepted when UI work is in scope (its sample screen iterated to acceptance first, when taste needed deciding).
7. Plan accepted — integration reality matrix included; no silent mocks on judged paths.
8. Implementation verified — screen batch audits green; spec/story deltas accepted as they arose.
9. Handoff written.

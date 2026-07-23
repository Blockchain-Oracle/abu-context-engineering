---
name: goal-writer
description: Use when Abu asks what goal to set, wants a Codex/agent goal prompt, or needs a Context Engineering objective after research, spec, stories, surface map, design document, planning, implementation, verification, or handoff. Writes a paste-ready goal that makes agents inspect actual project state, follow Abu Context Engineering gates in order, keep running without losing design-document and surface-map fidelity, and pause only for real blockers such as missing credentials, tokens, funding, external accounts, irreversible publishing, or user decisions.
---

# Goal Writer

Write the goal Abu should set for an agent. The output is a paste-ready goal prompt, not a substitute for doing the work.

## Core Rule

The goal must preserve process memory. It should tell the next agent where the project is, what to inspect, what gates must happen in order, and when to keep going versus when to stop for Abu.

Do not write a vague goal like "build the app." Write a goal that forces the agent to:

- inspect actual repo and `.thoughts/` state before acting,
- follow the accepted Abu Context Engineering workflow,
- keep design-document tokens/laws and surface-map coverage intact,
- resolve every integration through the plan's integration reality matrix (no silent mocks),
- implement only after accepted gates allow implementation,
- verify before claiming done (screen batch audits green for UI work),
- pause only for real blockers.

## Inputs To Inspect

Read what exists before writing the goal:

- `AGENTS.md`, `CLAUDE.md`, or project instruction files.
- `.thoughts/` artifacts: wiki, research, quality, specs, stories, design (design doc, direction evidence, coverage-audit log), plans, verification, handoffs — plus legacy prototype-discovery/reintegration dirs in pre-v0.8.0 projects.
- Design evidence Abu provided: sample screens, screenshots, HTML exports, or commissioned external-designer output.
- Current repo state and scaffold status.
- Existing package/tooling commands.
- Any user constraints about mocks, credentials, funding, publishing, deployment, or judging.

If the project has no `.thoughts/` folder yet, write a goal for the next missing Context Engineering stage rather than pretending artifacts exist.

## Stage Selection

Choose the narrowest goal that can keep meaningful work moving.

- If research is missing, write a research/domain/wiki goal.
- If quality profile is missing or stale, write a quality-profile goal.
- If spec or stories are missing, write a spec/story goal.
- If the surface map is missing before UI work, write a product-surface-map goal.
- If the design document is missing before UI work, write a design-document goal (taste protocol included when the visual language is undecided).
- If the plan is missing — or exists without an integration reality matrix — write a research-backed-plan goal.
- If the plan is accepted, write an implementation goal with screen batch audits, verification, and handoff included.
- If batch audits or planning produced spec/story deltas, write a goal to accept/update those artifacts.
- If implementation is done or nearly done, write a verification/handoff goal.
- Legacy projects with an unaudited external prototype: write a screen-batch-audit (external mode) goal feeding the plan's integration reality matrix.

For Abu's post-design handoff case, prefer a single goal that starts at the plan and continues through implementation, verification, and handoff only when each gate passes.

## Goal Prompt Contract

The generated goal should contain these sections:

```markdown
Set a goal to <objective>.

Objective:
<one clear outcome>

Current context to inspect:
- <actual files/folders/artifacts>

Required workflow:
1. <next Context Engineering gate>
2. <following gate>
3. <continue through implementation/verification only if gates pass>

Autonomy rules:
- Keep working through the accepted gates without asking Abu to restate the process.
- Inspect actual files before deciding what exists.
- Do not skip the design document, the plan's integration reality matrix, screen batch audits, accepted deltas, verification, or handoff when they are required.
- Preserve design-document fidelity and surface-map coverage — do not lose screens, states, copy, or interaction details.
- Do not silently ship mocks as real product behavior; every mock lives in the integration reality matrix or it is a blocker.

Pause and ask Abu only for:
- missing API keys, OAuth apps, wallet keys, testnet funding, NPM tokens, deployment tokens, external accounts, paid services, or irreversible publishing/deployment approval;
- unresolved product decisions that cannot be answered from the accepted artifacts;
- live settlement, payment, or production credentials that cannot be safely simulated or deferred.

Constraints:
- <project-specific constraints>

Definition of done:
- <proof the goal is actually achieved>
```

Do not add a token budget unless Abu explicitly asks for one.

## Post-design-document Goal Pattern

When Abu has accepted the design document and wants the agents to continue end to end, write the goal in this shape:

```markdown
Set a goal to carry the project from the accepted design document through planning, implementation, verification, and handoff without losing design-document or surface-map fidelity.

Objective:
Inspect the actual project state and accepted artifacts, complete the remaining Abu Context Engineering gates in order, then build and verify the accepted MVP only after those gates permit implementation.

Required workflow:
1. Write or update the research-backed plan (Plan Mode when available): phases, granular pass/fail feature checklist, and the Integration Reality Matrix classifying every integration-bearing surface (REAL_MVP / REAL_LATER / SIMULATED_DEMO_ONLY / OUT_OF_SCOPE / BLOCKED) — resolve or escalate every BLOCKED judged-path surface.
2. Implement the smallest complete real product loop first, honoring design-document tokens/laws.
3. Land UI screens in batches of 3-4; run `screen-batch-audit` on each batch before the next; append to design/coverage-audit.md.
4. Accept spec/story/design-doc deltas at checkpoints as audits reveal them.
5. Continue expanding only where the plan and quality gates allow.
6. Run lint/typecheck/build/tests/browser checks or the project-equivalent verification.
7. Write a verification audit and handoff report.

Pause and ask Abu only for missing secrets, API keys, OAuth credentials, wallet funding, NPM/deployment tokens, external account setup, irreversible publish/deploy approval, or product decisions not answerable from artifacts.
```

Customize it with real project file paths and constraints.

## Output

Return:

1. A short note explaining why this is the right next goal.
2. One paste-ready goal prompt.
3. Any immediate blockers or keys Abu should prepare.

When creating a file, default to:

```text
<project-root>/.thoughts/goals/YYYY-MM-DD-<topic>-goal.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

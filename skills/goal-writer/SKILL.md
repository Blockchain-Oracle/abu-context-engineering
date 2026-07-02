---
name: goal-writer
description: Use when Abu asks what goal to set, wants a Codex/agent goal prompt, or needs a Context Engineering objective after research, spec, stories, designer brief, prototype, prototype discovery, prototype reintegration, planning, implementation, verification, or handoff. Writes a paste-ready goal that makes agents inspect actual project state, follow Abu Context Engineering gates in order, keep running without losing frontend/prototype details, and pause only for real blockers such as missing credentials, tokens, funding, external accounts, irreversible publishing, or user decisions.
---

# Goal Writer

Write the goal Abu should set for an agent. The output is a paste-ready goal prompt, not a substitute for doing the work.

## Core Rule

The goal must preserve process memory. It should tell the next agent where the project is, what to inspect, what gates must happen in order, and when to keep going versus when to stop for Abu.

Do not write a vague goal like "build the app." Write a goal that forces the agent to:

- inspect actual repo and `.thoughts/` state before acting,
- follow the accepted Abu Context Engineering workflow,
- keep prototype details and frontend fidelity intact,
- convert prototype mocks into real integration decisions,
- implement only after accepted gates allow implementation,
- verify before claiming done,
- pause only for real blockers.

## Inputs To Inspect

Read what exists before writing the goal:

- `AGENTS.md`, `CLAUDE.md`, or project instruction files.
- `.thoughts/` artifacts: wiki, research, quality, specs, stories, design, prototype discovery, prototype reintegration, plans, verification, handoffs.
- Prototype paths, screenshots, HTML exports, Figma exports, or designer output Abu provided.
- Current repo state and scaffold status.
- Existing package/tooling commands.
- Any user constraints about mocks, credentials, funding, publishing, deployment, or judging.

If the project has no `.thoughts/` folder yet, write a goal for the next missing Context Engineering stage rather than pretending artifacts exist.

## Stage Selection

Choose the narrowest goal that can keep meaningful work moving.

- If research is missing, write a research/domain/wiki goal.
- If quality profile is missing or stale, write a quality-profile goal.
- If spec or stories are missing, write a spec/story goal.
- If the designer brief is missing before UI prototype work, write a designer-brief goal.
- If a high-fidelity prototype exists but has not been audited, write a prototype-discovery goal.
- If prototype discovery exists but real integrations have not been mapped, write a prototype-reintegration goal.
- If discovery or reintegration found deltas, write a goal to accept/update spec, stories, and quality profile before planning.
- If the plan is missing after accepted deltas, write a research-backed-plan goal.
- If the plan is accepted, write an implementation goal with verification and handoff included.
- If implementation is done or nearly done, write a verification/handoff goal.

For Abu's post-prototype handoff case, prefer a single goal that starts at prototype discovery or prototype reintegration and continues through planning, implementation, verification, and handoff only when each gate passes.

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
- Do not skip prototype discovery, prototype reintegration, accepted deltas, planning, implementation, verification, or handoff when they are required.
- Preserve frontend/prototype fidelity and do not lose screens, states, copy, or interaction details.
- Do not silently ship prototype mocks as real product behavior.

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

## Post-prototype Goal Pattern

When Abu has handed over a high-fidelity prototype and wants the agents to continue end to end, write the goal in this shape:

```markdown
Set a goal to carry the project from the accepted high-fidelity prototype through Context Engineering reintegration, implementation, verification, and handoff without losing prototype fidelity.

Objective:
Inspect the actual project state and prototype artifacts, complete the remaining Abu Context Engineering gates in order, then build and verify the accepted MVP only after those gates permit implementation.

Required workflow:
1. Audit the prototype with `prototype-discovery`; extract screens, flows, states, data, API/event candidates, auth/payment/wallet boundaries, edge cases, and spec/story/quality deltas.
2. Run `prototype-reintegration`; map every prototype screen and mock to real data, services, auth, wallet/payment, storage, proof, and external integration decisions.
3. Update or rewrite spec, stories, and quality profile only for accepted deltas.
4. Write or update a research-backed plan from the accepted artifacts.
5. Implement the smallest complete real product loop first, preserving frontend fidelity from the prototype.
6. Continue expanding only where the plan and quality gates allow.
7. Run lint/typecheck/build/tests/browser checks or the project-equivalent verification.
8. Write a verification audit and handoff report.

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

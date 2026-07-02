---
name: prototype-discovery
description: Use when Abu provides a finished UI prototype, static HTML/CSS/JS export, screenshots, Figma-like output, or design artifact and wants Codex to explore it end to end before implementation. Extracts screens, flows, states, hidden requirements, auth/API/schema/data needs, and spec/story/plan deltas. Translates prototype findings into the target project stack such as React or Next.js instead of copying static HTML blindly.
---

# Prototype Discovery

Use this skill after a designer/prototype agent has produced a high-fidelity mocked prototype.

## Core Rule

The prototype is evidence, not the source of truth. Explore it deeply, extract what it reveals, then write a discovery report with proposed spec/story/quality/profile/plan deltas. Do not silently rewrite specs or start implementation unless the user explicitly asks.

If the prototype was produced after prior research/spec/story/design work, prototype discovery is not the last pre-plan step. It must feed a prototype reintegration pass that maps the mocked UI back to real integrations, constraints, and non-shipping blockers.

## Stack Translation Rule

Prototype exports may be static HTML, CSS, JSX, screenshots, or generated design-system files. Treat those as design evidence. Before implementation, translate findings into the actual target stack from `project-quality-profile`.

Examples:

- If the project is React/Next, infer routes, components, hooks, server actions/API routes, schemas, and state boundaries.
- If the project is mobile, infer screens, navigation, native components, permissions, and platform states.
- If the project is static HTML, then HTML/CSS may be directly relevant.

Do not tell the implementation agent to copy prototype HTML/CSS into a React codebase unless that is the chosen architecture.

## Mock Boundary Rule

The high-fidelity prototype may use mocked data, mocked auth, mocked wallets, mocked API responses, mocked payments, or simulated backend behavior. These mocks are prototype evidence only.

Do not treat prototype mocks as implementation defaults. Every mocked surface that appears required for the product must be handed to `prototype-reintegration` to decide one of:

- real integration path for MVP,
- real integration path after MVP with a visible non-shipping limitation,
- explicit out-of-scope/non-goal,
- blocker requiring more research or user decision.

If Abu says the product should not ship mocks, call that out and require reintegration before implementation planning.

## Inputs To Gather

Prefer these inputs:

- Prototype folder, static HTML files, screenshots, design export, or hosted preview.
- Designer brief.
- Product surface map when it exists (the checklist of expected screens, states, and data shapes).
- Spec and stories.
- Project quality profile.
- Existing repo architecture if the project already exists.
- Any raw notes or inspiration that led to the prototype.

## What To Extract

Inspect the prototype end to end and identify:

- Screens, routes, modals, drawers, tabs, cards, and navigation paths.
- User journeys and decision points.
- Empty, loading, error, disabled, success, stopped/paused, and permission states.
- Data objects shown in the UI.
- Candidate database tables/collections and fields.
- Candidate API endpoints/server actions/events.
- Auth, wallet, account, session, permission, and role requirements.
- External integrations and provider keys.
- Settings and configuration surfaces.
- Background jobs, scheduled work, streams, queues, or realtime updates.
- Analytics, audit logs, history, receipts, and traceability needs.
- Mismatches with the existing spec or stories.
- Questions the prototype raises.

## Process

1. Inventory the prototype files/screens.
2. If runnable, inspect the main screens visually; otherwise inspect source and screenshots.
3. Build a screen map and user-flow map.
4. Extract implied product requirements.
5. Extract implied technical requirements.
6. Translate implementation implications into the target project stack.
7. Compare against spec, stories, designer brief, product surface map, and quality profile when available — for the surface map, check every listed screen, state, and data shape and flag anything the prototype dropped, changed, or invented.
8. Identify every prototype mock or simulation that would need real integration before shipping.
9. Write proposed deltas instead of editing source artifacts automatically.
10. Recommend `prototype-reintegration` before planning whenever the prototype represents flows that depend on real APIs, wallets, payments, auth, storage, MCP servers, agents, or external infrastructure.

## Output

Use this structure:

```markdown
# Prototype Discovery: <project or feature>

## Prototype Inspected

## Screen Map

## User Flows

## Revealed Product Requirements

## Revealed Technical Requirements

## Data Model Candidates

## API And Event Candidates

## Auth, Permissions, And Security Implications

## State And Edge Cases

## Target-stack Translation

## Mocked Prototype Surfaces

## Required Prototype Reintegration

## Spec Deltas

## Story Deltas

## Plan Deltas

## Quality Profile Deltas

## Open Questions

## Evidence
```

When creating a file, default to:

```text
<project-root>/.thoughts/prototype-discovery/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

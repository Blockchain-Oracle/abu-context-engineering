---
name: prototype-reintegration
description: Use after prototype-discovery when Abu has brought back a high-fidelity mocked prototype and wants the design reconciled with prior research, real APIs/tools/auth/wallet/payment/storage constraints, and implementation reality before spec/story updates or planning. Produces a real-integration map and blocks plans that would quietly ship prototype mocks.
---

# Prototype Reintegration

Use this skill after `prototype-discovery` and before `research-backed-plan` whenever a prototype exists and the real product depends on integrations, external tools, APIs, wallets, payments, auth, databases, agents, or infrastructure.

## Core Rule

The prototype is design evidence. It is not permission to ship mocks.

Before planning implementation, map every important prototype surface and state back to the research-backed reality of the product. Every mocked prototype behavior must become one of:

- real integration path for MVP,
- real integration path after MVP with a visible non-shipping limitation,
- explicit out-of-scope/non-goal,
- blocker requiring more research or Abu decision.

Do not start or approve an implementation plan while required product behavior is only represented by a prototype mock.

## Required Inputs

Prefer these inputs:

- Prototype discovery report.
- Prototype folder/screenshots/static export.
- Reality research briefs.
- Domain wiki.
- Quality profile.
- Spec.
- Stories and acceptance criteria.
- Designer brief.
- Current repo state, if implementation has started.
- Known tools/APIs/SDKs/services from research.

If any critical input is missing, state the gap and either request it or mark the reintegration report incomplete.

## What To Map

For each prototype screen, flow, and major state, map:

- User intent.
- Visible UI behavior.
- Data shown.
- Real source of that data.
- Real action or side effect.
- Required API/tool/SDK/service.
- Auth/session/wallet/payment boundary.
- Persistence or audit requirement.
- Error and recovery behavior.
- Mocked prototype behavior that must not ship.
- MVP integration decision.
- Open question or blocker.

## No-Shipping-Mock Rule

Use clear labels:

- `REAL_MVP`: must be real in MVP.
- `REAL_LATER`: can be deferred, but product must visibly avoid claiming it.
- `SIMULATED_DEMO_ONLY`: allowed only in demo/dev mode and must be labeled.
- `OUT_OF_SCOPE`: not part of the accepted product.
- `BLOCKED`: cannot proceed without more research or Abu decision.

For hackathon/submission work, prefer `REAL_MVP` for judged proof paths. `SIMULATED_DEMO_ONLY` is acceptable only when the UI clearly says it is simulated and no product claim depends on it.

## Process

1. Read prototype discovery, spec, stories, quality profile, designer brief, and relevant research.
2. Inventory prototype screens and critical states.
3. Create a screen-by-screen reintegration matrix.
4. Create an integration inventory for APIs, SDKs, MCP servers, wallets, x402/payment facilitators, databases, auth, and external services.
5. Classify every mocked or simulated prototype behavior with the no-shipping-mock labels.
6. Identify spec/story/quality deltas caused by reintegration.
7. Identify implementation-plan prerequisites and blockers.
8. State whether planning is allowed, blocked, or allowed only for a smaller real-integration slice.

## Multi-Agent Review Option

When the prototype is large or integration-heavy, use separate agents only with explicit roles:

- Prototype mapper: extracts screens, states, and data from the prototype.
- Reality mapper: maps screens to researched tools, APIs, services, and constraints.
- Skeptic reviewer: finds unsupported claims, accidental mocks, missing proof paths, and plan blockers.

The main agent must reconcile their outputs into one reintegration report. Multi-agent review is a guardrail, not a substitute for the reintegration matrix.

## Output

Use this structure:

```markdown
# Prototype Reintegration: <project or feature>

## Verdict

## Inputs Checked

## Screen-to-Reality Matrix

## Integration Inventory

## Mocked Prototype Surface Register

## No-Shipping-Mock Decisions

## Spec Deltas

## Story Deltas

## Quality Profile Deltas

## Plan Prerequisites

## Blockers And Open Questions

## Planning Gate Decision

## Evidence
```

When creating a file, default to:

```text
<project-root>/.thoughts/prototype-reintegration/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

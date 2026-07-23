---
name: prototype-discovery
description: Use during an in-repo prototype coverage build to audit each batch of 3-4 screens against the product surface map — states, canonical data, copy laws — appending findings to the running design/coverage-audit.md. Also use in the optional external mode when a commissioned prototype (static HTML/CSS/JS export, Figma-like output, screenshots) returns from a designer and needs a whole-artifact audit. Extracts revealed requirements, hidden data/auth/API/schema needs, and spec/story/plan deltas; never silently rewrites source artifacts.
---

# Prototype Discovery

The per-batch audit protocol of the in-repo coverage build — and, in the optional external mode, the whole-artifact audit of a commissioned prototype.

## Core Rule

The prototype is evidence, not the source of truth. The product surface map is the contract. Audit against it, extract what each batch reveals, and write findings as proposed deltas. Do not silently rewrite specs or start implementation unless the user explicitly asks.

## Why Per-Batch (the custody lesson)

A full-surface prototype audited after the fact accumulates its gap silently — drops, thinned differentiators, and law violations are only measured once they are expensive to fix (x402arc postmortem, 2026-07-23: the 24-screen external drop was missing whole mapped screens). Auditing every 3-4 screens keeps verification continuous, the same way every text stage of the pipeline audits one artifact against its parent immediately. A batch does not pass until its audit is green; the next batch does not start until the current one passes.

## Batch Audit Protocol (default mode, in-repo coverage build)

Inputs per batch: the batch's screens as built, the surface map sections they implement, the designer brief's LAWS, and the accepted direction-lock tokens.

Check, per screen:

1. **States** — every map-required state rendered (empty, loading, error, success, and the product-specific ones); flag MISSING, CHANGED, and INVENTED (mark inventions DISCOVERED — they are the point, not a violation, unless they change what the product is).
2. **Data** — on-screen data matches the map's canonical sample values verbatim; formats obey the map's number/address/unit rules.
3. **Copy laws** — the brief's fixed vocabulary and honesty rules appear exactly; banned words absent.
4. **Direction fidelity** — tokens from the accepted direction lock used; no per-screen aesthetic drift.
5. **Access basics** — contrast, focus visibility, reduced-motion, touch targets per the quality bar.
6. **Revealed needs** — new data objects, routes, auth/permission implications, API/schema candidates, background/realtime behavior the screens imply.

Append one entry per batch to `<project-root>/.thoughts/design/coverage-audit.md`:

```markdown
## Batch N — <screens> (YYYY-MM-DD)
Verdict: GREEN | RED (list blockers)
States: <missing/changed/discovered>
Data/canon: <deviations>
Laws: <violations>
Revealed: <requirements, data, API, auth implications>
Proposed deltas: <spec/story/quality/plan — proposed, not applied>
```

The running log IS the consolidated discovery record; `prototype-reintegration` consumes it.

## Mock Boundary Rule (both modes)

Prototype screens may mock data, auth, wallets, API responses, payments, or backend behavior. Mocks are prototype evidence only — never implementation defaults. Every mocked surface that appears required for the product is handed to `prototype-reintegration` to classify: real integration for MVP, real after MVP with a visible non-shipping limitation, explicit out-of-scope, or blocker needing research or a user decision. If the user says the product must not ship mocks, reintegration is mandatory before planning.

## Stack Translation Rule (both modes)

Prototype output is design evidence in whatever form it took (HTML/CSS, JSX, screenshots). Before implementation, translate findings into the target stack from `project-quality-profile` — routes, components, hooks, server actions, schemas, state boundaries for React/Next; screens, navigation, permissions for mobile. Do not instruct anyone to copy prototype markup into the codebase unless that is the chosen architecture.

## External Mode (optional — commissioned prototypes only)

When a human designer or dedicated design tool was deliberately commissioned (batch-gated contract per the designer brief), audit each returned batch with the protocol above. If a legacy full-surface drop arrives anyway, run one whole-artifact audit: inventory every file/screen, build the screen and flow map, then apply the batch checklist across the entire surface, comparing against spec, stories, brief, and surface map — flag everything dropped, changed, or invented. Write the report to `<project-root>/.thoughts/prototype-discovery/YYYY-MM-DD-<topic>.md` with sections: Prototype Inspected · Screen Map · User Flows · Revealed Product Requirements · Revealed Technical Requirements · Data Model Candidates · API And Event Candidates · Auth, Permissions, And Security Implications · State And Edge Cases · Target-stack Translation · Mocked Prototype Surfaces · Required Prototype Reintegration · Spec/Story/Plan/Quality Deltas · Open Questions · Evidence.

## Exit

Discovery is complete when every mapped screen has a green batch entry (or the external report is accepted), every mock is listed for reintegration, and proposed deltas are queued for the user's review. Recommend `prototype-reintegration` before planning whenever screens depend on real APIs, wallets, payments, auth, storage, MCP servers, agents, or external infrastructure.

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

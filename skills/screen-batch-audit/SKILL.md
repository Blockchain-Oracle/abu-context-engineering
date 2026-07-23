---
name: screen-batch-audit
description: Use during the implementation loop whenever UI screens are being built — after every batch of 3-4 real screens lands, audit them against the product surface map and the design document (required states, canonical data, copy laws, token fidelity, accessibility) and append findings to the running design/coverage-audit.md. Also use in the optional external mode to audit batches returned by a commissioned designer, or a legacy full-surface prototype drop. Successor of the retired prototype-discovery stage: same continuous-gate discipline, now applied to production screens instead of throwaway prototypes.
---

# Screen Batch Audit

The continuous design-coverage gate of the implementation loop. Every text stage of the pipeline audits one artifact against its parent immediately; this skill applies the same discipline to built screens.

## Core Rule

The surface map and the design document are the contract; the built screens are the claim. Audit every batch of 3-4 screens before the next batch starts. A batch does not pass until its audit is green. Findings are proposed deltas — specs, stories, and plans are updated after review, never silently.

## Why Per-Batch (the custody lesson)

Full-surface artifacts audited after the fact accumulate their gap silently — dropped screens, thinned differentiators, and law violations get measured only once they are expensive to fix (x402arc postmortem, 2026-07-23: a 24-screen external drop was missing whole mapped screens). Batching keeps verification continuous and cheap, on the real product.

## Batch Audit Checklist

Inputs per batch: the built screens, the surface map sections they implement, and the design document (LAWS + TOKENS).

Per screen:

1. **States** — every map-required state implemented (empty, loading, error, success, and the product-specific ones); flag MISSING, CHANGED, and INVENTED (mark inventions DISCOVERED — they are welcome unless they change what the product is).
2. **Data** — seeded/sample data matches the map's canonical values verbatim where the map pins them; number, unit, address, and linking rules obeyed.
3. **Copy laws** — the design document's fixed vocabulary and honesty rules appear exactly; banned words absent.
4. **Token fidelity** — palette semantics, type roles, motion rules, and signature elements per the design document; no per-screen aesthetic drift (deliberate evolution goes through a design-document update, not a one-off screen).
5. **Access basics** — contrast, focus visibility, reduced-motion, touch targets per the quality bar.
6. **Revealed needs** — new data objects, routes, auth/permission implications, API/schema candidates, background/realtime behavior the built screens expose.
7. **Integration honesty** — anything still mocked or simulated on this screen is checked against the plan's integration reality matrix; a mock not covered there is a RED flag and a proposed plan delta, not a shrug.

Append one entry per batch to `<project-root>/.thoughts/design/coverage-audit.md`:

```markdown
## Batch N — <screens> (YYYY-MM-DD)
Verdict: GREEN | RED (blockers listed)
States: <missing/changed/discovered>
Data/canon: <deviations>
Laws/tokens: <violations/drift>
Revealed: <requirements, data, API, auth implications>
Integration honesty: <mocks vs plan matrix>
Proposed deltas: <spec/story/plan/design-doc — proposed, not applied>
```

The running log is the consolidated record of what building the product taught us.

## External Mode (commissioned design work and legacy drops)

When a human designer or design tool was commissioned (see `design-document`, External Mode), audit each returned batch with the checklist above. If a legacy full-surface prototype drop arrives anyway, run the checklist across the entire artifact in one pass, write the report to `<project-root>/.thoughts/prototype-discovery/YYYY-MM-DD-<topic>.md`, and route every mocked surface into the plan's integration reality matrix before implementation planning proceeds.

## Exit

The build's design coverage is done when every mapped screen has a green batch entry and every proposed delta has been reviewed. Escalate to the user only the deltas that change what the product is.

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

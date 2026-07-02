---
name: product-surface-map
description: Use after stories and before designer-brief when Abu wants the concrete product surface written down — full screen inventory, navigation flow, per-screen required states (loading, empty, error, success, and product-specific states), on-screen data shapes, and entry points. Use whenever a designer brief would otherwise be written from spec/stories alone, when Abu says the project "feels shallow" for design handoff, or when a designer/prototype agent would be left to guess screens, states, or data. Prevents shallow briefs that delegate micro-decisions to the designer's imagination.
---

# Product Surface Map

Use this skill after stories exist and before writing a designer brief. It converts spec + stories into the concrete surface a designer must execute rather than guess.

## Core Rule

Make the implicit explicit. Every screen, state, and on-screen data shape a designer would otherwise invent must be written down here first. Stay on the product surface: no database schema, no API design, no code routes, no component architecture — those belong to prototype-discovery, reintegration, and planning.

## Why This Exists

A designer brief written from stories alone delegates dozens of micro-decisions (which screens exist, what an error looks like, what fields a document carries) to the designer's taste. Each guess is a coin-flip against what the user actually wants. The surface map converts "designer guesses" into "designer executes", and gives prototype-discovery a checklist to audit the returned prototype against.

## Required Inputs

Prefer these inputs:

- Accepted spec (requirements + acceptance criteria).
- Stories with scenarios.
- Reality research on comparable products (their screens, artifacts, and conventions).
- Quality profile (stack constraints that shape the surface, e.g. web vs mobile).
- Known demo/judging requirements when the project has them.

If stories are missing, recommend `story-writer` first.

## Process

1. Derive the screen inventory from stories: every screen, panel, and overlay a user can reach, grouped by role/actor.
2. Draw the navigation flow: entry points, the paths between screens, and the shortest path to the core action.
3. For EVERY screen, enumerate required states: loading, empty, error, success, disabled — plus product-specific states the designer could never invent (e.g. a deliberately-empty privacy view, an atomic-failure explanation, a claim-vs-auto variant).
4. Define on-screen data shapes: the exact fields each screen, row, card, and generated document displays (anchor to researched real-product anatomy when available).
5. Note copy tone and vocabulary rules (jargon bans, domain terms to use or avoid).
6. Mark open surface questions that are genuinely the designer's to answer (layout, visual treatment) versus decisions already made.
7. Keep each item traceable to a story or requirement ID where possible.
8. Stop before visual direction, wireframes, or implementation — the surface map feeds the designer brief; it does not replace it.

## Output

Use this structure:

```markdown
# Product Surface Map: <project or feature>

## Entry Points And Navigation Flow

## Screen Inventory (by role)

## Per-screen Required States

## On-screen Data Shapes

## Generated Artifacts (documents, exports, receipts)

## Copy And Vocabulary Rules

## Decided vs Designer's Call

## Traceability

## Open Questions
```

When creating a file, default to:

```text
<project-root>/.thoughts/design/YYYY-MM-DD-product-surface-map.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

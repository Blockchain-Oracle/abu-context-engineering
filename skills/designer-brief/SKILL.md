---
name: designer-brief
description: Use when Abu wants a designer-brief.md for an AI designer or prototype agent after research, specs, stories, inspiration, or project context have been gathered. Produces a rich product and flow brief for high-fidelity mocked UI prototypes, avoids AI-slop design patterns, and keeps backend/database/wallet/auth/API behavior mocked only inside the design prototype unless explicitly in scope.
---

# Designer Brief

Use this skill when preparing an external AI designer or prototype agent to design a product UI from existing project context.

## Core Rule

Give the designer enough product, domain, flow, and state context to make strong design decisions. Do not over-direct visual taste. Avoid prescribing colors, fonts, gradients, or exact aesthetics unless the user provided brand rules or explicitly asked for them.

## Relationship To Product Surface Map

When a product surface map exists, it is the source of truth for the screen inventory, per-screen states, and on-screen data shapes. The brief must consume it — embed or attach its content and add narrative direction on top — instead of re-deriving screens and states from spec/stories. The brief's own job is everything the surface map deliberately lacks: product story, users, domain teaching, journey narrative, inspiration, quality bar, mock boundaries, and creative freedom.

Only derive screens and states inline when no surface map exists, and say so — then recommend `product-surface-map` first for anything beyond a trivial surface.

## Interview The Designer First (when the designer is known)

When a specific designer/design agent will receive the brief, interview them BEFORE writing it — their answers shape the brief's structure and become the handback contract. Ask, from their point of view:

1. What input package do they need, in what format, and what do builders always forget to include?
2. Wireframes vs direction vs straight-to-hi-fi — their sequence, and where they want sign-off checkpoints.
3. Mobile vs desktop priority for this product's real audience.
4. Do they create the brand identity or receive it (plus the user's veto constraints).
5. The handback format they can realistically commit to (file structure, styling approach, how states are delivered, fonts/assets) — this becomes the contract both sides build against.
6. Their tools, and whether the toolchain changes what inputs they need.
7. The #1 thing builders do that ruins a handoff for them — then don't do it.

Give them just enough product context to answer meaningfully; the full brief comes after. Fold durable lessons from their answers back into this skill; fold project-specific terms into the brief only.

## Prototype Boundary

This brief is for high-fidelity design exploration and clickable/static prototype work. The prototype should feel production-quality in UX, information architecture, interaction detail, and visual polish, while using mocked data and mocked integrations by default.

Do not ask the designer to implement production database, auth, wallet, payment, API, or smart-contract integration unless the user explicitly says the design prototype should include real integration.

Mocked integrations in the design artifact are a design convenience only. They are not implementation decisions. When the prototype comes back, `prototype-discovery` and `prototype-reintegration` must identify every mocked data source, auth state, wallet action, payment path, API call, MCP/tool call, storage path, and proof/audit surface, then decide whether each becomes real in MVP, visibly simulated for demo only, deferred, out of scope, or blocked.

If the project depends on real integrations, include enough domain and integration context for the designer to represent realistic product states. Do not hide integration boundaries just because the prototype itself will mock them.

## Anti-slop Quality Bar

The brief should prevent generic AI-looking output without forcing the designer into one style. Require the prototype to be specific to the product, domain, users, and source material.

Call out these risks:

- Generic SaaS landing-page structure that could fit any product.
- Decorative effects with no product meaning.
- Wall-of-cards layouts where every section has the same weight.
- Nested cards inside cards.
- Fake metrics, vague buzzwords, or placeholder copy that does not teach the product.
- Hero sections that hide the actual product or workflow.
- Icons, charts, or animations that do not explain user intent.
- Missing empty, loading, error, disabled, and success states.

Phrase this as a quality bar, not a visual recipe. Do not ban or require specific colors, fonts, or aesthetics unless the project has brand constraints.

## Inputs To Gather

Prefer these inputs:

- Reality research.
- Domain wiki pages.
- Spec.
- Stories and acceptance criteria.
- Product surface map when available (screen inventory, per-screen states, data shapes) — prefer it as the backbone of the screen-by-screen direction.
- Product/user flow notes.
- Raw user notes and inspiration links.
- GitHub links, README files, screenshots, demos, or docs the designer should inspect.
- Known constraints and non-goals.
- Prototype target: landing page, dashboard, app flow, mobile, desktop, or responsive prototype.
- The designer's own stated working preferences and handback format when they have been interviewed — the brief should confirm that contract back to them verbatim so both sides build against the same terms.

## What To Include

Include:

- Product summary and why it exists — and when the project is demo-judged, LEAD with the demo script: what the audience must feel at each beat. The demo script drives design decisions more than the screen list does.
- Target users and their intent.
- Domain concepts the designer must understand.
- End-to-end journey and step-by-step flow.
- Screen inventory in recommended order (from the product surface map when it exists).
- Required content, data, empty states, loading states, and error states (from the product surface map when it exists; never silently drop a state it lists).
- Interaction ideas the designer may use, such as modals, drawers, tabs, carousels, timelines, animations, command menus, search, filters, or onboarding.
- Mock data expectations.
- Integration boundaries the prototype should represent, even when mocked.
- Inspiration sources and what each source is meant to communicate — plus at least one ANTI-reference: a named product/style the design must NOT resemble.
- Anti-slop quality bar and product-specific design risks.
- Explicit creative freedom for visual direction.
- Things not to design or implement.

Do not include:

- Fixed colors, fonts, spacing systems, or exact component styling unless brand constraints require them.
- Backend implementation instructions.
- Database schema requirements.
- Production integration instructions.
- Code architecture.

## Process

1. Read the available research, spec, stories, wiki, README, inspiration notes, and the product surface map when it exists.
2. Identify what the designer needs to understand before choosing screens or layout.
3. Convert user and product context into a concise but rich brief.
4. Give a recommended screen-by-screen journey — sourced from the product surface map when it exists, derived inline only when it does not.
5. State high-fidelity mocked prototype assumptions clearly.
6. Call out which mocked surfaces must be revisited during prototype discovery and reintegration.
7. Add anti-slop quality constraints based on the product, not generic style bans.
8. Preserve creative freedom for visual treatment.
9. List source links/files the designer should inspect.

## Output

Use this structure by default. When the designer has been interviewed and asked for a different structure, their requested structure wins — the headings below then become a coverage checklist (every element must still be present or consciously dropped with a stated reason), not mandatory sections.

```markdown
# Designer Brief: <project or feature>

## Purpose

## Prototype Scope

## Product Context

## Target Users

## Domain Knowledge The Designer Needs

## Core User Journey

## Screen-by-screen Direction

## Data, States, And Mocking Rules

## Prototype Quality Bar

## Anti-slop Risks To Avoid

## Interaction Opportunities

## Inspiration And Source Material

## Creative Freedom

## Explicit Non-goals

## Open Questions
```

When creating a file, default to:

```text
<project-root>/.thoughts/design/YYYY-MM-DD-designer-brief.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

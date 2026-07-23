---
name: designer-brief
description: Use whenever Abu wants a designer brief, design handoff, prototype commission, direction-lock commission, or "brief for Claude design" — any moment a design/prototype phase starts after research, spec, stories, or a product surface map exist. Also use when Abu criticizes an existing brief as shallow, rigid, demo-framed, or taste-dictating. Produces a product-first designer-brief.md woven from ALL project artifacts with visible source threads, structured in three registers (LAWS = product identity, CONTEXT = deep understanding, DIRECTION = overrulable suggestions), with a discovery protocol ("the floor, not a cage" — designers mark unlisted screens DISCOVERED), zero visual-taste dictation, zero demo framing, and mocked-only integrations inside the prototype unless explicitly in scope. Default recipient is the context-holding agent building the prototype in-repo (direction lock, then batch-audited coverage build); an external designer is an optional mode under a batch-gated contract.
---

# Designer Brief

Use this skill when preparing whoever builds the prototype to design a product UI from existing project context.

## Context Custody (who receives the brief)

By default the brief's recipient is the context-holding agent itself, building **in-repo**: first a **direction lock** (a few fully-alive screens auditioning a visual language on the product's demo-critical spine, iterated with the user until accepted), then a **coverage build** in batches of 3-4 screens, each batch audited against the surface map by `prototype-discovery` before the next starts. This is the custody rule (locked 2026-07-23): handing the corpus to an external, context-poor design environment structurally produces coverage loss the pipeline later pays to reconcile.

An **external designer or dedicated design tool is an optional mode**, chosen deliberately — and then the commission must carry the batch-gated contract explicitly: screens return in audited batches of 3-4, never as one full-surface drop, with the surface map attached as the coverage checklist.

## Core Rule

Give the designer deep product, domain, flow, and state understanding — and open hands. The brief transmits WHAT things are and WHO they serve so thoroughly the designer could argue about the product; it never dictates HOW things should look. The product story leads, always. No demo framing, stage beats, or audience language anywhere — designers design for users (product-not-demo doctrine, locked 2026-07-23); build/polish priority appears only as plain sequencing inside the screen direction when deadlines demand it.

Do not prescribe colors, fonts, dark/light mode, motifs, gradients, or aesthetics — even when a visual direction was discussed earlier in the project — unless the user explicitly says to put brand rules in the brief. The writer of a brief is not the designer (locked 2026-07-23).

## The Three Registers (structure every brief's content this way)

Open every brief with a short "How To Read This Brief" section declaring three kinds of content, then keep them distinguishable throughout:

- **LAWS** — the product's identity; non-negotiable. Fixed vocabulary, honesty/trust rules, jargon bans, real-data-only. These are what make the product itself.
- **CONTEXT** — the understanding: what each surface is, who uses it, why it exists, what research verified. The deep material.
- **DIRECTION** — the team's current picture: suggested emphasis, component ideas, foreseen traps. Explicitly overrulable: "when your idea beats ours, yours wins."

## The Discovery Protocol (the prototype is a discovery instrument)

Prototyping is how the product gets SEEN for the first time; the designer WILL discover screens, states, and connective flows nobody listed — that is the prototype's purpose, not a violation. The brief must say so: the scope list is **the floor, not a cage**. Instruct the designer to design what the product clearly needs and mark additions **DISCOVERED**; the per-batch coverage audit (`prototype-discovery`) reconciles them as each batch lands. Only additions that would change what the product IS come back as questions first. Never write "do not invent pages" as a blanket ban.

## Weave From The Artifacts (a brief is a culmination, not a riff)

The brief is written FROM the project's accumulated artifacts — research, spec, stories, surface map, requirements, wiki — and must show its threads: each section carries a short `Sources:` line naming what feeds it. If a section cannot cite a source, either the artifact stack has a gap (fix upstream) or the section is invention (cut it).

- **Personas are derived and counted, never invented color.** "Today's alternative is emailing the vendor and waiting" (observed) beats "allergic to contact-us forms" (quip). Per the 18F register: counted specifics, honest attribution, never overstate.
- **For agent-facing/API products, AI agents are first-class users** — a program that discovers/inspects/pays without seeing the UI, plus its human owner who audits the trail. One surface, two readers; every capability gets a human job name AND a machine path.
- **Every core surface gets proportionate, equal-depth direction** — the surface that took the longest to decide must not get the shortest paragraph.

## Prose Discipline (from published-brief canon: Shape Up, 18F, AI-design specs)

- Lead sections with observed evidence, not asserted desire; problems open with what was SEEN, with numbers and dates.
- State product LAWS as absolutes with a reason; never aspirations ("modern, clean, intuitive" are banned words).
- Organize each surface by user JOBS, not furniture (no "a header, a sidebar, a table").
- Per-surface cadence: one confident default sentence → the constraints that are truly law or map-contract → the TRAP (the rabbit hole a designer could sink a day into).
- Include Rabbit Holes and No-gos sections — real briefs say what NOT to build; AI-generated ones never volunteer subtraction.
- Peer register: senior colleague briefing a builder. No hedging adverbs, no throat-clearing.

## Relationship To Product Surface Map

When a product surface map exists, it is the source of truth for the screen inventory, per-screen states, and on-screen data shapes. The brief must consume it — embed or attach its content and add narrative direction on top — instead of re-deriving screens and states from spec/stories. Sample data from the map is used verbatim (it is audited canon); the designer may extend it in its spirit, never contradict it. The brief's own job is everything the surface map deliberately lacks: product story, users, domain teaching, journey narrative, inspiration, quality bar, mock boundaries, and creative freedom.

Only derive screens and states inline when no surface map exists, and say so — then recommend `product-surface-map` first for anything beyond a trivial surface.

## Interview The Designer First (when the designer is known)

When a specific designer/design agent will receive the brief, interview them BEFORE writing it — their answers shape the brief's structure. Ask, from their point of view:

1. What input package do they need, in what format, and what do builders always forget to include?
2. Wireframes vs direction vs straight-to-hi-fi — their sequence, and where they want sign-off checkpoints.
3. Mobile vs desktop priority for this product's real audience.
4. Do they create the brand identity or receive it (plus the user's veto constraints).
5. Their tools, and whether the toolchain changes what inputs they need.
6. The #1 thing builders do that ruins a handoff for them — then don't do it.

Give them just enough product context to answer meaningfully; the full brief comes after. Fold durable lessons from their answers back into this skill; fold project-specific terms into the brief only.

## Prototype Boundary

This brief is for high-fidelity design exploration and clickable/static prototype work. The prototype should feel production-quality in UX, information architecture, interaction detail, and visual polish, while using mocked data and mocked integrations by default.

Do not ask the designer to implement production database, auth, wallet, payment, API, or smart-contract integration unless the user explicitly says the design prototype should include real integration.

Mocked integrations in the design artifact are a design convenience only. They are not implementation decisions. As batches land (or when an external-mode prototype returns), `prototype-discovery` and `prototype-reintegration` must identify every mocked data source, auth state, wallet action, payment path, API call, MCP/tool call, storage path, and proof/audit surface, then decide whether each becomes real in MVP, visibly simulated for demo only, deferred, out of scope, or blocked.

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

Phrase this as a quality bar, not a visual recipe. Include at least one NAMED anti-reference (a real product/style the design must not resemble), labeled as qualities to avoid, not styles to copy in reverse.

## Inputs To Gather

Prefer these inputs:

- Reality research.
- Domain wiki pages.
- Spec.
- Stories and acceptance criteria.
- Product surface map when available (screen inventory, per-screen states, data shapes) — the backbone of the screen-by-screen direction.
- Product/user flow notes.
- Raw user notes and inspiration links.
- GitHub links, README files, screenshots, demos, or docs the designer should inspect.
- Known constraints and non-goals.
- Prototype target: landing page, dashboard, app flow, mobile, desktop, or responsive prototype.
- The designer's own stated working preferences when they have been interviewed.

## Process

1. Read ALL available artifacts — research, spec, stories, wiki, surface map, requirements — and build the section→source weave before writing anything.
2. Identify what the designer needs to understand before choosing screens or layout.
3. Write in the three registers, with per-section Sources lines and the discovery protocol stated.
4. Give per-surface direction at equal depth — default sentence, laws/contract constraints, the trap.
5. State high-fidelity mocked prototype assumptions clearly.
6. Call out which mocked surfaces must be revisited during prototype discovery and reintegration.
7. Add anti-slop constraints based on the product, not generic style bans.
8. Preserve full creative freedom for visual treatment — no taste dictation.
9. List source links/files the designer should inspect.

## Output

Use this structure by default. When the designer has been interviewed and asked for a different structure, their requested structure wins — the headings below then become a coverage checklist (every element must still be present or consciously dropped with a stated reason), not mandatory sections.

```markdown
# Designer Brief: <project or feature>

## Commission (one-liner: product + hi-fi mocked prototype; appetite/time-box if real; sequencing: direction lock first, coverage build in audited batches after acceptance)

## How To Read This Brief (LAWS / CONTEXT / DIRECTION + the discovery protocol: "the floor, not a cage"; mark additions DISCOVERED)

## The Problem (observed evidence with numbers and attribution — never a wished solution)

## The Product (what it is, in its own vocabulary — every core surface named and explained)

## Objectives & Success Criteria (goals = purpose; objectives = measurable)

## Target Users (derived + counted from artifacts; agents as first-class users where the product serves them)

## Domain Knowledge The Designer Needs (only what design decisions depend on)

## The Jobs / Core User Journeys (per user, traceable to stories)

## Surface Direction (one block PER core surface, equal depth: default sentence → law/contract constraints → the trap)

## Scope & Deliverables (in-scope floor + explicit out-of-scope; discovery protocol restated)

## Rabbit Holes (where a designer could sink a day and shouldn't)

## No-gos (what must never appear)

## Data, States, And Mocking Rules (surface-map canon verbatim; extend in spirit)

## Prototype Quality Bar (include accessibility as part of premium)

## Anti-slop Risks To Avoid (with named anti-references)

## Interaction Opportunities (optional palette, none mandatory)

## Inspiration And Source Material (qualities, not looks)

## Creative Freedom (full visual freedom stated outright)

## Open Questions
```

Every section carries a `Sources:` line citing the artifacts that feed it.

When creating a file, default to:

```text
<project-root>/.thoughts/design/YYYY-MM-DD-designer-brief.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

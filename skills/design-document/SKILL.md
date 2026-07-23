---
name: design-document
description: Use after the product surface map whenever UI work is in scope — when Abu wants a design document, design system, design doc, visual direction, tokens, or (legacy vocabulary) a designer brief or prototype commission. Produces .thoughts/design/YYYY-MM-DD-design-doc.md — the design contract for the build: product LAWS, visual-language TOKENS (palette per theme, type roles, spacing, motion, signature elements), per-surface direction, accessibility bar, and named anti-references — written in-repo by the context-holding agent from the whole corpus. When the visual language is genuinely undecided, this skill runs the taste protocol: ONE living sample screen on the demo-critical spine, iterated with Abu in fast rounds, tokens then extracted into the doc. Replaces the retired designer-brief + prototype pipeline stages; there is no prototype phase — coverage happens on production screens under screen-batch-audit.
---

# Design Document

The design contract for the build. Written after the product surface map is accepted, before planning. Design is aesthetics and aesthetics keep changing — so this document freezes only what the build needs frozen (laws, tokens, per-surface constraints) and explicitly expects visual evolution during implementation.

## Core Rule

Written in-repo, by the agent holding the full corpus (context-custody rule, locked 2026-07-23). Never delegate the design contract to a context-poor environment by default. The surface map is the source of truth for screens, states, and data shapes; this document adds the layer the map deliberately lacks — identity, language, and taste — and never contradicts it.

The document is a contract, not a freeze: tokens and laws bind every screen; layout and micro-aesthetics iterate freely during the build, and the user re-opens taste whenever they want.

## The Taste Protocol (when the visual language is undecided)

Text cannot settle taste — the user has to SEE it (x402arc evidence: five text-adjacent direction attempts rejected; the first in-repo living screen accepted). When the language is genuinely open:

1. Build at most **one living sample screen** — HTML or a real component, fully alive (real motion, real canonical data, both themes when the product needs both) — on the product's **demo-critical spine**, not a random screen.
2. Iterate it with the user in **fast rounds on the same artifact** — adjust the feeling they name; do not spawn menus of alternatives unless they ask for options.
3. On acceptance, **extract the tokens into this document** and archive the sample under `design/` as direction evidence.

The sample is a taste instrument, never a coverage artifact. Do not build screen sets before planning — coverage happens on production screens in the implementation loop, audited by `screen-batch-audit`.

## What The Document Contains

1. **LAWS** — the product's identity, verbatim from the corpus: fixed vocabulary, honesty/trust rules, jargon bans, data-formatting rules (units, truncation, linking). Non-negotiable; every screen inherits them.
2. **TOKENS** — the accepted visual language, concrete enough to build from: palette per theme (named hex, semantic bindings — what each accent MAY mean and may never mean), type roles (display/body/data faces, scale, weights), spacing/density/radius, motion rules (what animates, when, `prefers-reduced-motion` behavior), and the **signature elements** — the product-mechanic-derived moves that make it unmistakable — with their semantics.
3. **PER-SURFACE DIRECTION** — one block per core surface, equal depth: confident default sentence → the constraints that are law or map-contract → the trap (where a builder could sink a day).
4. **QUALITY BAR** — accessibility as part of premium (contrast, focus visibility, touch targets, reduced motion), density/calm expectations, and the copy register.
5. **ANTI-SLOP** — named anti-references (real products/styles this must not resemble, as qualities not reverse-recipes) and the generic-AI-look bans that apply to this product.

Every section carries a `Sources:` line citing the artifacts that feed it. If a section cannot cite a source, the stack has a gap (fix upstream) or the section is invention (cut it).

## Prose Discipline

Laws as absolutes with a reason; banned adjectives ("modern, clean, intuitive"); surfaces organized by user jobs, not furniture; peer register. Personas and evidence stay in the spec/stories/map — this document teaches the *language*, not the product over again.

## External Mode (optional — commissioning a human designer or design tool)

Only when deliberately chosen. This document then serves as the brief; attach the surface map as the coverage checklist; require work back in **audited batches of 3-4 screens, never one full-surface drop**; audit each batch with `screen-batch-audit`'s checklist. Zero taste dictation applies in this mode — the external designer owns the language, and their accepted work feeds the TOKENS section.

## Output

```markdown
# Design Document: <project>

## How To Read This (laws bind · tokens bind · direction guides · aesthetics iterate)

## LAWS

## TOKENS (palette per theme · type · spacing · motion · signature elements)

## Per-Surface Direction (default → constraints → trap, one block per surface)

## Quality Bar

## Anti-Slop (named anti-references)

## Direction Evidence (accepted sample + rejected alternates, linked)

## Open Questions
```

Default path:

```text
<project-root>/.thoughts/design/YYYY-MM-DD-design-doc.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

---
name: handoff-compaction
description: Use when Abu wants to preserve project or session state before context gets long, before ending a work session, before switching agents, after verification, or before resuming later. Produces concise handoffs that capture objective, decisions, artifacts, current state, commands, risks, and next steps without copying full research/specs/plans into the handoff.
---

# Handoff Compaction

Use this skill when work needs to continue later without rereading the whole conversation.

## Core Rule

A handoff is a resume artifact, not a transcript. Keep it compact, factual, and linked to source artifacts. Do not copy full specs, plans, research, or logs unless a short excerpt is necessary.

## Inputs To Gather

Prefer these inputs:

- Current objective.
- Relevant research, spec, stories, designer brief, plan, and verification files.
- Files changed or created.
- Commands run and their results.
- Decisions made.
- Open questions.
- Risks, blockers, and next actions.

## Process

1. Identify what a future agent must know to resume safely.
2. Link to artifacts instead of duplicating them.
3. Preserve decisions and rationale.
4. Record current implementation state and verification state.
5. Record exact next steps in order.
6. Separate completed work from pending work.
7. Keep the handoff short enough to load quickly in a new session.

## Output

Use this structure:

```markdown
# Handoff: <project or feature>

## Objective

## Current State

## Key Decisions

## Artifacts

## Files Changed

## Commands And Results

## Open Questions

## Risks Or Blockers

## Next Steps

## Resume Prompt
```

The resume prompt should be one short paragraph the user can paste into a new Codex session.

When creating a file, default to:

```text
<project-root>/.thoughts/handoffs/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

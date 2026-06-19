---
name: agents-md-author
description: Use when Abu wants Codex to create, audit, or update user-level ~/.codex/AGENTS.md, repo AGENTS.md, or nested AGENTS.override.md files. Keeps instructions small, practical, and sourced from the project quality profile, routes detailed workflows to skills, and avoids stuffing research, specs, plans, or full process manuals into AGENTS.md.
---

# AGENTS.md Author

Use this skill to create or maintain Codex instruction files.

## Core Rule

`AGENTS.md` is a thin always-on router, not the whole operating system. Put stable behavior, project commands, project conventions, and verification expectations there. Put detailed workflows in skills, deterministic enforcement in hooks/CI, and project artifacts in `<repo>/.thoughts/`.

## Instruction Layers

- User-level defaults: `~/.codex/AGENTS.md`.
- Temporary user-level override: `~/.codex/AGENTS.override.md`.
- Repository rules: `<repo>/AGENTS.md`.
- Local directory overrides: nested `AGENTS.override.md` files close to specialized work.

Codex loads instructions when a session starts. If files change, start a fresh session before assuming the new instructions are active.

## What Belongs Where

User-level `~/.codex/AGENTS.md`:

- Abu's durable personal defaults.
- Preferred collaboration style.
- Broad safety and quality expectations.
- Reusable skill-routing reminders.
- Things that should apply across most projects.

Repo `AGENTS.md`:

- Project purpose and layout.
- Build, test, lint, typecheck, and verification commands.
- Stack-specific conventions from `project-quality-profile`.
- CI and PR expectations.
- Project-specific constraints and do-not rules.
- Pointers to specs, plans, docs, or `<repo>/.thoughts/` locations.

Nested `AGENTS.override.md`:

- Directory-specific commands or constraints.
- Service/package-specific exceptions.
- Security-sensitive or domain-specific rules near the relevant code.

Do not put these in AGENTS.md:

- Long research notes.
- Full specs, stories, plans, or handoffs.
- Large style guides.
- Entire CI config.
- Long lists of generic best practices.
- Rules that should be enforced by tooling instead of prose.

## Process

1. Identify the target file: global, repo, or nested override.
2. Read any existing instruction file before editing.
3. Gather source material:
   - `project-quality-profile` output for commands and gates.
   - Repo manifests, CI files, docs, and scripts for verified commands.
   - Existing specs/plans only for short pointers, not full content.
4. Decide what belongs in AGENTS.md versus skills, hooks, CI, or `.thoughts`.
5. Write concise sections with concrete commands and expectations.
6. Preserve existing useful rules and remove duplicate/noisy process dumps only when explicitly asked.
7. If commands are uncertain, mark them as unknown instead of inventing them.

## Recommended Repo Template

```markdown
# AGENTS.md

## Project Snapshot

## Working Rules

## Commands

## Quality Gates

## Context Workflow

## PR And Review Expectations

## Do Not
```

## Recommended User-level Template

```markdown
# ~/.codex/AGENTS.md

## Working Agreements

## Context Engineering Defaults

## Quality Defaults

## Communication
```

When creating a reusable draft instead of writing the real file, default to:

```text
<repo>/.thoughts/patterns/agents-md-draft.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

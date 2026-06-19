---
name: claude-md-author
description: Use when Abu wants Claude Code to create, audit, or update user-level ~/.claude/CLAUDE.md, repo CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md, or .claude/rules/*.md files. Keeps instructions small, practical, and sourced from project evidence, while routing detailed workflows to skills instead of stuffing long process manuals into always-on memory.
---

# CLAUDE.md Author

Use this skill to create or maintain Claude Code instruction files.

## Core Rule

`CLAUDE.md` is always-on project memory, not the whole operating system. Put durable facts, commands, conventions, and short behavior rules there. Put multi-step procedures in skills, deterministic enforcement in hooks or CI, and project artifacts in `<repo>/.thoughts/`.

## Instruction Layers

- User defaults: `~/.claude/CLAUDE.md`.
- User rules: `~/.claude/rules/*.md`.
- Project instructions: `<repo>/CLAUDE.md` or `<repo>/.claude/CLAUDE.md`.
- Project rules: `<repo>/.claude/rules/*.md`.
- Local-only notes: `<repo>/CLAUDE.local.md`.

Claude Code reads these files as context, not as hard enforcement. Use hooks or CI for rules that must always run.

## What Belongs Where

User-level `~/.claude/CLAUDE.md`:

- Abu's durable personal defaults.
- Broad collaboration preferences.
- General safety and quality expectations.
- Pointers to reusable skills.

Repo `CLAUDE.md` or `.claude/CLAUDE.md`:

- Project purpose and layout.
- Build, test, lint, typecheck, and verification commands.
- Stack-specific conventions from the project quality profile.
- CI and PR expectations.
- Project-specific constraints and do-not rules.
- Pointers to `.thoughts/` artifacts instead of copying them.

`.claude/rules/*.md`:

- Focused rules that apply to a file type, package, service, or workflow.
- Short path-scoped guidance that would make the main `CLAUDE.md` noisy.

Do not put these in Claude instruction files:

- Long research notes.
- Full specs, stories, plans, or handoffs.
- Large style guides.
- Entire CI configs.
- Detailed process manuals that should be skills.
- Rules that should be enforced by tooling instead of prose.

## Process

1. Identify the target file and scope: user, project, rules, or local-only.
2. Read any existing instruction file before editing.
3. Gather source material:
   - Project quality profile for commands and gates.
   - Repo manifests, CI files, docs, and scripts for verified commands.
   - Existing specs, plans, and wiki pages only for short pointers.
4. Decide what belongs in `CLAUDE.md` versus skills, hooks, CI, rules, or `.thoughts`.
5. Write concise sections with concrete commands and expectations.
6. Preserve useful existing rules and remove duplicate/noisy process dumps only when explicitly asked.
7. If commands are uncertain, mark them as unknown instead of inventing them.

## Recommended Repo Template

```markdown
# CLAUDE.md

## Project Snapshot

## Working Rules

## Commands

## Quality Gates

## Project Context

## Skill Routing
```

Keep the file short enough to stay useful in every session. If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

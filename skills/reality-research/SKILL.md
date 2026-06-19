---
name: reality-research
description: Use when Abu asks Codex to research a codebase, repo, library, domain, product idea, bug area, hackathon project, or external source before specs, planning, or implementation. Produces a facts-only current-reality brief and explicitly avoids proposing fixes, architecture, or implementation unless the user asks for a solution pass.
---

# Reality Research

Use this skill before writing specs, plans, or code when the user needs facts.

## Core Rule

Document current reality only. Do not propose improvements, root causes, architecture, implementation plans, or fixes unless the user explicitly asks for a solution pass.

## Process

1. State the research question and scope in one or two sentences.
2. Gather primary evidence:
   - For repos: inspect actual files and commands.
   - For docs, SDKs, libraries, CLIs, or cloud services: follow the active project instructions for current documentation lookup.
   - For GitHub repos: use `gh` or raw URLs correctly; treat gists as gists, not repos.
3. Separate verified facts from inferences and open questions.
4. Cite every important claim with file paths, command output, URLs, or source notes.
5. Stop at the reality brief unless the user asks for the next artifact.

## Output

Use this structure:

```markdown
# Reality Research: <topic>

## Scope

## Sources Checked

## Verified Facts

## Inferences

## Unknowns And Questions

## Not Included
```

When creating a file, default to:

```text
<project-root>/.thoughts/research/YYYY-MM-DD-<topic>.md
```

If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

---
name: domain-wiki
description: Use when Abu wants a persistent Karpathy-style LLM wiki for a project or domain, including ingesting raw sources, summarizing and cross-linking concepts, updating index.md and log.md, querying accumulated knowledge, or linting stale and contradictory wiki pages.
---

# Domain Wiki

Use this skill to maintain compounding knowledge across sessions.

## Core Rule

Research documents are temporary artifacts. The domain wiki is persistent knowledge. Do not overwrite raw sources, and do not let wiki claims drift away from cited evidence.

## Layout

Default project wiki:

```text
<project-root>/.thoughts/
  raw/
  wiki/
    index.md
    log.md
```

## Operations

### Ingest

1. Add or reference immutable raw sources under `raw/`.
2. Summarize the source into the relevant wiki page.
3. Update related concept pages and cross-links.
4. Update `wiki/index.md`.
5. Append the action to `wiki/log.md`.

### Query

1. Answer from the wiki first.
2. Cite wiki pages and their source references.
3. If the answer exposes a useful synthesis, ask whether to file it back into the wiki.

### Lint

Check for:

- Contradictions.
- Stale claims.
- Missing source citations.
- Orphan pages.
- Missing backlinks.
- Concepts that deserve their own page.

## Output

When creating or updating wiki files, keep pages concise, linked, and source-backed. If artifact boundaries are unclear, read `../../references/operating-model.md` from the plugin root.

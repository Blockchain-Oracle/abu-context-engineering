# Abu Context Engineering

Research-first context engineering workflows for Codex and Claude Code.

This plugin packages reusable skills for repo-local `.thoughts` context, reality research, project quality profiling, source-backed domain wiki maintenance, specs, stories, product surface maps, design documents, screen batch audits, goal prompts, research-backed plans with integration-reality matrices, verification audits, handoff compaction, and instruction-file authoring.

## Claude Code

Test directly from the local checkout:

```bash
claude --plugin-dir /Users/abu/plugins/abu-context-engineering
```

Install from the local marketplace:

```bash
claude plugin marketplace add /Users/abu/plugins/abu-context-engineering
claude plugin install abu-context-engineering@abu-context-engineering --scope user
/reload-plugins
```

Use skills with the plugin namespace:

```text
/abu-context-engineering:reality-research
/abu-context-engineering:project-quality-profile
/abu-context-engineering:spec-writer
/abu-context-engineering:story-writer
/abu-context-engineering:product-surface-map
/abu-context-engineering:design-document
/abu-context-engineering:screen-batch-audit
/abu-context-engineering:goal-writer
/abu-context-engineering:research-backed-plan
/abu-context-engineering:verification-audit
/abu-context-engineering:handoff-compaction
/abu-context-engineering:claude-md-author
```

If installed from GitHub:

```bash
claude plugin marketplace add Blockchain-Oracle/abu-context-engineering
claude plugin install abu-context-engineering@abu-context-engineering --scope user
```

## Codex

The Codex manifest remains at `.codex-plugin/plugin.json`. The personal Codex marketplace can point at this local directory as `./plugins/abu-context-engineering`.

## Skills

- `reality-research`
- `project-quality-profile`
- `domain-wiki`
- `spec-writer`
- `story-writer`
- `product-surface-map`
- `design-document`
- `screen-batch-audit`
- `goal-writer`
- `research-backed-plan`
- `verification-audit`
- `handoff-compaction`
- `agents-md-author`
- `claude-md-author`

## Validation

```bash
claude plugin validate /Users/abu/plugins/abu-context-engineering
python3 /Users/abu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/abu/plugins/abu-context-engineering
```

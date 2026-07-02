# Goal Prompt: <project or feature>

Set a goal to <objective>.

## Objective

<One clear outcome.>

## Current Context To Inspect

- <Project instruction files>
- <.thoughts artifacts>
- <Prototype artifacts>
- <Repo state>

## Required Workflow

1. <Next Context Engineering gate>
2. <Following gate>
3. <Continue only when prior gates pass>

## Autonomy Rules

- Keep working through the accepted gates without asking Abu to restate the process.
- Inspect actual files before deciding what exists.
- Preserve frontend/prototype fidelity.
- Do not silently ship prototype mocks as real product behavior.
- Do not skip required Context Engineering stages.

## Pause And Ask Abu Only For

- Missing API keys, OAuth apps, wallet keys, testnet funding, NPM tokens, deployment tokens, external accounts, paid services, or irreversible publishing/deployment approval.
- Unresolved product decisions that cannot be answered from accepted artifacts.
- Live settlement, payment, or production credentials that cannot be safely simulated or deferred.

## Constraints

- <Project-specific constraints>

## Definition Of Done

- <Traceable proof that the goal is actually achieved>

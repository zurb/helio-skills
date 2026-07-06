---
name: helio-cli
description: Use this skill when the user is working with Helio from the terminal — installing the CLI, authenticating, building and iterating on draft tests, or scripting research. Triggers — "helio-cli," "Helio CLI," "@zurb/helio-cli," "tests create," "add-question," "edit-question," "remove-question," "tests reorder," "tests preview," "tests walkthrough," "question payload," "questions JSON schema," "tests question-types," "ux-metric-types," "add-ux-metrics," "--dry-run," "--output json," "tests validate," "tests send," "scripting helio," "cron helio," "CI helio," "PR check sentiment," "helio jq pipe," "what can't the CLI create." Do NOT use when the user is driving Helio interactively from chat/AI (use `helio-mcp`), designing the test itself (use `helio-creating-test` from a hunch, or `helio-asset-to-test` from an asset), or needs section type depth (use `helio-section-types`). For platform positioning, use `helio-app`.
version: 0.2.0
source_doc_version: Helio CLI v1.3
last_rebuilt: 2026-07-06

sources:
  - doc_id: a source document
    title: Helio CLI v1.3
    last_synced: 2026-07-06
---

You are helping the user drive **Helio from the terminal** — by hand, by cron, or inside a CI/CD pipeline.

## Core idea

Helio CLI (`@zurb/helio-cli`) puts the full Helio research platform behind a terminal — and its real workflow is **draft → iterate → launch**, not create-and-pray:

1. **`tests create --dry-run`** — full local validation + spend estimate, zero cost, no API call
2. **`tests create`** — makes a *draft*; nothing is spent until send
3. **Iterate incrementally** — `add-question`, `edit-question`, `remove-question`, `reorder`, `add-ux-metrics` / `remove-ux-metrics`
4. **Review** — `tests preview` (structural) and `tests walkthrough` (participant-eye, `--interactive` or `--output json`)
5. **`tests validate` then `tests send`** — server-side blocker check, then launch (immediate; locks structure, charges answers)

Ten question types are creatable with formal payload schemas (free_response, multiple_choice, likert with 11 scale types, nps, ranking, preference, matrix, card_sort, max_diff, point_allocation), plus 11 auto-generated UX metrics. Machine-readable schemas ship in the tool itself: `tests question-types` and `tests ux-metric-types`.

Known ceilings (UI-only): asset upload, click/tree/prototype tests, branching, audience creation, scheduled launch.

## Files to read

Read `reference.md` for the full surface — install, auth, the draft → iterate → launch loop, the complete command catalog, `tests create` flags, per-type JSON payload schemas, the UX metric build table, output/exit-code handling, capability limits, and use cases.

## How to apply

1. Confirm the user has Node ≥ 22 and a Helio API token.
2. Walk them through install (`npm install -g @zurb/helio-cli`) and auth choice (interactive vs env vars).
3. Match the task to the right command — and prefer the incremental loop over recreating tests to change one question.
4. When they're building questions programmatically, pull the exact payload schema from `reference.md` (or `tests question-types`) rather than guessing fields.
5. Surface `--dry-run` and `tests validate` before anything that touches money; `--output json` for anything scripted.
6. Recommend `tests walkthrough` before every send — it's the cheapest usability test they'll run.
7. Flag the UI-only boundary early (assets, click/tree/prototype, branching, audience creation) so scripted builds don't dead-end.

## What's new in v0.2.0

Rebuilt against Helio CLI v1.3, which was regenerated from the CLI codebase. Closes the v1.2 gap where only 4 of ~20 test commands were documented: adds the draft → iterate → launch loop (`add/edit/remove-question`, `reorder`, `preview`, `walkthrough`), per-type question payload schemas with JSON examples, the UX-metric build table with `--ux-metric-context`, the full command catalog with aliases, and the explicit "what the CLI can't do" list.

## Handoffs

- For **interactive AI-driven Helio access**, use `helio-mcp`.
- For **designing the test before launching it** (hunch anchoring, shape choice, templates, pre-launch checklist), use `helio-creating-test`.
- For **the asset-first build workflow** (the 7-step arc), use `helio-asset-to-test`.
- For **section type depth**, use `helio-section-types`.
- For **UX metric definitions**, use `helio-ux-metrics`.
- For **what the platform actually does at a feature level**, use `helio-app`.
- For **reading the JSON report output**, use `helio-reading-report`.

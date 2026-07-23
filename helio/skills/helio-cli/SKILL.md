---
name: helio-cli
description: Use this skill when the user is working with Helio from the terminal — installing the CLI, authenticating, building and iterating on draft tests, or scripting research. Triggers — "helio-cli," "Helio CLI," "@zurb/helio-cli," "tests create," "add-question," "edit-question," "remove-question," "tests reorder," "tests preview," "tests walkthrough," "tests participants," "question payload," "questions JSON schema," "tests question-types," "ux-metric-types," "add-ux-metrics," "--metrics-json," "--dry-run," "--output json," "tests validate," "tests send," "assets upload," "assets list," "--asset-id," "asset not found," "account name," "scripting helio," "cron helio," "CI helio," "what can't the CLI create." Do NOT use when the user is driving Helio interactively from chat/AI (use `helio-mcp`), designing the test itself (use `helio-creating-test` from a hunch, or `helio-asset-to-test` from an asset), or needs section type depth (use `helio-section-types`). For platform positioning, use `helio-app`.
version: 0.4.1
source_doc_version: Helio CLI v1.4 (+ live sync vs CLI v0.3.2)
last_rebuilt: 2026-07-23

sources:
  - doc_id: src-helio-cli-v1.4
    title: Helio CLI v1.4
    last_synced: 2026-07-21
  - title: Live verification against installed helio-cli v0.3.0 (--help output + real commands)
    last_synced: 2026-07-23
---

You are helping the user drive **Helio from the terminal** — by hand, by cron, or inside a CI/CD pipeline.

## Core idea

Helio CLI (`@zurb/helio-cli`) puts the full Helio research platform behind a terminal — and its real workflow is **draft → iterate → launch**, not create-and-pray:

1. **`tests create --dry-run`** — full local validation + spend estimate, zero cost, no API call
2. **`tests create`** — makes a *draft*; nothing is spent until send
3. **Iterate incrementally** — `add-question`, `edit-question`, `remove-question`, `reorder`, `add-ux-metrics` / `remove-ux-metrics` (canonical metric flags on those two are `--metrics` / `--metrics-json`; `--ux-metrics` aliases exist since v0.3.2)
4. **Review** — `tests preview` (structural) and `tests walkthrough` (participant-eye, `--interactive` or `--output json`)
5. **`tests validate` then `tests send`** — server-side blocker check, then launch (immediate; locks structure, charges answers)

Ten question types are creatable with formal payload schemas (free_response, multiple_choice, likert with 11 scale types, nps, ranking, preference, matrix, card_sort, max_diff, point_allocation), plus 11 auto-generated UX metrics. Machine-readable schemas ship in the tool itself: `tests question-types` and `tests ux-metric-types`.

Image assets are CLI-native too (v0.1.1): `assets upload <file>` (jpg/jpeg/png/gif, max 10MB), `assets list` to find IDs, `assets get <id>` for status and signed URLs — then attach with `tests add-question --asset-id` / `tests edit-question --asset-id` or `asset_id` in a question payload. Assets are **account-scoped** to the token's home account — cross-account attachment fails with `asset not found`.

Known ceilings (UI-only): video/audio upload, click/tree/prototype tests, branching, audience creation, scheduled launch.

## Files to read

Read `reference.md` for the full surface — install, auth, the draft → iterate → launch loop, the complete command catalog, `tests create` flags, per-type JSON payload schemas, the UX metric build table, output/exit-code handling, capability limits, and use cases.

## How to apply

1. Confirm the user has Node ≥ 22 and a Helio API token.
2. Walk them through install (`npm install -g @zurb/helio-cli`) and auth choice (interactive vs env vars).
3. Match the task to the right command — and prefer the incremental loop over recreating tests to change one question.
4. When they're building questions programmatically, pull the exact payload schema from `reference.md` (or `tests question-types`) rather than guessing fields.
5. Surface `--dry-run` and `tests validate` before anything that touches money; `--output json` for anything scripted.
6. Recommend `tests walkthrough` before every send — it's the cheapest usability test they'll run.
7. For image stimuli, use `assets upload` / `assets list` to get a numeric asset ID, then attach with `--asset-id` — no web-app detour needed.
8. Flag the UI-only boundary early (video/audio upload, click/tree/prototype, branching, audience creation) so scripted builds don't dead-end.

## What's new in v0.4.1

helio-cli v0.3.1/v0.3.2 (same day) smoothed the v0.3.0 rough edges: `--ux-metrics` / `--ux-metrics-json` now work as aliases on `add-ux-metrics` (and `--ux-metrics` on `remove-ux-metrics`), and `tests preview`/`walkthrough` headers show `Project: <name> · <account name>`. Canonical flags remain `--metrics` / `--metrics-json`; `--ux-metric-context` is still create-only; raw `tests get` JSON still lacks account fields until API an internal API issue deploys (the CLI already reads them when present).

## What's new in v0.4.0

Live-synced against installed helio-cli **v0.3.0** (2026-07-23), fixing doc drift caught in real use:

- `tests add-ux-metrics` / `remove-ux-metrics` flags corrected: `--metrics <types...>` and `--metrics-json` (object form keys on `"type"`, supports per-metric `"context"` and per-section overrides), plus `--position` on add. The old documented `--ux-metrics` flag errors on these commands.
- New commands: `tests participants <id>` (per-respondent journeys with demographic/segment filters), `helio-cli update [--check]` (self-update).
- New flags: `--ux-metrics-json` on `tests create`; follow-up questions on `add-question`/`edit-question` (`--followup`, `--followup-required`, `--followup-for-choices`, `--remove-followup`); `edit-question` with `--type` omitted edits UX-metric sections in place; `tests list` filters (`--status`, `--created-after/before`, `--tags`, response-count bounds).
- `projects list` now returns `account_id` + `account_name` per project (and takes `--name`).
- Documented the account-scoping rule for assets (cross-account attach → `HTTP 400 asset not found`) and the `npm i -g` EEXIST stale-binary trap.

## What's new in v0.3.1

Repointed to Drive doc Helio CLI v1.4, which now carries the assets command group — the skill is single-source again (the v0.3.0 codebase second source is folded into the doc).

## What's new in v0.3.0

helio-cli v0.1.1 (PR #6) added the `assets` command group — `list` (with `--type`, `--name`, `--limit`, `--offset`), `get <id>`, and `upload <file>` (images only: jpg/jpeg/png/gif, max 10MB, multipart). Asset upload is no longer a UI-only ceiling; uploaded asset IDs attach to questions via `--asset-id` or `asset_id` in payloads.

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

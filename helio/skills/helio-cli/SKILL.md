---
name: helio-cli
description: Use this skill when the user is working with Helio from the terminal — installing the CLI, authenticating, building and iterating on draft tests, or scripting research. Triggers — "helio-cli," "Helio CLI," "@zurb/helio-cli," "tests create," "add-question," "edit-question," "remove-question," "tests reorder," "tests preview," "tests walkthrough," "tests participants," "question payload," "questions JSON schema," "tests question-types," "ux-metric-types," "add-ux-metrics," "--metrics-json," "--dry-run," "--output json," "tests validate," "tests send," "assets upload," "assets list," "--asset-id," "asset not found," "account name," "scripting helio," "cron helio," "CI helio," "what can't the CLI create." Do NOT use when the user is driving Helio interactively from chat/AI (use `helio-mcp`), designing the test itself (use `helio-creating-test` from a hunch, or `helio-asset-to-test` from an asset), or needs section type depth (use `helio-section-types`). For platform positioning, use `helio-app`.
version: 0.5.0
source_doc_version: Helio CLI v1.4 (+ live sync vs CLI v0.3.2, + pending feat/helio-alias-clone-audiences)
last_rebuilt: 2026-07-23

sources:
  - doc_id: 1M2PXT5oASNk_CaITO4ekcVGWKYpTrzTkLOuqz2DrYLo
    title: Helio CLI v1.4
    drive_url: https://docs.google.com/document/d/1M2PXT5oASNk_CaITO4ekcVGWKYpTrzTkLOuqz2DrYLo/edit
    last_synced: 2026-07-21
  - title: Live verification against installed helio-cli v0.3.0 (--help output + real commands)
    last_synced: 2026-07-23
---

You are helping the user drive **Helio from the terminal** — by hand, by cron, or inside a CI/CD pipeline.

**The binary is `helio-cli`, not `helio`.** Agents reach for `helio` first and it fails on v≤0.3.2; a `helio` alias ships in the next release (branch feat/helio-alias-clone-audiences). Until the user confirms that version is installed, always invoke `helio-cli`.

## Core idea

Helio CLI (`@zurb/helio-cli`) puts the full Helio research platform behind a terminal — and its real workflow is **draft → iterate → launch**, not create-and-pray:

1. **`tests create --dry-run`** — full local validation + spend estimate, zero cost, no API call
2. **`tests create`** — makes a *draft*; nothing is spent until send
3. **Iterate incrementally** — `add-question`, `edit-question`, `remove-question`, `reorder`, `add-ux-metrics` / `remove-ux-metrics` (canonical metric flags on those two are `--metrics` / `--metrics-json`; `--ux-metrics` aliases exist since v0.3.2)
4. **Review** — `tests preview` (structural) and `tests walkthrough` (participant-eye, `--interactive` or `--output json`)
5. **`tests validate` then `tests send`** — server-side blocker check, then launch (immediate; locks structure, charges answers)

Ten question types are creatable with formal payload schemas (free_response, multiple_choice, likert with 11 scale types, nps, ranking, preference, matrix, card_sort, max_diff, point_allocation), plus 11 auto-generated UX metrics. Machine-readable schemas ship in the tool itself: `tests question-types` and `tests ux-metric-types`.

Image assets are CLI-native too (v0.1.1): `assets upload <file>` (jpg/jpeg/png/gif, max 10MB), `assets list` to find IDs, `assets get <id>` for status and signed URLs — then attach with `tests add-question --asset-id` / `tests edit-question --asset-id` or `asset_id` in a question payload. Assets are **account-scoped** to the token's home account — cross-account attachment fails with `asset not found`.

Known ceilings (UI-only): video/audio upload, tree/prototype tests, audience creation from scratch, scheduled launch, and branching on hotspots/variations/most-least labels. (Click tests AND multiple_choice branching became creatable in the pending release — see v0.5.0 below.) For the still-UI-only branching surfaces: `tests clone` an existing branched test and edit the copy — clone copies questions, UX metric groupings, branching, and the last audience/quota.

## Files to read

Read `reference.md` for the full surface — install, auth, the draft → iterate → launch loop, the complete command catalog, `tests create` flags, per-type JSON payload schemas, the UX metric build table, output/exit-code handling, capability limits, and use cases.

## How to apply

1. Confirm the user has Node ≥ 22 and a Helio API token.
2. Walk them through install (`npm install -g @zurb/helio-cli`) and auth choice (interactive vs env vars).
3. Match the task to the right command — and prefer the incremental loop over recreating tests to change one question.
4. When they're building questions programmatically, pull the exact payload schema from `reference.md` (or `tests question-types`) rather than guessing fields.
5. Surface `--dry-run` and `tests validate` before anything that touches money; `--output json` for anything scripted.
6. Recommend `tests walkthrough` before every send — it's the cheapest usability test they'll run. What to look for: duplicate questions from metric stacking (sentiment + desirability, appeal + reaction build identical sections), a context noun that breaks in some generated sentence, and evaluation questions landing before comprehension ones (`tests reorder` fixes sequence).
7. For image stimuli, use `assets upload` / `assets list` to get a numeric asset ID, then attach with `--asset-id` — no web-app detour needed.
8. Flag the UI-only boundary early (video/audio upload, click/tree/prototype, branching, audience creation) so scripted builds don't dead-end.

## What's new in v0.5.0 (pending CLI release)

Built 2026-07-23 from Benjamin's dogfooding feedback (helio-cli branch feat/helio-alias-clone-audiences + helio branch claude/helio-skills-feedback-2ea061; features work once both ship):

- **`helio` bin alias** alongside `helio-cli`.
- **`tests clone <id>`** — wraps `POST /tests/:id/clone` (API live since helio #4992). New draft in the same project; copies questions, UX metrics, branching, last audience. The scripted route to branched tests.
- **`audiences list`** grew `--name <partial>` (case-insensitive), `--recent` (most recently used in a test first), and richer columns: `participants_count`, `tests_count`, `last_used_at`. **`audiences clone <id>`** copies an audience within its customer list ("Copy of …" naming).
- **Branching is creatable on single-select multiple_choice** — `branching` in question payloads or `--branching <json|@file>` on `add-question`/`edit-question`: `[{choice: 0, action: "skip_to_question", question: 3}, {choice: 1, action: "end_test", message: "Not a fit", redirect_url: "..."}]`. choice = 0-based index; question = 1-based number (add/edit also take `section_id`). Mutually exclusive with followups. This is the scripted screener/disqualification pattern — see `helio-branching`.
- **`click_test` is creatable** (11th question type): requires `asset_id` (upload via `assets upload`), optional `hotspots` array `[{name?, x, y, width, height, priority?}]` with relative 0–1 coordinates — omit hotspots for an engagement heatmap, include them for a success click test. New `--hotspots <json|@file>` flag on `add-question`/`edit-question`. Priorities: Primary (default) | Secondary | Tertiary.
- Recommended pattern for "build it like our usual tests": `projects list` → project's tests → `tests preview` the recent ones (or just `tests clone` the closest match) before building fresh.

## What's new in v0.5.0

Journey-coherence guidance added to the walkthrough recommendation ("How to apply" step 6 and the failure-modes list in `reference.md`): what to actually look for on the participant-eye pass — duplicate questions from metric stacking (sentiment + desirability share the impressions MC; appeal + reaction build the identical Likert), a context noun that breaks in some generated sentence, and evaluation landing before comprehension (`tests reorder` fixes sequence). Full journey checks live in `helio-creating-test` v0.2.0.

## What's new in v0.4.1

helio-cli v0.3.1/v0.3.2 (same day) smoothed the v0.3.0 rough edges: `--ux-metrics` / `--ux-metrics-json` now work as aliases on `add-ux-metrics` (and `--ux-metrics` on `remove-ux-metrics`), and `tests preview`/`walkthrough` headers show `Project: <name> · <account name>`. Canonical flags remain `--metrics` / `--metrics-json`; `--ux-metric-context` is still create-only; raw `tests get` JSON still lacks account fields until API helio#4990 deploys (the CLI already reads them when present).

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

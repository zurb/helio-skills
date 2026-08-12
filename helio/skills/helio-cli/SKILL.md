---
name: helio-cli
description: Use this skill when the user is working with Helio from the terminal — installing the CLI, authenticating, building and iterating on draft tests, or scripting research. Triggers — "helio-cli," "Helio CLI," "@zurb/helio-cli," "tests create," "add-question," "edit-question," "remove-question," "tests reorder," "tests preview," "tests walkthrough," "tests participants," "question payload," "questions JSON schema," "tests question-types," "ux-metric-types," "add-ux-metrics," "--metrics-json," "--dry-run," "--output json," "tests validate," "tests send," "assets upload," "assets list," "--asset-id," "asset not found," "account name," "scripting helio," "cron helio," "CI helio," "what can't the CLI create." Do NOT use when the user is driving Helio interactively from chat/AI (use `helio-mcp`), designing the test itself (use `helio-creating-test` from a hunch, or `helio-asset-to-test` from an asset), or needs section type depth (use `helio-section-types`). For platform positioning, use `helio-app`.
version: 0.8.2
source_doc_version: Helio CLI v1.6 (rebuilt against CLI v0.8.0)
last_rebuilt: 2026-07-23

sources:
  - doc_id: src-helio-cli
    title: Helio CLI v1.6
    last_synced: 2026-08-01
  - title: Live verification against installed helio-cli v0.4.0–v0.8.1 (--help output + real commands)
    last_synced: 2026-08-12
---

You are helping the user drive **Helio from the terminal** — by hand, by cron, or inside a CI/CD pipeline.

**Check the version before stating any capability limit.** Run `helio-cli update --check` (or `--version`) first — capability boundaries move between releases, and a stale binary reports its own limits as the tool's. Since v0.6.0 the CLI prints an update notice to stderr even in `--output json` and non-TTY sessions — but that notice is refreshed by a **daily** background check, so a release published inside that window isn't announced yet. Two ways to get the truth now: `update --check` hits the registry live, and as of v0.8.1 `doctor` includes a `CLI version` check that does the same *and* refreshes the notice cache, so the passive notice agrees afterward. A stale CLI never fails doctor's exit code; with `HELIO_NO_UPDATE_CHECK` or `CI` set it skips the network and reports the check as disabled. Both `helio-cli` and the shorter `helio` work as of v0.4.0 (note a user's own shell alias can shadow `helio`).

## Core idea

Helio CLI (`@zurb/helio-cli`) puts the full Helio research platform behind a terminal — and its real workflow is **draft → iterate → launch**, not create-and-pray:

1. **`tests create --dry-run`** — full local validation + spend estimate, zero cost, no API call
2. **`tests create`** — makes a *draft*; nothing is spent until send
3. **Iterate incrementally** — `add-question`, `edit-question`, `remove-question`, `reorder`, `add-ux-metrics` / `remove-ux-metrics` (canonical metric flags on those two are `--metrics` / `--metrics-json`; `--ux-metrics` aliases exist since v0.3.2)
4. **Review** — `tests preview` (structural) and `tests walkthrough` (participant-eye, `--interactive` or `--output json`)
5. **`tests validate` then `tests send`** — server-side blocker check, then launch (immediate; locks structure, charges answers)

**Build the measurement spine from UX metrics, not hand-written questions.** `--ux-metrics <types...>` auto-generates each metric's sections with validated, non-leading wording and returns a 0–100 score with a threshold label, comparable across waves and rolled into the Overall Score; a hand-written look-alike returns only an answer distribution. Reach for `--questions` for what no metric covers. Sixteen metrics are creatable this way as of v0.7.0 (ask `tests ux-metric-types` for the current list); `helio-patterns` maps stage and asset to the right metric set.

Question types are creatable with formal payload schemas (free_response, multiple_choice, likert with 11 scale types, nps, ranking, preference, matrix, card_sort, max_diff, point_allocation, and click_test since v0.4.0). Machine-readable schemas ship in the tool itself: `tests question-types` and `tests ux-metric-types`.

Image assets are CLI-native too (v0.1.1): `assets upload <file>` (jpg/jpeg/png/gif, max 10MB), `assets list` to find IDs, `assets get <id>` for status and signed URLs — then attach with `tests add-question --asset-id` / `tests edit-question --asset-id` or `asset_id` in a question payload. Assets are **account-scoped** to the token's home account — cross-account attachment fails with `asset not found`.

Known ceilings as of **v0.8.0** (verify with `update --check` before repeating these): video/audio upload, tree/prototype tests, customer-list building and formal screener authoring, scheduled launch, branching on hotspots/variations/most-least labels, and the `completion` / `effort` metrics (each built from a Figma prototype section the API can't create). Everything else moved: click tests with hotspots and multiple_choice branching in v0.4.0; the click-backed metrics, `brand_score` and repeated metric types in v0.7.0; **audience recruiting** in v0.8.0. For the still-UI-only surfaces: `tests clone` an existing test and edit the copy.

**Read-back:** audience config, branching routes and hotspot geometry return from `tests preview --output json` (`.audience`, `.branching`, `.hotspots`) since v0.7.0; `walkthrough` screens carry branching and hotspots. v0.8.0 adds a top-level `ux_metrics` block and per-question `ux_metric` tags, which closes the last gap — **repeated metric instances are now reorderable from a fresh session** (`tests order` reports `reorderable: true` and emits paste-ready `metric:<uuid>` keys, so uuids no longer have to come from the original create response).

**Audience recruiting is scriptable as of v0.8.0.** `--audience-type` takes `open | basic | targeted | advanced | customer_list`, `--demographics` filters the panel, and `audiences list --source enroll` browses the panel catalog. `tests update --audience-type ...` retargets a draft, which makes clone-then-retarget a one-line flow. Note the API accepted only `open` audiences before v0.8.0, so `--audiences` was silently ignored on every test — pre-0.8.0 fanout scripts attached nothing. It's meaningful on `advanced`/`customer_list` now, and a loud error on `open`.

**Breaking in v0.8.0, deploy in lockstep with the API.** Metric-owned sections carry flat `metric_id` + `metric_type` stamps; the nested `ux_metric` object is gone from `tests get`. Scripts reading `.sections[].ux_metric` must move to the stamps or the new top-level summary. A v0.7.0 binary loses metric awareness against the new API, and v0.8.0's audience types 400 against the old one.

## Files to read

Read `reference.md` for the full surface — install, auth, the draft → iterate → launch loop, the complete command catalog, `tests create` flags, per-type JSON payload schemas, the UX metric build table, output/exit-code handling, capability limits, and use cases.

## How to apply

1. Confirm the user has Node ≥ 22, a Helio API token, and a current binary (`helio-cli update --check`) — never state a capability limit without knowing the version.
2. Walk them through install (`npm install -g @zurb/helio-cli`) and auth choice (interactive vs env vars).
3. Match the task to the right command — and prefer the incremental loop over recreating tests to change one question.
4. When they're building questions programmatically, pull the exact payload schema from `reference.md` (or `tests question-types`) rather than guessing fields.
5. Surface `--dry-run` and `tests validate` before anything that touches money; `--output json` for anything scripted.
6. Recommend `tests walkthrough` before every send — it's the cheapest usability test they'll run. What to look for: duplicate questions from metric stacking (sentiment + desirability, appeal + reaction build identical sections), a context noun that breaks in some generated sentence, and evaluation questions landing before comprehension ones (`tests reorder` fixes sequence).
7. For image stimuli, use `assets upload` / `assets list` to get a numeric asset ID, then attach with `--asset-id` — no web-app detour needed.
8. Flag the UI-only boundary early — as of v0.8.0: video/audio upload, tree/prototype tests, customer-list building, formal screeners, and the `completion` / `effort` metrics. Audience *recruiting* became scriptable in v0.8.0. Everything else has moved across the last four releases; don't repeat an older ceiling without running `update --check` — and note the passive update notice is cached for up to 24 hours, so the explicit check is the reliable one.

## What's new in v0.8.2

Disclosure scrub. Source documents are now referenced by opaque key (`src-*`) rather than by Drive id or link, with the real mapping held privately outside the repo. Named references were removed throughout: customer and engagement names, internal project and template codes, real test names, colleague names, and issue references into private repositories. No capability, workflow, or guidance content changed.

## What's new in v0.8.1

Two small CLI additions, both aimed at the discoverability problem this skill exists to work around.

- **`doctor` gained a `CLI version` check** — it compares against the registry, warns (never fails) when stale, and refreshes the update-notice cache so the passive stderr notice agrees afterward. That's the practical remedy for the daily-refresh lag: `doctor` is now a one-command "am I current and is my config sane".
- **`guide --output json` lists `doctor` and `update`.** Both top-level commands were previously missing from the JSON guide's `commands` object, so an agent reading the guide as onboarding could not discover the updater at all. The `update` entry now documents `--check` and the `HELIO_NO_UPDATE_CHECK=1` opt-out, and states the notice comes from a daily background check.

## What's new in v0.8.0

Synced to helio-cli **v0.8.0**, which is mostly about audiences and closes the last documented gap.

- **Audience recruiting is scriptable.** Five `--audience-type` values, `--demographics` panel filtering, `audiences list --source enroll` for the panel catalog, and `tests update` retargeting (the clone-then-retarget flow). "Audience creation is web-app work" was the biggest remaining ceiling in the family and it's now wrong — only customer-list building and formal screeners remain.
- **Repeated metric types are reorderable** — `tests order` returns `reorderable: true` with paste-ready `metric:<uuid>` keys. The v0.7.0 "capture uuids from the create response" workaround is retired.
- **Breaking:** metric-owned sections carry flat `metric_id` + `metric_type`; the nested `ux_metric` object is gone from `tests get`. `preview --output json` gains a top-level `ux_metrics` block and per-question tags. **Deploy in lockstep with the API** — a v0.7.0 binary loses metric awareness against the new API, and v0.8.0 audience types 400 against the old one.
- **`tests send` 502 semantics:** a panel rejection means nothing was charged and the test is still a draft, so widening a too-narrow audience and retrying is safe.
- Also documented: `--audiences` was silently ignored on non-`open` tests before v0.8.0, so pre-0.8.0 fanout scripts attached nothing; and the passive update notice is cached for up to 24 hours, so `update --check` is the reliable version check rather than waiting to be told.

## What's new in v0.7.0

Synced to helio-cli **v0.7.0** — the release that reversed most of v0.6.1's ceilings.

- **Sixteen metrics creatable** (was eleven): `engagement`, `success`, `usability`, `satisfaction`, `brand_score` joined once the API caught up with click-test creation. Only `completion` and `effort` remain, each excluded for a named reason rather than a blanket one.
- **A metric type may repeat on one test** — each instance owns its sections and score. `remove-ux-metrics` takes a type or a single metric id; `tests order` reports `reorderable: false` for repeated types because reorder needs uuids the read endpoint doesn't return.
- **Read-back of audience, branching, hotspots** via `preview --output json`, with branch targets resolved to CLI-listing question numbers.
- **Zero-score warnings** on create/add-ux-metrics for click-backed metrics without hotspots and `brand_score` without `brand_choice`; per-section `hotspots` / `choices` / `brand_choice` overrides on the metric object form.
- **Breaking:** `tests ux-metric-types --output json` moved the table under `.metrics` to make room for `.excluded`.

## What's new in v0.6.1

Non-creatable metric list now states *why* and names the split — click test sections became creatable in v0.4.0, their `engagement` / `success` metric tags did not. Verified against `create` and `add-ux-metrics`.

## What's new in v0.6.0

Metrics-first framing. Core idea now leads with building the measurement spine from `--ux-metrics` (scored, wave-comparable, Overall-Score-eligible) and reaching for `--questions` only for what no metric covers; the draft-loop create example leads with metrics plus `--ux-metric-context`. Question-type list adds `click_test` (creatable since CLI v0.4.0).

## What's new in v0.5.0

Built 2026-07-23 from hands-on dogfooding and **verified live against the shipped CLI v0.4.0–v0.6.0**:

- **`helio` bin alias** alongside `helio-cli`.
- **`tests clone <id>`** — wraps `POST /tests/:id/clone` (API support shipped server-side). New draft in the same project; copies questions, UX metrics, branching, last audience. The scripted route to branched tests.
- **`audiences list`** grew `--name <partial>` (case-insensitive), `--recent` (most recently used in a test first), and richer columns: `participants_count`, `tests_count`, `last_used_at`. **`audiences clone <id>`** copies an audience within its customer list ("Copy of …" naming).
- **Branching is creatable on single-select multiple_choice** — `branching` in question payloads or `--branching <json|@file>` on `add-question`/`edit-question`: `[{choice: 0, action: "skip_to_question", question: 3}, {choice: 1, action: "end_test", message: "Not a fit", redirect_url: "..."}]`. choice = 0-based index; question = 1-based number counting researcher questions only (add/edit also take `section_id`, uuid or numeric). **Requires a Helio Enterprise account** (same gate as the editor); skips are **forward-only** (later questions); mutually exclusive with followups. This is the scripted screener/disqualification pattern — see `helio-branching`.
- **Position round-trip rule**: mutation responses echo `position` as the 1-based question number matching the `position`/`add_ux_metrics_position` params — safe to feed back. Raw `tests get` section positions remain 0-based platform storage.
- **`click_test` is creatable** (11th question type): requires `asset_id` (upload via `assets upload`), optional `hotspots` array `[{name?, x, y, width, height, priority?}]` with relative 0–1 coordinates — omit hotspots for an engagement heatmap, include them for a success click test. New `--hotspots <json|@file>` flag on `add-question`/`edit-question`. Priorities: Primary (default) | Secondary | Tertiary.
- Recommended pattern for "build it like our usual tests": `projects list` → project's tests → `tests preview` the recent ones (or just `tests clone` the closest match) before building fresh.

## What's new in v0.5.0

Journey-coherence guidance added to the walkthrough recommendation ("How to apply" step 6 and the failure-modes list in `reference.md`): what to actually look for on the participant-eye pass — duplicate questions from metric stacking (sentiment + desirability share the impressions MC; appeal + reaction build the identical Likert), a context noun that breaks in some generated sentence, and evaluation landing before comprehension (`tests reorder` fixes sequence). Full journey checks live in `helio-creating-test` v0.2.0.

## What's new in v0.4.1

helio-cli v0.3.1/v0.3.2 (same day) smoothed the v0.3.0 rough edges: `--ux-metrics` / `--ux-metrics-json` now work as aliases on `add-ux-metrics` (and `--ux-metrics` on `remove-ux-metrics`), and `tests preview`/`walkthrough` headers show `Project: <name> · <account name>`. Canonical flags remain `--metrics` / `--metrics-json`; `--ux-metric-context` is still create-only; raw `tests get` JSON still lacks account fields until the corresponding API change deploys (the CLI already reads them when present).

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

helio-cli v0.1.1 added the `assets` command group — `list` (with `--type`, `--name`, `--limit`, `--offset`), `get <id>`, and `upload <file>` (images only: jpg/jpeg/png/gif, max 10MB, multipart). Asset upload is no longer a UI-only ceiling; uploaded asset IDs attach to questions via `--asset-id` or `asset_id` in payloads.

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

# Helio CLI — Reference

**Skill:** `helio-cli`
**Source:** Helio CLI v1.4
**Source last synced:** 2026-07-21
**Notes:** v1.3 was regenerated from the CLI codebase (README, built-in guide, validation schemas) so the doc matches what the tool ships. This rebuild closes the v1.2 gap where only 4 of ~20 test commands were documented. Amended 2026-07-20 for helio-cli v0.1.1 (PR #6), which added the `assets` command group — asset upload/listing is no longer UI-only.

---

<!-- DERIVED FROM: 1M2PXT5oASNk_CaITO4ekcVGWKYpTrzTkLOuqz2DrYLo — Helio CLI v1.4 -->

Helio CLI is the most robust way to script Glare data collection — by hand, by cron, or by AI agent. It puts the full Helio research platform behind a terminal, with structured JSON output, dry-run validation, predictable exit codes, and test definitions you can version-control alongside the code they evaluate. Anywhere automation or an AI agent needs to call into Glare, the CLI is the contract.

The web app is still there when you want it. The CLI is there when you need to move.

## What this solves

Most teams that script Helio know four commands: create, report, validate, send. That's enough to launch a test once — and not enough to work on one. The CLI's actual surface is around twenty test commands, including an incremental editing loop (add, edit, remove, reorder questions on a draft), two ways to review a draft before spending (a structural preview and a participant-eye walkthrough), and a formal payload schema for every creatable question type. The create-and-pray workflow should be a draft → iterate → launch workflow.

## When to use CLI (vs MCP vs web)

Three ways to reach Helio. Pick the one that fits the work.

- **CLI** — when a script, cron job, or pipeline should drive the work. Nightly pulls, CI checks that gate releases on sentiment, version-controlled test definitions next to the code they evaluate. Best for deterministic, repeatable, auditable runs.
- **MCP** — when an AI assistant should drive the work interactively. Cohort comparisons in chat, concept assessments from a prompt, end-to-end test launches a model can run by itself. Best for exploratory research and ad-hoc analysis where the question evolves.
- **Web app** — when a person should drive the work. Initial project setup, careful review of responses, designing tests with a teammate at a screen.

The same Helio API is underneath all three. The choice is about who's driving, not what's available.

## Requirements

- Node.js ≥ 22. The shebang resolves to whatever `node` is first in PATH; if your default is older, run `nvm use 22` first.
- A Helio API token — generate one at [my.helio.app/account/organization](https://my.helio.app/account/organization)

## Install

```shell
npm install -g @zurb/helio-cli
```

## Authenticate

The CLI accepts credentials two ways. Pick whichever fits the environment.

**Interactive login** — for local development:

```shell
helio-cli auth login
```

Credentials are stored in your local config file and reused on every subsequent command.

**Environment variables** — for CI, sandboxes, containers, or anywhere a config file would be awkward:

```shell
export HELIO_API_ID=...
export HELIO_API_TOKEN=...
```

Once these are set, every command authenticates without touching disk. This is the recommended path for GitHub Actions, nightly crons, and any internal tool that runs on someone else's machine.

Sanity checks: `helio-cli auth status` confirms who you are; `helio-cli doctor` diagnoses connectivity; `helio-cli status` pings the API.

## The draft → iterate → launch loop

This is the workflow the CLI is actually built for. A test created via the CLI is a **draft** — nothing is spent until you send it — and every part of a draft can be edited incrementally from the terminal.

1. **Validate locally, before anything exists:**

```shell
helio-cli tests create --dry-run --project-id <uuid> \
    --name "..." --intro "..." --target-audience-size 100 \
    --questions @questions.json
```

`--dry-run` runs the full client-side validation (schema, required fields, choice minimums, scale types), estimates spend (questions × audience size), and never calls the API.

2. **Create the draft** — same command without `--dry-run`.

3. **Iterate on it:**

```shell
helio-cli tests add-question <test-id> --type likert \
    --instructions "The checkout was easy to complete." --scale-type agreement
helio-cli tests edit-question <test-id> <section-id> --instructions "..."
helio-cli tests remove-question <test-id> <section-id>
helio-cli tests order <test-id>            # view current order
helio-cli tests reorder <test-id> --order "metric:sentiment" "section:<uuid>"
helio-cli tests add-ux-metrics <test-id> --ux-metrics loyalty intent
helio-cli tests remove-ux-metrics <test-id> --ux-metrics loyalty
```

4. **Review it two ways:**

- `helio-cli tests preview <test-id>` — structural summary, every question on one page.
- `helio-cli tests walkthrough <test-id>` — the test as a participant will experience it, screen by screen. Add `--interactive` for TTY navigation, or `--output json` for a structured screen list an agent can read.

5. **Validate server-side, then launch:**

```shell
helio-cli tests validate <test-id>   # launch blockers, estimated spend, answers remaining
helio-cli tests send <test-id>       # launches — locks structure, charges answers
```

Always run `validate` before `send`. Send is immediate; there is no scheduled launch.

## Command surface

- **Setup & diagnostics:** `auth login`, `auth status`, `config set`, `config get`, `doctor`, `status`, `guide`
- **Browsing:** `projects list/get/tests`, `tests list`, `tests get <id>`, `audiences list/get`, `intercepts list/get`, `custom-lists list/participants/add-participants`, `participants create`
- **Building a draft:** `tests create`, `tests add-question`, `tests edit-question`, `tests remove-question`, `tests order`, `tests reorder`, `tests add-ux-metrics`, `tests remove-ux-metrics`, `tests update` (name, intro, audience size), `tests delete`
- **Assets:** `assets list` (filters: `--type`, `--name`, `--limit`, `--offset`), `assets get <id>`, `assets upload <file>` (images: jpg/jpeg/png/gif, max 10MB)
- **Schema lookups:** `tests question-types` (all types with required/optional fields and examples), `tests ux-metric-types` (all metrics with what sections they build)
- **Reviewing:** `tests preview`, `tests walkthrough [--interactive] [--output json]`
- **Launching:** `tests validate`, `tests send`
- **Reading results:** `tests report <id>`, `tests responses <id>`
- **Aliases:** `t` (tests), `p` (projects), `cl` (custom-lists), `pt` (participants), `a` (audiences), `ic` (intercepts), `r` (responses)

## tests create — inputs

| Flag | Meaning |
|---|---|
| `--project-id <uuid>` or `--project-name <name>` | Target project (name resolves by substring match) |
| `--name <name>` | Test name (required) |
| `--intro <text>` | Participant-facing intro (required) |
| `--target-audience-size <n>` | Responses to collect (required, positive integer) |
| `--audience-type <type>` | Default `open` |
| `--audiences <ids...>` | Existing audience segment IDs |
| `--questions <json or @file>` | Question array, inline or from a file |
| `--ux-metrics <types...>` | Auto-generated metric sections (space-separated) |
| `--ux-metric-context <text>` | Replaces the "[product]" noun in metric instructions |
| `--dry-run` | Validate + estimate spend, no API call |

A test needs at least one of `--questions` or `--ux-metrics`.

## Question payload schemas

Ten question types are creatable via the API. Each accepts snake_case or PascalCase (`multiple_choice` / `MultipleChoice`). Required fields are per type; the CLI validates everything before submitting.

**free_response** — open-ended text. Required: `type`, `instructions`. Optional: `asset_id`, `site_link`.

```json
{ "type": "free_response", "instructions": "What would you improve about our product?" }
```

**multiple_choice** — pick one or more. Required: `type`, `instructions`, `choices`. Optional: `allow_multiple`, `randomize_choices`.

```json
{ "type": "multiple_choice", "instructions": "How did you hear about us?",
  "choices": ["Search engine", "Social media", "Friend", "Other"],
  "allow_multiple": false, "randomize_choices": false }
```

**likert** — agreement/satisfaction scale. Required: `type`, `instructions`, `scale_type`. Optional: `custom_choices` (with `scale_type: "custom"`). Scale types: `agreement`, `occurrence`, `importance`, `quality`, `comprehension`, `impression`, `expectations`, `usefulness`, `difficulty`, `likelihood`, `custom`.

```json
{ "type": "likert", "instructions": "The checkout process was easy to complete.",
  "scale_type": "agreement" }
```

```json
{ "type": "likert", "instructions": "Rate the visual design.", "scale_type": "custom",
  "custom_choices": ["Love it", "Like it", "Neutral", "Dislike it"] }
```

**nps** — 0–10 recommendation scale. Required: `type`, `instructions`.

```json
{ "type": "nps", "instructions": "How likely are you to recommend us to a friend?" }
```

**ranking** — order items by preference. Required: `type`, `instructions`, `choices`.

```json
{ "type": "ranking", "instructions": "Rank these features by importance",
  "choices": ["Speed", "Design", "Price", "Support"] }
```

**preference** — pick a preferred option. Text-only via API; image variants are UI-only. Required: `type`, `instructions`, `choices`.

```json
{ "type": "preference", "instructions": "Which option do you prefer?",
  "choices": ["Option A", "Option B", "Option C"] }
```

**matrix** — rate multiple items on one scale. Required: `type`, `instructions`, `choices` (rows), `categories` (columns).

```json
{ "type": "matrix", "instructions": "Rate each feature",
  "choices": ["Speed", "Design", "Price"],
  "categories": ["Poor", "Fair", "Good", "Excellent"] }
```

**card_sort** — sort cards into categories. Required: `type`, `instructions`, `choices`, `categories`. Optional: `random_category_order`, `can_skip_cards`.

```json
{ "type": "card_sort", "instructions": "Sort these items into categories",
  "choices": ["Item A", "Item B", "Item C", "Item D"],
  "categories": ["Category 1", "Category 2", "Category 3"] }
```

**max_diff** — best/worst scaling. Required: `type`, `instructions`, `choices`.

```json
{ "type": "max_diff", "instructions": "Choose the most and least important",
  "choices": ["Feature A", "Feature B", "Feature C", "Feature D"] }
```

**point_allocation** — distribute a budget across options. Required: `type`, `instructions`, `choices`. Optional: `points` (default 100), `points_label`.

```json
{ "type": "point_allocation", "instructions": "Distribute 100 points across these features",
  "choices": ["Speed", "Design", "Price"], "points": 100, "points_label": "points" }
```

**Not creatable via API — UI-only:** `click_test`, `tree_test`, `prototype_task`. These need hotspot configuration or Figma prototypes, which the API doesn't accept. Build them in the web app; the CLI can still read their reports (click coordinates, tree paths, Direct/Indirect/Failed grades and per-screen journeys via `--include prototype_journeys`).

`asset_id` and `site_link` attach an asset or a URL to a question (`asset_id` is optional on `free_response`, and available on `tests add-question` / `edit-question` as `--asset-id`). Get asset IDs from `assets upload` or `assets list` — see the Assets section below.

## Assets — upload, list, get

As of helio-cli v0.1.1, image assets are fully CLI-native:

```shell
helio-cli assets upload ./homepage-mock.png      # jpg/jpeg/png/gif, max 10MB (multipart)
helio-cli assets list --type image --name homepage --limit 25 --offset 0
helio-cli assets get <asset-id>                  # status, dimensions, signed URLs
```

- **Upload** validates client-side first (file type and size) so bad files fail fast without a network call. Uploads return with `status: "processing"`; poll `assets get <id>` until `status` is `complete` for dimensions and URLs. Processing usually takes a few seconds.
- **Asset IDs are numeric** — unlike test and project UUIDs.
- **Attach to questions:** `tests add-question <test-id> --asset-id <id>` (free_response stimulus), `tests edit-question <test-id> <section-id> --asset-id <id>`, or `asset_id` in a question JSON payload.
- **`list` filters:** `--type` (image, video, audio), `--name` (case-insensitive partial match on filename), `--limit` (default 25, max 100), `--offset`. All assets in the account library are listable, including video/audio uploaded via the web app.
- **Still UI-only:** video and audio *upload* — `assets upload` accepts images only.
- `--output json` works on all three, like every other command.

## UX metrics — auto-generated sections

Tagging a metric auto-builds the right section structure. Eleven are creatable via the CLI:

| Metric | Builds |
|---|---|
| `sentiment` | 1 MultipleChoice (8 words, randomized) |
| `feeling` | 1 MultipleChoice (8 emotions, max 3, randomized) |
| `appeal` | 1 Likert (impression) |
| `reaction` | 1 Likert (impression) |
| `comprehension` | 1 Likert (comprehension, 4 choices) |
| `frequency` | 1 Likert (occurrence) |
| `loyalty` | 1 NPS |
| `intent` | 1 MultipleChoice (4 action choices, randomized) |
| `desirability` | 2 sections: MC (8 words) + Likert (likelihood) |
| `usefulness` | 2 Likerts (agreement) |
| `expectations` | 2 sections: FreeResponse + Likert (expectations) |

Each metric ships default instructions with a "[product]" noun that `--ux-metric-context` replaces (e.g. `--ux-metric-context "checkout flow"`).

**Not creatable via CLI** (they require prototypes or click tests, which are UI-only): `brand_score`, `engagement`, `success`, `completion`, `usability`, `satisfaction`, `effort`.

Metrics can be added to or removed from an existing draft (`tests add-ux-metrics` / `remove-ux-metrics`) without recreating the test. Duplicate metrics are rejected at validation.

## Working with output

**`--output json` on every command.** Add it to any command and the result becomes a structured payload. Pipe it into `jq`, a data warehouse, a notebook, or a script — every command honors the same flag, so your tooling only has to learn one contract.

```shell
helio-cli tests report <uuid> --output json | jq '.questions_summary'
```

**Structured errors and predictable exit codes.** When `--output json` is set, errors come back as JSON too. Exit codes stay consistent across commands, so scripts can branch on them without parsing stderr.

```json
{ "error": "Unauthorized", "code": 401 }
```

## What the CLI can't do

Know the ceilings before you script against them:

- **No video or audio upload.** `assets upload` handles images (jpg/jpeg/png/gif, max 10MB); video and audio files still go up through the web app. `assets list` can find them once they're there.
- **No click tests, tree tests, or prototype tasks** — creation is UI-only (see above).
- **No branching or skip logic.** Conditional routing and conditional follow-ups are configured in the web app.
- **No audience segment creation.** `audiences list` browses existing segments and `--audiences` attaches them; building a segment or screener is UI-side.
- **No scheduled launch.** `tests send` fires immediately.

If a test design needs any of these, do the CLI-buildable part first, finish in the web app, then `validate` and `send` from wherever is convenient — drafts are shared across all three surfaces.

## Use cases

**For developers.** You already live in a terminal. Now your research does too. Schedule nightly pulls, gate releases on sentiment thresholds, and version-control your test definitions next to the code they evaluate. Treat user feedback like any other production signal — observable, scriptable, and tied to a build.

```shell
helio-cli tests report $TEST_ID --output json | jq '.ux_metrics' | ./post-to-slack.sh
```

**For researchers and PMs.** Save a test once, run it a hundred times. Re-run last quarter's onboarding study against a fresh audience — no clicking through screens, no re-typing instructions, no losing the wording you spent two weeks tuning. The test definition is a file you can share, edit in a PR, and replay forever.

```shell
helio-cli tests create --project-id $PROJECT --name "Onboarding · Q3 wave" \
    --intro "$(cat onboarding-intro.txt)" --target-audience-size 100 \
    --ux-metrics sentiment loyalty
```

**For AI agents.** The combination of `--output json` everywhere, `--dry-run`, `tests question-types` / `ux-metric-types` (machine-readable schemas), and `tests walkthrough --output json` (a structured participant-eye view) makes the CLI fully drivable by an agent without a human at the screen. For interactive AI workflows, the MCP server is usually the better fit — the CLI is for when the agent's work should be a repeatable script.

## Where to go next

- `helio-cli guide` — guided walkthrough and full command schemas, also available as JSON
- `helio-cli tests question-types` / `tests ux-metric-types` — the schemas, from the tool itself
- `helio-creating-test` — how to design the test you're about to script
- `helio-mcp` — the same platform for AI assistants that speak MCP
- `helio-app` — positioning, plans, and how Helio fits the Glare workflow

<!-- /DERIVED -->

---

<!-- ADDED 2026-07-06 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Installing or authenticating the CLI
- Looking up the right command for a task — creating a draft, adding/editing/removing questions, reordering, previewing, walking through, validating, sending, pulling reports
- Building a test programmatically and needing the **question payload schema** for a specific type
- Uploading an image asset from the terminal, finding an asset ID, or attaching a stimulus with `--asset-id`
- Scripting Helio inside cron, CI, or a build pipeline
- Piping CLI JSON output to jq, Slack, or a data warehouse
- Wiring `--dry-run` into PR checks
- Asking what the CLI can and can't create (the UI-only boundary)
- Comparing the CLI surface to the MCP and web surfaces

For interactive AI workflows over Helio, route to `helio-mcp`. For designing the test itself, route to `helio-creating-test` (from a hunch) or `helio-asset-to-test` (from an asset).

## Worked example — iterate on a draft before spending

The loop that distinguishes CLI-native test work from create-and-pray:

```shell
# 1. Local validation, zero cost
helio-cli tests create --dry-run --project-name "Homepage" \
    --name "Homepage V2 eval" --intro "Quick feedback on our homepage." \
    --target-audience-size 100 --questions @questions.json --ux-metrics comprehension

# 2. Create the draft
helio-cli tests create --project-name "Homepage" ... --output json | jq -r '.id'

# 3. Realize Q3 is leading; fix it in place
helio-cli tests edit-question <test-id> <section-id> \
    --instructions "How does this page feel to you?"

# 4. See it as a participant will
helio-cli tests walkthrough <test-id> --interactive

# 5. Server-side check, then launch
helio-cli tests validate <test-id>
helio-cli tests send <test-id>
```

## Failure modes

- **Confusing the CLI with the MCP.** They share the underlying API but have different driver models. CLI = scripts. MCP = AI assistants.
- **Assuming everything is creatable.** Click tests, tree tests, prototype tasks, video/audio upload, branching, and audience creation are UI-only. (Image upload is CLI-native as of v0.1.1 — `assets upload`.) Check "What the CLI can't do" before promising a fully scripted build.
- **Recreating a test to change one question.** Use `add-question` / `edit-question` / `remove-question` / `reorder` on the draft instead — the incremental loop exists for this.
- **Skipping `preview`/`walkthrough` before `send`.** The walkthrough is the cheapest usability test you'll ever run — on your own test.
- **Forgetting `--dry-run` before a real launch.** Live `tests send` locks the structure and charges answers. Always dry-run first, and `validate` before `send`.
- **Pasting tokens into chat history.** Use env vars (`HELIO_API_ID`, `HELIO_API_TOKEN`) instead of inline credentials.
- **Using Node <22.** The CLI shebang resolves to whatever `node` is first in PATH. Run `nvm use 22` (or equivalent) before invoking if your default is older.

## Where to go next

- For AI assistants driving Helio: `helio-mcp`
- For designing the test from a hunch: `helio-creating-test`
- For the asset-first build workflow: `helio-asset-to-test`
- For section types: `helio-section-types`
- For UX metrics attachment: `helio-ux-metrics`
- For synthesizing report JSON into a Glare signal: `helio-reading-report`

<!-- /ADDED -->

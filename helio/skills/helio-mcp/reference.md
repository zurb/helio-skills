# Helio MCP — Reference

**Skill:** `helio-mcp`
**Source:** Helio MCP v1.3
**Source last synced:** 2026-07-06
**Notes:** v1.3 was regenerated from the MCP server codebase, correcting the v1.2 "twenty-six tools" claim to the actual registered surface: twenty tools, two prompts, one resource. The v1.3 Drive doc is a new document (a source document); the v1.2 doc (a source document) was moved to Archive on 2026-07-06.

---

<!-- DERIVED FROM: src-helio-mcp-v1.3 — Helio MCP v1.3 -->

Helio MCP is the safe, standard way to put AI assistants on top of Glare data. It exposes the entire Helio research platform — every test, response, demographic filter, and AI assessment — to any client that speaks the Model Context Protocol. Claude Desktop, Cursor, Claude Code, custom agents. One contract, auth handled at the protocol layer instead of being pasted into a prompt.

The web app is still there when you want it. The MCP server is there when your assistant should be the one driving.

## What this solves

An assistant that can only *read* Helio data answers questions; an assistant that can *build and launch tests* does research. The server supports both — but most write-ups list a handful of reporting tools and stop. The full registered surface: **twenty tools** spanning discovery, test creation, incremental editing, launch, reporting with demographic filters, segment comparison, and AI assessments — plus **two guided prompts** and **one workflow resource** that teach an assistant how to use them.

## When to use MCP (vs CLI vs web)

Three ways to reach Helio. Pick the one that fits the work.

- **MCP** — when an AI assistant should drive the work interactively. Cohort comparisons in chat, concept assessments from a prompt, end-to-end test launches a model can run by itself. Best for exploratory research and ad-hoc analysis where the question evolves.
- **CLI** — when a script or a cron job should drive the work. Nightly pulls, CI checks that gate releases on sentiment, version-controlled test definitions next to the code they evaluate. Best for deterministic, repeatable, auditable runs.
- **Web app** — when a person should drive the work. Initial project setup, careful review of responses, designing tests with a teammate at a screen.

The same Helio API is underneath all three. The choice is about who's driving, not what's available.

## Requirements

- Node.js ≥ 18 (stdio transport)
- A Helio API token (or OAuth credentials) — generate one at [my.helio.app/account/organization](https://my.helio.app/account/organization)
- An MCP-aware client (Claude Desktop, Cursor, Claude Code, Claude.ai web, or a custom agent)

## Install

Helio MCP ships in two transports. Pick whichever fits your client.

### Local (stdio)

For Claude Desktop, Cursor, and Claude Code, add the server to your MCP config (`~/.cursor/mcp.json`, Claude Desktop settings, or equivalent):

```json
{
  "mcpServers": {
    "helio": {
      "command": "npx",
      "args": ["-y", "@zurb/helio-mcp"],
      "env": {
        "HELIO_API_ID": "your-api-id",
        "HELIO_API_KEY": "your-api-key"
      }
    }
  }
}
```

Restart your assistant. The helio server should appear in your MCP tool list.

### Hosted (HTTP)

For clients that support remote MCP servers — Cursor, Claude.ai web, custom agents — skip the local install and point at the hosted endpoint:

```json
{
  "mcpServers": {
    "helio": {
      "url": "https://mcp.helio.app/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_HELIO_TOKEN"
      }
    }
  }
}
```

This uses the streamable-HTTP MCP transport. Older clients that don't support custom headers on remote servers will need the local stdio path instead.

## Quickstart

Confirm the server is connected by asking your assistant:

```
List my Helio projects.
```

You should get back a list of projects via the `list_projects` tool. From there, every Helio surface is one prompt away.

## The tool catalog

Twenty tools, grouped by what they're for.

### Discovery (5)

- `list_projects` — all projects, with test/response counts; filter by name
- `get_project` — one project with its tests
- `get_project_tests` — test ids and names inside a project
- `list_tests` — discover tests account-wide; filter by status, response count, tags, date range; the starting point for analysis
- `get_test` — full test object: configuration, questions, audience, metadata

### Building a draft (5)

- `create_test` — create a draft: `project_id`, `name`, `intro`, `target_audience_size`, plus `questions` and/or `ux_metrics`. Same ten creatable question types and eleven auto-generated UX metrics as the CLI. Also accepts `ux_metric_context` (noun replacement) and `ux_metric_assets` (attach an asset_id or site_link per metric — **not available in the CLI**). Returns spend estimate, answers remaining, test and preview URLs.
- `add_question` — append a question to a draft
- `update_question` — replace a regular question in place (provide `type`), or safely edit a UX metric section (omit `type`; only instructions / asset_id / site_link, plus choices on intent metrics)
- `remove_question` — remove a question (subsequent questions shift down; UX metric sections are removed via `update_test` instead)
- `update_test` — modify draft metadata (name, intro, audience size), add/remove UX metrics, and reorder sections — the MCP bundles what the CLI splits across `update` / `add-ux-metrics` / `remove-ux-metrics` / `reorder`

### Launching (3)

- `validate_test` — launch blockers, estimated spend, question count; call before send
- `send_test` — launch; uses the test's existing audience quota; returns spend, remaining answers, take/report URLs
- `delete_test` — delete a draft (irreversible)

### Reading results (4)

- `get_test_report` — the workhorse. Structured report with an `include` list: `summary`, `followups`, `responses` (paginated), `audiences`, `demographics`, `ux_metrics`, `prototype_journeys`, `filter_options`. Every section respects demographic filters (age, country, segment, sentiment, and more, all as arrays). Recommended flow: call with `filter_options,summary` first, then drill in.
- `get_filtered_responses` — one question's individual answers with demographic filters; the drill-down tool
- `get_responses` — raw, unaggregated responses for a test
- `compare_segments` — two filtered report calls in parallel, returned side by side (men vs women, US vs international, 18–24 vs 55–64)

### AI assessments / Design Analysis (3)

- `list_assessments` — all Design Analyses with status and progress
- `get_assessment` — scores, AI-generated sections, user-needs analysis, takeaways
- `create_assessment` — new Design Analysis from a title, concept, and at least one asset (URL, base64 image, or website URL)

### Prompts (2) and resource (1)

`analyze_test` (guided analysis of one test, optional focus) and `compare_audiences` (guided comparison of two audience groups) are MCP *prompts*, not tools — they inject a workflow, then drive the tools above. `helio://guide/analysis-workflow` is the built-in guide resource.

## Building a test from an assistant

The same draft → iterate → launch loop the CLI uses, driven conversationally:

1. `create_test` — draft with questions and/or UX metrics (nothing spent yet)
2. `add_question` / `update_question` / `remove_question` / `update_test` — iterate
3. `get_test` — inspect the structure
4. `validate_test` — server-side blocker check and spend estimate
5. `send_test` — launch

The question payload schema is identical to the CLI's: `type` + `instructions` required; `choices`, `scale_type` (11 Likert scales), `custom_choices`, `allow_multiple`, `randomize_choices`, `categories`, `points`, `points_label`, `asset_id`, `site_link` per type. See `helio-cli` for the per-type JSON examples — they transfer 1:1.

## What the MCP can't do

Same API, same ceilings as the CLI:

- **No asset upload or listing** — `asset_id` references existing assets; create or find them in the web app or via helio-cli (`assets upload` / `assets list`, images only)
- **No click tests, tree tests, or prototype tasks** — creation is UI-only (reports for them are fully readable, including prototype journeys)
- **No branching or skip logic, no audience segment creation, no scheduled launch**

Two MCP-specific notes: there is **no dry-run** — `validate_test` is the pre-spend check — and there is **no participant-eye walkthrough** (that's a CLI feature; the preview URL returned by `create_test` covers it in the browser).

## Workflows

### Compare cohorts without writing a query

```
You: "On test abc-123, compare what 25–34s and 45–54s said about the new
      pricing page. Highlight where sentiment splits."

→ get_test_report(test_id: "abc-123", include: ["summary", "demographics"])
→ compare_segments(test_id: "abc-123",
      segment_a: { age: ["25-34"] },
      segment_b: { age: ["45-54"] })
```

### Score a new concept end to end

```
You: "Run an assessment on the attached onboarding mockup against our
      'New SaaS users' audience. Tell me where it loses people."

→ create_assessment(title: "Onboarding v3 — first read",
      concept: "...", asset_url: "...")
→ get_assessment(id: "...")
```

### Re-run last quarter's study against a fresh audience

```
You: "Take test xyz-789 from last quarter, clone it with a new audience
      of 100 US/CA users aged 25–44, and launch it as 'Checkout · Q3 wave'."

→ get_test(id: "xyz-789")
→ create_test(name: "Checkout · Q3 wave", ..., target_audience_size: 100)
→ validate_test(id: "...")
→ send_test(id: "...")
```

## Where to go next

- `analyze_test` prompt — guided analysis workflow from your assistant
- `helio://guide/analysis-workflow` resource — the workflow guide, from the server itself
- `helio-creating-test` — how to design the test your assistant is about to build
- `helio-cli` — the same platform for scripts and pipelines, including the per-type question payload examples
- `helio-app` — positioning, plans, and how Helio fits the Glare workflow

<!-- /DERIVED -->

---

<!-- ADDED 2026-07-06 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Connecting Claude Desktop, Cursor, Claude Code, or a custom agent to Helio
- Choosing between the stdio and hosted-HTTP transports
- Asking what the MCP exposes (20 tools, 2 prompts, 1 resource — grouped as discovery / building / launching / reading / assessments)
- Building or iterating on a draft test from an assistant (`create_test` → `add/update/remove_question` → `update_test` → `validate_test` → `send_test`)
- Slicing reports by demographics or comparing segments from chat
- Comparing the MCP surface to the CLI and web surfaces
- Stuck because their MCP-aware client doesn't see the helio server after config

For scripted (non-interactive) Helio access, route to `helio-cli`. For designing the test itself, route to `helio-creating-test` (from a hunch) or `helio-asset-to-test` (from an asset).

## Failure modes

- **Quoting the old "26 tools" number.** The registered surface is 20 tools + 2 prompts + 1 resource. Count from the server, not from memory.
- **Pasting API keys into chat instead of the MCP env block.** The whole point of MCP is auth at the protocol layer. If a token is in a prompt, the architecture isn't working.
- **Forgetting to restart the client.** New MCP servers need a client restart to appear.
- **Picking hosted HTTP for a client that doesn't support custom headers on remote servers.** Older clients fail silently. Drop to stdio.
- **Expecting a dry-run.** The MCP has no `--dry-run` equivalent; `validate_test` before `send_test` is the pre-spend check.
- **Using the wrong editor for UX metric sections.** Regular questions: `update_question` with `type`. Metric sections: `update_question` without `type` (safe fields only), or `update_test` to add/remove metrics. `remove_question` refuses metric sections.
- **Treating MCP as a replacement for CLI in pipelines.** MCP is built for interactive AI workflows. For deterministic scripted runs, use the CLI.

## Where to go next

- For scripted access and payload JSON examples: `helio-cli`
- For designing the test from a hunch: `helio-creating-test`
- For the asset-first build workflow: `helio-asset-to-test`
- For section type depth: `helio-section-types`
- For UX metrics: `helio-ux-metrics`
- For interpreting MCP-returned report data: `helio-reading-report`
- For the AI Design Analysis workflow the assessment tools drive: `helio-design-analysis`

<!-- /ADDED -->

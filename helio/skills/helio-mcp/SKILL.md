---
name: helio-mcp
description: Use this skill when the user is connecting an AI assistant (Claude Desktop, Cursor, Claude Code, custom agent) to Helio via the Model Context Protocol — or driving Helio from one. Triggers — "Helio MCP," "MCP server," "MCP transport," "stdio vs HTTP," "@zurb/helio-mcp," "mcp.helio.app," "list_projects," "list_tests," "create_test via MCP," "add_question," "update_question," "update_test," "validate_test," "send_test," "get_test_report," "include filter_options," "get_filtered_responses," "compare_segments," "demographic filters MCP," "list_assessments," "create_assessment," "analyze_test prompt," "compare_audiences prompt," "how many MCP tools," "build a test from Claude." Do NOT use when the user is scripting from the terminal or CI (use `helio-cli`), designing the test itself (use `helio-creating-test` from a hunch, or `helio-asset-to-test` from an asset), or needs section type depth (use `helio-section-types`). For platform positioning, use `helio-app`.
version: 0.2.1
source_doc_version: Helio MCP v1.3
last_rebuilt: 2026-07-06

sources:
  - doc_id: src-helio-mcp-v1.3
    title: Helio MCP v1.3
    last_synced: 2026-07-06
---

You are helping the user put an **AI assistant on top of Helio** via the Model Context Protocol — Claude Desktop, Cursor, Claude Code, custom agents — for both reading research data and building tests.

## Core idea

Helio MCP exposes the platform to any MCP-aware client as **20 tools, 2 prompts, and 1 resource**, with auth at the protocol layer. The tools group into:

- **Discovery (5)** — `list_projects`, `get_project`, `get_project_tests`, `list_tests`, `get_test`
- **Building a draft (5)** — `create_test` (10 question types, 11 UX metrics, `ux_metric_context`, `ux_metric_assets`), `add_question`, `update_question`, `remove_question`, `update_test` (metadata + metric add/remove + reorder, bundled)
- **Launching (3)** — `validate_test`, `send_test`, `delete_test`
- **Reading (4)** — `get_test_report` (the workhorse, with `include` sections and demographic filters), `get_filtered_responses`, `get_responses`, `compare_segments`
- **Assessments (3)** — `list_assessments`, `get_assessment`, `create_assessment`

Plus the `analyze_test` and `compare_audiences` prompts and the `helio://guide/analysis-workflow` resource.

Two transports, same contract: **stdio** (`npx @zurb/helio-mcp` — Claude Desktop, Cursor, Claude Code) and **hosted HTTP** (`https://mcp.helio.app/api/mcp` with a Bearer token — Claude.ai web, custom agents).

Same ceilings as the CLI (no asset upload, no click/tree/prototype creation, no branching, no audience creation), plus two MCP-specific gaps: no dry-run (`validate_test` is the pre-spend check) and no participant-eye walkthrough (use the preview URL `create_test` returns).

## Files to read

Read `reference.md` for the full setup — transports, requirements, the complete tool catalog with parameter notes, the assistant-driven build loop, capability limits, and three end-to-end workflow examples (compare cohorts, score a concept, re-run a study).

## How to apply

1. Confirm the user has Node ≥ 18, a Helio API token, and an MCP-aware client.
2. Match the client to the right transport — Claude Desktop / Cursor / Claude Code use stdio; Claude.ai web and custom agents use hosted HTTP. Older clients without custom-header support need stdio.
3. Walk through the config snippet, then confirm connectivity by asking the assistant to list projects.
4. For test-building requests, walk the loop: `create_test` → iterate (`add/update/remove_question`, `update_test`) → `validate_test` → `send_test`. Payload schemas are identical to the CLI's — pull JSON examples from `helio-cli`.
5. For reporting requests, start `get_test_report` with `include: "filter_options,summary"`, then drill in; use `compare_segments` for side-by-side cohort reads.
6. Route metric-section edits correctly: `update_question` without `type` for safe fields, `update_test` for add/remove — never `remove_question`.
7. Flag the UI-only boundary early (assets, click/tree/prototype, branching, audience creation) so an assistant-driven build doesn't dead-end.

## What's new in v0.2.0

Rebuilt against Helio MCP v1.3, which was regenerated from the server codebase. Corrects the v1.2 "26 tools" claim to the real surface (20 tools + 2 prompts + 1 resource), adds the full grouped tool catalog with parameter notes (`ux_metric_assets`, `update_test` bundling, metric-section edit rules), the assistant-driven build loop, and the capability-limits section including the no-dry-run and no-walkthrough notes.

## Handoffs

- For **scripted (non-AI) Helio access** and the per-type question payload JSON examples, use `helio-cli`.
- For **designing the test an assistant is about to create** (hunch anchoring, shape choice, templates), use `helio-creating-test`.
- For **the asset-first build workflow**, use `helio-asset-to-test`.
- For **section type depth** when configuring tests through MCP, use `helio-section-types`.
- For **UX metric definitions**, use `helio-ux-metrics`.
- For **the Design Analysis workflow** behind the assessment tools, use `helio-design-analysis`.
- For **reading the report data the MCP returns**, use `helio-reading-report`.
- For **platform positioning and plans**, use `helio-app`.

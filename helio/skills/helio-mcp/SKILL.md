---
name: helio-mcp
description: Use this skill when the user is connecting an AI assistant (Claude Desktop, Cursor, Claude Code, custom agent) to Helio via the Model Context Protocol. Triggers — "Helio MCP," "MCP server," "MCP transport," "stdio vs HTTP," "@zurb/helio-mcp," "Claude Desktop helio," "Cursor helio," "mcp.helio.app," "list_projects," "get_test_report," "compare_segments," "create_assessment," "demographic filters MCP," "segment comparison MCP," "AI assistant helio," "26 tools." Do NOT use when the user is scripting from the terminal or CI (use `helio-cli`), needs section type depth (use `helio-section-types`), or wants test design (use `helio-asset-to-test`). For platform positioning, use `helio-app`.
version: 0.1.0
source_doc_version: Helio MCP v1.2
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1MG34t7erUX6Lwy4OXfBAR8QludFabaLae359yLQg59Y
    title: Helio MCP v1.2
    drive_url: https://docs.google.com/document/d/1MG34t7erUX6Lwy4OXfBAR8QludFabaLae359yLQg59Y/edit
    last_synced: 2026-05-23
---

You are helping the user put an **AI assistant on top of Helio data** via the Model Context Protocol — Claude Desktop, Cursor, Claude Code, custom agents.

## Core idea

Helio MCP is the safe, standard way to put AI assistants on top of Helio's research platform. It exposes the entire surface — every test, response, demographic filter, and AI assessment — to any client that speaks MCP. Twenty-six tools, one contract, auth handled at the protocol layer instead of being pasted into a prompt.

Two transports:

1. **Local (stdio)** — for Claude Desktop, Cursor, Claude Code. Runs locally via `npx @zurb/helio-mcp`, config in `mcp.json` or equivalent.
2. **Hosted (HTTP)** — for Cursor, Claude.ai web, custom agents. Point at `https://mcp.helio.app/api/mcp` with a Bearer token.

Same tools, same Zod-validated schemas, same Helio API underneath, regardless of transport.

## Files to read

Read `reference.md` for the full setup — transports, requirements, capability tour, and three end-to-end workflow examples (compare cohorts, score a concept, re-run a study).

## How to apply

1. Confirm the user has Node ≥18, a Helio API token, and an MCP-aware client.
2. Match the client to the right transport — Claude Desktop / Cursor / Claude Code use stdio; Claude.ai web and custom agents use hosted HTTP.
3. Walk through the config snippet (stdio: `npx @zurb/helio-mcp` with env vars; hosted: URL + Authorization header).
4. After restart, confirm the server is reachable by asking the assistant to list projects.
5. Surface the three workflow patterns: cohort comparison, concept assessment, study re-run.
6. Note older clients without custom-header support need the stdio path.

## What's new in v0.1.0

Initial release. Sourced from Helio MCP v1.2 (which includes the "When to use MCP vs CLI vs web" callout added during the v1.2 reconciliation pass). No AEO scorecard gaps to close.

## Handoffs

- For **scripted (non-AI) Helio access**, use `helio-cli`.
- For **the build workflow** an AI assistant might walk a user through, use `helio-asset-to-test`.
- For **section type depth** when configuring tests through MCP, use `helio-section-types`.
- For **UX metric attachment**, use `helio-ux-metrics`.
- For **reading the report data the MCP returns**, use `helio-reading-report`.
- For **platform positioning and plans**, use `helio-app`.

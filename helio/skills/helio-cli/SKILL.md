---
name: helio-cli
description: Use this skill when the user is working with Helio from the terminal — installing the CLI, authenticating, running commands, scripting research, gating CI on sentiment, version-controlling test definitions. Triggers — "helio-cli," "Helio CLI," "@zurb/helio-cli," "install helio-cli," "helio-cli auth login," "tests create," "tests report," "tests validate," "tests send," "--dry-run," "--output json," "helio CLI commands," "scripting helio," "cron helio," "CI helio," "PR check sentiment," "helio in pipeline," "helio jq pipe." Do NOT use when the user is driving Helio interactively from chat/AI (use `helio-mcp`), needs section type depth (use `helio-section-types`), or wants the build workflow (use `helio-asset-to-test`). For platform positioning, use `helio-app`.
version: 0.1.0
source_doc_version: Helio CLI v1.2
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1eNqJH7N-FC8sZn1_z5vFxopUS-UizuC7XDHv8xAwO60
    title: Helio CLI v1.2
    drive_url: https://docs.google.com/document/d/1eNqJH7N-FC8sZn1_z5vFxopUS-UizuC7XDHv8xAwO60/edit
    last_synced: 2026-05-23
---

You are helping the user drive **Helio from the terminal** — by hand, by cron, or inside a CI/CD pipeline.

## Core idea

Helio CLI (`@zurb/helio-cli`) puts the full Helio research platform behind a terminal, with structured JSON output, dry-run validation, predictable exit codes, and test definitions you can version-control alongside the code they evaluate. Three usage modes:

1. **By hand** — interactive use during test design
2. **By cron / CI** — nightly pulls, release gates on sentiment thresholds
3. **By AI agent** — when an agent needs deterministic scripted Helio access (use the MCP server instead for interactive AI workflows)

Pick the CLI when: a script or pipeline should drive the work, the run needs to be repeatable and auditable, or test definitions need to live in version control next to the code they evaluate.

## Files to read

Read `reference.md` for the full surface — install, authenticate, command catalog, JSON output handling, dry-run patterns, and use cases.

## How to apply

1. Confirm the user has Node ≥22 and a Helio API token.
2. Walk them through install (`npm install -g @zurb/helio-cli`) and auth choice (interactive vs env vars).
3. Match the user's task to the right command — `tests create`, `tests report`, `tests validate`, `tests send`, etc.
4. Surface `--output json` and `--dry-run` for any operation that touches money or production.
5. Point to the JSON pipeline pattern (`helio-cli tests report <uuid> --output json | jq '.questions_summary'`) for analysis workflows.
6. Flag CLI-only limits (no asset upload, no hotspot drawing — those are UI-only; covered in `helio-asset-to-test`).

## What's new in v0.1.0

Initial release. Sourced from Helio CLI v1.2. No AEO scorecard gaps to close.

## Handoffs

- For **interactive AI-driven Helio access**, use `helio-mcp`.
- For **the end-to-end build workflow** (the 7-step arc), use `helio-asset-to-test`.
- For **section type depth**, use `helio-section-types`.
- For **UX metric attachment commands**, use `helio-ux-metrics`.
- For **what the platform actually does at a feature level**, use `helio-app`.
- For **reading the JSON report output**, use `helio-reading-report`.

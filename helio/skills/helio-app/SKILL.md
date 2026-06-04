---
name: helio-app
description: Use this skill when the user is asking about Helio at the platform level — what Helio is, what it does, what plans cost, how to choose a plan, capability tour, or how Helio fits the Glare workflow. Triggers — "what is Helio," "how does Helio work," "Helio pricing," "Helio plans," "Pilot vs Scale vs On Demand vs Business," "what can Helio do," "how do I get started with Helio," "build → recruit → read," "Helio capabilities," "where does Helio fit," "Helio panel," "Helio + Glare." Do NOT use when the user wants section type depth (use `helio-section-types`), audience details (use `helio-audience-flow`), UX metric specifics (use `helio-ux-metrics`), the AI heuristic evaluator (use `helio-design-analysis`), or the CLI/MCP surfaces (use `helio-cli` / `helio-mcp`). For test design, use `helio-asset-to-test`. For synthesis, use `helio-reading-report`.
version: 0.1.0
source_doc_version: Helio App v1.3 + Using Helio v0.2 (merged)
last_rebuilt: 2026-05-23

sources:
  - doc_id: 12IcYGKc-sOPM-4zR-Oo-FdZl0gZLo9wc2b7qJvMiMR4
    title: Helio App v1.3
    drive_url: https://docs.google.com/document/d/12IcYGKc-sOPM-4zR-Oo-FdZl0gZLo9wc2b7qJvMiMR4/edit
    last_synced: 2026-05-23
  - doc_id: 1snPQ7OQY4UKqt7Pakgs2WY_1eqgX-hnbMG6AKtwuXS4
    title: Using Helio v0.2
    drive_url: https://docs.google.com/document/d/1snPQ7OQY4UKqt7Pakgs2WY_1eqgX-hnbMG6AKtwuXS4/edit
    last_synced: 2026-05-23
---

You are helping the user understand **Helio** at the platform level — what it is, what it does, what it costs, and how it fits the Glare workflow.

## Core idea

Helio is ZURB's fast user research and testing platform for product design teams. It runs 14 section types (Click Tests, Prototype Tests, Likert scales, Multiple Choice, NPS, MaxDiff, Card Sort, Tree Test, and more) against a real audience (~1M panelists) and produces UX Metric scores (0–100, with a consistent 5-tier label: Very Good / Good / Average / Poor / Very Poor) that drop straight into Glare.

Every study follows the same shape:

1. **Build** — pick the section types that match what you're asking; configure branching and UX Metric tagging
2. **Recruit** — pick an audience (Helio panel, custom list, intercept, API, AI personas)
3. **Read** — the report updates live; slice with filters; capture findings

Helio implements two of Glare's four metric families: **Behavioral (8 metrics)** and **Attitudinal (9 metrics)** — 17 total. Performance and Intelligence are Glare concepts not yet in Helio's code.

## Files to read

Read `reference.md` for the full positioning, plans, capability tour, and Glare-workflow framing. The reference is structured as two DERIVED blocks (Helio App v1.3 + Using Helio v0.2) followed by ADDED sections.

## How to apply

1. If the user is new to Helio, lead with the build → recruit → read framing.
2. If the user is asking about plans / pricing, route to the "Pricing" + "Choosing a plan" sections.
3. If the user wants to know what they can do, route to the "Building a Study" + "Recruiting Participants" + "Reading the Report" sections (from Using Helio).
4. If the user is connecting Helio to a broader research framework, route to the "Helio in the Glare workflow" section.
5. For depth on any specific surface, hand off to the sibling skill (see Handoffs).
6. If the user is asking about engineering specifics (controllers, models, feature flags), hand off to `helio-features`.

## What's new in v0.1.0

Initial release. Merges Helio App v1.3 (positioning + plans + Glare workflow) and Using Helio v0.2 (capability tour) into a single skill. The Helio App content was reconciled in v1.3 against UX Metrics v0.1 — pricing tiers and the Behavioral + Attitudinal metric taxonomy are now accurate.

## Handoffs

- For **section type depth** (Click Test, Prototype Test, MaxDiff, etc.), use `helio-section-types`.
- For **audience choice** (panel, custom lists, intercept, AI personas), use `helio-audience-flow`.
- For **the 17 UX Metrics** (definitions, sections required, thresholds), use `helio-ux-metrics`.
- For **building a study end to end** (the 7-step workflow), use `helio-asset-to-test`.
- For **the CLI surface**, use `helio-cli`. For **the MCP surface**, use `helio-mcp`.
- For **the engineering-side feature reference**, use `helio-features`.
- For **reading and synthesizing results**, use `helio-reading-report`.
- For **the broader Glare framework**, use `glare-getting-started` or `glare-decision-map`.

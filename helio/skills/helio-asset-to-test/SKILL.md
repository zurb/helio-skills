---
name: helio-asset-to-test
description: Use this skill when the user is going from a design (screenshot, mockup, prototype) to a launched Helio test — building the test, validating it, and sending it. Triggers — "how do I build a test," "from asset to test," "set up a Helio test," "what test should I run," "test build workflow," "validate before launch," "dry-run a test," "how do I structure my questions," "Signal Blitz worked example," "pre-launch checklist," "naming the risk," "picking a template," "audience for my test," "questions JSON," "send test." Do NOT use when the user wants section type depth (use `helio-section-types`), metric attachment specifics (use `helio-ux-metrics`), audience setup specifics (use `helio-audience-flow`), or branching configuration (use `helio-branching`). For reading the resulting report, use `helio-reading-report`. For recognizing test shapes by pattern, use `helio-patterns`.
version: 0.1.0
source_doc_version: From Asset To Test v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1mzj79nyrqDPLqhW1nC4ib7ug5HMbOKfRGJxIgAz8CcA
    title: From Asset To Test v0.1
    drive_url: https://docs.google.com/document/d/1mzj79nyrqDPLqhW1nC4ib7ug5HMbOKfRGJxIgAz8CcA/edit
    last_synced: 2026-05-23
---

You are helping the user run the **From Asset To Test** workflow — taking a design and turning it into a launched Helio study, in seven steps.

## Core idea

Going from a design (screenshot, mockup, prototype) to a launched Helio test follows a seven-step arc, roughly 40 minutes total once you've done it a few times:

1. **Classify the asset** (1 min) — single screen or multi-screen, what kind of page, B2C or B2B, primary outcome
2. **Name the testable risk** (5 min) — riskiest assumption, mapped to a question type
3. **Pick a template** (30 sec) — by shape and goal, not by question count
4. **Define the audience** (5 min) — single segment or fanout, prebuilt or custom list
5. **Customize the questions** (15 min) — the question array, with followups and CTAs
6. **Attach UX metrics** (1 min) — mostly mechanical, mapped from goal
7. **Build, validate, launch** (10 min) — `helio-cli tests create`, UI for asset upload + hotspots, validate + send

The step most often skipped is **Step 2 — name the testable risk**. It's also the one that distinguishes a useful test from a templated one. If you can't name the risk, you'll get a report with no decisive finding.

## Files to read

Read `reference.md` for the full seven-step walkthrough, the worked Signal Blitz example, the pre-launch checklist, and what the workflow doesn't yet cover (asset upload, hotspots, branching — all UI-only today).

## How to apply

1. Start by classifying the asset (single screen vs flow, page type, B2C/B2B, primary outcome). This sets up everything downstream.
2. Force the testable risk discussion. If the user can't name a risk, surface that gap — testing without a risk produces "interesting findings" not decisions.
3. Match the risk to a template (Core 5-Q, multi-screen, content-prioritization variant, etc.). Use the decision tree in the reference.
4. Walk through audience selection — prebuilt segment vs custom list vs fanout — using `helio-audience-flow` for depth.
5. Help draft the questions array. Surface the question shapes per template. Use `helio-section-types` for section depth and `helio-ux-metrics` for metric attachment.
6. Walk the user through validation: `helio-cli tests validate`, dry-run, preview. Don't `send` until validate passes clean.
7. Surface the workflow gaps explicitly: asset upload, hotspot drawing, and branching path config are all UI-only today.

## What's new in v0.1.0

Initial release. Sourced from From Asset To Test v0.1. AEO scorecard flagged a Problem-opener gap — addressed in the ADDED section of `reference.md`.

`agent-operations.md` is **not** built for v0.1.0. The workflow has a natural runtime contract (the 7-step arc, the pre-launch checklist), but no clear escalation triggers or output schema that need promotion yet. Surface to user during v0.2+ if a real runtime contract emerges.

## Handoffs

- For **section type depth** during step 5 (questions), use `helio-section-types`.
- For **picking the UX Metric** during step 6, use `helio-ux-metrics`.
- For **audience configuration depth** during step 4, use `helio-audience-flow`.
- For **branching setup** (if the test uses conditional routing), use `helio-branching`.
- For **asset handling specifics** (image upload, Figma integration, hotspot drawing), use `helio-assets`.
- For **recognizing test shapes by pattern**, use `helio-patterns`.
- For **reading the resulting report**, use `helio-reading-report`.
- For **the CLI commands referenced in step 7**, use `helio-cli`.

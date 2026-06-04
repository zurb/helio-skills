---
name: helio-patterns
description: Use this skill when the user wants to recognize or construct Helio tests by shape — the core 5-Q template, multi-screen flows, audience fanouts, MaxDiff content variants, R3/R5 generations, the 145-vs-144 iteration distinction. Triggers — "Helio test patterns," "the 5-Q template," "core template," "test shapes," "single-screen vs multi-screen," "R3 vs R5," "144 series vs 145 series," "audience fanout," "iteration methodology," "branching as multi-screen tell," "engagement vs success click test," "test name reads multi-screen," "30-second scan." Do NOT use when the user wants section type spec (use `helio-section-types`), the full build workflow (use `helio-asset-to-test`), audience setup mechanics (use `helio-audience-flow`), or report synthesis (use `helio-reading-report`).
version: 0.1.0
source_doc_version: Helio Test Patterns v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1G1yPnRDZeY9nKXENSQb_LOkj5T2tdNBU2_DTE1YQ7ts
    title: Helio Test Patterns v0.1
    drive_url: https://docs.google.com/document/d/1G1yPnRDZeY9nKXENSQb_LOkj5T2tdNBU2_DTE1YQ7ts/edit
    last_synced: 2026-05-23
---

You are helping the user **recognize, read, or construct** Helio tests by shape — the recurring patterns that show up across real studies.

## Core idea

Most Helio tests are variations on a single five-question template. Recognize the template and you can read about 70% of reports without further instruction. The remaining 30% are specialized patterns identifiable at a glance.

The patterns, drawn from a sample of 15 tests across four projects:

1. **The core 5-Q template** — comprehension Likert + engagement Click Test + desirability Multi-Select + likelihood Likert + commit/loyalty (NPS or forced next-action)
2. **Two intro styles** — generic boilerplate (with the scenario buried in Q1) vs scenario-led
3. **Click tests do double duty** — `engagement` metric (broad, many hotspots) vs `success` metric (targeted, branching usually on)
4. **Required followups carry the insight** — the comprehension followup is the only one that converts self-rating to knowledge probe
5. **The UX metric is the real instrument** — not the question wording
6. **Audience definitions are strategic** — not generic; fanout testing is its own method
7. **Two iteration methodologies** — 145-style template iteration (locked structure) vs 144-style flow evolution (structure drifts)
8. **Single-screen vs multi-screen are fundamentally different shapes**
9. **R3 vs R5 depth/cost tradeoff** — R3 captures pre/post comprehension shift; R5 is just impression
10. **Branching ≈ "this test has connected screens"**

Plus a 30-second scan routine for reading new reports and a quick decision tree for constructing new tests.

## Files to read

Read `reference.md` for the full pattern catalog with concrete examples (Stoko, KUIU, Disney, StoryTrading, USAA, 144/145 series), the 30-second reading routine, and the construction decision tree.

## How to apply

1. If the user is reading a new report, walk the 30-second scan: test name → intro → audience → Q-count/asset-count → UX metrics.
2. Identify which pattern the test follows by shape, not by question count.
3. For each metric in use, surface what to watch for — divergences (`engagement` high but `intent` low is the headline read).
4. If the user is constructing a new test, walk the decision tree: single-screen vs multi-screen, A/B iteration vs flow redesign, headline outcome, audience.
5. Surface "what's not in the sample" caveats for less-common shapes (MaxDiff, card sort, point allocation).

## What's new in v0.1.0

Initial release. Sourced from Helio Test Patterns v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **section type spec** (Click vs Prototype, Likert templates, etc.), use `helio-section-types`.
- For **the full build/validate/launch workflow**, use `helio-asset-to-test`.
- For **audience setup depth** (panel, custom lists, intercept, AI), use `helio-audience-flow`.
- For **UX metric definitions and scoring**, use `helio-ux-metrics`.
- For **branching configuration**, use `helio-branching`.
- For **reading and synthesizing results**, use `helio-reading-report`.

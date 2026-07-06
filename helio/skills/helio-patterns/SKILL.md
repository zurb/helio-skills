---
name: helio-patterns
description: Use this skill when the user wants to recognize or construct Helio tests by shape — the core 5-Q template, multi-screen flows, audience fanouts, MaxDiff content variants, legacy template generations, the fixed-template vs evolving-flow iteration distinction. Triggers — "Helio test patterns," "the 5-Q template," "core template," "test shapes," "single-screen vs multi-screen," "deep vs light template," "the evolving-flow series vs the fixed-template series," "audience fanout," "iteration methodology," "branching as multi-screen tell," "engagement vs success click test," "test name reads multi-screen," "30-second scan." Do NOT use when the user wants section type spec (use `helio-section-types`), the full build workflow (use `helio-asset-to-test`), audience setup mechanics (use `helio-audience-flow`), or report synthesis (use `helio-reading-report`).
version: 0.2.0
source_doc_version: Helio Test Patterns v0.2 (scrubbed)
last_rebuilt: 2026-07-06

sources:
  - doc_id: src-helio-test-patterns-v0.2
    title: Helio Test Patterns v0.2 (scrubbed)
    last_synced: 2026-07-06
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
7. **Two iteration methodologies** — fixed-template style template iteration (locked structure) vs evolving-flow style flow evolution (structure drifts)
8. **Single-screen vs multi-screen are fundamentally different shapes**
9. **deep vs light template depth/cost tradeoff** — R3 captures pre/post comprehension shift; R5 is just impression
10. **Branching ≈ "this test has connected screens"**

Plus a 30-second scan routine for reading new reports and a quick decision tree for constructing new tests.

## Files to read

Read `reference.md` for the full pattern catalog with concrete examples (the athletic-apparel homepage, the hunting-apparel store, the press-room site, the investment-platform, the veteran careers landing page, 144/the fixed-template series), the 30-second reading routine, and the construction decision tree.

## How to apply

1. If the user is reading a new report, walk the 30-second scan: test name → intro → audience → Q-count/asset-count → UX metrics.
2. Identify which pattern the test follows by shape, not by question count.
3. For each metric in use, surface what to watch for — divergences (`engagement` high but `intent` low is the headline read).
4. If the user is constructing a new test, walk the decision tree: single-screen vs multi-screen, A/B iteration vs flow redesign, headline outcome, audience.
5. Surface "what's not in the sample" caveats for less-common shapes (MaxDiff, card sort, point allocation).

## What's new in v0.2.0

Rebuilt against Helio Test Patterns v0.2 (scrubbed) — the Drive-side anonymized revision. Customer engagement names in the source are now category descriptors (matching the local scrub shipped in marketplace v0.3.2), the "O2" project prefix is dropped in favor of "the 145/the evolving-flow series," and the tooling notes gain the Node 22 / nvm PATH caveat. No pattern content changed.

## What's new in v0.1.0

Initial release. Sourced from Helio Test Patterns v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **section type spec** (Click vs Prototype, Likert templates, etc.), use `helio-section-types`.
- For **the full build/validate/launch workflow**, use `helio-asset-to-test`.
- For **audience setup depth** (panel, custom lists, intercept, AI), use `helio-audience-flow`.
- For **UX metric definitions and scoring**, use `helio-ux-metrics`.
- For **branching configuration**, use `helio-branching`.
- For **reading and synthesizing results**, use `helio-reading-report`.

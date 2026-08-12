---
name: helio-patterns
description: Use this skill when the user wants to recognize or construct Helio tests by shape and stage — the core 5-Q template, the seven data-backed templates (T1 Two-Tap Check, T2 MaxDiff Read, T3 Shelf & NPS, T4 Findability Sweep, T5 Homepage Five, T6 Expectation Probe, T7 Flow Expectation), multi-screen flows, audience fanouts, brand-template depth, and two iteration methodologies. Triggers — "Helio test patterns," "test pattern playbook," "which template," "what test should I run at this stage," "first look vs iterate vs benchmark," "findability sweep," "expectation probe," "single-screen vs multi-screen," "engagement vs success click test," "metric coverage," "30-second scan," "audience fanout," "deep vs light." Do NOT use when the user wants section type spec (use `helio-section-types`), the hunch → shape design arc (use `helio-creating-test`), the asset-first build workflow (use `helio-asset-to-test`), audience setup mechanics (use `helio-audience-flow`), or report synthesis (use `helio-reading-report`).
version: 0.4.3
source_doc_version: Helio Test Patterns v0.3 + Test Pattern Playbook v0.1 (merged)
last_rebuilt: 2026-07-06

sources:
  - doc_id: src-helio-test-patterns
    title: Helio Test Patterns v0.3
    last_synced: 2026-07-06
  - doc_id: src-test-pattern-playbook
    title: Test Pattern Playbook v0.1
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
7. **Two iteration methodologies** — fixed-template iteration (locked structure) vs evolving-flow iteration (structure drifts)
8. **Single-screen vs multi-screen are fundamentally different shapes**
9. **Deep vs light brand template** — the deep version captures pre/post comprehension shift; the light version is just impression
10. **Branching ≈ "this test has connected screens"**

Plus a 30-second scan routine for reading new reports and a quick decision tree for constructing new tests.

**New in v0.3.0 — the Playbook layer (285-test analysis):** seven data-backed templates mapped to the project moment where each earns its place. Ask the **asset** first (one screen → T2/T3/T5/T6; connected flow → T1/T7; either → T4), then the **stage**:

- **First look** (new asset, no data): T5 Homepage Five, T2 MaxDiff Read, T3 Shelf & NPS, T4 as baseline
- **Iterate** (V1/V2/V3, locked shape): T1 Two-Tap Check, T6 Expectation Probe, T7 Flow Expectation, T4 Findability Sweep
- **Benchmark** (competitor's screens, your questions): T7, T3

Each template ships a full question table (type, metric, prompt, required follow-up). 61% of real tests fit a template; ~39% are custom — starting points, not cages.

## Files to read

Read `reference.md` for both layers: the reading synthesis (pattern catalog with concrete examples, the 30-second routine, the construction decision tree) and the Playbook (stage triggers, metric coverage table, all seven template question tables, the two operating styles, house follow-up rules).

## How to apply

1. If the user is reading a new report, walk the 30-second scan: test name → intro → audience → Q-count/asset-count → UX metrics.
2. Identify which pattern the test follows by shape, not by question count.
3. For each metric in use, surface what to watch for — divergences (`engagement` high but `intent` low is the headline read).
4. If the user is constructing a new test, walk the decision tree: single-screen vs multi-screen, A/B iteration vs flow redesign, headline outcome, audience.
5. Surface "what's not in the sample" caveats for less-common shapes (MaxDiff, card sort, point allocation).

## What's new in v0.4.3

Disclosure scrub. Source documents are now referenced by opaque key (`src-*`) rather than by Drive id or link, with the real mapping held privately outside the repo. Named references were removed throughout: customer and engagement names, internal project and template codes, real test names, colleague names, and issue references into private repositories. No capability, workflow, or guidance content changed.

## What's new in v0.4.2

Synced to helio-cli v0.7.0: `engagement` and `success` are now taggable from the CLI (the v0.4.1 correction is obsolete), with the caveat that a click section needs hotspots or the metric scores zero — pass them via `--ux-metrics-json`.

## What's new in v0.4.1

**Correction to v0.4.0.** The decision tree told readers to "tag `success`" / "tag `engagement`" — the API rejects both on create and on `add-ux-metrics`. Corrected to: build the click test from the CLI, attach the metric in the web app.

## What's new in v0.4.0

Metrics-first framing. §5 upgraded from "each question *can* carry a metric" to the default build move (tag first, then adjust wording; hand-write only what no metric builds). The construction decision tree now maps each headline outcome to a **metric to tag** rather than a question shape to assemble, with click-test-backed metrics (`engagement`, `success`) called out as the exception that still needs a hand-built section. This skill is now the routing target for `helio-asset-to-test` Step 3, which picks templates from the canonical T1–T7 set here.

## What's new in v0.3.0

Merged in the **Test Pattern Playbook v0.1** as a second source (new Drive doc, derived from a 285-test / 5-month analysis — 19× the original sample). Adds the stage axis (first look / iterate / benchmark) with real use counts, seven concrete templates with full question tables, the empirical metric-coverage table (20 metrics, 6 carrying ~⅔ of measurement), the two operating styles, and the asset-first template picker. The playbook resolves several of Test Patterns' "what's NOT in this sample" caveats. Customer names and researcher identifiers were scrubbed during the doc build.

## What's new in v0.2.0

Rebuilt against Helio Test Patterns v0.2 — the anonymized revision. Engagement names in the source are now category descriptors, project prefixes are replaced with descriptive series names, and the tooling notes gain the Node 22 / nvm PATH caveat. No pattern content changed.

## What's new in v0.1.0

Initial release. Sourced from Helio Test Patterns v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **designing a new test from a hunch** (the hunch → shape → test → signal arc, with ready-to-edit templates), use `helio-creating-test`.
- For **section type spec** (Click vs Prototype, Likert templates, etc.), use `helio-section-types`.
- For **the full build/validate/launch workflow**, use `helio-asset-to-test`.
- For **audience setup depth** (panel, custom lists, intercept, AI), use `helio-audience-flow`.
- For **UX metric definitions and scoring**, use `helio-ux-metrics`.
- For **branching configuration**, use `helio-branching`.
- For **reading and synthesizing results**, use `helio-reading-report`.

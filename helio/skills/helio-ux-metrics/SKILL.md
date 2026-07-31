---
name: helio-ux-metrics
description: Use this skill when the user is working with Helio's UX Metrics — picking which metric to attach, understanding what a score means, comparing metrics across studies, or interpreting threshold labels. Triggers — "UX metric," "what does Sentiment mean," "Behavioral vs Attitudinal," "Brand Score," "Desirability v1 vs v2," "what's a Good score," "threshold labels," "Very Good Good Average Poor Very Poor," "Overall Score," "the 17 metrics," "metric sections," "auto-build sections," "metric versioning," "Effort metric," "Feeling metric," "Appeal metric," "Usability metric," "AI-derived metrics," "metric isn't showing." Do NOT use when the question is about picking a section type (use `helio-section-types`), the AI heuristic evaluator (use `helio-design-analysis`), filtering report data (use `helio-report-filtering`), or synthesis (use `helio-reading-report`). For the Glare framework's broader metric taxonomy, use `glare-ux-metrics`.
version: 0.4.0
source_doc_version: UX Metrics v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 10FW5AadbkNBirvE_CBGO3gqro-AcPtJSaSLgYSu1HLQ
    title: UX Metrics v0.1
    drive_url: https://docs.google.com/document/d/10FW5AadbkNBirvE_CBGO3gqro-AcPtJSaSLgYSu1HLQ/edit
    last_synced: 2026-05-23
---

You are helping the user understand and apply **Helio's UX Metrics** — the 17 measurable aspects of user experience Helio scores from participant responses.

## Core idea

A UX Metric is a measurable aspect of the user experience that Helio scores from participant responses. Each one produces a **0–100 score** and a **quality label**.

Two key ideas drive everything else:

1. **Metrics auto-build the questions they need.** Tag a section with a UX Metric and Helio generates the specific section structure that metric requires.
2. **Scores are computed live.** Every report view re-runs scoring against current responses and any active filters. Scores aren't stored.

**Framing that matters:** metrics are the default way to set up a test, not an add-on. A tagged metric produces a 0–100 score, a threshold label, cross-wave comparability, and a slot in the Overall Score; a hand-written section that merely resembles it produces an answer distribution and feeds none of that. Lead test setup with metrics; hand-write sections only for what no metric measures (see "Why tag a metric instead of writing your own sections" in `reference.md`).

Helio implements two of Glare's four metric families:

- **Behavioral (8)** — what people did: Success, Completion, Usability, Engagement, Effort, Comprehension, Frequency, Intent
- **Attitudinal (9)** — how people felt: Sentiment, Feeling, Desirability, Loyalty, Appeal, Usefulness, Expectations, Satisfaction, Brand Score

Performance and Intelligence metrics are Glare concepts not implemented in Helio today.

Every metric maps to a consistent 5-tier label:

| Score | Label |
|---|---|
| 90–100 | Very Good |
| 70–89 | Good |
| 50–69 | Average |
| 30–49 | Poor |
| Below 30 | Very Poor |

Helio also rolls every metric tagged on a study into a single **Overall Score** — the equal-weight average across all metrics.

## Files to read

Read `reference.md` for the full per-metric reference — what each metric captures, the section(s) it needs, the scoring logic, when to use it, and the at-a-glance summary table.

## How to apply

1. Identify what the user wants to measure (a behavior, a feeling, a comprehension level, a recommendation) — and if they're hand-writing a question a metric already covers, steer them to tagging the metric instead.
2. Pick the metric family (Behavioral or Attitudinal) by whether the user is asking about what people *did* or how they *felt*.
3. Pick the specific metric within that family by what it captures.
4. Surface the required section structure (1 section, 2 sections, or 3 sections — some metrics like Brand Score need composite setups).
5. Name the threshold label the user should expect / target.
6. Flag versioning gotchas (especially Desirability v1 vs v2 — they coexist; confirm which is active before comparing across studies).
7. Note the AI-derived metric caveat: Design Analysis scores use the same metric names but live in a separate data structure as labels only (no numeric 0–100).

## What's new in v0.4.0

Same-metric-twice rewritten for helio-cli v0.7.0 / the 2026-07-30 API release: repeating a metric type now works — tag it as many times as you need, each instance owns its sections and score. The web-app workaround is retired to a historical note. Adds the two consequences: `tests order` emits one block per instance and reports `reorderable: false` for repeated types (capture uuids from the create response), and `remove-ux-metrics` accepts either a type or a specific metric id.

## What's new in v0.3.0

*(Superseded by v0.4.0 — the restriction described here was lifted in helio-cli v0.7.0.)* Documents the same-metric-twice case, previously undocumented anywhere and the cause of a real hand-built workaround: the platform scores multiple instances of one metric (a live test carries three `expectations` metrics at 77/78/78), but the API and CLI reject the duplicate. Guidance is to build that instance in the web app — never to hand-build look-alike sections, which trades a scored metric for a distribution.

## What's new in v0.2.1

Added the journey counterweight to the "Why tag a metric" section in `reference.md`: tagging guarantees each section is valid, not that the sequence is coherent. Names the known collisions (sentiment ↔ desirability share the impressions MC; appeal ↔ reaction build the identical Likert) and the context-noun rule (one noun feeds every generated instruction — it must read naturally in all of them). Points to the journey checks in `helio-creating-test`.

## What's new in v0.2.0

Added the metrics-first framing: a "Why tag a metric instead of writing your own sections" section in `reference.md` (score vs distribution, validated wording, cross-wave comparability, Overall Score membership, unbreakable structures, speed — plus when hand-writing is right), and the framing paragraph in this file's Core idea. Echoed in `helio-cli` (UX metrics section) and `helio-creating-test` (rules of thumb). Metrics are the default test-setup move, not an add-on.

## What's new in v0.1.0

Initial release. Sourced from UX Metrics v0.1. AEO scorecard flagged a Problem-opener gap — addressed in the ADDED section of `reference.md`.

## Handoffs

- For **section types** that get tagged with these metrics, use `helio-section-types`.
- For **the AI heuristic evaluator** that scores against the same metrics from an AI source, use `helio-design-analysis`.
- For **filtering the report** (segments, demographics, sentiment, response time), use `helio-report-filtering`.
- For **synthesis and signal-writing** using these scores, use `helio-reading-report`.
- For **Glare's broader UX Metrics framework** (all four families, including Performance and Intelligence), use `glare-ux-metrics`.

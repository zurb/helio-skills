---
name: helio-ux-metrics
description: Use this skill when the user is working with Helio's UX Metrics — picking which metric to attach, understanding what a score means, comparing metrics across studies, or interpreting threshold labels. Triggers — "UX metric," "what does Sentiment mean," "Behavioral vs Attitudinal," "Brand Score," "Desirability v1 vs v2," "what's a Good score," "threshold labels," "Very Good Good Average Poor Very Poor," "Overall Score," "the 17 metrics," "metric sections," "auto-build sections," "metric versioning," "Effort metric," "Feeling metric," "Appeal metric," "Usability metric," "AI-derived metrics," "metric isn't showing." Do NOT use when the question is about picking a section type (use `helio-section-types`), the AI heuristic evaluator (use `helio-design-analysis`), filtering report data (use `helio-report-filtering`), or synthesis (use `helio-reading-report`). For the Glare framework's broader metric taxonomy, use `glare-ux-metrics`.
version: 0.1.0
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

1. Identify what the user wants to measure (a behavior, a feeling, a comprehension level, a recommendation).
2. Pick the metric family (Behavioral or Attitudinal) by whether the user is asking about what people *did* or how they *felt*.
3. Pick the specific metric within that family by what it captures.
4. Surface the required section structure (1 section, 2 sections, or 3 sections — some metrics like Brand Score need composite setups).
5. Name the threshold label the user should expect / target.
6. Flag versioning gotchas (especially Desirability v1 vs v2 — they coexist; confirm which is active before comparing across studies).
7. Note the AI-derived metric caveat: Design Analysis scores use the same metric names but live in a separate data structure as labels only (no numeric 0–100).

## What's new in v0.1.0

Initial release. Sourced from UX Metrics v0.1. AEO scorecard flagged a Problem-opener gap — addressed in the ADDED section of `reference.md`.

## Handoffs

- For **section types** that get tagged with these metrics, use `helio-section-types`.
- For **the AI heuristic evaluator** that scores against the same metrics from an AI source, use `helio-design-analysis`.
- For **filtering the report** (segments, demographics, sentiment, response time), use `helio-report-filtering`.
- For **synthesis and signal-writing** using these scores, use `helio-reading-report`.
- For **Glare's broader UX Metrics framework** (all four families, including Performance and Intelligence), use `glare-ux-metrics`.

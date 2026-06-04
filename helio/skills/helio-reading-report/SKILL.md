---
name: helio-reading-report
description: Use this skill when the user is reading a Helio report and turning it into a Glare signal — the synthesis workflow plus the conceptual bridge to Glare. Triggers — "read a Helio report," "synthesize Helio results," "one-sentence signal," "cross-metric divergence," "30-second scan," "headline reading," "Direct Indirect Failed," "Overall Score caveat," "decisive vs inconclusive," "call the test," "Glare signal," "behavior metric context direction," "Design Review handoff," "Decision Map placement," "Measure Focus Lead," "next hunch," "hunch vs risk frame," "Behavioral vs Attitudinal divergence," "spot red flags." Do NOT use when the user wants per-metric definitions (use `helio-ux-metrics`), section type details (use `helio-section-types`), filter mechanics (use `helio-report-filtering`), or finding capture (use `helio-findings`). For the broader Glare framework, use `glare-getting-started`.
version: 0.1.0
source_doc_version: Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2 (merged)
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1XfSMQbJRw7s6H9Gjct6dWQunmwf7IVuhiC_1LpSySgM
    title: Reading a Helio Report (Drive has v0.1; skill uses v0.2 content from local Glare Skills folder)
    drive_url: https://docs.google.com/document/d/1XfSMQbJRw7s6H9Gjct6dWQunmwf7IVuhiC_1LpSySgM/edit
    last_synced: 2026-05-23
  - doc_id: 1TH6KgDxnwtW56FwVAikvDcyaUBRjWlos8lopL9mrEwU
    title: From Helio Test to Glare Signal (Drive has v0.1; skill uses v0.2 content from local Glare Skills folder)
    drive_url: https://docs.google.com/document/d/1TH6KgDxnwtW56FwVAikvDcyaUBRjWlos8lopL9mrEwU/edit
    last_synced: 2026-05-23
---

You are helping the user **read a Helio report and turn it into a Glare signal** — both the mechanical synthesis (scan → headline → divergence → open text → compare → red flags → one-sentence signal) and the conceptual bridge to where that signal goes (Design Review, Decision Map, next hunch).

## Core idea

A Helio test produces a report. A report isn't a signal — it's the raw material a signal is built from. This skill covers two halves of the same conversation:

**Mechanical synthesis** — the cognitive work of going from a report to a one-sentence signal:

1. **30-second scan** — test name → intro → audience → section/asset count → UX metrics tagged
2. **Read the headline** — Helio's consistent 5-tier scheme (90+ Very Good, 70–89 Good, 50–69 Average, 30–49 Poor, <30 Very Poor)
3. **Read for divergence** — cross-metric, cross-audience, cross-iteration, stated-vs-behavioral
4. **Read the open text** — Common Phrases entry, then individual responses paired with the rating they explain
5. **Compare** — against the hunch, baseline, prior iteration, other audiences
6. **Spot red flags** — Poor / Very Poor on any metric, especially Success / Comprehension / Intent gap
7. **Synthesize to one sentence** — behavior + metric + context + direction
8. **Call the test** — decisive / inconclusive / re-test

**Conceptual bridge to Glare** — what the signal IS and where it goes:

- Glare's 4-piece signal definition (behavior + metric + context + direction)
- Helio implements 2 of Glare's 4 metric families (Behavioral + Attitudinal; not Performance or Intelligence)
- Where signals go: Design Review (Ground step) → Decision Map (Measure → Focus → Lead) → next hunch
- Hunches and risks are the same anchor in two voices

## Files to read

Read `reference.md` for the full surface — two DERIVED blocks (Reading + Glare Signal), each with worked examples, threshold tables, divergence patterns, and the metric mapping across all 17 Helio metrics.

## How to apply

1. If the user is mid-report, walk the synthesis chain: scan → headline → divergence → followups → compare → red flags → one-sentence signal.
2. Surface the threshold scheme (5-tier consistent across all 17 metrics).
3. Watch for the most diagnostic patterns: cross-metric divergence (especially Behavioral high + Intent low = "attractive but not persuasive"), audience spread of 20+ points, Success < 30 = invisible affordance.
4. For the one-sentence signal, walk the template: [audience/context] [behavior or reaction with metric+label] [context from followups] — suggesting [interpretation], and the next iteration should [direction].
5. For the "what happens next" question, surface the three landings: Design Review (Ground step), Decision Map (Measure/Focus/Lead), next hunch.
6. Be explicit about Performance / Intelligence — Glare concepts not implemented in Helio. If a decision needs those, source from analytics or AI eval tooling instead.
7. For "call the test," surface the three honest reads: decisive, inconclusive, re-test. Inconclusive is the hardest call to make.

## What's new in v0.1.0

Initial release. Merges Reading a Helio Report v0.2 and From Helio Test to Glare Signal v0.2 into a single skill. Source docs in Drive are still at v0.1; this skill reflects the v0.2 corrections (real Helio vocabulary, correct family assignments, marked illustrative examples).

## Handoffs

- For **per-metric definitions and threshold scheme**, use `helio-ux-metrics`.
- For **filter mechanics that synthesis depends on**, use `helio-report-filtering`.
- For **capturing synthesis-grade observations as Findings**, use `helio-findings`.
- For **the broader Glare framework** (Design Review SIGNAL, Decision Map facets, framework site), use `glare-getting-started`, `glare-design-review`, `glare-decision-map`.
- For **test design** that produces a synthesizable report, use `helio-asset-to-test`.
- For **the test shape patterns** the synthesis recognizes, use `helio-patterns`.
- For **engineering-side details** (Glare metrics gem, etc.), use `helio-features`.

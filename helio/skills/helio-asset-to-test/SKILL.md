---
name: helio-asset-to-test
description: Use this skill when the user is going from a design (screenshot, mockup, prototype) to a launched Helio test — building the test, validating it, and sending it. Triggers — "how do I build a test," "from asset to test," "set up a Helio test," "what test should I run," "test build workflow," "validate before launch," "dry-run a test," "how do I structure my questions," "Signal Blitz worked example," "pre-launch checklist," "naming the risk," "picking a template," "audience for my test," "questions JSON," "send test." Do NOT use when the user wants section type depth (use `helio-section-types`), metric attachment specifics (use `helio-ux-metrics`), audience setup specifics (use `helio-audience-flow`), or branching configuration (use `helio-branching`). For reading the resulting report, use `helio-reading-report`. For recognizing test shapes by pattern, use `helio-patterns`.
version: 0.2.2
source_doc_version: From Asset To Test v0.2
last_rebuilt: 2026-07-21

sources:
  - doc_id: 1W6jPyH2ex7PkcpvycSzHMwLBr_3DAc4CqQHzYgISEYs
    title: From Asset To Test v0.2
    drive_url: https://docs.google.com/document/d/1W6jPyH2ex7PkcpvycSzHMwLBr_3DAc4CqQHzYgISEYs/edit
    last_synced: 2026-05-23
---

You are helping the user run the **From Asset To Test** workflow — taking a design and turning it into a launched Helio study, in seven steps.

## Core idea

Going from a design (screenshot, mockup, prototype) to a launched Helio test follows a seven-step arc, roughly 35 minutes total once you've done it a few times:

1. **Classify the asset** (1 min) — single screen or multi-screen, what kind of page, B2C or B2B, primary outcome
2. **Name the testable risk** (5 min) — riskiest assumption, mapped to a question type
3. **Pick a template** (30 sec) — one of T1–T7 in `helio-patterns`; the template names your metric set
4. **Define the audience** (5 min) — single segment or fanout, prebuilt or custom list
5. **Tag the metrics** (2 min) — `--ux-metrics`; Helio builds those sections with validated wording
6. **Customize** (12 min) — tune the generated wording, add only what no metric builds
7. **Build, validate, launch** (10 min) — `helio-cli tests create` + `assets upload`, validate + send

The step most often skipped is **Step 2 — name the testable risk**. It's also the one that distinguishes a useful test from a templated one. If you can't name the risk, you'll get a report with no decisive finding.

**Metrics before questions.** Steps 5 and 6 are in this order deliberately: a tagged metric returns a 0–100 score with a threshold label, comparable across waves and rolled into the Overall Score, while a hand-written look-alike returns only an answer distribution. Hand-write what no metric covers — never a near-copy of one.

## Files to read

Read `reference.md` for the full seven-step walkthrough, the worked Signal Blitz example, the pre-launch checklist, and what the workflow doesn't yet cover. Capability boundaries are version-dependent — confirm with `helio-cli update --check` before telling a user something can't be done.

## How to apply

1. Start by classifying the asset (single screen vs flow, page type, B2C/B2B, primary outcome). This sets up everything downstream.
2. Force the testable risk discussion. If the user can't name a risk, surface that gap — testing without a risk produces "interesting findings" not decisions.
3. Match the risk to one of the canonical T1–T7 templates in `helio-patterns` — the template names the metric set, so this is also how the metrics get chosen. Use the decision tree in the reference.
4. Walk through audience selection — prebuilt segment vs custom list vs fanout — using `helio-audience-flow` for depth.
5. **Tag the template's metrics first** (`--ux-metrics`) and let Helio build those sections with validated wording. A hand-written look-alike returns a distribution, not a scored, wave-comparable metric — see `helio-ux-metrics`.
6. Then customize: add what no metric builds (click tests, MaxDiff, risk-specific questions), and tune the generated wording in place with `edit-question` (omit `--type` to keep the metric attached). Use `helio-section-types` for section depth.
7. Walk the user through validation: `helio-cli tests validate`, dry-run, preview/walkthrough. Don't `send` until validate passes clean — and check the journey reads as one conversation (`helio-test-review` for a full pre-launch review).

## What's new in v0.2.2

Synced to helio-cli v0.7.0: every metric in the T1–T7 sets is CLI-taggable, so the Step 3 metric-tag caveat becomes a hotspots reminder for click-backed metrics; the same-metric-twice note in Step 5 drops the web-app workaround (repeating a type is supported).

## What's new in v0.2.1

**Correction to v0.2.0.** Clarified the click-test split wherever it appeared: the section is CLI-creatable since v0.4.0, but `engagement` / `success` metric tags are still API-rejected. Added a metric-tag caveat under the Step 3 template tree, since the templates' declared sets include those two.

## What's new in v0.1.0

Initial release. Sourced from From Asset To Test v0.1. AEO scorecard flagged a Problem-opener gap — addressed in the ADDED section of `reference.md`.

`agent-operations.md` is **not** built for v0.1.0. The workflow has a natural runtime contract (the 7-step arc, the pre-launch checklist), but no clear escalation triggers or output schema that need promotion yet. Surface to user during v0.2+ if a real runtime contract emerges.

## What's new in v0.1.1

Image asset upload left the UI-only list (helio-cli v0.1.1 `assets upload`, `--asset-id`); Step 7 no longer needs a web-app detour for image-based tests. Hotspots, branching, and video/audio upload remain UI-only.

## What's new in v0.2.0

Metrics-first restructure. Step 3 now routes to the canonical **T1–T7 templates in `helio-patterns`** (retiring the parallel R5/R3/Core-5-Q vocabulary that diverged from it), and each template names the metric set it measures — so picking the template is how you pick the metrics. Old steps 5 and 6 swapped: **tag the metrics first** and let them build validated sections, then customize wording and add only what no metric covers. The Signal Blitz worked example was rebuilt to match (it previously modelled a hand-built `questions.json` using legacy `enable_followup`/`followup_question` keys that helio-cli now rejects). Pre-launch checklist gains metric-coverage and context-noun checks; capability boundaries now carry a version-check instruction.

## Handoffs

- For **section type depth** during step 6 (customization), use `helio-section-types`.
- For **picking the UX Metric** during steps 3 and 5, use `helio-ux-metrics`.
- For **audience configuration depth** during step 4, use `helio-audience-flow`.
- For **branching setup** (if the test uses conditional routing), use `helio-branching`.
- For **asset handling specifics** (image upload, Figma integration, hotspot drawing), use `helio-assets`.
- For **recognizing test shapes by pattern**, use `helio-patterns`.
- For **designing a test from a hunch** (no asset yet — the hunch → shape → test → signal arc, with templates), use `helio-creating-test`.
- For **reading the resulting report**, use `helio-reading-report`.
- For **the CLI commands referenced in step 7**, use `helio-cli`.
- For **screening at step 5** (formal Customer List screeners or inline screening at the top of the study), use `helio-forms-screeners`.
- For **the account → project → test data model**, use `helio-concepts`.

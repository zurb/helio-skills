---
name: helio-creating-test
description: Use this skill when the user wants to design a Helio test end to end — from a hunch to a launched test that produces a decision-grade signal. Triggers — "create a Helio test," "design a test," "turn this hunch into a test," "which test shape," "test template," "marketing page eval," "multi-screen flow eval," "content prioritization," "concept comparison," "hunch → shape → test → signal," "required followups," "bias check," "pre-launch checklist," "how many questions," "MaxDiff shows 0%," "one hunch per test," "web app vs CLI vs MCP." Also use when a test produced "interesting findings" but no decision, or the user starts from a belief rather than an asset. Do NOT use when the user starts from an existing asset/mockup (use `helio-asset-to-test`), wants shape recognition across past tests (use `helio-patterns`), section spec (use `helio-section-types`), audience mechanics (use `helio-audience-flow`), launch commands (use `helio-cli` / `helio-mcp`), or report synthesis (use `helio-reading-report`).
version: 0.1.2
source_doc_version: Creating a Helio Test v0.1
last_rebuilt: 2026-07-06

sources:
  - doc_id: src-creating-a-helio-test-v0.1
    title: Creating a Helio Test v0.1
    last_synced: 2026-07-06
---

You are helping the user **design a Helio test that produces a signal worth using** — one a designer, a PM, or a leader can carry into a Design Review and act on. Not just "ran a study."

## Core idea

Every good Helio test runs the same arc — **Hunch → Shape → Test → Signal** — and each step constrains the next. Skip the hunch and you can't write the right questions. Pick the wrong shape and you collect the wrong metrics. Don't tie the signal back to a hunch and the result has nowhere to land.

The working parts:

1. **Four house shapes** — marketing page eval (5 Qs), multi-screen flow eval (6–8 Qs), content prioritization (5 Qs with MaxDiff), concept comparison — with a decision rule for picking one. If two feel possible, pick the simpler.
2. **The hunch template** — *We believe that [change] for [audience] will [impact] because [reason].* Every question must tie to it; drop questions that don't.
3. **One metric per question**, behavioral + attitudinal paired across the test.
4. **The followup pattern** — required "why" after every Likert and multi-select; optional after click tests. The followups are where the design move lives.
5. **Validate before you spend** — CLI dry-run, web preview, pre-launch checklist (≤ 8 questions, every question metric-tagged, hunch still answerable).
6. **Three ready-to-edit templates** (A: marketing eval, B: multi-screen flow, C: content prioritization) lifted from real Zurb tests.

Surface rule: **person → web app, script → CLI, assistant → MCP.** Test design is the same either way.

## Files to read

Read `reference.md` for the full arc: the four shapes with real examples, the hunch worked example, the metric table (Helio metric → Glare type), audience shaping and sizing, question types/modes/bias checks, the followup pattern, the validation checklist, launch-and-read guidance, the one-sentence signal format, anti-patterns, Templates A/B/C, and the **canonical UI-only boundary checklist** (the seven steps that must happen in the web app, with workarounds and effort estimates — other skills point here for it).

## How to apply

1. Start with the hunch. If the user doesn't have one, draft it for them from what they've said and confirm it. No hunch, no test.
2. Pick the shape with the decision rule (single page → marketing eval; flow → multi-screen; content sections competing → prioritization; two directions → comparison).
3. Instantiate the matching template, filling every bracketed slot ([context], [primary action]) with the user's specifics.
4. Attach one UX metric per question; pair behavioral and attitudinal.
5. Run the bias check (leading / loaded / jargon / forced) on every prompt.
6. Walk the pre-launch checklist; recommend a CLI dry-run before spending.
7. Flag UI-only steps early: click tests, tree tests, prototype tasks, and hotspot drawing can't be built via CLI/MCP.

## What's new in v0.1.2

Added the shapes → T1–T7 cross-reference to `reference.md` (ADDED content): this doc's four conceptual shapes mapped to the Test Pattern Playbook's seven data-backed templates (now in `helio-patterns` v0.3.0), including the four templates this doc's shapes don't cover (Findability Sweep, Expectation Probe, Two-Tap Check, Shelf & NPS) and the stage-trigger layer.

## What's new in v0.1.1

Added the canonical UI-only boundary checklist to `reference.md` (skill-builder ADDED content): the seven web-app-only steps — asset upload, hotspots, click/tree/prototype sections, branching, audience/screener creation, the 7 prototype-dependent UX metrics, scheduled launch — with workarounds and effort estimates. `helio-assets`, `helio-branching`, and `helio-asset-to-test` now point here instead of carrying divergent partial lists.

## What's new in v0.1.0

Initial release. Sourced from Creating a Helio Test v0.1. Customer names in the source scrubbed to category descriptors during the build (v0.3.2 pattern). This skill is the design-first hub for test creation; `helio-asset-to-test` remains the asset-first walkthrough.

## Handoffs

- For the **asset-first build walkthrough** (you have a mockup, need a test), use `helio-asset-to-test`.
- For **recognizing shapes across real past tests** and the **seven data-backed templates with stage triggers** (T1–T7: which template at first look vs iterate vs benchmark), use `helio-patterns`.
- For **section type spec**, use `helio-section-types`.
- For **UX metric definitions and scoring**, use `helio-ux-metrics`.
- For **audience setup mechanics**, use `helio-audience-flow`.
- For **screening participants**, use `helio-forms-screeners`.
- For **branching configuration**, use `helio-branching`.
- For **launching via terminal**, use `helio-cli`; **via AI assistant**, use `helio-mcp`.
- For **reading the report and writing the signal**, use `helio-reading-report`.

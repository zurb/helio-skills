---
name: helio-creating-test
description: Use this skill when the user wants to design a Helio test end to end — from a hunch to a launched test that produces a decision-grade signal. Triggers — "create a Helio test," "design a test," "turn this hunch into a test," "which test shape," "test template," "marketing page eval," "multi-screen flow eval," "content prioritization," "concept comparison," "hunch → shape → test → signal," "required followups," "bias check," "pre-launch checklist," "how many questions," "MaxDiff shows 0%," "one hunch per test," "web app vs CLI vs MCP." Also use when a test produced "interesting findings" but no decision, or the user starts from a belief rather than an asset. Do NOT use when the user starts from an existing asset/mockup (use `helio-asset-to-test`), wants shape recognition across past tests (use `helio-patterns`), section spec (use `helio-section-types`), audience mechanics (use `helio-audience-flow`), launch commands (use `helio-cli` / `helio-mcp`), or report synthesis (use `helio-reading-report`).
version: 0.3.0
source_doc_version: Creating a Helio Test v0.2
last_rebuilt: 2026-07-23

sources:
  - doc_id: 13tZ1UE38PNTmDClkRD51OYgNXps7uszGLHJaIi7qrPQ
    title: Creating a Helio Test v0.2
    drive_url: https://docs.google.com/document/d/13tZ1UE38PNTmDClkRD51OYgNXps7uszGLHJaIi7qrPQ/edit
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

Read `reference.md` for the full arc: the four shapes with real examples, the hunch worked example, the metric table (Helio metric → Glare type), audience shaping and sizing, question types/modes/bias checks, the followup pattern, the validation checklist, launch-and-read guidance, the one-sentence signal format, anti-patterns, Templates A/B/C, and the **canonical surface-boundary guidance** (which parts of a test still need the web app, stated by kind rather than by list — other skills point here for it, and it defers to the tool for anything version-dependent).

## How to apply

1. Start with the hunch. If the user doesn't have one, draft it for them from what they've said and confirm it. No hunch, no test.
2. **Check the project's history before designing fresh.** Projects reuse structures over time — pull the project's recent tests (`helio-cli projects list` → project tests → `tests preview`) and mirror the house structure; if a past test is close, `tests clone` it and edit the copy (clone also carries branching and the audience, neither of which can be built via CLI). Use `helio-patterns` for shape recognition across those past tests.
3. Pick the shape with the decision rule (single page → marketing eval; flow → multi-screen; content sections competing → prioritization; two directions → comparison).
4. **Draft in text first, then hand to the CLI.** Write the full test as a reviewable draft — hunch, shape, questions with types and metric tags — get the human yes, then convert to the CLI's JSON payload — `tests create --questions @draft.json --dry-run` validates the file without spending. Iterating on prose is cheaper than iterating on a created draft, and the review catches bias before anything exists in Helio.
5. Instantiate the matching template, filling every bracketed slot ([context], [primary action]) with the user's specifics.
6. Attach one UX metric per question; pair behavioral and attitudinal.
7. Run the bias check (leading / loaded / jargon / forced) on every prompt.
8. Walk the pre-launch checklist; recommend a CLI dry-run before spending.
9. Flag UI-only steps early — as of helio-cli v0.7.0: video/audio upload, tree/prototype tasks, audience creation, and the `completion` / `effort` metrics. Click tests, hotspots, and multiple_choice branching went CLI-native in v0.4.0; the click-backed metrics, `brand_score`, and repeated metric types in v0.7.0. Check `helio-cli update --check` before repeating an older ceiling.

## What's new in v0.3.0

Canonical UI-only checklist synced to helio-cli v0.7.0. Five metrics left the non-creatable row — `engagement`, `success`, `usability`, `satisfaction`, `brand_score` — leaving only `completion` and `effort`, each excluded for a specific reason (built from a Figma prototype section the API can't create). The duplicate-metric row is gone entirely: repeating a type is supported. The no-longer-UI-only note now covers repeated metric types and read-back of audience/branching/hotspots. Version stamp updated, with the tally: three rows left this list in v0.4.0 and four more in v0.7.0.

## What's new in v0.2.3

*(Superseded by v0.3.0 — `engagement` and `success` became creatable in helio-cli v0.7.0.)* **Correction to v0.2.2.** The UI-only checklist wrongly dropped `engagement` and `success` from the non-creatable-metrics row on the reasoning that click tests became CLI-creatable in v0.4.0. Verified against the API: the *section* is creatable, the *metric tag* is not — `create` and `add-ux-metrics` both reject them ("requires click tests or prototypes and cannot be created via the API"). All seven remain non-creatable; the row now states the section-vs-tag split explicitly.

## What's new in v0.2.2

Canonical UI-only boundary checklist corrected against shipped CLI v0.4.0–v0.6.0: click tests, hotspot definition, and single-select multiple_choice branching left the list (CLI-native since v0.4.0), as did `engagement` and `success` from the prototype-dependent metric row. Added the duplicate-metric-instance row. The table now carries a version stamp and a "this boundary moves — run `update --check`" instruction, since three rows left it after being documented as permanent.

## What's new in v0.2.1

Templates section now says how to build a template: tag its named metrics first, adjust the generated wording in place with `edit-question`, hand-build only click tests / MaxDiff / risk-specific slots. The listed prompts are house wording to aim for, not payloads to paste.

## What's new in v0.2.0

Two workflow steps added to "How to apply" from Benjamin's 2026-07-23 dogfooding feedback: (1) check the project's recent tests before designing fresh — mirror the house structure or `tests clone` the closest match (the only scripted route to branching + audience reuse); (2) draft the test in reviewable text first, get the human yes, then convert to the CLI JSON payload.

## What's new in v0.2.0

Added "The journey must read as one conversation" to the preview step in `reference.md`, plus a matching pre-launch checklist item. Three concrete checks, born from a real walkthrough that failed all three: no duplicate questions from metric stacking (sentiment + desirability, appeal + reaction), the context noun read aloud in every generated sentence, and understanding-before-evaluation ordering (`tests reorder` fixes sequence without rebuilding). Companion caveat lives in `helio-ux-metrics` v0.2.1.

## What's new in v0.1.4

Added the metrics-first rule of thumb to "Pick UX metrics" in `reference.md`: let the metric auto-build its section when it can — hand-written prompts must earn their custom wording; near-copies of a metric's question should be a tag plus a context noun (they otherwise produce distributions, not scores). Part of the metrics-first framing pass (see `helio-ux-metrics` v0.2.0).

## What's new in v0.1.3

UI-only boundary checklist updated for helio-cli v0.1.1: image asset upload left the list (`assets upload/list/get`, `--asset-id`); the row now covers video/audio upload only. MCP still has no asset tools.

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

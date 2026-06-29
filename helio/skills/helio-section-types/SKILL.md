---
name: helio-section-types
description: Use this skill when the user is working with section types in Helio — picking which section to use for a question, configuring sections, or understanding what each captures. Triggers — "what section type," "click test," "prototype test," "likert," "MaxDiff," "card sort," "tree test," "matrix," "preference," "rank," "free response," "point allocation," "NPS section," "free response followup," "conditional follow-ups," "what's the difference between," "how do I configure a section," "section won't validate," "hotspots," "Figma prototype." Do NOT use when the question is about which UX metric to attach (use `helio-ux-metrics`), how to build a whole test end to end (use `helio-asset-to-test`), conditional routing between sections (use `helio-branching`), or the AI heuristic evaluator (use `helio-design-analysis`). For test shapes that combine sections, use `helio-patterns`.
version: 0.1.0
source_doc_version: Section Types v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 165DVFQskrAuCBgYItH0Oz_IxZO3GPHupIFrZZvAyJGs
    title: Section Types v0.1
    drive_url: https://docs.google.com/document/d/165DVFQskrAuCBgYItH0Oz_IxZO3GPHupIFrZZvAyJGs/edit
    last_synced: 2026-05-23
---

You are helping the user pick, configure, or troubleshoot **section types** in Helio — the building blocks of every Helio study.

## Core idea

Helio sections are grouped by purpose. There are 14 section types Helio researchers can add to a study, plus one separate workflow (Design Analysis) that isn't a section but lives alongside.

**Choice-based — what people pick:** Multiple Choice, Preference, Rank, Point Allocation, MaxDiff
**Open text — what people say:** Free Response, Free Response Followup, Conditional Follow-ups
**Scales — what people feel and judge:** Likert, Numerical Scale (NPS), Matrix
**Usability — what people do:** Prototype Test, Click Test, Tree Test
**Information architecture:** Card Sort
**AI heuristic evaluation:** Design Analysis (separate workflow, not part of test-create)

Picking the right section type is the highest-leverage decision in test design. Teams that default to Multiple Choice + Likert for everything miss the moves (MaxDiff for content, Tree Test for IA, Prototype Test for flows) that would actually surface the signal they're looking for.

## Files to read

Read `reference.md` for the full per-section spec — setup options, participant experience, report views, when to reach for each, and the cross-cutting notes on multivariate support, UX Metric pairings, and branching.

## How to apply

1. Identify what the user wants to learn (what choice / what behavior / what reaction).
2. Match the question shape to the section type group (choice-based / open text / scales / usability / IA).
3. Within the group, pick by what the section *outputs* — preference frequency, ranked importance, win/loss, click coordinates, etc.
4. Surface the configuration knobs the user will hit (variation count limits, randomization, branching support, sentiment tagging).
5. Name the UX Metric pairings that auto-build the right section structure (e.g., tagging a section with Brand Score auto-creates the 3-section template).
6. Flag known limits — partial ranking isn't supported, multi-select branching isn't supported, etc.

## What's new in v0.1.0

Initial release. Sourced from Section Types v0.1. AEO scorecard flagged two minor gaps (Problem opener; Action pointer) — both addressed in the ADDED sections of `reference.md`.

## Handoffs

- For **picking which UX metric to attach to a section**, use `helio-ux-metrics`.
- For **the full build/validate/launch workflow**, use `helio-asset-to-test`.
- For **conditional routing between sections** (jump-to-section, end-the-test, redirect), use `helio-branching`.
- For **the AI heuristic evaluator** (a separate workflow), use `helio-design-analysis`.
- For **recognizing test shapes that combine sections** (the core 5-Q template, multi-screen flows, MaxDiff content variants), use `helio-patterns`.
- For **asset handling** (uploading images, Figma integration), use `helio-assets`.

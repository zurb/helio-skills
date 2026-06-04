---
name: helio-design-analysis
description: Use this skill when the user is running or interpreting Helio's AI heuristic evaluation — Design Analysis. Triggers — "Design Analysis," "Helio AI evaluation," "AI heuristic," "Feel Understand Do Trust," "four master user needs," "AI score 1-5," "annotated screenshot," "design analysis cost," "AI evaluator," "evaluate without participants," "headline AI scores," "design analysis pipeline," "AI scoring without users," "design critique AI." Do NOT use when the user wants participant-driven UX metrics (use `helio-ux-metrics`), the AI Audience for synthetic participant responses (use `helio-audience-flow`), or the broader test build (use `helio-asset-to-test`).
version: 0.1.0
source_doc_version: Design Analysis v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1bYfLuQqxIYYf5OBzWXskhqpndNXK4rkc-STc-8j1SMU
    title: Design Analysis v0.1
    drive_url: https://docs.google.com/document/d/1bYfLuQqxIYYf5OBzWXskhqpndNXK4rkc-STc-8j1SMU/edit
    last_synced: 2026-05-23
---

You are helping the user run or interpret **Design Analysis** — Helio's AI-powered heuristic evaluation of a design or prototype.

## Core idea

Design Analysis is a separate workflow from regular Helio studies. You don't add a Design Analysis section to a test — it's a different entry point with its own UI, data model, and report. Every score, observation, and suggestion comes from an AI model evaluating the design against UX heuristics. No participants.

Every Design Analysis evaluates against four **master user needs**, each backed by a weighted bundle of UX metrics:

1. **Feel** — Appeal (40%) + Desirability (40%) + Feeling (20%) — emotional response, aesthetic draw
2. **Understand** — Comprehension (40%) + Expectations (25%) + Usefulness (25%) + Usability (10%) — clarity, learnability
3. **Do** — Success (33%) + Completion (33%) + Intent (17%) + Effort (17%) — task feasibility, friction
4. **Trust** — Sentiment (30%) + Expectations (25%) + Usefulness (25%) + Loyalty (20%) — credibility, perceived reliability

Cost: flat **4 answers per analysis**, regardless of design size or AI usage.

When to use: heuristic sanity check before participant tests, quick design critique, comparing iterations (v1 vs v2) or competitors. **Not a replacement for user testing** — AI can flag heuristic issues but can't tell you whether real users will struggle, succeed, or convert.

## Files to read

Read `reference.md` for the full setup, the four user needs (with backing metric weights), the pipeline phases, the output (scores, explanations, annotations, follow-up questions), sharing, cost details, plan gates, and the architectural notes (separate metric storage, fixed metric mapping, AI usage characteristics).

## How to apply

1. Confirm the user wants the AI evaluator (not the AI Audience, which is synthetic-participant responses).
2. Walk through setup: design input (image upload / image URL / website URL / library asset) + context (ideal user, demographics, goal, concept).
3. Surface the four user-need lenses — Feel, Understand, Do, Trust — and which metrics back each.
4. Set expectations: ~1 minute runtime, the result is one-shot (no iterative refine).
5. Surface the headline architectural caveats: AI scores live in a separate data structure (don't mix with participant scores), stored as labels only (not numeric 0–100), and tied to a Design Analysis report (not a regular study).
6. For follow-up questions the AI suggests, note they don't auto-convert to a real study — researcher manually creates one.
7. Cost: 4 answers regardless of complexity — only place in Helio where cost is fixed.

## What's new in v0.1.0

Initial release. Sourced from Design Analysis v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **participant-driven UX metrics** (the same metric names, but scored from real responses), use `helio-ux-metrics`.
- For **the AI Audience** (synthetic participant responses, different feature), use `helio-audience-flow`.
- For **building a real study from AI-suggested follow-up questions**, use `helio-asset-to-test`.
- For **interpreting AI-derived metrics during synthesis**, use `helio-reading-report` (with the "don't blend AI and participant scores" caveat).
- For **cost details**, use `helio-licensing`.
- For **broader feature gating and plan tier**, use `helio-features`.

---
name: helio-licensing
description: Use this skill when the user is working with Helio's billing — answers, plan tiers, license refills, refund rules, follow-up costs, AI Audience cost. Triggers — "Helio answers," "what's an answer," "answers cost," "5 sections × 100 = 500 answers," "Pro tier," "Business tier," "Scale tier," "Design Analysis 4 answers," "follow-up costs," "Customer List pre-charge," "bounce refund," "flagged response refund," "AI Audience cost," "annual refills," "answers balance," "answers remaining," "monthly refills," "Helio billing," "license tier." Do NOT use when the user wants the marketing-facing plan tour (use `helio-app`), audience setup (use `helio-audience-flow`), or what features each plan tier unlocks (use `helio-features`).
version: 0.1.0
source_doc_version: Answers & Licensing v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1Z21r50fYUx31NDLzLLwnOVmho6G6NrqMS279Jl4i5WI
    title: Answers & Licensing v0.1
    drive_url: https://docs.google.com/document/d/1Z21r50fYUx31NDLzLLwnOVmho6G6NrqMS279Jl4i5WI/edit
    last_synced: 2026-05-23
---

You are helping the user understand **Helio's billing model** — the answers unit, license tiers, refund rules, and how cost scales with test complexity.

## Core idea

The unit of consumption in Helio is the **answer**. One answer = one section response.

This is the most-miscalculated part of Helio. A 100-participant quota on a 5-section study isn't 100 answers — it's **500 answers** (100 × 5).

Every Helio account has a **License** with an answers limit. As you use answers, the balance counts down. The balance you see in the UI is what's left.

License plan types (internal, distinct from the marketing-facing plans):

- **Trial** — limited test answers
- **Pro tier (legacy)** — flat self-serve plan
- **Business tiers 1–3** — 1,000 / 2,000 / 3,000 answers/month
- **Scale tiers** — 5,000 / 10,000 answers/month
- **Design / Agency / Enterprise** — custom, typically invoiced
- **Custom** — one-off configurations

Annual subscriptions get monthly refills (no rollover). Monthly subscriptions renew through the billing provider.

Non-obvious costs to track:

- **Moderated follow-up:** 10 answers per follow-up sent (refunded if unanswered after 3 days)
- **Design Analysis:** flat 4 answers per analysis (not per-section)
- **AI Audience:** 1 answer per section per persona response (same as a real participant)
- **Customer List:** pre-charged at email send; bounces don't auto-refund

## Files to read

Read `reference.md` for the full billing model — answer definition, license tiers, action-by-action cost table, refund rules (what does and doesn't refund), refill mechanics, the audit trail, and known issues.

## How to apply

1. Walk the user through the answer math first: participants × sections = total answers needed.
2. For non-standard actions (follow-ups, Design Analysis, AI Audience), surface the specific cost rule.
3. For refund questions: confirm whether the case auto-refunds (timeouts, cleanup), requires admin (flagged/spam/deleted/bounces), or doesn't refund at all.
4. For annual subscribers, surface the no-rollover rule on monthly refills.
5. For plan-tier confusion, surface the distinction between marketing-facing plans (Pilot/Scale/On Demand/Business) and internal license tiers — both are valid, they describe different things.
6. For "missing feature" questions, route to `helio-features` for the actual feature gates.

## What's new in v0.1.0

Initial release. Sourced from Answers & Licensing v0.1. AEO scorecard flagged Problem and Action gaps — both addressed in the ADDED sections.

## Handoffs

- For **marketing-facing plans and choosing a plan**, use `helio-app`.
- For **audience setup and per-audience cost**, use `helio-audience-flow`.
- For **engineering-side feature gates** (the flag names that control feature availability), use `helio-features`.
- For **the AI heuristic evaluator's specific cost model** (flat 4 answers), also covered in `helio-design-analysis`.
- For **moderated follow-ups** (the 10-answer cost item), use `helio-section-types` and `helio-findings`.

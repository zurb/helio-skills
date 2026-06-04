---
name: helio-features
description: Use this skill when the user is asking which Helio features are available on their plan, what's gated to Enterprise / Pro / Admin / Beta, or wants the lifecycle-organized inventory of every feature (creating tests, sending, reading reports, account-level). Triggers — "what's available on my plan," "what's gated by plan," "what's beta in Helio," "admin-only feature," "Pro vs Enterprise features," "Helio feature catalog," "Helio feature gates," "what plan tier do I need for X," "section types by plan," "audience options by plan," "report features by plan," "Helio capabilities by tier," "what features exist." Do NOT use when the user wants positioning and plan choice (use `helio-app`), section type spec (use `helio-section-types`), UX metric specifics (use `helio-ux-metrics`), or billing accounting (use `helio-licensing`).
version: 0.2.0
source_doc_version: Helio Features v0.2
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1EiBeoXl0EmzDx_Q--lzdydpA6lbtpfCTZRFU22JmE2I
    title: Helio Features v0.2
    drive_url: https://docs.google.com/document/d/1EiBeoXl0EmzDx_Q--lzdydpA6lbtpfCTZRFU22JmE2I/edit
    last_synced: 2026-05-23
---

You are surfacing the **feature catalog of Helio with plan-tier gating** — organized by the test lifecycle, with [Enterprise] / [Pro] / [Admin] / [Beta] annotations on features that aren't on all plans.

## Core idea

Helio Features is the catalog of what's available in the platform, organized by the lifecycle of a test:

1. **Creating a Test** — section types, configuration, test management
2. **Sending a Test** — audience types and per-audience plan tier
3. **Reading the Report** — per-section visualizations, filters, UX Metrics, Findings, AI features, moderation, sharing & export
4. **Cross-cutting & account-level** — projects, roles, SSO, public API, audit log

Plan-tier annotations attached throughout:

- **[All plans]** — available everywhere
- **[Pro]** — requires Pro tier or higher
- **[Enterprise]** — requires Enterprise tier
- **[Admin]** — restricted to account admins
- **[Beta]** — newer features still being rolled out

If a feature is missing from your account and isn't gated by a tier annotation here, it may be enabled per-account separately. Contact your account manager.

## Files to read

Read `reference.md` for the full lifecycle-organized feature catalog with plan-tier annotations and an Open Questions section listing items still to verify against the live product.

## How to apply

1. Identify whether the user is asking "what features exist" (capability question) or "why can't I see feature X" (gating question).
2. For capability questions, walk through the lifecycle section relevant to their task (Create / Send / Read).
3. For gating questions, surface the tier annotation and route to `helio-licensing` for billing/plan tier mechanics or `helio-app` for plan selection.
4. For features marked [Admin], confirm the user is or has access to an account admin.
5. For features in the Open Questions section, be honest that the source-of-truth status isn't fully confirmed — verify against live product before relying.
6. For deeper functionality questions (how a section type works, how UX metrics are scored, how branching works), route to the appropriate sibling skill.

## What's new in v0.2.0

Cleaned up internal codebase references that shouldn't be public — file paths, internal class names, feature flag names, migration numbers, internal constants. The skill is now focused on the customer-facing feature catalog with plan-tier gating, rather than the engineering-side reference.

## Handoffs

- For **positioning, plans, and plan choice**, use `helio-app`.
- For **billing accounting** (answers, refunds, refills), use `helio-licensing`.
- For **section type details**, use `helio-section-types`.
- For **UX metrics specifics**, use `helio-ux-metrics`.
- For **the AI heuristic evaluator**, use `helio-design-analysis`.
- For **audience setup**, use `helio-audience-flow`.
- For **report filtering**, use `helio-report-filtering`.
- For **Findings details**, use `helio-findings`.
- For **what participants see**, use `helio-participant-experience`.

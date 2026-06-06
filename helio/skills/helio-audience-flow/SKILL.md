---
name: helio-audience-flow
description: Use this skill when the user is configuring how Helio recruits participants for a study — picking an audience type, setting demographics or segments, uploading customer lists, configuring intercept, or running an API audience. Triggers — "audience for my test," "Helio panel," "targeted demographics," "advanced segments," "customer list upload," "intercept survey," "API audience," "AI audience," "AI personas," "how do I send a test," "send test flow," "launch validation," "panelist availability," "audience fanout," "Order More Customer Lists," "audience cost." Do NOT use when the user wants test design (use `helio-asset-to-test`), section types (use `helio-section-types`), or filtering the report after launch (use `helio-report-filtering`).
version: 0.1.0
source_doc_version: Audience Flow v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 17o6U7qrfQC6QASAW8aX4w1L5CbSMiYNH0Wh5sxh5H1k
    title: Audience Flow v0.1
    drive_url: https://docs.google.com/document/d/17o6U7qrfQC6QASAW8aX4w1L5CbSMiYNH0Wh5sxh5H1k/edit
    last_synced: 2026-05-23
---

You are helping the user **send a Helio study to participants** — picking an audience, configuring it, and launching.

## Core idea

When a Helio test is built, the next step is choosing where the responses come from. Eight audience types, each with different targeting, cost, and plan-tier gating:

1. **Open Audience** — shareable link, no targeting (all plans)
2. **Basic Helio Panel** — unfiltered panel access (all plans)
3. **Targeted Demographics** — panel + demographic filters (Pro+)
4. **Advanced Segments** — panel + pre-built behavioral segments (Enterprise)
5. **Customer Lists** — email invites to your own list (Enterprise)
6. **Intercept** — inline survey on your own site (Enterprise)
7. **API Audience** — programmatic submission (Enterprise)
8. **AI Audience** — synthetic responses from AI personas (Enterprise)

The launch flow: pass validation → pick audience → configure → set response count → confirm payment → status flips Draft → Running.

Audience choice is the biggest cost-and-quality lever in a test, and the one teams default on most often (everyone picks Open). This skill exists so the choice gets made deliberately.

## Files to read

Read `reference.md` for the launch flow, validation rules, each audience's setup details and cost model, the after-launch behaviors, and the pricing summary.

## How to apply

1. Identify what the user is doing — launching a new test, swapping audiences post-launch, or troubleshooting a stuck/blocked launch.
2. If launching: walk the validation checks first (required name, audience, at least one section, all assets uploaded, all sections configured).
3. Match the user's situation to the right audience type (panel, list, intercept, etc.).
4. Surface the plan-tier gate for the audience they want.
5. Walk through audience-specific setup (demographics for Targeted, segments for Advanced, CSV upload for Customer Lists, etc.).
6. For Customer Lists, flag pre-charge behavior and bounce/unsubscribe rules — answers are debited at send, not at response.
7. For AI Audience, note the higher per-completion cost (4 answers per section per persona response).
8. Surface post-launch behaviors: tests don't auto-stop at quota; flagged responses don't refund automatically.

## What's new in v0.1.0

Initial release. Sourced from Audience Flow v0.1. AEO scorecard flagged one Problem-opener gap — addressed in the ADDED section.

## Handoffs

- For **the full test-build workflow** (audience is step 4 of 7), use `helio-asset-to-test`.
- For **picking section types** that determine what the audience sees, use `helio-section-types`.
- For **filtering report data after launch**, use `helio-report-filtering`.

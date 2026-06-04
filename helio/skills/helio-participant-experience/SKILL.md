---
name: helio-participant-experience
description: Use this skill when the user is asking what participants actually see and do when they take a Helio study — for IRB / ethics review, customer questions about embedded studies, screening / consent design, accessibility considerations, or drop-off behavior. Triggers — "what do participants see," "Helio take link," "consent in Helio," "screener," "disqualification UX," "Helio accessibility," "WCAG compliance," "participant flow," "intercept iframe," "AI Audience participant," "send to mobile," "carrier charge disclaimer," "Helio thank you screen," "completion redirect," "kiosk mode," "Helio IRB," "ethics review Helio." Do NOT use when the user wants test design (use `helio-asset-to-test`), audience setup mechanics (use `helio-audience-flow`), branching action types (use `helio-branching`), or section type spec (use `helio-section-types`).
version: 0.1.0
source_doc_version: Participant Experience v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1_fpHvnll4epixxGRl3SCWC5HJj3NoaPMPL-PUFUr07w
    title: Participant Experience v0.1
    drive_url: https://docs.google.com/document/d/1_fpHvnll4epixxGRl3SCWC5HJj3NoaPMPL-PUFUr07w/edit
    last_synced: 2026-05-23
---

You are helping the user understand **what participants actually see and do** when they take a Helio study — useful for IRB / ethics review, supporting customer questions about embedded studies, and designing tests with real participant constraints in mind.

## Core idea

Every Helio study has a take link (`/t/{test_id}`). How a participant arrives depends on the audience type — link share, panel invitation email, Customer List email, intercept iframe, API submission, or AI persona.

The participant flow:

1. **Welcome** — intro card (skippable via query param)
2. **Optional screener** — Multiple Choice / Likert / NPS / Free Response questions before the main study; disqualify off wrong answer
3. **Sections** — main study flow, linear by default, branches per researcher config
4. **Demographics** (after sections) — gender, age, education, income, plus audience-specific extras
5. **Thank-you screen** — custom message, optional logo, ~2.5 sec then redirect (or kiosk loop)

Helio's consent model is **accept-by-participation** — opening the link and clicking through is implicit consent. For IRB-style explicit consent, use a Multiple Choice screener at the start with "End test with custom message" for "I do not agree."

Progress saves to `localStorage` — participants can resume if they return to the same link on the same browser.

## Files to read

Read `reference.md` for the full participant journey — arrival paths, welcome / consent / screening, per-section interaction, timers, mobile vs desktop behavior, accessibility considerations, languages, completion / redirect / kiosk, drop-off, disqualification, identity / dedup, branding, intercept specifics, and edge cases.

## How to apply

1. Identify why the user is asking — IRB review, customer question about embed, accessibility audit, or screener design.
2. For IRB: walk the consent model and the screener-as-explicit-consent pattern.
3. For customer/embed questions: surface intercept iframe behavior and postMessage integration.
4. For accessibility: be honest about the limits (custom drag controls aren't keyboard-friendly, WCAG isn't formally certified, no captions/transcripts enforcement).
5. For drop-off / abandonment questions: surface `localStorage` resume behavior and per-section timing capture.
6. For dedup questions: match the audience type to its dedup behavior (panel is strict; Open isn't enforced).
7. For mobile / Send-to-mobile feature: surface the SMS-handoff flow and the carrier-charge disclaimer.

## What's new in v0.1.0

Initial release. Sourced from Participant Experience v0.1. AEO scorecard flagged Problem and Action gaps — both addressed in the ADDED sections.

## Handoffs

- For **screener configuration and disqualification routing**, use `helio-branching`.
- For **section types participants encounter**, use `helio-section-types`.
- For **audience types that determine how participants arrive**, use `helio-audience-flow`.
- For **what test design should consider given participant behavior**, use `helio-asset-to-test`.
- For **broader feature gating and plan tier**, use `helio-features`.

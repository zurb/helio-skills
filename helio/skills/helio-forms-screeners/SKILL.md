---
name: helio-forms-screeners
description: Use this skill when the user is designing screening questions or Forms in Helio — either formal screeners on Customer List signup Forms (up to 5 qualifying questions attached to the participant record for later study targeting), or inline screening at the start of a study (Multiple Choice section + branch to end-of-test). Triggers — "Helio screener," "Helio form," "customer list signup form," "qualification questions," "who qualifies for my study," "screener types," "Multiple Choice screener," "Likert screener," "NPS screener," "Free Response screener," "disqualify at test start," "screener vs demographics," "target study by screener answers," "IRB consent flow," "screener limit 5," "screener can't be deleted." Do NOT use when the user wants audience configuration on an existing Customer List (use `helio-audience-flow`), Multiple Choice section spec in general (use `helio-section-types`), or branching config beyond screening (use `helio-branching`).
version: 0.1.0
source_doc_version: Forms & Screeners v0.1
last_rebuilt: 2026-06-29

sources:
  - doc_id: 1wW2_BSgD_8RNuF3FzFwGyCKNW0xY3MtBfb-0MzjYux4
    title: Forms & Screeners v0.1
    drive_url: https://docs.google.com/document/d/1wW2_BSgD_8RNuF3FzFwGyCKNW0xY3MtBfb-0MzjYux4/edit
    last_synced: 2026-06-29
---

You are helping the user **design screening** in Helio — either formal screeners on Customer List signup Forms, or inline screening at the start of a study.

## Core idea

Two distinct things in Helio carry the word "screener," and they're often confused:

1. **Formal Screeners** — up to 5 qualifying questions attached to a **Form** (Helio-hosted landing page or embeddable modal) that signs people up to a **Customer List**. They capture data on the participant record so future studies can target that list by screener answers.
2. **Inline Screening** — a regular Multiple Choice section at the top of a study, with **branching** configured to route disqualified participants to "end of test with a custom message."

These are different features solving different problems. Formal Screeners build a long-term qualified audience. Inline Screening filters participants for one specific study.

Four formal screener types, each with the same data shape as the corresponding regular section: Multiple Choice, Likert, NPS, Free Response. Maximum 5 per Form. Screeners don't disqualify automatically — every submission still becomes a list member; disqualification happens downstream when you target a subset at study launch.

## Files to read

Read `reference.md` for the full Form-based system — Form config, screener types, what gets captured, how targeting works at launch time, disable-vs-delete rules, and when to use formal screeners vs inline screening.

## How to apply

1. Ask which situation the user is in: building a long-term qualified audience (Formal Screeners) or filtering participants for one study (Inline Screening).
2. If Formal Screeners: walk Form setup — branding, demographics, up to 5 screeners, email verification, opt-in, active/suspended status. Then how to target subsets of the resulting Customer List at study launch.
3. If Inline Screening: walk the Multiple Choice + branch-to-end pattern. Confirm single-select (multi-select branching isn't supported — see `helio-branching`).
4. For IRB / regulated-research consent, surface the inline pattern (Multiple Choice "I agree / I do not agree" with branch on "do not agree").
5. Flag the "screeners don't auto-disqualify" gotcha — every Form submission joins the list; qualifying happens at launch-time targeting.
6. Flag the 5-screener-per-Form hard limit and the disable-vs-delete rule (screeners with responses can only be disabled).

## What's new in v0.1.0

Initial release. Sourced from Forms & Screeners v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **the Customer List audience type** once the list is populated, use `helio-audience-flow`.
- For **branching configuration** (the inline-screening pattern uses the same branch machinery), use `helio-branching`.
- For **Multiple Choice section spec in general**, use `helio-section-types`.
- For **the broader test build workflow** where screening is one of many decisions, use `helio-asset-to-test`.
- For **what participants see** during the screening flow, this skill covers it. For post-screening participant experience, see the broader participant-side content in `helio-concepts`.

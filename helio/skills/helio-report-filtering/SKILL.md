---
name: helio-report-filtering
description: Use this skill when the user is slicing report data — applying demographic, question-level, sentiment, or segment filters; combining filters; or troubleshooting why a filter shows no results. Triggers — "Helio report filter," "demographic filter," "filter by age," "filter by country," "sentiment filter," "question-level filter," "Tree Test filter," "Card Sort filter," "Prototype path filter," "View Flows modal," "Direct Indirect Failed filter," "filter combine AND OR," "URL-persistent filter," "cohort comparison," "clear filters," "no participants match." Do NOT use when the user wants synthesis (use `helio-reading-report`), test design (use `helio-asset-to-test`), or section type spec (use `helio-section-types`).
version: 0.1.0
source_doc_version: Report Filtering v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1s9892SdPp4NeuyZqXclunIYKDawo1qB6S_LZWCGihgg
    title: Report Filtering v0.1
    drive_url: https://docs.google.com/document/d/1s9892SdPp4NeuyZqXclunIYKDawo1qB6S_LZWCGihgg/edit
    last_synced: 2026-05-23
---

You are helping the user **slice data on the Helio report** — applying filters, combining them, and reading the filtered view.

## Core idea

Filters apply to **all questions at once** on the report — set them on the demographic panel or per-question, and the report re-renders with only the matching participants.

Filter combination logic:

- **Across categories: AND** (Female + age 25–34 + answered "Yes" to Q3 = participants who match all three)
- **Within a single category: OR** (Female + Male = anyone of either gender)

Filters are URL-persistent — the filtered view is shareable as a link (URL updates on page load, not on toggle, so refresh before copying).

Filter types:

1. **Demographic filters** (Gender, Age, Country/State/City, Company, Income, Education, Response time, Sentiment, Segment) — sourced from participant data or panel attribute
2. **Question-level filters** — drill into any question and filter by how participants answered
3. **Status filters** (Admin) — Hidden, Flagged, Spam
4. **View Flows modal** (Prototype-specific) — custom screen sequences with Contains / Includes / Exact match modes

Missing data is excluded silently — there's no "unknown" bucket. A country filter excludes participants whose country wasn't captured.

## Files to read

Read `reference.md` for the full filter surface — every filter type, its source, the combine logic, the sentiment-filter specifics (6 languages, Enterprise gate), the View Flows modal for Prototype path filtering, the UI behavior, what's missing today (no saved filter sets, no side-by-side cohort view), and the performance / caching gotchas.

## How to apply

1. Identify the user's filter goal: cohort isolation, drill-down on a specific answer, or audience comparison.
2. Surface the right filter type (demographic, question-level, status, or View Flows for prototype paths).
3. Walk the combine logic (AND across categories, OR within).
4. For sentiment-filter questions, confirm the study has Free Response sections and is on Enterprise tier.
5. For "no participants match" issues, check the missing-data behavior — participants without the filtered demographic are silently excluded.
6. For complex prototype-path filtering, route to the View Flows modal (Contains / Includes / Exact path modes).
7. Surface the URL-persistence quirk (refresh before copying for share).
8. Note the absence of saved filter sets and side-by-side cohort views — both are common requests that don't exist yet.

## What's new in v0.1.0

Initial release. Sourced from Report Filtering v0.1. AEO scorecard flagged Problem and Action gaps — both addressed in the ADDED sections.

## Handoffs

- For **synthesizing filtered data into a Glare signal**, use `helio-reading-report`.
- For **UX metric scores that recompute against filters**, use `helio-ux-metrics`.
- For **demographic capture mechanics** (where the data comes from), use `helio-audience-flow`.
- For **sentiment as captured on Free Response**, use `helio-section-types`.

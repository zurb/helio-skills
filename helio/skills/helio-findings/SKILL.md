---
name: helio-findings
description: Use this skill when the user is capturing or organizing observations from a Helio study — Findings. Triggers — "Helio findings," "capture insight," "share finding URL," "favorite finding," "search findings," "findings panel," "filter context snapshot," "comments vs findings," "AI-generated findings," "moderated follow-up findings cost," "tag findings," "workspace insights," "regenerate share URL." Do NOT use when the user wants synthesis (use `helio-reading-report`), report filtering (use `helio-report-filtering`), or moderated follow-up section configuration (use `helio-section-types`).
version: 0.1.0
source_doc_version: Findings v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 1PouJK0KPyZLxH54j6gntjirCxHXOzF1jupwzPJRX1K4
    title: Findings v0.1
    drive_url: https://docs.google.com/document/d/1PouJK0KPyZLxH54j6gntjirCxHXOzF1jupwzPJRX1K4/edit
    last_synced: 2026-05-23
---

You are helping the user **capture, organize, and share observations** from Helio studies — Findings.

## Core idea

A finding is a captured observation tied to something specific in a study — a section, a variation, a particular response, or the study as a whole. Findings turn raw report data into a synthesized story you can share with stakeholders.

In the UI these are called **Findings**. The terms "finding" and "insight" are used interchangeably across the platform — they refer to the same thing.

Each finding has:

- Text (rich, with formatting and inline references to other findings)
- What it's attached to (study / section / variation / account-level)
- Tags (default: "observation")
- Filter context (snapshotted at capture — remembers the cohort the observation applied to)
- Favorite flag (per user, not shared across team)
- Optional public share URL (no login needed to view)
- Author and timestamp
- Relative ID (friendly per-project sequence number)

**Important status note:** AI-generated findings *aren't actually wired up yet*. The system is currently manual — researchers write findings themselves. AI Summary and Common Phrases are adjacent features that don't store as Findings.

Comments are a separate-but-related concept — discussion threads on a section or finding. A finding is an observation; a comment is a conversation.

## Files to read

Read `reference.md` for the full surface — what gets captured automatically, levels (test / section / variation / account), the AI status caveat, browsing / searching / sorting, favorites, sharing, comments, editing / deletion (soft), filter-context snapshot behavior, and limits.

## How to apply

1. Identify the level the finding should attach to (whole study, specific section, specific variation, or account workspace).
2. Walk the capture flow: open the Findings panel, write the rich text, optionally attach an image / tag / favorite, optionally enable share URL.
3. Surface the filter-context snapshot — finding remembers the filters active at capture but doesn't auto-reapply them on later views.
4. For team collaboration questions, distinguish findings (observations to capture / share) from comments (discussions threads, with @-mentions and resolve).
5. For "AI didn't auto-generate findings" questions, be honest: the infrastructure exists but auto-generation isn't shipping yet. AI Summary and Common Phrases are different features.
6. For bulk export, note the API is the path — no CSV export of findings yet.

## What's new in v0.1.0

Initial release. Sourced from Findings v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **synthesizing findings into a one-sentence Glare signal**, use `helio-reading-report`.
- For **the moderated follow-up workflow** (the "Free Response Followup" section type, which is researcher-initiated and creates linked responses), use `helio-section-types`.
- For **filter context that gets snapshotted onto findings**, use `helio-report-filtering`.
- For **AI Chat / AI Summary / Common Phrases** (adjacent AI features that don't store as Findings), use `helio-features`.
- For **broader feature gating and plan tier**, use `helio-features`.

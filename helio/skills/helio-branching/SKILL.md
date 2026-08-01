---
name: helio-branching
description: Use this skill when the user is configuring conditional routing in a Helio study — branching participants based on their answers, screening / disqualifying, redirecting at end-of-test, or troubleshooting why a branch isn't firing. Triggers — "Helio branching," "conditional routing," "screener," "disqualify participants," "jump to section," "end test with custom message," "redirect URL after test," "branching from a choice," "branching on best/worst answer," "hotspot branching," "Branching and quotas," "Branching and UX metrics," "Branching and Conditional Follow-ups," "Why is my branch not firing," "multi-select branching." Do NOT use when the user wants conditional follow-ups inline (those live in `helio-section-types`), section type details (use `helio-section-types`), or test build workflow (use `helio-asset-to-test`).
version: 0.2.1
source_doc_version: Branching v0.1 (+ CLI v0.4.0 create, v0.7.0 read-back)
last_rebuilt: 2026-07-23

sources:
  - doc_id: src-branching-v0.1
    title: Branching v0.1
    last_synced: 2026-05-23
---

You are helping the user **configure conditional routing** in a Helio study — branching participants to different sections, ending the test early, redirecting at completion, or screening / disqualifying.

## Core idea

Branching changes what happens *after* a participant answers a question. Without it, every participant goes through the same sections in order. With it: jump to a follow-up, skip past it, end early with a custom message, or redirect to your own URL after completing.

Branching is configured at the **choice level**, not the section level. Each individual choice (or hotspot, or ranked answer) can carry its own routing.

What can trigger a branch:

- **Multiple Choice** (each choice — single-select only)
- **Click Test** (each hotspot)
- **Rank, MaxDiff** (best or worst answer)
- **Tree Test** (each leaf choice)
- **Card Sort, Point Allocation, Matrix** (each choice)
- **Prototype Test** (limited; most routing happens inside Figma)

Not supported: Likert, NPS, Preference, Free Response. Multi-select Multiple Choice. No backward looping. One target per choice.

What a branch can do: Jump to section, End test, End with custom message (= disqualification), Redirect to external URL, or Continue (default fall-through).

## Files to read

Read `reference.md` for the full surface — trigger sections, action types, disqualification pattern, target-stability via UUIDs, validation rules, the relationship between branching and UX Metrics / quotas, and the difference between branching and Conditional Follow-ups.

## How to apply

1. Identify what the user wants to route on — answer to a question, click on a hotspot, or rank position.
2. Check the section type supports branching (Likert, NPS, Preference, Free Response don't).
3. Confirm single-select if branching from Multiple Choice (multi-select branching isn't supported).
4. Match the action to the user's goal: jump vs end vs end-with-message vs redirect.
5. If screener/disqualification, walk the "End the test with a custom message" pattern.
6. Surface the UX Metric interaction: branching past a metric-tagged section means those participants don't contribute to that metric's score.
7. Surface the quota interaction: branched-out participants still count toward quota.
8. Note: branches don't fire in preview mode; you need to take the test as a real participant to verify.

## What's new in v0.2.1

Corrects a "pending deploy" claim that shipped a week ago, and closes the gap it left. Single-select multiple_choice branching has been creatable since **helio-cli v0.4.0** — the reference now carries the actual payload shape (`choice` 0-based, `question` 1-based counting researcher questions only, forward-only skips, `end_test` stray-key rules, the Enterprise gate) instead of only announcing that it exists. Adds branch **read-back** (v0.7.0): `preview --output json` returns `.branching` with resolved target question numbers, and `walkthrough` screens carry it — so a scripted branch is now verifiable without opening the editor. Also documents the two numbering systems the resolution reconciles, and the `remove-ux-metrics` interaction that can silently orphan a branch target.

## What's new in v0.2.0

Branching creation is no longer UI-only: the public API and CLI can create branches on **single-select multiple_choice** questions — `branching: [{choice: 0, action: "skip_to_question", question: 3}, {choice: 1, action: "end_test", message: "...", redirect_url: "..."}]` in question payloads, or `--branching <json|@file>` on `add-question`/`edit-question`. `end_test` with a message/redirect is the scripted disqualification pattern. Branching and followups are mutually exclusive per question. Other branchable surfaces (hotspots, variations, MaxDiff/Rank most/least labels) remain UI-only; `tests clone` of a branched test still covers those.

## What's new in v0.1.0

Initial release. Sourced from Branching v0.1. No AEO scorecard gaps to close.

## Handoffs

- For **inline conditional follow-ups** (in-flow text fields on the same section, not routing across sections), use `helio-section-types` — they're covered there.
- For **section type spec** (which sections support branching), use `helio-section-types`.
- For **the build workflow**, use `helio-asset-to-test`.
- For **the canonical surface-boundary guidance**, use `helio-creating-test`. Note single-select multiple_choice branching is CLI-creatable and readable back; other trigger types remain editor-only (or `tests clone` a test that has them) — see v0.2.1 above; hotspot/variation/most-least branching remains UI-only).
- For **UX metric impact** of branching, use `helio-ux-metrics`.
- For **how quotas count branched-out participants**, use `helio-audience-flow`.
- For **screening / disqualifying at the top of a study** (the End-with-custom-message pattern is one of the two Helio screening patterns), use `helio-forms-screeners`.
- For **the account → project → test data model** and where Branches attach, use `helio-concepts`.

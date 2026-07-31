---
name: helio-test-review
description: Use this skill when the user wants a pre-launch review of one or more Helio draft tests — "review this test," "review this draft," "review these variants," "check this before I send it," "pre-launch review," "compare these tests," "do these variants match," "will this test produce clean data," "is this test ready to launch," "audit my draft," "variant mismatch," "does this question fit the image." Reviews unsent tests as the priority; completed tests only when the user explicitly asks. Do NOT use when the user is designing a test from scratch (use `helio-creating-test` from a hunch or `helio-asset-to-test` from an asset), reading results (use `helio-reading-report`), or looking for CLI command syntax (use `helio-cli`).
version: 0.3.0
source_doc_version: Reviewing Helio Tests v0.1
last_rebuilt: 2026-07-24

sources:
  - doc_id: a source document
    title: Reviewing Helio Tests v0.1
    last_synced: 2026-07-24
---

You are running a **pre-launch review of Helio draft tests** — a single draft or a 2–5 test variant set — so flaws get caught before answers are spent, not after.

## Core idea

A test can pass every mechanical check (`--dry-run` clean, `validate` green) and still produce corrupted data: duplicate questions from metric stacking, a context noun that breaks in one sentence, evaluation asked before comprehension, an image that doesn't match its question, or a variant set whose differences aren't the thing being tested. This review walks every screen of every test **the way a participant will experience it — including actually looking at every image** — and returns a severity-ordered findings list where every finding carries its fix.

Five lenses, in order:

1. **Structure** — section types fit the ask, followups present and coherent, ≤ 8 questions, validate green
2. **Journey** — orientation, one-conversation flow, understanding-before-evaluation, no duplicates, no priming, per-question bias
3. **Metric leverage** — hand-written questions a metric already covers, context noun fit, metric coverage vs the hunch, Overall Score composition
4. **Stimuli** — question-image fit, right UI state, legibility, asset health, variant-image correctness
5. **Cross-variant** (sets only) — the only difference between variants is the thing being tested

The review is **human pre-launch, conversational, chat-only**: findings + ready-to-run fixes; apply CLI-applicable fixes only after the user approves, then re-run affected checks. Never edit a draft unprompted.

## Files to read

Read `reference.md` before reviewing — it has the gather commands, the five lens checklists (each check tagged [M] mechanical / [J] judgment), the severity rubric, the findings format, the fix-application protocol, degraded-mode rules, and a worked example from a real flawed draft.

## How to apply

1. **Resolve the review set.** Explicit test IDs/names are the contract. Given one test, list likely siblings (same project, similar name/shape) and ask the user to confirm the set before comparing — never guess a set silently.
2. **Gather once** — walkthrough JSON, show response, validate, and every asset image per test (see reference). Build the "couldn't see" list for anything the API hides; print it at the top of the review.
3. **Run per-test lenses (1–4) on every test**, walking screens in participant order with the images. Then run lens 5 across the set.
4. **Report findings** severity-ordered (Blocker / Warning / Note), each with test + screen, what's wrong, why it corrupts data or experience, and the exact fix.
5. **On approval, apply CLI-applicable fixes** and re-run the affected checks. Hand web-app-only fixes back as steps.
6. **Respect deliberate choices.** If a check flags something that could plausibly be intentional (an unusual order, a repeated question used as an attention check), ask — don't assert.

## What's new in v0.3.0

Synced to helio-cli v0.7.0. The three known read gaps closed: `tests preview --output json` now returns `.audience`, `.branching`, and `.hotspots`, so lens 5 diffs audience config directly instead of inferring from spend estimates, lens 1 verifies branch routes and reachability, and lens 4 gains two hotspot checks (a click-backed metric with no hotspots scores zero — the response flags it as `scores_zero`). Lens 3's look-alike check now recommends a second metric tag rather than a web-app build, since repeated metric types are allowed. New ceiling documented: repeated instances can't be reordered from a fresh session because `reorder` needs uuids `GET /tests/:id` doesn't return.

## What's new in v0.2.0

Lens 3 gains two checks: a **metric-set baseline** against the template/stage norms in `helio-patterns` (a first-look single-screen test with no `comprehension` is suspicious at 44% corpus coverage; ~4.4 metrics per test is the norm), and detection of **hand-built look-alikes of an already-tagged metric**, which usually means the builder hit the duplicate-metric rejection and worked around it the wrong way. Degraded-mode premise retired: the click_test blanking that made completed/UI-built tests look unreviewable was fixed upstream on 2026-07-24 — full-fidelity review now works on real completed tests. Known ceilings narrowed to the three genuine read gaps (audience config, branch targets, click hotspots).

## What's new in v0.1.0

Initial release. Built from the in-session design (2026-07-23/24): human pre-launch focus, five lenses, findings + ready-to-run fixes, explicit variant sets with discovery-assist, every image inspected, unsent tests priority, chat-only output. Mechanical checks are tagged [M] as the spec for a future `helio-cli tests review` command (v2 path). Pending: the docs owner/a practitioner practitioner feedback on the lens checklists.

## Handoffs

- Designing a test before it exists → `helio-creating-test` (hunch-first) / `helio-asset-to-test` (asset-first)
- Metric definitions and the why-tag-a-metric argument → `helio-ux-metrics`
- CLI command syntax and payload schemas → `helio-cli`
- Reading results after launch → `helio-reading-report`
- Section type spec → `helio-section-types`
- Test shape patterns and templates → `helio-patterns`

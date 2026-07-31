# Helio Test Review — Reference

**Skill:** `helio-test-review`
**Source:** Reviewing Helio Tests v0.1 (Drive doc `1AxiYCRgRFZoIUEXZJlECuvjvik_hajCjZgJ0Uy_xPaA`)
**Source last synced:** 2026-07-24
**Scope:** Pre-launch review of unsent Helio tests — single drafts or 2–5 test variant sets. Completed tests only when the user explicitly asks (forensics mode). Since the 2026-07-24 API fix, completed and UI-built tests return full-fidelity data.

---

<!-- DERIVED FROM: 1AxiYCRgRFZoIUEXZJlECuvjvik_hajCjZgJ0Uy_xPaA — Reviewing Helio Tests v0.1 -->

## Inputs and set resolution

- **Explicit is the contract.** The user names 1–5 tests by ID or name. Names resolve via `projects tests <project-id>` or `tests list`.
- **Discovery is an assist, never silent.** Given one test that smells like part of a set (version suffixes, sibling names like "…FlashArray"/"…FlashBlade", same project + same question shape), list the candidates and ask the user to confirm the set before running lens 5. A wrong grouping poisons the whole comparison.
- **Unsent tests are the priority.** Review completed tests only when the user explicitly asks (forensics mode) — say so in the report header when you do.

## Gather (one pass, before any lens)

Per test, collect and cache:

```shell
helio-cli tests walkthrough <id> --output json   # participant-eye screens: order, question text, choices, assets
helio-cli tests get <id> --output json           # structural fields walkthrough lacks: followup flags, randomization, branching, likert_type
helio-cli tests validate <id> --output json      # launch blockers, spend, answers remaining (drafts only)
helio-cli tests preview <id> --output json       # audience config, branching routes, hotspot geometry (v0.7.0+)
```

Then **fetch and actually look at every asset image** (walkthrough `assets[].url` signed URLs, or `assets get <id>`). The stimuli lens and the question-image checks are impossible without eyes on the images — a review that skipped them must say so.

For set discovery: `helio-cli projects tests <project-id> --output json`.

**Normalize before comparing:** strip HTML entities (`&nbsp;` etc.) from instructions; treat PascalCase/snake_case section types as equal.

### Degraded mode — the "couldn't see" list

*Fixed upstream (2026-07-24): the API previously blanked `type`, `variations`, and `ux_metric` on **every** section of any test containing a `click_test`, which looked like a UI-built-vs-CLI-built split but wasn't. Verified resolved — real completed tests now return full types, metric names, and per-question assets. Re-verify before assuming any gap.*

Gaps can still appear (an older API deploy, a section type the serializer doesn't know, an expired asset URL). **Never silently review less than the user thinks you did.** Open the report with a "Couldn't see" list naming exactly which fields were unavailable for which tests and which checks were therefore skipped or weakened. If images were unavailable, the stimuli lens is explicitly marked not-run.

## The five lenses

Each check is tagged **[M]** (mechanical — deterministic from the data, portable to a future `tests review` CLI command) or **[J]** (judgment — needs a reviewer reading questions and looking at images).

### Lens 1 — Structure: is it mechanically sound?

- [M] `validate` green; no launch blockers; spend and answers-remaining sane for the audience size
- [M] ≤ 8 questions (longer tests drop participants and dilute every signal)
- [J] Section type fits the ask: forced trade-off → max_diff, ordered priority → ranking, budget mindset → point_allocation, one-of-many → multiple choice single, sentiment words → multi-select
- [M] Every Likert / rating section has a followup; [J] the followup is required where the "why" matters
- [J] Each followup makes sense against the exact question above it
- [M] Branching routes don't strand participants (every branch reaches an end). Read from `preview --output json` → `.branching`: each entry gives `from_question_number`, the choice `label`, `action`, and a resolved `target_question_number`. Check every skip is forward, every `end_test` is intended, and no question is unreachable

### Lens 2 — Journey: does it read as one conversation? (Walk screens in participant order, with the images.)

- [J] Orientation: after intro + Q1, the participant knows what they're looking at and what's being asked of them
- [J] Order: open impressions → comprehension → evaluation (usefulness, purchase/intent) → advocacy (NPS). Never evaluation before understanding
- [M] No duplicate or near-duplicate questions — metric stacking creates these silently: **sentiment + desirability build the same 8-word impressions MC; appeal + reaction build the identical Likert**
- [J] Priming/leakage: the intro or an early question doesn't give away a later comprehension answer ("this checkout flow…" then "what do you think this page is?")
- [J] Per-question bias: leading, loaded, jargon, double-barreled
- [J] Fatigue shape: repetitive section types back-to-back, free-response walls

### Lens 3 — Metric leverage: are we measuring, or just asking?

- [J] Any hand-written question a UX metric already covers → recommend tagging instead (tagged = 0–100 score, threshold label, cross-wave comparability, Overall Score membership; hand-written look-alike = one-off distribution feeding none of that — see `helio-ux-metrics`)
- [J] Context noun reads naturally in **every** generated sentence — one noun feeds all metric instructions ("the checkout flow" works for impressions, breaks in "How likely would you be to purchase this ___?")
- [J] Metric coverage vs the hunch: behavioral paired with attitudinal; comprehension/advocacy not just missing
- [J] **Metric set vs the template/stage baseline.** Identify the shape (single screen vs flow; first look / iterate / benchmark) and compare against the corpus norms in `helio-patterns`: a first-look single-screen test with no `comprehension` is suspicious (44% coverage across the corpus), a findability test with no `success`, an iteration test with no `expectations`. Average is ~4.4 metrics per test — a one-metric test rarely supports a decision, and a nine-metric test usually dilutes the Overall Score. Flag as a Note with the template it resembles, not as a rule
- [M] **Hand-built look-alikes of an already-tagged metric.** A hand-written section duplicating a metric already on the test usually means the builder worked around the old duplicate-metric rejection. Since v0.7.0 the type can simply be tagged again — each instance scores independently — so the fix is to replace the look-alike with a second tag rather than keep a distribution. See `helio-ux-metrics`
- [M] Metric collisions present (the lens-2 duplicates, caught here as cause: which tags produced them)
- [J] Overall Score composition: every tagged metric counts equally — anything tagged that won't inform the decision dilutes the composite

### Lens 4 — Stimuli: do the images hold up? (Requires having looked at every image.)

- [J] Question-image fit: each question makes sense against what its image actually shows
- [J] Right state: the UI state shown matches what's asked (not the cart when the question is about checkout)
- [J] Legibility at participant sizes: resolution, cropping, phone readability
- [M] Asset health: status complete (not processing/expired), attached to the section it belongs to
- [M] **Hotspots on click-backed metrics.** `preview --output json` → `.hotspots` returns each click section's geometry plus a `scores_zero` flag. A click test scored by `engagement` / `success` / `usability` with no hotspots measures nothing — the CLI warns at create time, but a draft can reach review with the gap unfilled. Fix with `edit-question --hotspots`
- [J] Hotspot placement matches the affordance the question names — geometry is now readable, so check the rectangle actually covers the CTA rather than trusting it was drawn right
- [J] (Sets) each variant carries **its own** image — not a copy-paste of another variant's

### Lens 5 — Cross-variant: is the only difference the thing being tested? (Sets of 2+ only.)

Align tests question-by-question (by position, then by type+wording similarity when positions drift), then:

- [M] Structural parity: same question count, order, section types
- [M] Wording parity modulo the intended difference — flag any drift the user didn't name as the variable
- [M] Metric parity: same metrics tagged on every variant
- [M] Followup parity: same followups, same required flags
- [M] Audience parity: same target size, audience type, filters/screeners — a mismatch turns a preference read into noise. Read it directly from `tests preview --output json` → `.audience` (type, target_size, segments, customer_lists, demographics, screener, allow_retake, exclude_test_ids) and diff across variants
- [J] Stimulus-difference isolation: the images differ **only** in the intended variable (same fidelity, crop, state; right frame per variant)

## Severity rubric

- **Blocker — don't send.** Corrupts data or breaks the comparison: duplicate questions a participant will see, context noun producing nonsense, evaluation before comprehension on the decision question, any lens-5 parity mismatch not named as the test variable, wrong image on a variant, validate blockers.
- **Warning — should fix.** Weakens the signal: missing "why" followups, a hand-written section that should be a metric tag, borderline image legibility, mild priming, metrics diluting the Overall Score.
- **Note — consider.** Improvements and questions: section-type upgrades, ordering polish, possibly-deliberate choices (always phrased as a question, not an assertion).

<!-- /DERIVED -->

<!-- ADDED 2026-07-24 (agent-operational layer; not in the source doc) -->

## Findings format

Open with: review set (tests + status), the "couldn't see" list (or "full visibility"), then findings ordered Blocker → Warning → Note:

```
[BLOCKER · journey · both tests] Q2/Q3 are the identical question
  Participants are asked "What impressions does concept page give you?" twice in a row —
  sentiment and desirability both auto-build the impressions MC. Second answer is noise.
  Fix (CLI): helio-cli tests remove-ux-metrics <id> --metrics desirability
       — or keep both and reword one: helio-cli tests edit-question <id> <section-id> --instructions "..."
```

Every finding: severity · lens · which test(s) + screen · what's wrong · why it corrupts data/experience · the fix — a ready-to-run CLI command when one exists (`edit-question`, `reorder`, `add/remove-ux-metrics`, `tests update`), a web-app step when it doesn't (branching, screeners, video assets).

## Fix application protocol

1. Present findings; **wait for the user to say which fixes to apply**. Never edit a draft unprompted.
2. Apply approved CLI-applicable fixes to the draft (`edit-question`, `reorder`, `remove-ux-metrics`, …).
3. Re-run the affected checks (at minimum: re-walk the touched screens; re-run lens 5 if any variant changed) and confirm each finding is resolved.
4. Anything web-app-only goes back as a checklist for the user; offer to re-review after they've made those edits.

## Worked example (real)

A five-question draft built entirely by the book — metrics tagged (`sentiment desirability comprehension loyalty`), context noun "concept page", dry-run clean, validate green — produced on walkthrough:

```
Q2 [MC]     What impressions does concept page give you?      ← sentiment
Q3 [MC]     What impressions does concept page give you?      ← desirability (identical; BLOCKER)
Q4 [Likert] How likely would you be to purchase this concept page?   ← noun breaks (BLOCKER)
Q5 [Likert] How well do you understand what concept page does?       ← comprehension AFTER purchase intent (BLOCKER, reorder)
```

Three blockers in five questions, invisible to every mechanical pre-send check. This is the class of flaw the review exists to catch.

## Failure modes

- **Reviewing without the images.** Lens 4 and half of lens 2 are meaningless if you didn't look. If images can't be fetched, say so in the "couldn't see" list — never imply a visual pass happened.
- **Silently degrading.** UI-built tests hide types/metrics/assets. Name what you couldn't check, every time.
- **Nagging deliberate choices.** A repeated question can be an attention check; an odd order can be intentional. Possibly-deliberate flags are Notes phrased as questions.
- **Skipping per-test lenses in a set.** "V2 mismatches V1" and "V2's journey is broken" are different findings; run lenses 1–4 on every variant.
- **Trusting walkthrough nulls.** `ux_metric: null` on a UI-built test means *unknown*, not *no metric attached*. Cross-check `tests get` (`ux_metric_id` presence) before claiming a section is untagged.
- **Comparing raw strings across variants.** Strip HTML entities and normalize whitespace first, or wording parity produces false positives.
- **Editing drafts before approval.** Findings first, fixes on explicit go-ahead, re-check after.

## Known ceilings (v0.1)

- ~~Completed/UI-built tests review in degraded mode~~ — **resolved 2026-07-24.** `GET /api/public/tests/:id` now returns section `type`, resolved `ux_metric` names, and per-section assets, including on tests containing click tests.
- ~~Audience config, branch targets, and hotspots are write-only~~ — **resolved in helio-cli v0.7.0 / the 2026-07-30 API release.** All three read back through `tests preview --output json` (`.audience`, `.branching`, `.hotspots`), and `walkthrough` screens carry `branching` and `hotspots` too. Lenses 1, 4, and 5 now check them directly instead of inferring.
- **Repeated metric instances can't be reordered from a fresh session.** `reorder` distinguishes them by `metric:<uuid>`, which `GET /tests/:id` doesn't return; `tests order` reports `reorderable: false` and `ambiguous_metric_types` rather than printing a command that would 400. If a review recommends reordering such a test, say the uuids must come from the original create response — or that the reorder happens in the web app.
- No `tests compare` CLI command yet — lens 5 alignment is done by the reviewer from N walkthroughs. The [M]-tagged checks above are the spec for that future command.
- Branching soundness is only fully checkable in the web app; the CLI exposes `enable_branching` but not the route graph.
- Audience configuration (target size, audience type, filters/screeners) isn't exposed by any CLI read — audience parity is checked indirectly via `validate` spend estimates. API ask: audience block on the show response.

<!-- /ADDED -->

## Handoffs

- Test design from scratch → `helio-creating-test` / `helio-asset-to-test`
- Metric definitions, why-tag-a-metric, collisions → `helio-ux-metrics`
- Command syntax, payload schemas, draft-editing loop → `helio-cli`
- Post-launch synthesis → `helio-reading-report`
- Section type spec → `helio-section-types`

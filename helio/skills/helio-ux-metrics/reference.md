# UX Metrics — Reference

**Skill:** `helio-ux-metrics`
**Source:** UX Metrics v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had one minor AEO-rubric gap (Problem opener). Addressed in the ADDED section at the end of this file.

---

<!-- DERIVED FROM: src-ux-metrics — UX Metrics v0.1 -->

The full reference for Helio's measurement layer — all 17 metrics, how they're computed, what sections they need, and when to reach for each.

## How UX Metrics Work in Helio

A UX Metric is a measurable aspect of the user experience that Helio scores from participant responses. Each one produces a **0–100 score** and a **quality label**.

**Two key ideas:**

1. **Metrics auto-build the questions they need.** When you tag a section with a UX Metric in the editor, Helio generates the specific section structure that metric requires — including the scale, choice text, and number of sections. You don't structure them by hand.
2. **Scores are computed live.** Every time you view the report, Helio re-runs the scoring against the current set of responses (and any active filters). Scores aren't stored — they reflect the data right now.

<!-- ADDED 2026-07-23: metrics-first framing -->

## Why tag a metric instead of writing your own sections

Metrics aren't a convenience layer on top of normal sections — they're the difference between a test that produces *answers* and a test that produces a *score*. Lead with metrics when setting up a test; hand-write sections only for what no metric covers.

What a tagged metric gives you that a hand-built section never will:

1. **A score, not a distribution.** A plain Likert gives you "42% agreed." A tagged metric gives you a 0–100 score with a threshold label ("Good") that a PM or a Design Review can act on without interpretation. Only metric-tagged sections feed scoring — a hand-built section that *looks* like the metric's section contributes nothing to it.
2. **Validated wording for free.** The generated instructions, scale choices, and word lists are the tested, non-leading versions. Hand-written near-copies drift — and wording drift is a classic source of unrepeatable results between waves.
3. **Comparability.** Same structure every time means wave 2 is comparable to wave 1, project B to project A, and — because threshold labels are shared — a "Good" Sentiment to a "Good" Usability. Hand-built sections are only ever comparable to themselves.
4. **The Overall Score.** Only tagged metrics roll into the study's composite. A study built from hand-written sections has no Overall Score at all.
5. **Structures that can't quietly break.** Composite metrics (Brand Score especially) need internal flags the auto-template sets for you; hand-building or hand-editing those structures silently kills scoring.
6. **Speed.** One tag replaces designing, wording, and ordering one to three sections. In the CLI, `--ux-metrics sentiment loyalty desirability` builds four validated sections in one flag.

**When to hand-write instead:** when no metric measures the thing (a bespoke ranking of your feature list, a screener, an open-ended probe), or when you need a question shape a metric doesn't generate. The strong default for a decision-grade test: metrics for every measurement, hand-written sections only for exploration — and a custom context (e.g. "the checkout flow") so the validated wording still reads naturally.

**When you need the same metric twice.** Multi-screen tests often want `expectations` (or `comprehension`) on several screens — one instance per screen, each scored on its own. **This works as of helio-cli v0.7.0 / the 2026-07-30 API release**: tag the type as many times as you need and every instance owns its sections and its own score.

```shell
helio-cli tests create ... --ux-metrics expectations expectations expectations
```

`tests order` emits one block per *instance*. As of helio-cli v0.8.0 those instances are reorderable from a fresh session — `tests order` returns `reorderable: true` with paste-ready `metric:<uuid>` keys, and the uuids also read from `preview`, so they no longer have to be captured from the create response. `remove-ux-metrics --metrics` takes either a type (removes every instance) or a specific metric id (removes just that one).

*Historical note:* before v0.7.0 the API rejected the duplicate even though the platform scored multiple instances, which pushed people into hand-building look-alike sections as a workaround. That was always the wrong trade — a scored metric for a raw distribution — and it's no longer necessary.

**The counterweight — metrics don't guarantee the journey.** Tagging guarantees each section is valid; it says nothing about whether the *sequence* reads as one coherent conversation. Known collisions: sentiment and desirability both open with the same 8-word impressions Multiple Choice, and appeal and reaction generate the identical Likert — tag both and the participant sees the same question twice in a row. The context noun also feeds *every* generated instruction, so it must read naturally in all of them ("the checkout flow" works for impressions, breaks in "How likely would you be to purchase this ___?"). Always walk the assembled test participant-eye before sending and order it understanding-before-evaluation — see the journey checks in `helio-creating-test`.

<!-- /ADDED -->


## The Two Families

Helio implements two of the four Glare framework families today.

**Behavioral (8 metrics)** — what people *did*. Did they succeed? Did they finish? Did they understand?

**Attitudinal (9 metrics)** — how people *felt*. Did they like it? Trust it? Find it useful?

Performance metrics (drop-off, time on task) and Intelligence metrics (AI-experience quality) are concepts from the Glare framework but aren't implemented in Helio's code today.

## Threshold Labels

Every metric maps its 0–100 score to a 5-tier label:

| Score | Label |
|---|---|
| 90–100 | Very Good |
| 70–89 | Good |
| 50–69 | Average |
| 30–49 | Poor |
| Below 30 | Very Poor |

The labels are consistent across all metrics, so a "Good" Sentiment is directly comparable to a "Good" Usability.

## The Overall Score

Helio rolls every metric tagged on a study into a single **Overall Score** — the equal-weight average of every metric's score. Same 0–100 scale, same labels.

A few things to note:

- Equal weight means every metric counts the same. Adding a low-scoring metric to a study lowers the overall composite.
- Metrics with no responses yet are excluded from the average (they don't drag it down with a 0).
- The overall score recomputes whenever you change filters on the report.

## Behavioral Metrics (8)

### Success

**Definition:** Did participants achieve the intended goal?
**Built from:** A Click Test with hotspots tagged as Primary, Secondary, and Tertiary.
**Scoring:** Weighted by hotspot priority — Primary hotspot clicks contribute the most to the score.
**When to use:** When there's a clear "right answer" and you want to know what percentage of participants found it.

### Completion

**Definition:** Did participants finish the task?
**Built from:** A Prototype Test with an expected path.
**Scoring:** Direct Success + Indirect Success rate combined — anyone who reached the goal counts, whether they took the direct route or wandered.
**When to use:** When the goal is whether the task can be completed at all, not whether it's efficient.

### Usability

**Definition:** How smoothly did the experience flow across multiple tasks?
**Built from:** Three Click Test sections, each with its own task and hotspots.
**Scoring:** Weighted average across all three click tasks.
**When to use:** When you want a broad usability read across several screens or interactions, not just one.

### Engagement

**Definition:** Are participants clicking the *right* things?
**Built from:** A Click Test with a Primary hotspot.
**Scoring:** Ratio of Primary-hotspot clicks to all clicks on the image.
**When to use:** When you want to know whether your CTA or focal element is actually drawing attention, separated from whether participants succeed.

### Effort

**Definition:** How hard did the experience feel?
**Built from:** A Prototype Test followed by an NPS-style question rating effort (a 7-point scale, not the standard 0–10).
**Scoring:** Average effort rating, normalized to 0–100.
**When to use:** After a Prototype Test, when you want a self-reported difficulty score alongside the behavioral success metric.

### Comprehension

**Definition:** Did participants understand what they saw?
**Built from:** A 4-point Likert section ("Did not understand" → "Understood very well").
**Scoring:** Weighted by position on the scale.
**When to use:** After introducing a new feature, concept, or copy block. Pair with usability to separate "I get it but it's hard to use" from "I don't get it."

### Frequency

**Definition:** How often would participants engage with this?
**Built from:** A 5-point Likert section ("Very rarely" → "Very frequently").
**Scoring:** Weighted by selected frequency.
**When to use:** When you want stated usage habits — though remember stated frequency is famously different from actual frequency.

### Intent

**Definition:** What action are participants planning to take?
**Built from:** A Multiple Choice section with four options (most desired → least desired action), single-select.
**Scoring:** Distribution of intent across the four options.
**When to use:** After showing a design or proposition, when you want to know what people plan to do next.

## Attitudinal Metrics (9)

### Sentiment

**Definition:** Overall emotional reaction.
**Built from:** A Multiple Choice section with 8 reaction words (helpful, innovative, simple, joyful, complicated, confusing, overwhelming, annoying) shown in random order.
**Scoring:** Net positive vs. net negative across selected words.
**When to use:** Quick gut-check on overall vibe. Pair with Free Response to understand *why*.

### Feeling

**Definition:** The specific emotion the design evokes.
**Built from:** A Multiple Choice section with 8 emotions drawn from the Plutchik emotion model (joy, trust, anticipation, surprise, sadness, fear, anger, disgust). Participants pick up to 3.
**Scoring:** Net positive emotions vs. net negative.
**When to use:** When you want a richer emotional signal than Sentiment — what *kind* of positive or negative reaction.

### Desirability

**Definition:** Would someone choose this — and would they pay for it?
**Built from:**

- **v1 (deprecated):** A single 8-word sentiment Multiple Choice. Returns a label only, no numeric score.
- **v2 (current):** Two sections — an 8-word sentiment Multiple Choice plus a 5-point likelihood-to-purchase Likert.

**Scoring:** v2 combines sentiment + intent into a 0–100 score.
**When to use:** Concept testing where you need to know whether people are drawn to it strongly enough to act.
**Note:** v1 and v2 coexist in older accounts. New tests default to v1 unless v2 is explicitly chosen — confirm which version is in use before comparing scores across older studies.

### Loyalty

**Definition:** Will participants recommend this?
**Built from:** A standard 11-point NPS question (0–10).
**Scoring:** NPS calculation expressed as a 0–100 score.
**When to use:** When the question is about likelihood to recommend or stick with a product.

### Appeal

**Definition:** Immediate aesthetic / conceptual draw.
**Built from:** A 5-point Likert "impression" scale (Very dissatisfied → Very satisfied).
**Scoring:** Weighted by position.
**When to use:** Visual appeal of a design or mockup, separate from whether it works.
**Note:** Older accounts may see this metric labeled "Reaction" — the name was changed but both still appear in some places.

### Usefulness

**Definition:** Does it actually help?
**Built from:** Two 5-point Likert sections — one on ease ("easy to use") and one on feature fit ("features meet my needs").
**Scoring:** Average agreement across both statements.
**When to use:** When you want a balanced read on practical utility, not just emotional response.

### Expectations

**Definition:** Did it meet what people thought it would do?
**Built from:** A Free Response section (what participants expected) followed by a 5-point Likert ("Failed expectations" → "Exceeded expectations").
**Scoring:** Based on the Likert; the Free Response is context for the researcher.
**When to use:** When testing whether a UI behaves the way users predict it will, before clicking.

### Satisfaction

**Definition:** How satisfied are people after a specific task?
**Built from:** A Click Test (the task) followed by a 5-point Likert satisfaction scale.
**Scoring:** Based on the Likert; the Click Test sets the task context.
**When to use:** Post-task satisfaction, scoped to a particular interaction.

### Brand Score

**Definition:** Composite brand health — awareness + perception + advocacy.
**Built from:** Three sections in order:

1. A Multiple Choice asking participants to pick the brand from a list (awareness).
2. An 8-word sentiment Multiple Choice (perception).
3. An NPS question (advocacy).

**Scoring:** A composite that combines all three into one score.
**When to use:** Brand health assessment — when you need a single defensible read across recognition, attitude, and loyalty.
**Note:** This is the most complex metric to set up; the auto-templating builds all three sections for you.

## AI-Derived UX Metrics (Design Analysis)

When Helio's Design Analysis runs, it scores the same set of UX metrics — but the scores come from an AI model evaluating the design, not from participant responses.

**Key differences:**

- AI-derived scores live in a separate data structure (they don't mix with participant-driven scores on the same chart).
- AI scores are stored as **labels only** (Very Good / Good / Average / Poor / Very Poor), not numeric 0–100 values.
- AI-derived metrics are tied to a Design Analysis report, not a regular study.

The same metric names mean the same things — it's just the source of the score that differs. For the full Design Analysis spec, use `helio-design-analysis`.

## Plan & Feature Gates

UX Metrics are gated by an account-level feature toggle. If you don't see them in your account, the feature may not be enabled — contact your account manager.

There's no per-metric beta gating today — once the feature is on, all 17 metrics are available.

## Good to Know

**Metrics without responses show N/A.** A tagged metric that hasn't received any participant data yet displays as N/A — score, label, and threshold all blank. It doesn't contribute to the Overall Score until responses arrive.

**Filters change scores.** Every metric recomputes against whatever filters are active on the report. A metric might be "Good" overall but "Poor" for a specific demographic — that's a real insight, not a bug.

**Multiple sections per metric (and why it matters).** Some metrics need more than one section (Usability needs 3; Brand Score needs 3; Usefulness, Expectations, Satisfaction, Desirability v2, and Effort each need 2). When auto-templating builds them, the questions are linked — deleting one breaks the metric's scoring.

**The math is versioned separately from the platform.** If a score shifts unexpectedly after a platform update, the scoring library may have been updated independently — contact your account manager if a baseline comparison looks off.

**Desirability is in two versions, side by side.** v1 (label-only, single section) and v2 (numeric, two sections) both exist. New accounts default to one or the other based on settings. If you're comparing Desirability scores across two studies, confirm both use the same version.

**Reaction = Appeal.** "Reaction" was renamed to "Appeal" but both terms still appear. Same metric.

**Brand Score requires the right setup.** The first Multiple Choice section in a Brand Score group needs a specific choice marked as the "brand" being evaluated. If that flag isn't set, scoring won't work — the auto-template handles this for you when you tag the metric, so don't manually edit the structure unless you know what you're doing.

## At-a-Glance Summary

| Metric | Family | Sections | Best for |
|---|---|---|---|
| Success | Behavioral | 1× Click | Right-answer findability |
| Completion | Behavioral | 1× Prototype | Task feasibility |
| Usability | Behavioral | 3× Click | Broad usability read |
| Engagement | Behavioral | 1× Click | CTA / focal-element attention |
| Effort | Behavioral | 1× Prototype + 1× NPS | Perceived difficulty |
| Comprehension | Behavioral | 1× Likert (4-pt) | Understanding new concepts |
| Frequency | Behavioral | 1× Likert | Stated usage habits |
| Intent | Behavioral | 1× Multiple Choice | Planned next action |
| Sentiment | Attitudinal | 1× Multiple Choice (8 words) | Quick emotional vibe |
| Feeling | Attitudinal | 1× Multiple Choice (8 emotions) | Specific emotional response |
| Desirability | Attitudinal | 1× MC (v1) or 1× MC + 1× Likert (v2) | Concept appeal + intent |
| Loyalty | Attitudinal | 1× NPS | Recommendation intent |
| Appeal | Attitudinal | 1× Likert (impression) | Aesthetic draw |
| Usefulness | Attitudinal | 2× Likert (agreement) | Practical utility |
| Expectations | Attitudinal | 1× Free Response + 1× Likert | Behavior vs. prediction |
| Satisfaction | Attitudinal | 1× Click + 1× Likert | Post-task satisfaction |
| Brand Score | Attitudinal | 3× (MC + MC + NPS) | Brand health composite |

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem-opener gap) -->

## What this solves

Without a working model of every UX metric, teams attach Sentiment to everything (it's the easiest) and miss the metrics that would actually answer the decision. This is the catalog so the choice is deliberate.

## When to use

Reach for this skill when the user is:

- Picking which UX Metric to attach to a section
- Asking what a specific score means or what's "good"
- Confused about why a metric isn't computing (often a section-structure issue)
- Comparing scores across studies (especially Desirability, which has v1/v2 versions)
- Setting up Brand Score, Effort, Usefulness, Expectations, Satisfaction, or Desirability v2 — the multi-section composites

For section types that get tagged with these metrics, use `helio-section-types`. For interpreting scores in a finished report, use `helio-reading-report`. For the AI-evaluator version of these metrics, use `helio-design-analysis`.

## Failure modes

- **Attaching Sentiment as a default.** It's the easiest to set up; it's also the least diagnostic. Pick the metric that matches the decision.
- **Manually editing Brand Score's section structure.** Auto-templating handles the brand-flag setup. Manual edits usually break scoring.
- **Comparing Desirability scores across studies without checking version.** v1 and v2 produce different outputs (label vs numeric). Confirm which is in use before comparing.
- **Treating Design Analysis labels as comparable to participant-driven scores.** Different data structure, different source. They don't share a chart.
- **Treating Overall Score as decisive.** It's an equal-weight average. A Good Overall can hide a Poor metric. Always read the breakdown.
- **Expecting Performance metrics (drop-off, time on task) to be available.** They're Glare framework concepts not implemented in Helio. Source from analytics instead.

## Score patterns from real tests

Real scores drawn from the test corpus catalogued in `helio-patterns`. Use these as calibration anchors when reading new reports.

### Success (Behavioral) — invisible affordance pattern

- **The hunting-apparel PLP Q5: 12% (Very Poor)** — the filter UI was essentially invisible from the PLP. Below-30 Success is the textbook red flag.

### Engagement (Behavioral) — high attention concentration

- **A PDP variant: 92 (Very Good)** — Primary-hotspot click rate dominated the page. Healthy on its own; only meaningful in context with Intent (see below).
- **An athletic-apparel DTC homepage Q1: 30** — clicks distributed across 5 hotspots. Not broken; means no single CTA is dominant.

### Comprehension (Behavioral) — message clarity

- **A veteran careers landing page: 89 (Very Good)** — 65% "Understood very well." Page audience is clearly identified.
- **An athletic-apparel DTC homepage: 85 (Good)** — 47% "Understood very well," 42% "Most of it." Good range.
- **A B2B data-platform homepage: 80 (Good)** — but 22% "A little" reading "data fabric" — the followup exposed jargon that the score didn't.

### Desirability (Attitudinal) — emotional reaction

- **The same PDP variant: 87 (Good)** with positive descriptors dominant (Helpful 73%, Innovative 69%).
- **An athletic-apparel DTC homepage: 87 (Good)** — paired with NPS 14 (see below) for the "liked but not advocated" pattern.

### Intent (Behavioral) — planned next action

- **The same PDP variant: 38 (Poor)** while Engagement 92 / Desirability 87 — the headline cross-metric divergence. Attractive but not persuasive.
- **The B2B data-platform homepage Q5: 37** — stated intent for "Explore the Platform" at 35%, but actual first-click went elsewhere. Stated-vs-behavioral mismatch.

### Loyalty / NPS (Attitudinal) — recommendation intent

- **An athletic-apparel DTC homepage: 14 (Average)** — paired with Desirability 87. The gap is the finding: emotional response without a share moment.

### Satisfaction (Attitudinal) — used as intent disclosure

- **A press-room site** — `satisfaction` attached to questions that looked like findability. The metric choice itself disclosed the team's actual goal: "does the press feel served," not "can journalists find things."

### Frequency (Behavioral) — stickiness

- **The investment-platform Q5** — "How often would you use a platform like this?" Unique in the corpus. Worth replicating for any retention-sensitive product.

## Where to go next

- For attaching metrics in a test build: `helio-asset-to-test`
- For section structures that metrics auto-build: `helio-section-types`
- For interpreting scores during synthesis: `helio-reading-report`
- For the AI evaluator that uses the same metric names: `helio-design-analysis`
- For Glare's broader UX Metrics framework (all four families): `glare-ux-metrics`

<!-- /ADDED -->

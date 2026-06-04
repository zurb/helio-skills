# Reading a Helio Report + From Helio Test to Glare Signal — Reference

**Skill:** `helio-reading-report`
**Source:** Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2 (merged)
**Source last synced:** 2026-05-23
**Notes:** The Drive copies of these two source docs are still at v0.1. This skill uses the v0.2 content from the local Glare Skills working folder. v0.2 reconciled the mechanical synthesis vocabulary against UX Metrics v0.1 — real Helio threshold labels, Direct/Indirect/Failed grading, the correct Behavioral / Attitudinal family assignments, and explicit Performance / Intelligence "not implemented" notes. When Bryan syncs v0.2 back to Drive, update the `last_synced` dates and replace these doc IDs if they change.

---

<!-- DERIVED FROM: 1XfSMQbJRw7s6H9Gjct6dWQunmwf7IVuhiC_1LpSySgM — Reading a Helio Report v0.2 -->

## Reading a Helio Report (the synthesis workflow)

A Helio test produces a report. A report isn't a signal — it's the raw material a signal is built from. This is the synthesis step: the cognitive work of reading a report and producing the one-sentence signal that lands in a Design Review.

### What good synthesis looks like

A good synthesis:

- Reads the report in under 30 minutes for a single-screen test
- Produces a one-sentence signal that names behavior, metric, context, and direction
- Cites at least two specific numbers, one followup quote, and the audience slice they belong to
- Tells you what the next test should be

If your reading produces "interesting findings," you're not done yet.

### The 30-second scan

Before reading question-by-question, scan five things:

1. **Test name** — homepage / landing / PDP / flow / "X > Y > Z" (the ">" is the multi-screen tell)
2. **Intro** — boilerplate or scenario-led? If boilerplate, the first section carries the framing
3. **Audience** — single niche, fanout across personas, adjacent audience?
4. **Section count + asset count** — 5 sections / 1 asset = single-screen; 6+ sections / 3+ assets = flow
5. **UX metrics tagged** — which metrics are attached, and where do they diverge? Also check the Overall Score (Helio's equal-weight average across all tagged metrics)

### Read the headline

Helio uses one consistent 5-tier threshold scheme across every metric:

| Score | Label | Reading move |
|---|---|---|
| 90–100 | Very Good | Strong signal. The next test should pressure-test something else. |
| 70–89 | Good | Healthy. Read the followups for the dissenting tail. |
| 50–69 | Average | The page works for some, not others. The audience or content gap is the find. |
| 30–49 | Poor | Real problem. Chase the followups and the segment cuts. |
| < 30 | Very Poor | Red flag. Don't synthesize past this. |

**Per-metric reading moves**

- **Comprehension** (Behavioral) — the score is the entry point. The required open-text followup is the actual signal.
- **Success** (Behavioral) — Primary hotspot click rate. Below 30 means the affordance is invisible.
- **Completion** (Behavioral) — Prototype Test Direct + Indirect Success rate. High Indirect share = users get there but the path is wrong.
- **Engagement** (Behavioral) — Primary-hotspot clicks as a share of all clicks. High Engagement + low Success = right zone, wrong affordance.
- **Desirability** — v1 is label-only; v2 is sentiment MC + likelihood Likert composite. Confirm version before cross-study comparison.
- **Intent vs Loyalty (NPS)** — Intent is Behavioral (planned next action); Loyalty is Attitudinal (recommendation). They drift apart often; the gap is usually a finding.
- **Brand Score** — composite of awareness + perception + advocacy. The breakdown tells you which leg is dragging.
- **Free Response open text** — Helio auto-clusters into Common Phrases.

### Read for divergence

Four shapes:

**1. Cross-metric divergence.** Behavioral high + Attitudinal/Intent low = attractive but not persuasive. Attitudinal high + Behavioral/Success low = liked but not usable. The **Overall Score** can hide divergence — always read the breakdown, not just the composite.

**2. Cross-audience divergence.** Same test, different segments. Never report the headline when meaningful segment spread exists.

**3. Cross-iteration divergence.** Same screen, multiple variants. Comparison only works if the test structure was locked.

**4. Stated-vs-behavioral divergence.** "What would you do next?" vs the actual Click Test. When they conflict, behavior wins — but the gap is the finding.

### Read the open text

- Use Common Phrases first (auto-clustered with confidence scores).
- Read all of them. 100 short answers is 20 minutes.
- Theme by repetition, not by your hypothesis.
- Look for the minority quote that contradicts the headline.
- Read followups paired with the rating they explain.

The comprehension followup is special — it's the only one that converts self-rating into a knowledge probe. A user can rate themselves Very Good and then describe the company as something it isn't. That gap is the real signal for marketing/positioning tests.

### Compare

- Against the team's hunch
- Against the baseline
- Against a prior iteration (only clean if structure was locked)
- Against other audiences

If you have none of these comparisons, say so. "Baseline established at Desirability Good" is more honest than presenting Good as if it's good.

### Spot red flags

- Any metric Poor or Very Poor
- Success Poor (under 30) → affordance invisible (KUIU Q5 12% pattern)
- Failed share above 30% on Prototype Test → task is broken
- Comprehension Poor → page isn't communicating
- High Indirect Success share on Prototype Test → path is wrong
- Negative descriptor spike on Sentiment/Desirability v1 (>15%) → coherent minority signal
- Audience spread of 20+ score points → page isn't built for both segments
- MaxDiff aggregated percentages showing 0% → wrong-view-of-the-data symptom; use raw best/worst counts

### Synthesize to one sentence

Template:

> [audience / context] [behavior or reaction] [metric with score and threshold label] [context from followups] — suggesting [interpretation], and the next iteration should [direction].

Illustrative worked example:

> On the PDP V5 variant, US shoppers engaged with the page (Engagement Very Good) and reacted positively to it (Desirability Good), but planned next-action intent dropped to Poor — suggesting the page is doing visual and emotional work but isn't clearing the threshold for commitment, and the next iteration should pressure-test the CTA placement and the value-prop framing closer to the fold.

Tests for a finished signal:

- Names *who* (not "users in general")
- Cites two metrics with threshold labels
- Includes the context (followup theme, audience slice, comparison)
- Ends with the direction (the next move)
- Fits in one sentence

If it won't compress to one sentence, you have multiple signals. Write them separately as Findings.

### Call the test

Three honest reads:

- **Decisive** — write the signal, take to Design Review
- **Inconclusive** — most metrics in Average band, followups don't theme strongly. Don't manufacture a signal — say so.
- **Re-test** — the test design itself was the problem (audience too narrow, question biased, branching pulled people past key metrics).

Inconclusive is the hardest call to make. When in doubt, call it inconclusive.

### Anti-patterns

- Cherry-picking the high number
- Anecdote bias from one followup
- Ignoring n
- "Interesting findings" without direction
- Reading the test against the design instead of the hunch
- Reading the Overall Score in isolation
- Treating Design Analysis labels as comparable to participant scores

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1TH6KgDxnwtW56FwVAikvDcyaUBRjWlos8lopL9mrEwU — From Helio Test to Glare Signal v0.2 -->

## From Helio Test to Glare Signal (the conceptual bridge)

Helio is the platform. Glare is the framework. This part of the reference connects them — how a launched test becomes a signal you can carry into a Design Review, and a decision the Decision Map can hold.

### Hunches and risks — same anchor, two voices

Both frames work for choosing what a test should test:

- **Hunch frame** — for a design that's committed. "We believe [change] for [audience] will [impact] because [reason]." The test confirms or kills the belief.
- **Risk frame** — for a design that's uncertain. "What's the riskiest assumption? What would I be most surprised by if it failed?" The test exposes the assumption.

A hunch is a bet against a risk; a risk is the negative of a hunch. Use the language the team uses.

If neither produces an answer, you have curiosity, not a test. Don't spend on curiosity.

### Where Helio sits in Glare's four metric families

| Glare family | In Helio? | What it captures |
|---|---|---|
| Behavioral | Yes (8 metrics) | What people actually did |
| Attitudinal | Yes (9 metrics) | How people felt |
| Performance | *No* | Drop-off rate, time on task, error rate. Glare concept, not implemented in Helio today. |
| Intelligence | *No* | AI-experience quality. Glare concept, not implemented in Helio today. |

If your decision needs Performance or Intelligence evidence, source it from analytics or AI eval tooling and bring it alongside the Helio result.

### Mapping Helio's 17 metrics

| Helio metric | Glare family | What it captures |
|---|---|---|
| Success | Behavioral | Primary hotspot click on a Click Test |
| Completion | Behavioral | Prototype Test Direct + Indirect Success |
| Usability | Behavioral | Weighted average across multiple Click Tests |
| Engagement | Behavioral | Primary-hotspot clicks / total clicks |
| Effort | Behavioral | Self-reported difficulty, 7-point scale |
| Comprehension | Behavioral | Understanding (4-point Likert + open-text knowledge probe) |
| Frequency | Behavioral | Stated usage on a 5-point Likert |
| Intent | Behavioral | Planned next action (4-option Multiple Choice) |
| Sentiment | Attitudinal | 8-word descriptor Multiple Choice |
| Feeling | Attitudinal | Plutchik 8-emotion Multiple Choice (pick up to 3) |
| Desirability | Attitudinal | v1 label-only or v2 numeric (sentiment + likelihood) |
| Loyalty (NPS) | Attitudinal | Recommendation intent, 0–10 NPS |
| Appeal | Attitudinal | Aesthetic draw, 5-point impression Likert |
| Usefulness | Attitudinal | 2× Likert composite (ease + feature fit) |
| Expectations | Attitudinal | Free Response + Likert |
| Satisfaction | Attitudinal | Click Test + Likert |
| Brand Score | Attitudinal | 3-section composite (awareness + perception + advocacy) |

The reading move: when a test mixes Behavioral and Attitudinal metrics on the same screen, you're collecting two kinds of evidence at once. Watch where they agree (the design is working through and through) and where they diverge (that's the headline finding).

### Reading a Helio result as a Glare signal

Glare's four-piece signal definition:

1. **Behavior observed** — what you tested
2. **Metric** — what was captured (Helio gives a 0–100 score and a 5-tier label)
3. **Context** — how you sliced the audience and what the followups said
4. **Direction** — what the team will do next (you supply this)

Helio gives you the first three. You supply the fourth.

The signal should be one sentence. If it takes a paragraph, you're describing the test, not the signal.

### Where the signal goes

**1. The next Design Review.** The signal is the evidence the Design Review's Ground step is built on. With it, the team moves through Surface → Identify → Ground → Navigate → Align → Lock without losing time on "who likes which version."

**2. The Decision Map.**

- **Measure** — where the signal is captured (the Helio test itself sits here)
- **Focus** — where the signal narrows direction
- **Lead** — where the signal connects to business KPIs

**3. The next hunch.** A signal that exposes a risk creates the next hunch. A signal that doesn't generate a next hunch isn't a finished signal — it's a fact.

### Anti-patterns from a Glare lens

- Running a test without naming the decision it serves
- Treating the report as the deliverable instead of the signal
- Reading the Overall Score in isolation (equal-weight average hides Poor metrics inside Good composites)
- Letting the metric pick the question (decision → metric → section structure, not section first)
- Reading Attitudinal as Behavioral (what they said vs what they did)
- Mixing Design Analysis labels with participant scores
- Stopping at the signal (a signal that doesn't enter a Design Review or anchor a next decision died on the dashboard)

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Sitting in front of a Helio report and asking "what now"
- Trying to write a one-sentence signal for a Design Review
- Confused about how Helio results connect to Glare's broader framework
- Looking for the divergence patterns (the headline findings live there)
- Calling a test as decisive, inconclusive, or re-test
- Carrying a signal into Decision Map's Measure / Focus / Lead

For per-metric definitions, use `helio-ux-metrics`. For filter mechanics that synthesis depends on, use `helio-report-filtering`. For capturing findings as first-class objects, use `helio-findings`. For the broader Glare framework (Design Review SIGNAL, Decision Map facets), route to `glare-getting-started`, `glare-design-review`, `glare-decision-map`.

## Failure modes

- **Stopping at "interesting findings."** Force the direction or call it inconclusive.
- **Reading the Overall Score and skipping the breakdown.** Equal-weight average hides Poor inside Good.
- **Comparing Desirability across studies without checking v1/v2.** Different scoring.
- **Blending Design Analysis labels with participant-driven scores.** Different data structures, different sources.
- **Treating the worked example numbers (PDP V5 92/87/Poor) as a specific real test.** They're illustrative of the pattern; not verified to a specific test.
- **Forgetting Performance and Intelligence aren't in Helio.** If the decision needs them, source elsewhere and bring alongside.
- **Synthesizing without comparison.** A score in isolation doesn't mean much. Always compare to hunch / baseline / iteration / audiences.

## Where to go next

- For per-metric definitions: `helio-ux-metrics`
- For filtering report data: `helio-report-filtering`
- For finding capture: `helio-findings`
- For test design that produces synthesizable reports: `helio-asset-to-test`
- For test shape patterns: `helio-patterns`
- For Glare framework: `glare-getting-started`, `glare-design-review`, `glare-decision-map`

<!-- /ADDED -->

# Helio Test Patterns — Reference

**Skill:** `helio-patterns`
**Source:** Helio Test Patterns v0.2 (scrubbed) + Test Pattern Playbook v0.1 (merged)
**Source last synced:** 2026-07-06
**Notes:** Two DERIVED blocks. The Test Patterns block is the *reading* synthesis (15-test sample): recognize shapes, the 30-second scan, iteration methodologies. The Playbook block is the *construction* companion (285-test analysis): when each of seven templates gets pulled (first look / iterate / benchmark), the metric coverage data, and per-template question tables. The playbook empirically resolves several of Test Patterns' "what's NOT in this sample" caveats.

---

<!-- DERIVED FROM: src-helio-test-patterns-v0.2 — Helio Test Patterns v0.2 (scrubbed) -->

A reference for reading and constructing Helio tests, drawn from a sample of 15 tests across four projects (a continuous-experimentation project, the homepage-baseline project, an internal product project, and a multi-screen iteration series referred to here as the "145" and "144" series).

## The thesis

Most Helio tests are variations on a single five-question template. Recognize that template and you can read ~70% of reports without further instruction. The remaining ~30% are specialized patterns (multi-screen flows, audience fanouts, MaxDiff content prioritization) that you can identify by shape at a glance.

## 1. The core 5-question template

Almost every homepage / landing-page / single-screen test follows this functional arc, in some order:

| Slot | Typical question | UX metric |
|---|---|---|
| 1. Comprehension | Likert "How well do you understand what this company is offering?" + required open-text followup *"What is this company offering?"* | `comprehension` |
| 2. Engagement | Click test "Click where you would go first on this page" | `engagement` |
| 3. Desirability | Multi-select (up to 8) "How does this feel?" with a positive set (Helpful / Clear / Simple / Innovative) and a negative tail (Confusing / Complicated / Unnecessary / Uninteresting) | `desirability` |
| 4. Likelihood | Likert "How likely would you be to [purchase / use / request a demo / sign up]?" + required *"Why?"* followup | `desirability` or `intent` |
| 5. Commit / loyalty | Either an NPS question, or a forced "What would you most likely do next?" multi-select across the page's actual CTAs | `loyalty` or `intent` |

This pattern appears verbatim (with order shuffles) across single-screen marketing-page tests in the corpus — athletic-apparel DTC homepages, B2B SaaS data-platform homepages, investment-platform homepages, veteran careers landing pages, and all six variants of the the fixed-template series PDP. The order shifts but the *roles* do not.

**When the order shifts:** if Q1 is a click test rather than a comprehension likert, the test is leading with behavior (where will they look) before opinion (what do they think). Common on PDP / CTA-heavy pages where engagement is the headline outcome.

## 2. Two intros do almost all the work

There are essentially two intro styles across the entire batch:

- **Generic boilerplate:** *"Welcome to our test! We'll use the results to improve the design of our site."* When this appears, the actual scenario is buried in Q1's instructions (e.g., the athletic-apparel homepage Q1 starts with *"Imagine you're shopping for athletic apparel"*).
- **Scenario-led:** *"Imagine you're shopping for a seasonal occasion invites"* / *"We'll be asking you questions as if you're using a mobile banking app."*

**Reading rule:** when the intro is boilerplate, always read Q1 carefully. The framing lives there, not in the intro.

## 3. Click tests do double duty

Same question type, two completely different intents. The UX metric is the tell:

| Metric | Question shape | What it measures |
|---|---|---|
| `engagement` | "Click where you would go first on this page" | Broad exploration — where does the eye/click land first, with many hotspots possible |
| `success` | "Click where you would go to [specific task]" | Targeted findability — usually 1 primary hotspot, branching usually on, pass/fail framing |

**Example — a hunting-apparel Homepage > PLP > PDP flow:** Q1 is `engagement` (broad, 10 hotspots). Q2, Q4, Q5, Q8 are all `success` (find this specific thing). Q5 scored 12% — a direct red flag that the filter UI on the PLP isn't working. Without the engagement-vs-success distinction in the metric, that signal would be hidden in raw click data.

## 4. Required followups are where the actual insight lives

Every likert and multi-select with a meaningful score has a *required* open-text followup. The score is the headline; the open text explains it. The followups are remarkably templated:

| Question type | Standard followup |
|---|---|
| Comprehension likert | *"What is this company offering?"* (knowledge probe, not opinion) |
| Likelihood likert | *"Why did you choose that option?"* |
| Multi-select desirability | *"Why did you choose those options?"* |
| Click test | *"Why did you click there?"* |
| NPS | *"Why did you choose that option?"* |

**The comprehension followup is special** — it's the only one that converts a self-rating into a knowledge probe. A user might say "Understood very well" but then fail to describe the company. That gap is the actual finding for marketing/positioning tests.

## 5. The UX metric is the real instrument

Each question can carry a UX metric. The metric — not the question wording — determines what the test is measuring. Metrics seen across these 15 tests:

`comprehension`, `engagement`, `success`, `desirability`, `sentiment`, `intent`, `likelihood`, `satisfaction`, `frequency`, `loyalty`

Non-obvious metric choices worth noticing:

- **A press-room/media site test in the corpus uses `satisfaction`** (via impression likerts) rather than `success`. This signals the team's actual goal was *"does the press feel served by this site"* rather than *"can journalists find things,"* even though most of the test is findability. The metric clarifies intent that the questions alone don't.
- **An investment-platform test uses `frequency`** — unique in the batch. Q5 asks "How often would you use a platform like this?" — a retention proxy, not a one-shot intent. Worth replicating for stickiness-sensitive products.
- **The the fixed-template series uses `intent` and `desirability` as separate metrics on adjacent questions, and watches them diverge.** V5 scored high on engagement (92) and desirability (87) but tanked on intent (38). That divergence *is* the finding.

## 6. Audience definitions are a strategic statement

Audience lists are deliberately built to mirror who the design is for. They're not generic.

| Test | Audience | What it tells you |
|---|---|---|
| a press-room site | 7 segments of journalists, bloggers, vloggers, social media marketers | Built for press, tested by press |
| the hunting-apparel store | "Hunting Apparel Consumers" (sole segment) | Niche audience, narrow target |
| 145 seasonal invites | 6 overlapping event-planner / wedding-planner / host segments | The buyer is one of several adjacent personas |
| a veteran careers landing page | Banking, credit-card, credit-union users | Adjacent audience — not literally veterans. Deliberate choice. |
| a campaign page run three ways — [Consumers] / [SMB Owners] / [Strangers] | Same test, three audiences | Audience-fanout testing |

**Audience-fanout testing** (running identical tests across multiple audiences) is itself a method. the homepage-baseline project uses it deliberately to see how the same page lands for different buyer types.

## 7. Two iteration methodologies

Comparing the the evolving-flow series and the fixed-template series shows two distinct iteration methods sitting side by side:

| | the fixed-template series (template iteration) | the evolving-flow series (flow evolution) |
|---|---|---|
| Test structure | Fixed 5 Qs across all 6 variants | Shifted: V1–V3 had 8 Qs, V4 dropped to 7 |
| What's compared | Just the screen design | Both the design *and* the flow shape |
| Clean comparison? | Yes — all 6 metric scores directly comparable | Partial — Q-positions shifted between V3 and V4 |
| When to use | A/B/C on the same screen | Funnel redesign where steps get added/removed |

**Heuristic:** if you're A/B-ing within the same screen, lock the test structure (à la 145). If you're refactoring a flow, expect the test to evolve with the design (à la 144), and call out structural drift when comparing variant scores.

## 8. Single-screen vs multi-screen tests are fundamentally different shapes

| | Single-screen | Multi-screen / flow |
|---|---|---|
| Asset count | 1 | 3–7 |
| Examples in this batch | the athletic-apparel homepage, the B2B data-platform homepage, the investment-platform, legacy template series, all fixed-template variants | the hunting-apparel store (3 screens), the press-room site (7), the banking-app prototype, the evolving-flow series |
| Branching | Rarely enabled | Almost always enabled on click tests |
| Question rhythm | Explore → comprehend → react → decide | Each screen gets 1–3 task-oriented Qs |
| What it's measuring | First impression | End-to-end usability |

**Identifying by name:** anything with `>` (e.g. "Homepage > PLP > PDP"), "Flow", "Onboarding", "Dashboard", or a numbered series (e.g. "Q1...Q6") is multi-screen. Anything with just "Homepage" or "Landing Page" is almost always single-screen.

## 9. deep vs light template — the depth/cost tradeoff

Within the homepage-baseline project two template generations coexist:

| Template | Questions | What it captures |
|---|---|---|
| R3 | 4 Qs: familiarity (yes/no) → describe **before** seeing → describe **after** seeing → multi-pick brand impressions | Pre/post comprehension shift — what changed in their understanding from seeing the page |
| R5 | 2 Qs: familiarity (yes/no) → multi-pick brand impressions | Just the impression — no before/after |

R3 is more diagnostically useful (you can see how the page changed understanding) but takes roughly 2× the response time. R5 trades that signal for cheaper iteration. The choice is a cost-per-insight tradeoff worth making consciously per project.

## 10. Branching ≈ "this test has connected screens"

Quick reading heuristic: if branching is enabled on click tests, the test is probably a multi-screen flow where the user's click determines what they see next. If branching is off, it's a single-screen "where would you go?" with no follow-through.

Branching status across this batch:

- **the fixed-template series:** branching on Q1 only (the engagement click test). Other Qs have no follow-through.
- **the evolving-flow series:** branching on the `success` click tests (the path through the flow).
- **The hunting-apparel store:** branching on all 5 click tests (3 connected screens).
- **The investment-platform:** branching on Q2 (the engagement click test).
- **The press-room site:** branching off (each click test is isolated to its screen, not a flow).

## Reading a new report — the 30-second routine

Before reading question-by-question, scan these five things in order. They tell you what the test is for:

1. **Test name** — homepage / landing / PDP / flow / "X > Y > Z"
2. **Intro** — boilerplate or scenario? If boilerplate, read Q1 for context.
3. **Audience** — single niche, fanout across personas, or adjacent audience?
4. **Question count + asset count** — single-screen impression test (5 Qs / 1 asset) vs multi-screen flow (8 Qs / 3+ assets)?
5. **UX metrics in use** — which combination is attached, and where do they diverge across questions?

After that, the question-by-question detail is interpreting variations on a known theme.

## Constructing a new test — quick decision tree

When designing a new test:

**Is it one screen or a flow?**

- One screen → use the 5-Q core template (Section 1).
- A flow → use the multi-screen pattern: 1 engagement click + 1–2 task-oriented success clicks per screen, plus a final reaction question on the last screen.

**Is it an A/B/C iteration or a redesign?**

- A/B/C on the same screen → lock the test structure (fixed-template style).
- Redesigned flow → expect the test to evolve too (evolving-flow style), and document structural drift.

**What's the headline outcome you want?**

- Comprehension → comprehension likert + open-text knowledge probe.
- Findability → success click tests with branching.
- Engagement → engagement click test with many hotspots.
- Purchase / sign-up → likelihood likert + required followup.
- Stickiness → frequency or loyalty metric (NPS or "how often would you use this").

**Who's it for?**

- Single niche audience → one segment.
- Validation across buyer types → audience fanout (same test, multiple audiences).

## What's *not* in this sample

This synthesis is drawn from 15 tests. Patterns to verify if you go deeper:

- **MaxDiff usage** — only seen in two tests in the batch (a content-heavy careers page and the press-room site). Worth pulling more MaxDiff tests to see how it's typically scoped.
- **Card-sort / preference / matrix / point-allocation** — none appeared in this sample. The CLI supports them; whether they're rare or absent in actual usage is unknown.
- **Tests saved as templates** — none in this sample. The platform has a template system that's separate from the iteration pattern documented here.
- **Long tests (>10 Qs)** — only a continuous-experimentation project's "a 15-Q homepage assessment" (15 Qs) appeared as an outlier in the listings. Worth pulling to see if it's a different methodology or just a longer version of the same template.

## Tooling notes

- Pulling test structure + report: `helio-cli tests get <uuid> --output json` and `helio-cli tests report <uuid> --include questions_summary --output json`. Both accept either the test UUID or the report UUID from `https://my.helio.app/report/<uuid>`.
- The CLI requires Node 22+. The shebang resolves to whatever `node` is first in PATH; if your default is older, run `nvm use 22` first.
- Asset URLs in the report are presigned and expire ~30 days from generation. Re-pull to refresh.
- The full asset URL set lives under `questions_summary[*].image_url` / `full_image_url` for question-attached screens, and `questions_summary[*].variations[*].image` for click-test variation screens.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: src-test-pattern-playbook-v0.1 — Test Pattern Playbook v0.1 -->

# The Test Pattern Playbook

Not just *which* test to build, but *when* to build it. Seven templates, mapped to the moment in a project where each one earns its place — reverse-engineered from **285 real tests over five months** (Feb–Jul 2026): 7 shared templates, 61% of tests fit one, ~39% are custom variations. Templates are starting points, not cages.

## When does each test get pulled?

Tests track the arc of a project: cold read → variant sweep → benchmark. Each template lives mostly at one of these moments. Counts are real uses at each stage.

### Stage 01 — First look

*Trigger: new asset, no data yet.* Do people get it, feel it, know where to go?

- **T5 · Homepage Five** — 9 of 9 uses here
- **T2 · MaxDiff Read** — 17 of 24
- **T3 · Shelf & NPS** — 12 of 19
- **T4 · Findability Sweep** — used as the baseline

### Stage 02 — Iterate

*Trigger: V1 · V2 · V3 · Round N.* Lock the shape, change the design, compare scores.

- **T1 · Two-Tap Check** — 8 of 8 uses here
- **T6 · Expectation Probe** — 18 of 25
- **T7 · Flow Expectation** — 20 of 37
- **T4 · Findability Sweep** — 26 of 52

### Stage 03 — Benchmark

*Trigger: a competitor to beat.* Same questions, their screens.

- **T7 · Flow Expectation** — 4 of 7
- **T3 · Shelf & NPS** — 2 of 7

**The first tell — before stage, ask the asset:** one screen → T2 · T3 · T5 · T6 | a connected flow → T1 · T7 | either → T4

## The UX metrics doing the work

Every template is a stack of standardized metric instruments — a "desirability" score means the same thing on a granola box as on a banking app. Across the corpus: 20 distinct metrics, 6 carry ~⅔ of all measurement, 1,241 instruments deployed, 4.4 metrics per test average.

| Family | Metric | Answers | Coverage |
|---|---|---|---|
| Understand | `comprehension` | Do they grasp what it is? | 44% |
| Behave | `engagement` | Where do they go first? | 36% |
| Behave | `success` | Can they complete the task? | 30% |
| Behave | `effort` | How hard did it feel? | 14% |
| Expect | `expectations` ★ | Does it behave as predicted? (most-deployed — 208 uses) | 35% |
| Feel | `sentiment` | How does it feel overall? | 45% |
| Feel | `desirability` | Do they actually want it? | 20% |
| Feel | `satisfaction` | Were they satisfied with it? | 14% |
| Convert | `intent` | Will they take the next step? | 31% |
| Convert | `loyalty` | Would they recommend or return? | 6% |

Long tail (each <10%): usability, appeal, usefulness, frequency, likelihood, quality, occurrence.

**Note:** `expectations` outdeploys its 35% reach (208 uses) because the expectation-heavy templates (T1, T7) fire it on *every screen* — the quantified fingerprint of the "does it behave as predicted?" house style.

## The seven templates

### T5 · Homepage Five — `first look` · `one screen`

**Use when:** a brand-new homepage or landing page you've never tested. Look, comprehend, react, decide, act — in one pass. (9 of 9 uses at first look.)
**Measures:** engagement · comprehension · desirability · intent. **Shape:** `click → likert → multi → likert → multi`.

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | click test | engagement | "You're exploring [category] solutions and come across this. Click where you'd go first." | Why did you click there? |
| 2 | likert | comprehension | "How well do you understand what this company is offering?" | What is this company offering? |
| 3 | multi-select | desirability | "How does this page make you feel about this company?" (Helpful · Innovative · Clear · Joyful · Complicated +3) | Why did you choose those options? |
| 4 | likert | desirability | "How likely would you be to [primary action]?" | Why did you choose that option? |
| 5 | multi-select | intent | "What would you most likely do next from this page?" (real CTAs) | Why did you choose that option? |

### T2 · MaxDiff Read — `first look` · `one screen`

**Use when:** a content-heavy page where you don't know which sections pull. Ranks the parts by interest. (17 of 24 at first look.)
**Measures:** comprehension · desirability · engagement. **Shape:** `likert → max_diff → multi → likert → click`.

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | likert | comprehension | "How well do you understand who this webpage is for?" | Who is this webpage for? |
| 2 | max-diff | — | "What parts of this page are Most and Least Interesting to your [context]?" (sections ranked) | Why did you choose those options? |
| 3 | multi-select | desirability | "How does the information on this page feel to you?" (Helpful · Trustworthy · Clear · Motivating · Unnecessary +3) | Why did you choose those options? |
| 4 | likert | desirability | "How likely would you be to use this site to [primary action]?" | Why did you choose that option? |
| 5 | click test | engagement | "Click where you would go next on this page." | Why did you click there? |

### T3 · Shelf & NPS — `first look` · `benchmark` · `one screen`

**Use when:** judging a product, package, or brand's market appeal — or stacking it against a competitor. Adds recommend-likelihood.
**Measures:** comprehension · desirability · loyalty · occurrence · quality. **Shape:** `likert → multi → likert → nps → likert → likert`.

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | likert | comprehension | "You see this product on the shelf. How well do you understand what it is?" | Describe this product in your own words. |
| 2 | multi-select | desirability | "How do you feel about this product?" (Exciting · Premium · Healthy · Trustworthy · Unappealing +3) | Why did you choose those options? |
| 3 | likert | desirability | "How likely would you be to buy this product?" | Why did you choose that option? |
| 4 | nps | loyalty | "How likely would you be to recommend this product to a friend? (0–10)" | Why? |
| 5 | likert | occurrence | "How often do you purchase [category]?" | — |
| 6 | likert | quality | "How does this product's appearance compare to others you've bought?" | Why did you choose that option? |

### T4 · Findability Sweep — `spans stages` · `either asset`

**Use when:** the workhorse — any page where the question is "can they find or do X?" Broad first click, then targeted task clicks. Baseline through every iteration (first look 20 · iterate 26 — the most-used template, 52 uses).
**Measures:** engagement · success · sentiment · effort. **Shape:** `click → click → click → multi → nps`.

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | click test | engagement | "This is the [page] for a [category] company. Click where you would go first." | Why did you click there? |
| 2 | click test | success | "Click where you would go to [specific task 1]." | — |
| 3 | click test | success | "Click where you would go to [specific task 2]." | — |
| 4 | multi-select | sentiment | "How does this page feel to you?" (Helpful · Innovative · Exciting · Joyful · Incomplete +3) | Why did you choose those options? |
| 5 | nps | effort | "How difficult or easy does it feel to [core task]? (1–7)" | Why did you choose that option? |

### T6 · Expectation Probe — `iterate` · `one screen`

**Use when:** refining a specific name, URL, label, or copy line. Predict-then-reveal: ask what they expect, show it, measure the gap. A V2/V3 tuning tool (18 of 25 in iteration).
**Measures:** expectations · sentiment. **Shape:** `free → likert → multi`.

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | free response | expectations | "There's a part of the site called [X]. What do you expect to find there?" | — |
| 2 | likert | expectations | "The page is [reveal]. How well does this match your expectation?" | Why did you choose that option? |
| 3 | multi-select | sentiment | "How do you feel about this [name/URL]?" (Helpful · Clear · Simple · Useful · Unimportant +3) | Why did you choose those options? |

### T1 · Two-Tap Check — `iterate` · `connected flow`

**Use when:** A/B-ing one interaction step inside an existing flow. Navigate two taps, then rate whether the result met expectations. Never a first look — pure variant sweep (8 of 8 in iteration).
**Measures:** engagement · expectations · sentiment. **Shape:** `click → click → likert → multi`.

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | click test | — | "Imagine you're [context] and come across this page…" | — |
| 2 | click test | engagement | "This is the screen you land on after [tap 1]. Tap where you would go to [change/adjust it]." | — |
| 3 | likert | expectations | "How well did this screen match your expectations?" | Why did you choose that option? |
| 4 | multi-select | sentiment | "What impressions does this flow give you?" (Helpful · Innovative · Simple · Joyful · Complicated +3) | Why did you choose those options? |

### T7 · Flow Expectation — `iterate` · `benchmark` · `connected flow`

**Use when:** validating an end-to-end app flow, step by step — predict, reveal, and task-click at each screen. Also the go-to for benchmarking a competitor's flow (iterate 20 · competitive 4).
**Measures:** expectations · success · sentiment. **Shape:** `free → likert → click → free → likert → click → multi` (the predict-reveal-click triplet repeats per screen).

| # | Type | Metric | Question | Follow-up (required) |
|---|---|---|---|---|
| 1 | free response | expectations | "You just [entered context] on the [screen]. What do you expect to see?" | — |
| 2 | likert | expectations | "This is the [screen]. How well does it match your expectations?" | Why did you choose that option? |
| 3 | click test | success | "Click where you'd go to [primary task]." | — |
| 4 | free response | expectations | "What do you expect to see when you click [next element]?" | — |
| 5 | likert | expectations | "How well does this page match your expectations?" | Why did you choose that option? |
| 6 | click test | success | "Tap where you'd go to [secondary task]." | — |
| 7 | multi-select | sentiment | "How do you feel about this [screen]?" (Helpful · Innovative · Simple · Clear · Busy +3) | Why did you choose those options? |

## Two operating styles, split by reflex

The *when* also depends on who's holding it. The corpus splits into two recognizable operating styles:

| | **Iteration-deep** | **First-look volume** |
|---|---|---|
| Reflex metric | `expectations` (23% of metric use) | `success` + `intent` (12% / 9%) |
| Style | Deeper, multi-screen, iteration-heavy. Owns T1; splits T7. | Leaner, single-screen, first-look volume. Owns T4; drives T2. |
| Median questions | 6 | 4 |
| Multi-screen share | 32% | 24% |
| Distinct shapes | 33 | 88 |

**When ownership shifts** between researchers, shared stage triggers are what keep test timing consistent — the templates travel even when the people change.

## House rules — the templated follow-ups

The score is the headline; the required open-text is the insight. Near-universal pairings — reuse verbatim:

| Question type | Standard follow-up |
|---|---|
| Comprehension likert | "What is this offering?" / "Who is this for?" — a knowledge probe. The gap between rating and answer is the finding. |
| Likelihood / expectations | "Why did you choose that option?" |
| Desirability multi-select | "Why did you choose those options?" — 8 options: a positive set plus a negative tail. |
| Click test | "Why did you click there?" — `engagement` = "where first", `success` = "find X". |

## Method & caveats

The complete test output of two researchers, Feb–Jul 2026, via the Helio public API. Templates are shared question-type sequences; stage inferred from naming (Baseline / V-number / Round / Competitive) and asset count. Read counts as "X of Y at this stage" — T4 and T7 genuinely span stages. ~39% of tests are custom variations. Percentages are share-of-uses, not response scores.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Reading a Helio test they didn't design and need to orient quickly
- Constructing a new test and wants the shape decision tree — or the **stage-based template picker** (first look / iterate / benchmark → T1–T7)
- Asking "what test should I run at this point in the project?" — the playbook's stage triggers answer the *when*, not just the *which*
- Trying to identify which iteration methodology to use (fixed-template vs evolving-flow)
- Curious why a `success` click test and an `engagement` click test look the same but mean different things
- Recognizing audience-fanout testing as a method
- Comparing test versions and wondering whether structural drift makes comparison partial
- Wanting the empirical metric-coverage data (which metrics actually carry the measurement load across 285 real tests)

**Which block to read:** reading/synthesis questions → the Test Patterns block. Construction/timing questions → the Playbook block. The two-tell opener for construction: ask the **asset** first (one screen → T2/T3/T5/T6; connected flow → T1/T7; either → T4), then the **stage**.

For the full build/validate/launch workflow, route to `helio-asset-to-test`. For per-section detail, `helio-section-types`. For metric definitions, `helio-ux-metrics`. For synthesis, `helio-reading-report`.

## Failure modes

- **Reading every Click Test as the same thing.** The metric matters more than the question shape — `engagement` vs `success` are different reads.
- **Comparing variants across the fixed-template vs evolving-flow boundary.** If question positions or counts shifted, the comparison is partial. Surface the structural drift before reporting metric changes.
- **Defaulting to "the 5-Q template" without checking whether the page calls for it.** Multi-screen flows, retention tests, and content prioritization all need different shapes.
- **Treating the audience as an afterthought.** Audience choice is a strategic statement — fanout testing is a method, not noise.
- **Treating the seven templates as cages.** ~39% of the corpus is custom variations; templates are starting points. Match the moment and asset first, then adapt.
- **Automating a click-heavy template end to end.** T1, T4, T5 (and parts of T2/T7) contain click tests, which are UI-only to create. Programmatic builds instantiate the creatable subset and finish hotspots in the web app — see the UI-only boundary checklist in `helio-creating-test`.

## Where to go next

- For the build workflow: `helio-asset-to-test`
- For section types: `helio-section-types`
- For UX metrics: `helio-ux-metrics`
- For branching: `helio-branching`
- For audience: `helio-audience-flow`
- For synthesis: `helio-reading-report`

<!-- /ADDED -->

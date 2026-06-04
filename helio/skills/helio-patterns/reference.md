# Helio Test Patterns — Reference

**Skill:** `helio-patterns`
**Source:** Helio Test Patterns v0.1
**Source last synced:** 2026-05-23

---

<!-- DERIVED FROM: 1G1yPnRDZeY9nKXENSQb_LOkj5T2tdNBU2_DTE1YQ7ts — Helio Test Patterns v0.1 -->

A reference for reading and constructing Helio tests, drawn from a sample of 15 tests across four projects (O2, Test and Learn, Homepage Baselines, Helio Services).

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

This pattern appears verbatim (with order shuffles) in Stoko Homepage v1, Informatica Homepage, StoryTrading Homepage, USAA Veteran Jobs, and all six variants of the O2 "145: Polymorphism PDP" series. The order shifts but the *roles* do not.

**When the order shifts:** if Q1 is a click test rather than a comprehension likert, the test is leading with behavior (where will they look) before opinion (what do they think). Common on PDP / CTA-heavy pages where engagement is the headline outcome.

## 2. Two intros do almost all the work

There are essentially two intro styles across the entire batch:

- **Generic boilerplate:** *"Welcome to our test! We'll use the results to improve the design of our site."* When this appears, the actual scenario is buried in Q1's instructions (e.g., Stoko Q1 starts with *"Imagine you're shopping for athletic apparel"*).
- **Scenario-led:** *"Imagine you're shopping for Galentine's Day invites"* / *"We'll be asking you questions as if you're using a mobile banking app."*

**Reading rule:** when the intro is boilerplate, always read Q1 carefully. The framing lives there, not in the intro.

## 3. Click tests do double duty

Same question type, two completely different intents. The UX metric is the tell:

| Metric | Question shape | What it measures |
|---|---|---|
| `engagement` | "Click where you would go first on this page" | Broad exploration — where does the eye/click land first, with many hotspots possible |
| `success` | "Click where you would go to [specific task]" | Targeted findability — usually 1 primary hotspot, branching usually on, pass/fail framing |

**Example — KUIU Homepage > PLP > PDP:** Q1 is `engagement` (broad, 10 hotspots). Q2, Q4, Q5, Q8 are all `success` (find this specific thing). Q5 scored 12% — a direct red flag that the filter UI on the PLP isn't working. Without the engagement-vs-success distinction in the metric, that signal would be hidden in raw click data.

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

- **Disney Experiences uses `satisfaction`** (via impression likerts) on a press-room/media site. This signals the team's actual goal was *"does the press feel served by this site"* rather than *"can journalists find things,"* even though most of the test is findability. The metric clarifies intent that the questions alone don't.
- **StoryTrading uses `frequency`** — unique in the batch. Q5 asks "How often would you use a platform like this?" — a retention proxy, not a one-shot intent. Worth replicating for stickiness-sensitive products.
- **O2 145 series uses `intent` and `desirability` as separate metrics on adjacent questions, and watches them diverge.** V5 scored high on engagement (92) and desirability (87) but tanked on intent (38). That divergence *is* the finding.

## 6. Audience definitions are a strategic statement

Audience lists are deliberately built to mirror who the design is for. They're not generic.

| Test | Audience | What it tells you |
|---|---|---|
| Disney Experiences | 7 segments of journalists, bloggers, vloggers, social media marketers | Built for press, tested by press |
| KUIU | "Hunting Apparel Consumers" (sole segment) | Niche audience, narrow target |
| 145 Galentine's invites | 6 overlapping event-planner / wedding-planner / host segments | The buyer is one of several adjacent personas |
| USAA Veteran Jobs | Banking, credit-card, credit-union users | Adjacent audience — not literally veterans. Deliberate choice. |
| R5 Campaign Full V1 — [Consumers] / [SMB Owners] / [Strangers] | Same test, three audiences | Audience-fanout testing |

**Audience-fanout testing** (running identical tests across multiple audiences) is itself a method. Homepage Baselines uses it deliberately to see how the same page lands for different buyer types.

## 7. Two iteration methodologies

Comparing the O2 144 series and 145 series shows two distinct iteration methods sitting side by side:

| | 145 series (template iteration) | 144 series (flow evolution) |
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
| Examples in this batch | Stoko, Informatica, StoryTrading, R3/R5 series, all 145 variants | KUIU (3 screens), Disney (7), Credit One, 144 series |
| Branching | Rarely enabled | Almost always enabled on click tests |
| Question rhythm | Explore → comprehend → react → decide | Each screen gets 1–3 task-oriented Qs |
| What it's measuring | First impression | End-to-end usability |

**Identifying by name:** anything with `>` ("KUIU Homepage > PLP > PDP"), "Flow", "Onboarding", "Dashboard", or a numbered series ("Credit One Q1...Q6") is multi-screen. Anything with just "Homepage" or "Landing Page" is almost always single-screen.

## 9. R3 vs R5 — the depth/cost tradeoff

Within Homepage Baselines two template generations coexist:

| Template | Questions | What it captures |
|---|---|---|
| R3 | 4 Qs: familiarity (yes/no) → describe **before** seeing → describe **after** seeing → multi-pick brand impressions | Pre/post comprehension shift — what changed in their understanding from seeing the page |
| R5 | 2 Qs: familiarity (yes/no) → multi-pick brand impressions | Just the impression — no before/after |

R3 is more diagnostically useful (you can see how the page changed understanding) but takes roughly 2× the response time. R5 trades that signal for cheaper iteration. The choice is a cost-per-insight tradeoff worth making consciously per project.

## 10. Branching ≈ "this test has connected screens"

Quick reading heuristic: if branching is enabled on click tests, the test is probably a multi-screen flow where the user's click determines what they see next. If branching is off, it's a single-screen "where would you go?" with no follow-through.

Branching status across this batch:

- **145 series:** branching on Q1 only (the engagement click test). Other Qs have no follow-through.
- **144 series:** branching on the `success` click tests (the path through the flow).
- **KUIU:** branching on all 5 click tests (3 connected screens).
- **StoryTrading:** branching on Q2 (the engagement click test).
- **Disney:** branching off (each click test is isolated to its screen, not a flow).

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

- A/B/C on the same screen → lock the test structure (145-style).
- Redesigned flow → expect the test to evolve too (144-style), and document structural drift.

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

- **MaxDiff usage** — only seen in USAA Veteran Jobs and Disney Experiences. Worth pulling more MaxDiff tests to see how it's typically scoped.
- **Card-sort / preference / matrix / point-allocation** — none appeared in this sample. The CLI supports them; whether they're rare or absent in actual usage is unknown.
- **Tests saved as templates** — none in this sample. The platform has a template system that's separate from the iteration pattern documented here.
- **Long tests (>10 Qs)** — only Test and Learn's "57: Homepage Assessment - New Visitor V3" (15 Qs) appeared as an outlier in the listings. Worth pulling to see if it's a different methodology or just a longer version of the same template.

## Tooling notes

- Pulling test structure + report: `helio-cli tests get <uuid> --output json` and `helio-cli tests report <uuid> --include questions_summary --output json`. Both accept either the test UUID or the report UUID from `https://my.helio.app/report/<uuid>`.
- The CLI requires Node 22+.
- Asset URLs in the report are presigned and expire ~30 days from generation. Re-pull to refresh.
- The full asset URL set lives under `questions_summary[*].image_url` / `full_image_url` for question-attached screens, and `questions_summary[*].variations[*].image` for click-test variation screens.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Reading a Helio test they didn't design and need to orient quickly
- Constructing a new test and wants the shape decision tree
- Trying to identify which iteration methodology to use (145 vs 144)
- Curious why a `success` click test and an `engagement` click test look the same but mean different things
- Recognizing audience-fanout testing as a method
- Comparing test versions and wondering whether structural drift makes comparison partial

For the full build/validate/launch workflow, route to `helio-asset-to-test`. For per-section detail, `helio-section-types`. For metric definitions, `helio-ux-metrics`. For synthesis, `helio-reading-report`.

## Failure modes

- **Reading every Click Test as the same thing.** The metric matters more than the question shape — `engagement` vs `success` are different reads.
- **Comparing variants across the 144-vs-145 boundary.** If question positions or counts shifted, the comparison is partial. Surface the structural drift before reporting metric changes.
- **Defaulting to "the 5-Q template" without checking whether the page calls for it.** Multi-screen flows, retention tests, and content prioritization all need different shapes.
- **Treating the audience as an afterthought.** Audience choice is a strategic statement — fanout testing is a method, not noise.

## Where to go next

- For the build workflow: `helio-asset-to-test`
- For section types: `helio-section-types`
- For UX metrics: `helio-ux-metrics`
- For branching: `helio-branching`
- For audience: `helio-audience-flow`
- For synthesis: `helio-reading-report`

<!-- /ADDED -->

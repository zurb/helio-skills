# From Asset To Test — Reference

**Skill:** `helio-asset-to-test`
**Source:** From Asset To Test v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had one minor AEO-rubric gap (Problem opener). Addressed in the ADDED section at the end of this file.

---

<!-- DERIVED FROM: 1mzj79nyrqDPLqhW1nC4ib7ug5HMbOKfRGJxIgAz8CcA — From Asset To Test v0.1 -->

A prescriptive walkthrough for going from a design (a screenshot, mockup, or live page) to a launched Helio test. Companion to `helio-patterns` — that skill tells you what the patterns *are*; this one tells you how to *use* them.

## The seven steps

| # | Step | Time | Where |
|---|---|---|---|
| 1 | Classify the asset | 1 min | Reading |
| 2 | Name the testable risk | 5 min | Thinking + writing |
| 3 | Pick a template — it names your metric set | 30 sec | `helio-patterns` (T1–T7) |
| 4 | Define the audience | 5 min | `helio-cli audiences list` + UI |
| 5 | Tag the metrics — they build their own sections | 2 min | `--ux-metrics` on create / `--metrics` on `add-ux-metrics` |
| 6 | Customize wording + add what no metric covers | 12 min | `edit-question` / `--questions` |
| 7 | Build, validate, launch | 10 min | `helio-cli tests create` → UI → `send` |

Total: ~35 minutes for a single-screen test once you've done it a few times.

**The order matters.** Steps 5 and 6 used to run the other way — write the questions, then map metrics onto them. That produces hand-written sections that merely *resemble* metrics: they return answer distributions, not 0–100 scores with threshold labels, they aren't comparable across waves, and they don't roll into the Overall Score. Tag first and Helio builds the section with validated, non-leading wording; then you're only customizing what the template didn't hand you. See "Why tag a metric instead of writing your own sections" in `helio-ux-metrics`.

## Step 1 — Classify the asset

Answer four questions:

| Question | Why it matters |
|---|---|
| **Single screen or multi-screen?** | Determines the template family. Multi-screen flows need 1–3 task Qs per screen; single screens use the 5-Q core. |
| **What kind of page?** Homepage / landing / PDP / dashboard / app flow / onboarding | Sets up the Q3 desirability descriptor set and the Q5 next-action choices. |
| **B2C or B2B?** | Changes which outcome metric matters: purchase intent (B2C) vs recommend-to-team (B2B) vs demo intent (B2B-SaaS). |
| **Primary outcome the page is selling?** | The most important answer — it determines Q4 likelihood phrasing and Q5's choice list. |

Write each answer down in one line. You'll reuse them throughout.

## Step 2 — Name the testable risk

This is the step most often skipped, and it's the one that distinguishes a useful test from a templated one.

Ask: **"What's the riskiest assumption about this design? What would I be most surprised by if it failed?"**

Common risks and the questions that probe them:

| Risk | Test treatment |
|---|---|
| Comprehension — "they might not get what this is" | Use a pre/post comprehension variant (T5 with a knowledge probe before and after). Open-text knowledge probe in the comprehension followup. |
| Findability — "the main CTA might be invisible" | Add a targeted `success` Click Test on top of the standard engagement click test. |
| Trust / credibility — "the tone might land as gimmicky" | Tune the Q3 desirability descriptors with both positive *and* negative words that map directly onto the risk (e.g., "Overhyped", "Gimmicky" alongside "Credible", "Useful"). |
| Conversion — "people might enjoy this but not act" | Add Q5's forced next-action multi-select with the page's actual CTAs as choices. The "intent vs desirability divergence" pattern is the diagnostic to watch. |
| Audience fit — "this might land for one persona but not another" | Audience fanout — same test, multiple segments. |
| Dual-product confusion — "they might lose one of the two things being offered" | Comprehension knowledge probe explicitly designed to expose whether respondents name both. |

If you can't name a risk, you probably shouldn't run a test — you'll get a templated report with no decisive finding.

## Step 3 — Pick a template (it names your metric set)

Templates are the canonical T1–T7 in `helio-patterns`, derived from the real test corpus. **Picking one is how you pick your metrics** — each template declares the set it measures, so Step 5 is mostly confirmation rather than a fresh decision.

Decide by shape + stage, not by question count. Ask the asset first, then the stage:

```
One screen?
  ├── Brand-new page, never tested?        → T5 · Homepage Five
  │                                          engagement · comprehension · desirability · intent
  ├── Content-heavy, which parts pull?     → T2 · MaxDiff Read
  │                                          comprehension · desirability · engagement
  ├── Product / package / shelf appeal?    → T3 · Shelf & NPS
  │                                          comprehension · desirability · loyalty · occurrence · quality
  └── Tuning a name, label, or copy line?  → T6 · Expectation Probe   (iterate)
                                             expectations · sentiment

Connected flow?
  ├── A/B-ing one interaction step?        → T1 · Two-Tap Check       (iterate)
  │                                          engagement · expectations · sentiment
  └── End-to-end flow, or a competitor?    → T7 · Flow Expectation    (iterate · benchmark)
                                             expectations · success · sentiment

Either asset, any stage — "can they find or do X?"
                                           → T4 · Findability Sweep   (the workhorse, 52 uses)
                                             engagement · success · sentiment · effort
```

**Tie-breaker:** when in doubt, start with **T5** for a single screen or **T4** when the question is findability, then add specialized questions as needed. Removing a question from a draft is one CLI call (`tests remove-question`); restructuring a launched test is impossible.

**Click-backed metrics need hotspots.** Every metric in the sets above is CLI-taggable as of v0.7.0, including `engagement` and `success` — but those two build a click section, and a click section with no hotspots scores zero. Pass them inline when you tag: `--ux-metrics-json '[{"type":"engagement","sections":[{"asset_id":<id>,"hotspots":[{"name":"Primary CTA","x":0.1,"y":0.2,"width":0.3,"height":0.08}]}]}]'`. The CLI warns at create time if a click-backed metric has none.

**Stage check:** T1, T6, and T7 are iteration tools — they assume a locked shape and a prior round. Never open a cold read with them. Full stage-by-stage counts and the per-slot question tables are in `helio-patterns`.

## Step 4 — Define the audience

Two decisions:

1. **Single segment or fanout?** Run identical tests across multiple personas when you don't know which audience is the *real* target, or when the same page has to serve multiple buyer types. Otherwise pick one segment that mirrors who the design is for.
2. **Use a prebuilt segment or upload a custom list?** Helio has many prebuilt audiences. For niche audiences (e.g., "Hunting Apparel Consumers") it's usually a prebuilt. For specific clients/companies, use `custom-lists`.

Audience selection on the CLI:

```shell
helio-cli audiences list                     # see what's available
helio-cli audiences get <audience-uuid>      # confirm match
helio-cli tests create --audiences <uuid> <uuid> ...   # multi = fanout
```

**Note:** The CLI accepts `--audiences <ids...>` at create time. Browsing the actual catalog and choosing live-mode pricing is still typically done in the Helio UI. For full audience setup depth, use `helio-audience-flow`.

## Step 5 — Tag the metrics (they build their own sections)

Your template named the metric set in Step 3; this step tags it so Helio builds those sections for you, with validated wording, before you write anything by hand.

```shell
# T5 · Homepage Five, on create
helio-cli tests create --project-id <uuid> --name "..." --intro "..." \
    --target-audience-size 100 \
    --ux-metrics comprehension desirability intent \
    --ux-metric-context "this homepage"

# or onto an existing draft
helio-cli tests add-ux-metrics <test-uuid> --metrics comprehension desirability intent
```

`--ux-metric-context` replaces the generic noun in every generated instruction — set it once, then read each generated question aloud to confirm the noun works in *all* of them ("purchase this homepage" is what failure sounds like).

**What metrics can't build, and you'll hand-write in Step 6:** MaxDiff section-ranking and any question specific to your risk. Standalone click tests are still hand-built (`--type click_test --asset-id --hotspots`), but if the click test exists to feed `engagement` or `success`, tag the metric instead and give it hotspots inline — the tag builds the section for you.

**Non-obvious metric choices**, when the template's default set doesn't fit the risk you named in Step 2:

| If the design's goal is… | Pick this metric |
|---|---|
| Retention / stickiness | `frequency` |
| Affective satisfaction with a flow | `satisfaction` |
| Brand-level loyalty | `loyalty` (NPS) |
| Findability of a specific affordance | `success` (targeted click test) |
| Conversion likelihood | `intent` |
| First impression strength | `engagement` (broad click test) |

**If you need the same metric twice** (e.g. `expectations` on three screens), just tag it repeatedly — supported since v0.7.0, and each instance is scored on its own. See `helio-ux-metrics`.

For the full per-metric reference, use `helio-ux-metrics`.

## Step 6 — Customize wording, add what no metric covers

Most tests follow their template's shape; this step tunes the generated wording and adds the sections metrics can't build. Edit a metric-built section in place with `tests edit-question <test-id> <section-id> --instructions "..."` (omit `--type` to keep the metric attached).

### Question shapes by slot

The T5 shape, with each slot's source. Slots marked *(metric-built)* already exist after Step 5 — you're only adjusting wording.

| Slot | Source | Standard text |
|---|---|---|
| Q1 — Comprehension Likert | *(metric-built:* `comprehension`*)* | "How well do you understand what this company offers?" |
| Q1 followup (open-text) | *(metric-built)* | "What does this company do?" — or for dual-product pages, "What does this company do, and what can they offer you?" |
| Q2 — Engagement click test | hand-built (`--type click_test --asset-id`) | "Click where you would go first on this page." |
| Q3 — Desirability multi-select | *(metric-built:* `desirability`*)* | "How does this feel?" with descriptor set tuned to the risk |
| Q4 — Likelihood Likert | *(metric-built:* `desirability`*)* | The verb matches the page's actual conversion outcome (see table below) |
| Q5 — Next action | *(metric-built:* `intent`*)* | NPS for consumer pages; forced multi-select of actual CTAs for B2B |

### Q4 verb by page type

| Page type | Q4 verb |
|---|---|
| E-commerce homepage / PDP | "purchase from this site" / "buy this product" |
| SaaS marketing page | "request a demo of this platform" |
| Agency / services page | "share this with someone on your team" / "reach out about a project" |
| Game / utility / content | "use a platform like this" / "play a game like this" |
| Onboarding | "complete this sign-up flow" |

Followup: always required, always *"Why did you choose that option?"*

### Q5 — Commit / next-action

For most B2B pages, replace the standard NPS with a forced-choice next-action multi-select. List the **actual CTAs from the page** as choices, plus a "None of these" escape hatch. This is the load-bearing question for any page with multiple competing CTAs.

If the page is a pure consumer surface with one clear conversion, use NPS instead.

## Step 7 — Build, validate, launch

### The minimum-viable create command

```shell
helio-cli tests create \
    --project-id <project-uuid> \
    --name "Signal Blitz Homepage" \
    --intro "Imagine you're a product designer looking for new ways to test your UX." \
    --target-audience-size 100 \
    --audiences <audience-uuid> \
    --questions @questions.json
```

Where `questions.json` is a file containing the question array. This is much cleaner than inline JSON for anything beyond two questions.

### After create — iterate on the draft

The CLI lets you edit drafts cleanly:

```shell
helio-cli tests order <test-uuid>                           # see current order
helio-cli tests add-question <test-uuid> ...                # add more
helio-cli tests edit-question <test-uuid> <section-uuid> ... # edit
helio-cli tests remove-question <test-uuid> <section-uuid>  # remove
helio-cli tests reorder <test-uuid> --order section:<uuid> ... # reorder
helio-cli tests preview <test-uuid>                          # human-readable summary
helio-cli tests validate <test-uuid>                         # check readiness to launch
```

### The asset gap

*Capability boundaries move — verify with `helio-cli update --check` before telling anyone something can't be done. Accurate as of helio-cli 0.6.0.*

Most of this gap has closed:

- **Image upload** — CLI-native since v0.1.1 (`assets upload <file>`, jpg/jpeg/png/gif, max 10MB; find IDs with `assets list`; attach with `--asset-id`).
- **Click tests, hotspots included** — CLI-native since v0.4.0. `--type click_test --asset-id <id>` builds an engagement heatmap; add `--hotspots '[{"name":"...","x":0.1,"y":0.2,"width":0.3,"height":0.05,"priority":"Primary"}]'` (relative 0–1 coordinates) for a success click test.
- **Branching** — CLI-native since v0.4.0 on single-select multiple_choice (`--branching`, forward-only skips or `end_test`). Requires a Helio Enterprise account.

What still needs the web UI: **video and audio upload**, **audience segment creation**, **prototype and tree tests**, and **a second instance of a metric already tagged on the test** (the API rejects the duplicate even though the platform scores multiple instances). Note also that branch targets and hotspot definitions aren't readable back through the API yet, so verify those visually in the UI.

For depth on asset handling, use `helio-assets`. For branching path config, use `helio-branching`.

### Launch

```shell
helio-cli tests validate <test-uuid>
helio-cli tests send <test-uuid>
```

Once sent, the structure is locked. Don't `send` until validate passes clean and preview matches your intent.

## Worked example — Signal Blitz homepage

Running the full workflow on the Signal Blitz / Outside The Layouts landing page.

### Step 1 — Classify

- Single screen, long-scroll. One asset.
- Marketing landing page promoting two things at once: a game (*Signal Blitz*) and an agency (*Outside The Layouts*).
- B2B-ish — agency wants project conversations; game is the lead magnet.
- Primary outcome the page is selling: **debatable** (game adoption vs agency contact). This is itself a finding the test should expose.

### Step 2 — Risk

Three candidate risks, ranked:

1. **Dual-product comprehension** — visitors might internalize only the game or only the agency, not both. (Highest risk.)
2. **Tone / credibility** — "vibe-coded with AI" framing might land as gimmicky to the design audience.
3. **CTA confusion** — five competing CTAs (Play, Leaderboard, Cheatsheet, Build Story, Contact). Which wins?

### Step 3 — Template

Single screen, never tested, impression + intent + dual-CTA risk → **T5 · Homepage Five** (`engagement · comprehension · desirability · intent`) with two adaptations:

- Q1 followup as dual-knowledge probe ("…and what can they offer you?")
- Q5 forced next-action with all five CTAs + "None of these"

### Step 4 — Audience

Primary: Product Designers (US). Secondary fanout: UX Researchers, Design Managers. Maybe a "non-designer marketing/product lead" segment as a counterpoint to test whether the methodology language is too in-group.

### Step 5 — Tag the metrics

T5's set, with the context noun set once so every generated instruction reads naturally:

```shell
helio-cli tests create --project-name "Helio Services" \
    --name "Signal Blitz Homepage v1" --intro "..." --target-audience-size 100 \
    --ux-metrics comprehension desirability intent \
    --ux-metric-context "this homepage"
```

That builds the comprehension Likert, the desirability multi-select and likelihood Likert, and the intent multi-select — validated wording, scored, comparable across waves. Only the engagement click test is left to hand-build.

### Step 6 — Customize

Add what no metric builds, then tune the generated wording in place:

```shell
# the one hand-built section — engagement click test on the homepage asset
helio-cli tests add-question <test-uuid> --type click_test --position 2 \
    --instructions "Click where you would go first on this page." \
    --asset-id <asset-id> \
    --followup "Why did you click there?" --followup-required

# dual-knowledge probe on the comprehension followup (metric stays attached: no --type)
helio-cli tests edit-question <test-uuid> <section-id> \
    --followup "What does this company do, and what can they offer you?" --followup-required

# the five real CTAs on the intent question, plus an escape hatch
helio-cli tests edit-question <test-uuid> <section-id> \
    --choices "Play the game" "See the leaderboard" "View the 28-metric cheatsheet" \
              "Read about the build process" "Contact the team about a project" "None of these"
```

Metric coverage per question: `comprehension`, `engagement`, `desirability`, `desirability`, `intent`.

The desirability pair is deliberate — the multi-select reads the feeling, the likelihood Likert reads the commitment, and watching them diverge is the test's headline diagnostic. (Both come from the one `desirability` tag, which builds two sections. If you ever need the *same* metric tagged twice, see the note in Step 5.)

### Step 7 — Build

```shell
helio-cli tests create \
    --project-name "Helio Services" \
    --name "Signal Blitz Homepage v1" \
    --intro "Imagine you're a product designer looking for new ways to test your UX. You come across this page." \
    --target-audience-size 100 \
    --audiences <designer-uuid> <ux-researcher-uuid> \
    --questions @signal-blitz-questions.json

helio-cli assets upload signal-blitz-homepage.png   # -> asset id

helio-cli tests add-ux-metrics <test-uuid> --metrics comprehension desirability intent
helio-cli tests preview <test-uuid>
helio-cli tests validate <test-uuid>
helio-cli tests send <test-uuid>
```

## Pre-launch checklist

Before `tests send`:

- [ ] Intro is scenario-led or Q1 carries the scenario.
- [ ] Comprehension followup is a knowledge probe, not an opinion.
- [ ] Click test directives are unambiguous (one specific affordance per `success` click).
- [ ] Q3 descriptor set has both positive *and* negative words mapped to the risk.
- [ ] Q4 verb matches the page's actual conversion outcome.
- [ ] Q5 choices are the page's *actual* CTAs (not generic ones).
- [ ] Every measurement is a **tagged metric**, not a hand-written look-alike — anything hand-built should be there because no metric covers it (click test, MaxDiff, a risk-specific probe), not because it was quicker to type.
- [ ] The metric set matches the template you chose in Step 3.
- [ ] The context noun reads naturally in *every* generated instruction (read them aloud).
- [ ] Audience matches who the design is for (or is a deliberate fanout).
- [ ] `helio-cli tests preview` reads like a real test to you.
- [ ] `helio-cli tests validate` passes.

After launch:

- [ ] Note expected analysis: which metric divergences you'll be watching for, which followup themes you'll be reading.
- [ ] If audience fanout, plan how you'll compare results across segments.

## What this workflow doesn't yet cover

- **Asset upload via API** — landed for images in helio-cli v0.1.1 (`assets upload`, jpg/jpeg/png/gif, max 10MB; attach with `--asset-id`). For image-based tests, Step 7's upload detour is gone. Video/audio upload remains UI-only.
- **Hotspot region definition** — CLI-native since v0.4.0 (`--hotspots`, relative 0–1 coordinates). Hotspots aren't readable back through the API yet, so confirm placement visually in the UI.
- **Branching path config** — also UI-only. For complex prototype flows this is the biggest remaining manual step.
- **Reading the resulting report** — covered in `helio-reading-report`.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem-opener gap) -->

## What this solves

Without a defined workflow, teams either skip the test-build steps that matter (audience targeting, follow-ups, validation) or invent ad-hoc ones — both produce tests that look thorough but don't answer the actual question. This is the workflow so the build is deliberate and the test produces a decision-grade signal.

## When to use

Reach for this skill when the user is:

- Starting from a design (screenshot, mockup, prototype) and needs to launch a test
- Stuck on which template to pick
- Asking what the right question shape is for their page type
- Approaching `tests send` and wants the pre-launch sanity check
- Confused about which steps are CLI-runnable vs UI-only

For single-aspect depth, drop into sibling skills (sections, metrics, audience, branching). For reading the result, route to `helio-reading-report`.

## Failure modes

- **Skipping Step 2.** "What's the riskiest assumption" is the step that makes the test useful. Skip it and you get a templated report with no finding.
- **Picking the template by question count.** Pick by shape + goal. Question count is downstream.
- **Forgetting the dual-knowledge probe** on dual-product pages. The Comprehension followup needs to expose whether respondents name both things.
- **Generic Q5 choices.** "Learn more / Sign up / Other" tells you nothing. Use the page's actual CTAs.
- **Sending before validating.** `validate` catches real config issues. `send` locks the structure permanently.
- **Assuming a ceiling that has moved.** Click tests, hotspots, and branching all became CLI-native in v0.4.0; image upload in v0.1.1. Run `helio-cli update --check` before telling a user something requires the web app — a stale binary reports its own limits as the tool's.

## More worked examples (beyond Signal Blitz)

Quick shape-references for the most common test types — drawn from the corpus in `helio-patterns`. Use these as templates to copy from when designing a new test.

### An athletic-apparel DTC homepage v1 — Marketing page eval (T5 · Homepage Five)

E-commerce landing page, athletic-apparel shoppers.

- **Risk:** does the value prop read clearly enough to drive purchase intent?
- **Audience:** US athletic-apparel shoppers (single segment)
- **Template:** T5 · Homepage Five
- **Section order:** Click test → Comprehension Likert → Desirability multi-select (8 descriptors) → Likelihood Likert (purchase) → NPS
- **Metrics:** `engagement` → `comprehension` → `desirability` → `desirability` → `loyalty`
- **Headline read:** Desirability 87 / NPS 14 — liked but not advocated. Next test: share-moment design.

### A veteran careers landing page — Content prioritization (T2 · MaxDiff Read)

Careers page, content-heavy.

- **Risk:** which page sections actually pull job-seekers?
- **Audience:** Banking, credit-card, credit-union users — adjacent audience, not literal veterans
- **Template:** T2 · MaxDiff Read (MaxDiff insert at Q2)
- **Section order:** Comprehension Likert → **MaxDiff** (best/worst on page sections) → Desirability → Likelihood (use this site) → Click test (next step)
- **Metrics:** `comprehension` → (no metric on MaxDiff — uses raw best/worst counts) → `desirability` → `desirability` → `engagement`
- **Headline read:** MaxDiff revealed which sections to lead with vs. demote. Action: reorder hero content.

### A hunting-apparel Homepage → PLP → PDP flow — Multi-screen flow eval

Niche hunting-apparel shoppers, 3 connected screens.

- **Risk:** can hunters complete the buy flow?
- **Audience:** Hunting Apparel Consumers (single niche segment)
- **Template:** Multi-screen flow — 1 engagement click + 1–2 success clicks per screen
- **Section order:** 5 Click Tests with branching ON; Q1 is `engagement`; Q2/Q4/Q5/Q8 are `success` on specific affordances
- **Metrics:** `engagement` (Q1) → `success` (Q2/Q4/Q5/Q8)
- **Headline read:** Q5 `success` at 12% — PLP filter UI essentially invisible. Action: elevate the filter to a primary control.

### A press-room site — Press-room with `satisfaction` as intent disclosure

Multi-segment audience, evaluation-style test.

- **Risk:** does the press feel served, not just informed?
- **Audience:** 7-segment fanout — journalists, bloggers, vloggers, social-media marketers
- **Template:** Multi-screen with impression Likerts tagged `satisfaction`
- **Metric tell:** Most questions look like findability, but the `satisfaction` metric says "make press feel taken care of" was the real goal. Picking the right metric here disclosed what the team actually cared about.

## Where to go next

- For section types in step 6: `helio-section-types`
- For metric selection in steps 3 and 5: `helio-ux-metrics`
- For audience setup in step 4: `helio-audience-flow`
- For branching config in step 7: `helio-branching`
- For asset handling in step 7: `helio-assets`
- For recognizing test shapes by pattern: `helio-patterns`
- For reading the resulting report: `helio-reading-report`
- For CLI command depth: `helio-cli`

<!-- /ADDED -->

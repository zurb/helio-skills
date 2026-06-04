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
| 3 | Pick a template | 30 sec | Decision tree below |
| 4 | Define the audience | 5 min | `helio-cli audiences list` + UI |
| 5 | Customize the questions | 15 min | Drafting |
| 6 | Attach UX metrics | 1 min | Mapping (see `helio-ux-metrics`) |
| 7 | Build, validate, launch | 10 min | `helio-cli tests create` → UI → `send` |

Total: ~40 minutes for a single-screen test once you've done it a few times.

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
| Comprehension — "they might not get what this is" | Use the R3 pre/post variant. Open-text knowledge probe in the comprehension followup. |
| Findability — "the main CTA might be invisible" | Add a targeted `success` Click Test on top of the standard engagement click test. |
| Trust / credibility — "the tone might land as gimmicky" | Tune the Q3 desirability descriptors with both positive *and* negative words that map directly onto the risk (e.g., "Overhyped", "Gimmicky" alongside "Credible", "Useful"). |
| Conversion — "people might enjoy this but not act" | Add Q5's forced next-action multi-select with the page's actual CTAs as choices. The "intent vs desirability divergence" pattern is the diagnostic to watch. |
| Audience fit — "this might land for one persona but not another" | Audience fanout — same test, multiple segments. |
| Dual-product confusion — "they might lose one of the two things being offered" | Comprehension knowledge probe explicitly designed to expose whether respondents name both. |

If you can't name a risk, you probably shouldn't run a test — you'll get a templated report with no decisive finding.

## Step 3 — Pick a template

Decide by shape + goal, not by question count.

```
Single screen?
  ├── Quick brand impression only? → R5 (2 Qs)
  ├── Need pre/post comprehension shift? → R3 (4 Qs)
  ├── Standard impression + intent? → Core 5-Q
  └── Need to rank page sections by interest? → Core 5-Q + MaxDiff insert

Multi-screen flow?
  ├── Linear walkthrough (A → B → C)? → 1 engagement click + 1–2 success
  │   clicks per screen + reaction likert on final screen
  ├── Prototype with branching paths? → Same shape, branching ON, define
  │   hotspot paths in UI
  └── Onboarding or setup flow? → Per-step expectation likert
      + completion click test
```

**Tie-breaker:** when in doubt, start with the **Core 5-Q** and add specialized questions (MaxDiff, success click, R3 pre/post probe) as needed. Removing a question from a draft is one CLI call (`tests remove-question`); restructuring a launched test is impossible.

For the test shape catalog, use `helio-patterns`.

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

## Step 5 — Customize the questions

This is the longest step. Most tests follow one of the templates from Step 3, but every test needs question-text customization.

### Question shapes by slot

| Slot | Standard text |
|---|---|
| Q1 — Comprehension Likert | "How well do you understand what this company offers?" |
| Q1 followup (open-text) | "What does this company do?" — or for dual-product pages, "What does this company do, and what can they offer you?" |
| Q2 — Engagement click test | "Click where you would go first on this page." |
| Q3 — Desirability multi-select | "How does this feel?" with descriptor set tuned to the risk |
| Q4 — Likelihood Likert | The verb matches the page's actual conversion outcome (see table below) |
| Q5 — Next action | NPS for consumer pages; forced multi-select of actual CTAs for B2B |

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

## Step 6 — Attach UX metrics

Mostly mechanical — map each question to its standard metric. The non-obvious choices to flag:

| If the design's goal is… | Pick this metric |
|---|---|
| Retention / stickiness | `frequency` |
| Affective satisfaction with a flow | `satisfaction` |
| Brand-level loyalty | `loyalty` (NPS) |
| Findability of a specific affordance | `success` (targeted click test) |
| Conversion likelihood | `intent` |
| First impression strength | `engagement` (broad click test) |

CLI:

```shell
helio-cli tests add-ux-metrics <test-uuid> \
    --metrics comprehension desirability intent
```

For the full per-metric reference, use `helio-ux-metrics`.

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

The CLI **cannot upload screen images or define hotspots**. These steps must happen in the Helio web UI:

1. Upload the screenshot(s) to the test.
2. Attach each screen to its corresponding click test or stimulus question.
3. Draw the hotspot regions on each click test.
4. Configure branching paths (if a multi-screen flow).

After those UI steps, return to the CLI to validate and send.

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

Single screen + standard impression + intent + dual-CTA risk → **Core 5-Q with two adaptations**:

- Q1 followup as dual-knowledge probe ("…and what can they offer you?")
- Q5 forced next-action with all five CTAs + "None of these"

### Step 4 — Audience

Primary: Product Designers (US). Secondary fanout: UX Researchers, Design Managers. Maybe a "non-designer marketing/product lead" segment as a counterpoint to test whether the methodology language is too in-group.

### Step 5 — Customize

```json
[
  {
    "type": "likert",
    "instructions": "How well do you understand what this company offers?",
    "scale_type": "comprehension",
    "followup_question": "What does this company do, and what can they offer you?",
    "enable_followup": true,
    "followup_required": true
  },
  {
    "type": "click_test",
    "instructions": "Click where you would go first on this page."
  },
  {
    "type": "multiple_choice",
    "instructions": "How does this company's offering feel to you?",
    "choices": [
      "Credible", "Useful", "Innovative", "Playful",
      "Gimmicky", "Self-promotional", "Overhyped", "Confusing"
    ],
    "allow_multiple": true,
    "followup_question": "Why did you choose those options?",
    "enable_followup": true,
    "followup_required": true
  },
  {
    "type": "likert",
    "instructions": "How likely would you be to share this with someone on your team?",
    "scale_type": "likelihood",
    "followup_question": "Why did you choose that option?",
    "enable_followup": true,
    "followup_required": true
  },
  {
    "type": "multiple_choice",
    "instructions": "What would you most likely do next from this page?",
    "choices": [
      "Play the game",
      "See the leaderboard",
      "View the 28-metric cheatsheet",
      "Read about the build process",
      "Contact the team about a project",
      "None of these"
    ],
    "allow_multiple": false,
    "followup_question": "Why did you choose that option?",
    "enable_followup": true,
    "followup_required": true
  }
]
```

### Step 6 — Metrics

Per question: `comprehension`, `engagement`, `desirability`, `intent`, `intent`.

The two `intent` slots are deliberate — Q4 measures share/recommend likelihood, Q5 measures stated next action. Watching them diverge is the test's headline diagnostic.

### Step 7 — Build

```shell
helio-cli tests create \
    --project-name "Helio Services" \
    --name "Signal Blitz Homepage v1" \
    --intro "Imagine you're a product designer looking for new ways to test your UX. You come across this page." \
    --target-audience-size 100 \
    --audiences <designer-uuid> <ux-researcher-uuid> \
    --questions @signal-blitz-questions.json

# UI: upload signal-blitz-homepage.png, attach to Q2's click test, draw hotspots
# UI: optionally set branching off (single-screen test)

helio-cli tests add-ux-metrics <test-uuid> --metrics comprehension engagement desirability intent
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
- [ ] UX metrics are attached to all measurement questions.
- [ ] Audience matches who the design is for (or is a deliberate fanout).
- [ ] `helio-cli tests preview` reads like a real test to you.
- [ ] `helio-cli tests validate` passes.

After launch:

- [ ] Note expected analysis: which metric divergences you'll be watching for, which followup themes you'll be reading.
- [ ] If audience fanout, plan how you'll compare results across segments.

## What this workflow doesn't yet cover

- **Asset upload via API** — currently UI-only. If/when the API exposes this, Step 7 collapses into a single CLI invocation.
- **Hotspot region definition** — also UI-only. Worth investigating whether the Helio API has a hotspot endpoint that could be scripted from a JSON spec.
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
- **Forgetting the UI-only steps.** Asset upload, hotspot drawing, and branching path config don't happen via the CLI. Plan for them in the workflow.

## Where to go next

- For section types in step 5: `helio-section-types`
- For metric attachment in step 6: `helio-ux-metrics`
- For audience setup in step 4: `helio-audience-flow`
- For branching config in step 7: `helio-branching`
- For asset handling in step 7: `helio-assets`
- For recognizing test shapes by pattern: `helio-patterns`
- For reading the resulting report: `helio-reading-report`
- For CLI command depth: `helio-cli`

<!-- /ADDED -->

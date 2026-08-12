# Creating a Helio Test — Reference

**Skill:** `helio-creating-test`
**Source:** Creating a Helio Test v0.3 (v0.1 archived)
**Source last synced:** 2026-07-06
**Notes:** Customer engagement names in the source doc were replaced with anonymized category descriptors during the skill build (same pattern as marketplace v0.3.2): the athletic-apparel DTC homepage, the B2B SaaS data-platform homepage, the banking app's Accounts & Dashboard flow, the veteran careers landing page.

---

<!-- DERIVED FROM: src-creating-a-helio-test-v0.3 — Creating a Helio Test v0.3 -->

This is how you create a Helio test that produces a signal worth using — one a designer, a PM, or a leader can carry into a Design Review and act on. Not just "ran a study." A signal tied to a hunch, a metric, and a decision.

Three other skills cover what comes around this: `helio-app` (what the platform is, what it measures, how to engage), `helio-mcp` (how to drive Helio from an AI assistant), and `helio-cli` (how to drive Helio from a script). This one covers the part those don't: **how to design the test itself.**

## What this solves

Most teams run research and end up with data that's interesting but doesn't move anything. The deck gets shared. The decision still gets made on a hunch.

The fix isn't more data. It's a tighter chain between the question you started with, the test you ran, and the signal you carried back. Helio supports that chain natively if you set up the test right. This doc names what right looks like.

## The chain

Every good Helio test runs the same arc:

1. **Hunch** — what you believe and want to test
2. **Shape** — which pattern of test fits the hunch
3. **Test** — the questions, the audience, the metrics
4. **Signal** — what comes back, what it means, what to do with it

Each step constrains the next. Skip the hunch and you can't write the right questions. Pick the wrong shape and you collect the wrong metrics. Don't tie the signal back to a hunch and the result has nowhere to land.

## The four shapes

Zurb's own tests use four recurring shapes. Lead with shape, not theory — the shape decides almost everything else.

### Marketing page eval (5 questions)

For a single landing page, homepage, or content page. The team needs to know whether it lands and whether it moves people forward.

The arc:

1. Click test — where do people go first?
2. Likert (comprehension) — do they understand what's offered?
3. Multi-select (desirability) — what does it feel like?
4. Likert (likelihood) — would they take the action?
5. NPS or next-action — would they advocate / what would they do next?

Real examples: the athletic-apparel DTC homepage, the B2B data-platform homepage. The veteran careers landing page uses this shape with MaxDiff swapped in — see *Content prioritization* below.

### Multi-screen flow eval (6–8 questions)

For prototypes or app flows. The team needs to know whether the screens land and whether users can complete key tasks.

The arc, repeated per screen:

1. **Expectation baseline** (open-text, no asset) — what do you expect to see?
2. **Reveal + match** (Likert against the expectation) — how well does this match?
3. **Findability** (click test with hotspots, branching enabled) — where would you go to do X?

Close with a desirability check (multi-select).

Real example: the banking app's Accounts & Dashboard flow — 7 questions across two screens.

### Content prioritization (5 questions with MaxDiff)

For content-heavy pages where the editorial decision — which sections matter most — is on the table.

The arc:

1. Likert (comprehension) — who is this for?
2. **MaxDiff (best/worst scaling)** — which sections are most/least interesting?
3. Multi-select (desirability) — how does it feel?
4. Likert (likelihood) — would you use this?
5. Click test — where would you go next?

Real example: the veteran careers landing page — MaxDiff produced a ranked list of which sections actually pull job-seekers.

⚠ MaxDiff results need raw best/worst counts, not aggregated percentages. The averaged percentages will show 0% on every item — that's not "nothing happened," that's the wrong view of the data.

### Concept comparison (variable)

For deciding between two design directions when both have champions.

The arc:

1. Show A — comprehension, desirability, likelihood
2. Show B — same questions
3. Forced choice — which would you use?
4. Why

Use this when "we keep circling between two directions" is the real problem.

## Pick your shape

A short decision rule:

- **Single page, single context?** → Marketing eval
- **Prototype with multiple screens or a flow?** → Multi-screen flow
- **Page with lots of content sections competing for attention?** → Content prioritization
- **Two competing design directions?** → Concept comparison

If two shapes feel possible, pick the simpler one. The marginal extra signal from a longer test isn't worth the dropout risk and the synthesis cost.

## Anchor the test in a hunch

Before you write a question, write the hunch — the thing you actually want to confirm or kill. Glare's template:

*We believe that [change] for [audience] will [impact] because [reason].*

Without this, the test produces "interesting findings" that don't enable a decision.

Worked example (the athletic-apparel homepage):

*We believe that the new homepage will drive purchase intent for athletic apparel shoppers because the value prop reads clearly within the first screen.*

Now every question on the test is anchored:

- **Q2 (comprehension)** tests "reads clearly"
- **Q3 (desirability)** tests whether the read is positive
- **Q4 (likelihood)** tests "drives purchase intent"
- **Q5 (NPS)** checks whether the signal travels (advocacy)

If a question doesn't tie to the hunch, drop it. If the hunch can't be tied to a question shape, the hunch isn't testable yet — go back to it.

## Pick UX metrics

These are the metrics actually used in Zurb's tests. Each is also a Glare UX metric type, so the signal slots back into the framework cleanly.

| Helio metric | Glare type | What it captures |
|---|---|---|
| **Expectations** | Attitudinal | Did the design match what users came in expecting |
| **Comprehension** | Attitudinal | Do users understand what it is, what it offers, who it's for |
| **Engagement** | Behavioral | First-click attention — where the eye goes |
| **Desirability** | Attitudinal | Emotional reaction — does it feel right |
| **Intent / Likelihood** | Attitudinal | Would they take the action |
| **Loyalty (NPS)** | Attitudinal | Would they recommend |
| **Completion / Success** | Behavioral | Can they actually do the task |

Rules of thumb:

- **One metric per question.** If a question carries two metrics, it carries neither well.
- **Behavioral + attitudinal together.** A click test alone tells you what happened; pair it with a "why did you click there?" followup so you know what they meant.
- **Expectations is its own move.** Use it when the design is supposed to land a specific reveal (the banking-app flow pattern), not by default.
- **Let the metric build the section when it can.** Tagging a metric auto-generates its validated section structure (wording, scale, choice text) — a scored, wave-comparable section for zero writing effort. The hand-written prompts in this doc's templates earn their custom wording (asset-specific context, a reveal to land); when yours doesn't, tag the metric and set the context noun instead of writing a near-copy — a look-alike section you write yourself produces a distribution, not a score, and stays out of the Overall Score. Full argument: `helio-ux-metrics`.

## Pick the audience

Helio's panel has nearly 1 million active users. You shape it three ways:

- **Behavioral filters** — what they do (banking consumers, credit card users, frequent travelers)
- **Demographic filters** — who they are (age, country, gender)
- **Segment / lifecycle filters** — where they are in the customer arc

Real example (the banking-app flow test): *"Banking consumers, credit card / credit-card-points users, credit union members (US). 100 responses."*

When the panel can't reach (niche B2B, internal stakeholders, existing-customer segments) → bring your own audience.

**Sizing.** 100 responses is the house default. Smaller (50) for fast directional reads. Larger (200+) when you need tight subgroup cuts.

## Write the questions

Map every question to one of Glare's four types and one of three modes.

### Types

- **People** — who they are, what they bring (expectation baselines, demographic-style open-text)
- **Process** — how they move (click tests with hotspots, task flows)
- **Product** — does this read, does this work (Likert comprehension, expectations, desirability)
- **Problem** — what's missing, confusing, in the way (open-text followups)

### Modes

- **Exploratory** — what's true? (open-text, free response)
- **Evaluative** — does this work? (Likert, multi-select)
- **Comparative** — which is better? (A vs B, MaxDiff)

### Bias check

Before launch, run every question through:

- **Leading?** "How great is this page?" → leading.
- **Loaded?** "How do you feel about our innovative new design?" → loaded.
- **Jargon?** "How does the conversion funnel feel?" → jargon.
- **Forced?** Likert with no neutral option → forced.

### Promote open to testable

- **✗** "Do people like our homepage?"
- **✓** "How well do you understand what this company is offering?" (Likert, comprehension metric, followup: "What is this company offering?")

## The followup pattern

The followup is doing the heavy lifting in every Zurb test. Make it part of the design, not an afterthought.

The pattern:

- **After every Likert** → "Why did you choose that option?" *(required)* — converts a rating into reasoning
- **After every click test** → "Why did you click there?" — converts a behavior into intent
- **After multi-select sentiment** → "Why did you choose those options?" *(required)* — converts emotional reaction into language

The required followups are the difference between "65% understood very well" and "65% understood very well, and the 35% who didn't are stuck on 'data fabric' as a term." The second one moves work. The first doesn't.

Make Likert and multi-select followups required. Click-test followups can stay optional — the click is the primary signal, and the dropout cost of forcing a reason is high.

## Validate before you spend

Three checks before you send a test:

### 1. Dry-run via CLI

```
helio-cli tests create --dry-run --project-id <uuid> \
    --name "..." --intro "..." \
    --target-audience-size 100 --questions '[...]'
```

Catches schema errors and validation issues before any incentives are charged.

### 2. Preview via web

Open the test as a participant would see it. Read every question aloud. Tap every interactive area. If something feels off, fix it now.

**The journey must read as one conversation.** Sections that are each fine in isolation can still add up to an experience that makes no sense — especially when auto-built metric sections are stacked, because tagging guarantees each *section* is valid, not that the *sequence* is coherent. Walk the test screen-by-screen (`tests walkthrough` in the CLI) and check:

- **No duplicate or near-duplicate questions.** Some metrics build the same section: sentiment and desirability both open with the 8-word impressions Multiple Choice, and appeal and reaction generate the identical Likert. Tag both and the participant is asked the same question twice in a row. Pick one, or space and reword via `edit-question`.
- **The context noun reads naturally in *every* generated sentence.** One noun feeds all metric instructions — "the checkout flow" works in "What impressions does ___ give you?" but produces nonsense in "How likely would you be to purchase this ___?" Read each generated question aloud with the noun in place; if any sentence breaks, change the noun or edit that section's wording.
- **Understanding before evaluation.** Order the journey the way a real encounter unfolds: open impressions → comprehension → evaluation (usefulness, purchase/intent) → advocacy (NPS). Asking "would you buy this?" before "do you understand what this is?" produces answers about confusion, not the product. `tests reorder` fixes sequence without rebuilding.

### 3. Pre-launch checklist

- Every question has a clear UX metric attached
- Every followup makes sense given the question above it
- The full participant journey reads as one conversation — no duplicate questions from metric stacking, the context noun works in every sentence, understanding comes before evaluation
- The audience filter is specific enough to be useful, not so narrow it can't fulfill
- Total questions ≤ 8 — longer tests drop more participants and dilute every signal
- The hunch from the start is still answerable by the test you've built

## Launch and read

### Fulfillment

Most tests fulfill in minutes to a few hours. If a test is stuck for more than a day, the audience filter is probably too narrow.

### When to read

Wait for full fulfillment unless the sample is large enough that an early peek (~50% in) would be directionally stable.

### What a signal looks like

A signal is a result that's:

- Tied to a hunch — you can name what it confirms or kills
- Strong enough to act on — not "interesting," but decisive
- Specific to a slice — not "users in general," but a named segment
- Coupled with a why — the followup explains the rating

### Worked example: the athletic-apparel homepage

Two results from the same test:

- **Desirability 87** — positive descriptors (Helpful 73%, Innovative 69%) dominate, negative ones near zero. The page *feels* right.
- **NPS 14** — modest. People won't actively recommend it.

That's a signal, not a contradiction. People like it but won't advocate. The useful follow-up direction: what would need to be true for them to share? That's the next test, not a flaw in this one.

## Tie back to Glare

A Helio test produces evidence. Glare turns that evidence into a signal.

Glare's four-piece definition of a design signal:

1. **Behavior observed** — what you tested (the test type)
2. **Metric** — what Helio computed (SUS, NPS, comprehension, etc.)
3. **Context** — how you sliced the audience and what the followups said
4. **Direction** — what the team will do next (you supply this)

Helio gives you the first three. The Design Review is where the fourth gets made. The Decision Map is where it lives over time.

The signal you carry out of a Helio test should be one sentence long. Example:

*On a B2B data-platform homepage, 11% of US enterprise data leaders called the offering "confusing," and most clicked into customer stories before the platform tour — suggesting the platform's value isn't legible on first read, and the homepage should lead with case studies, not product depth.*

That's behavior + metric + context + direction in one line. That's what a Design Review can act on.

## Anti-patterns

The shapes that produce data but not direction:

- **Running without a hunch.** "Let's see what users think" tests produce summaries, not decisions. Start with a "we believe…" statement or don't start.
- **Conflating stated intent with click behavior.** "What would you do next?" (multi-select) and "Click where you'd go" (click test) often disagree. The click is what people actually do. Trust it more than the self-report.
- **Averaging MaxDiff.** Aggregated percentages on MaxDiff items show 0% because the data is best/worst counts. Use the raw counts.
- **Ignoring followups.** A Likert score with no "why" is just a number. The followup is where the design move lives.
- **Assuming asset URLs persist.** Presigned URLs in test reports expire (~30 days). If you're handing a report off for archival, save the assets locally — the URLs won't resolve later.
- **Stretching one test to answer multiple hunches.** Long tests drop more participants and dilute every signal. One hunch per test.

## Templates

Three starting points based on the house patterns. Each is a question set you can edit and launch — not invented, lifted from the shapes Zurb already runs.

**How to build one:** each slot below names its metric. Tag those metrics first (`--ux-metrics …`) and Helio builds the sections with validated wording — then adjust the prompt text in place with `edit-question` (omit `--type` so the metric stays attached). Hand-build only the slots a metric can't generate: click tests, MaxDiff, and anything specific to your risk. The prompts shown are the house wording to aim for, not payloads to paste. For the full T1–T7 template catalog with stage guidance, use `helio-patterns`.

### Template A — Marketing page eval (5 questions)

Based on the athletic-apparel and B2B data-platform homepage tests.

1. **Click test, 5–10 hotspots, branching enabled.** Prompt: "Imagine you're [context]. Click where you would go first on this page." Followup: "Why did you click there?" (optional). Metric: engagement.
2. **Likert, 5-pt comprehension.** Prompt: "How well do you understand what this company is offering?" Followup: "What is this company offering?" (required). Metric: comprehension.
3. **Multi-select, up to 8.** Prompt: "How does this [page / offering] feel to you?" Choices: mix of positive and negative descriptors (Helpful, Innovative, Clear, Simple, Confusing, Complicated, Unnecessary, Uninteresting). Followup: "Why did you choose those options?" (required). Metric: desirability.
4. **Likert, 5-pt likelihood.** Prompt: "How likely would you be to [primary action]?" Followup: "Why did you choose that option?" (required). Metric: desirability or intent.
5. **NPS** (consumer) **or Multi-select single-pick** (B2B, of actual CTAs). Metric: loyalty or intent.

### Template B — Multi-screen flow eval (6–8 questions)

Based on the banking app's Accounts & Dashboard flow test.

Per screen, three questions:

1. **Free response, no asset.** Prompt: "Imagine you just [context]. What do you expect to see on the [screen]?" Metric: expectations baseline.
2. **Likert, 5-pt expectations** (asset: the screen). Prompt: "This is the [screen]. How well does this page match your expectations?" Followup: "Why did you choose that option?" (required). Metric: expectations.
3. **Click test, branching enabled** (asset: screen with hotspot). Prompt: "Click where you would go to [primary task]." Followup: "Why did you click there?" (optional). Metric: engagement.

Repeat for the next screen. Close with a multi-select desirability check on the final screen.

### Template C — Content prioritization (5 questions)

Based on the veteran careers landing page test.

1. **Likert, 5-pt comprehension.** Prompt: "How well do you understand who this webpage is for?" Followup: "Who is this webpage for?" (required). Metric: comprehension.
2. **MaxDiff (best/worst scaling).** Prompt: "What parts of this page are Most Interesting and Least Interesting to your [context]?" Items: the page sections. Followup: "Why did you choose those options?" (required). Metric: prioritization (read raw best/worst counts).
3. **Multi-select, up to 8.** Prompt: "How does the information on this page feel to you?" Metric: desirability.
4. **Likert, 5-pt likelihood.** Prompt: "How likely would you be to use this site to [primary action]?" Metric: desirability or intent.
5. **Click test, branching enabled.** Prompt: "Click where you would go next on this page." Metric: engagement.

## Where this fits

- **`helio-app`** — what the platform is. Read first if new.
- **`helio-creating-test`** (this skill) — how to design a test that produces a signal.
- **`helio-cli`** — how to launch and pull results via terminal.
- **`helio-mcp`** — how to do the same from an AI assistant.

If you're stuck choosing which surface to drive the test from: **person → web app, script → CLI, assistant → MCP.** Test design is the same either way.

<!-- /DERIVED -->

---

<!-- ADDED 2026-07-06 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Starting test creation from a **belief or question** rather than an existing asset ("we think the new homepage will convert better — how do we test that?")
- Asking **which test shape** fits their situation (marketing eval, multi-screen flow, content prioritization, concept comparison)
- Wanting a **ready-to-edit template** instead of designing question-by-question
- Asking how many questions a test should have, whether followups should be required, or how to phrase questions without bias
- Sitting on a test that produced "interesting findings" but no decision — the diagnosis usually lives in this skill's anti-patterns (no hunch, multiple hunches, ignored followups)
- Unsure whether to build in the web app, the CLI, or via MCP

Route away when the user starts from an **existing asset/mockup and wants the operational build walkthrough** (`helio-asset-to-test`), wants **shape recognition across real past tests** (`helio-patterns`), or is past design and into **launch mechanics** (`helio-cli` / `helio-mcp` / `helio-app`).

## Failure modes

- **Skipping the hunch because the user is in a hurry.** The hunch template takes two minutes and is the difference between a signal and a summary. If the user resists, write the hunch *for* them from what they've said and ask "is this the belief we're testing?"
- **Letting the test grow past 8 questions.** Every extra question costs completion rate and dilutes synthesis. Split into two tests — one hunch per test.
- **Treating the templates as fixed.** They're starting points lifted from real tests; the prompts' bracketed slots ([context], [primary action]) must be filled per test or the questions read as generic.
- **Forgetting the MaxDiff reading rule.** If a test includes MaxDiff, warn at design time that the report must be read as raw best/worst counts — aggregated percentages will show 0%.
- **Designing a shape the chosen surface can't build.** Tree tests and prototype tasks can't be created via CLI/MCP (click tests can, since v0.4.0). If the user plans to script the build, flag which template steps need the web app — and check `helio-cli update --check` first, since this boundary has moved every release lately.

## The template layer — shapes → T1–T7 (cross-reference)

This doc's four conceptual shapes now have a data-backed operational layer: the **Test Pattern Playbook** (285-test analysis, in `helio-patterns`) with seven templates mapped to project stage. When instantiating a shape, prefer the playbook's template — it carries exact questions, metric tags, and required follow-ups drawn from real use:

| This doc's shape | Playbook template | Notes |
|---|---|---|
| Marketing page eval (Template A) | **T5 · Homepage Five** | Same arc; T5 adds stage evidence (first-look only) |
| Content prioritization (Template C) | **T2 · MaxDiff Read** | Same arc |
| Multi-screen flow eval (Template B) | **T7 · Flow Expectation** | Same predict-reveal-click triplet per screen |
| Concept comparison | — | No canonical template in the corpus; build from this doc's arc |
| *(not in this doc)* | **T4 · Findability Sweep** | The workhorse — "can they find/do X?", spans stages |
| *(not in this doc)* | **T6 · Expectation Probe** | Name/URL/copy tuning in iteration |
| *(not in this doc)* | **T1 · Two-Tap Check** | One flow step, variant sweeps only |
| *(not in this doc)* | **T3 · Shelf & NPS** | Physical product / packaging appeal + benchmark |

The playbook also adds the **stage trigger** this doc doesn't cover: first look (cold read) → iterate (locked shape, V1/V2/V3) → benchmark (your questions, their screens). Ask the asset first, then the stage — see `helio-patterns`.

## The UI-only boundary — canonical checklist

Some parts of a Helio test can only be built in the web app. This is the one authoritative list; other skills point here. Plan these steps *before* choosing a surface, so a scripted or assistant-driven build doesn't dead-end.

**Accurate as of helio-cli v0.7.0 — this boundary moves, fast.** Run `helio-cli update --check` before telling anyone something can't be scripted; a stale binary reports its own limits as the tool's. Three rows left this list in v0.4.0 (click tests, hotspots, branching) and four more in v0.7.0 (the click-backed metrics, `brand_score`, repeated metric types, and read-back of audience/branching/hotspots) — all after being documented as permanent.

| Step | Why UI-only | Workaround | Rough effort |
|---|---|---|---|
| Video/audio asset upload | `assets upload` accepts images only — jpg/jpeg/png/gif, max 10MB | Upload video/audio in the web app; images upload via `helio-cli assets upload` (MCP has no asset tools) | ~1 min per asset |
| Tree test / Prototype task sections | API marks these non-creatable (need a Figma prototype or menu tree) | Build in the web app; CLI/MCP can still read their reports (paths, Direct/Indirect/Failed) | ~5 min per section |
| Branching beyond single-select multiple_choice (hotspots, variations, most/least labels) | Only MC branching has an API surface | `tests clone` an existing branched test and edit the copy | ~2 min per branch |
| Customer-list building & formal screeners | No API endpoint (audience *recruiting* is scriptable as of v0.8.0 — `--audience-type`, `--demographics`, `--source enroll`) | Build the list or screener in the web app; attach by ID via `--audiences` (CLI) / `audiences` (MCP), or `tests clone` to inherit the last audience | varies |
| 2 UX metrics: `completion`, `effort` | Each is built from a Figma prototype section, which the API can't create — the CLI names this reason per type | Build the prototype section in the web app, then tag the metric | ~1 min |
| Scheduled launch | `send` fires immediately on every surface | Send manually at the intended time | — |

**No longer UI-only.** Since v0.4.0: click test sections, hotspot definition (`--hotspots`, relative 0–1 coordinates), and single-select multiple_choice branching (`--branching`, Enterprise accounts). Since **v0.7.0**: the `engagement`, `success`, `usability`, `satisfaction` and `brand_score` metrics; **repeating a metric type** on one test (each instance scores independently — the multi-screen `expectations` case); and read-back of audience, branching, and hotspots via `preview` / `walkthrough` (so those no longer need visual verification in the web app).

The working pattern: **script the buildable part first, finish the UI-only steps in the web app, then validate and send from wherever is convenient** — drafts are shared across all three surfaces.

## Where to go next

- For the asset-first build walkthrough: `helio-asset-to-test`
- For test-shape recognition across real tests: `helio-patterns`
- For per-section configuration: `helio-section-types`
- For metric definitions and scoring: `helio-ux-metrics`
- For audience mechanics: `helio-audience-flow`
- For screening participants: `helio-forms-screeners`
- For launch via terminal or AI assistant: `helio-cli` / `helio-mcp`
- For reading the report and writing the signal: `helio-reading-report`

<!-- /ADDED -->

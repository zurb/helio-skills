# Section Types — Reference

**Skill:** `helio-section-types`
**Source:** Section Types v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had two minor AEO-rubric gaps (Problem opener; Action pointer). Both are addressed in the ADDED sections at the end of this file.

---

<!-- DERIVED FROM: 165DVFQskrAuCBgYItH0Oz_IxZO3GPHupIFrZZvAyJGs — Section Types v0.1 -->

A reference for every section type you can add to a Helio study — what it does, how to configure it, what participants experience, what comes back in the report, and when to reach for it.

## Choice-Based

### Multiple Choice

A list of options. Single- or multi-select.

**Setup**

- Between 2 and 50 choices.
- Single-select (default) or multi-select with a per-question selection limit.
- Tag each choice with a sentiment (Positive / Neutral / Negative) to power net-positive scoring.
- Add a follow-up question per choice, or a global follow-up for the whole section.
- Toggle a response timer.
- Optionally pin certain choices and randomize the rest.

**Participant experience.** A short list of buttons or cards. If randomization is on, choices shuffle (pinned ones stay put). Single or multi-tap depending on configuration. An optional follow-up text field appears after selection.

**Report.** Horizontal or vertical bar chart by count or percentage. If you tagged sentiment, you also get a net-positive alignment score (Positive +1, Neutral 0, Negative −1, weighted by share of responses).

**Best for.** Quick quantitative reads — preference, awareness, segmentation. Not the right call when you need ranking or weighted importance.

**Good to know**

- Multivariate A/B is not supported on this section type — one variation only.
- Branching requires single-select; multi-select branching isn't supported.
- Sentiment tagging is manual, not auto-inferred from the choice text.

### Preference

Show two or more designs side by side and ask which one wins.

**Setup**

- 2–3 variations. Beta accounts can go up to 5.
- Each variation is an image or prototype — no per-variation text options.
- Optional global follow-up ("Why did you choose this version?").
- Randomization order is per-participant.

**Participant experience.** A carousel of variations participants can browse with arrow keys or taps. One click selects a winner; an optional follow-up text field appears.

**Report.** Stacked bars showing which variation won, by count and percentage. Side-by-side comparison of selected vs. unselected variations.

**Best for.** Choosing between concepts when each option is a complete design (a homepage layout, a color palette, a hero shot). Not for fine-grained ranking — use Rank or MaxDiff for that.

**Good to know**

- Hard cap of 3 variations outside the beta group.
- No sentiment tagging on this type; reporting is purely count-based.
- Each participant sees variations in a freshly randomized order.

### Rank

Drag a list into order.

**Setup**

- 2–50 choices, all of which must be ranked (no partial ranking).
- Custom labels for the top and bottom of the list (defaults: "Most Important" / "Least Important").
- Optionally pin certain choices to fixed positions.
- Branching can fire on either the highest- or lowest-ranked choice.

**Participant experience.** A draggable list. Pinned items stay put; the rest shuffle. Drag to reorder until satisfied, then submit. Optional follow-up text after ranking.

**Report.** Horizontal bar chart of mean rank per choice, with the configured top/bottom labels on the axis. Switchable to a stacked view comparing filtered vs. unfiltered participants.

**Best for.** Prioritization studies where order matters and you have a small-to-medium item set. Less cognitively demanding than MaxDiff when you have under ~10 items.

**Good to know**

- Partial ranking ("rank your top 3") isn't supported.
- All items must end up in the list — no "skip if irrelevant."
- For larger sets (15+), reach for MaxDiff instead to reduce participant fatigue.

### Point Allocation

Distribute a fixed budget across options.

**Setup**

- 2–50 choices.
- Configurable point budget (default 100) and custom label for the budget ("Points", "Dollars", "Hours", etc.).
- All points must be allocated; partial allocation isn't supported.
- Pin choices, randomize order, set a timer, add a follow-up.

**Participant experience.** A list of choices with input fields or sliders next to each one. The interface enforces that totals add up before submission.

**Report.** Horizontal bar chart of mean points per choice. By definition, the mean values sum to the budget. Toggle filtered vs. unfiltered views.

**Best for.** When you want to see the **shape** of preference, not just order. Useful when some options are dramatically more important than others — Rank flattens that, Point Allocation preserves it.

**Good to know**

- The sum-equals-budget rule is enforced in the UI, not in stored data — exports may need a sanity check if you're importing.
- A single response time is captured for the whole allocation, not per choice.

### MaxDiff

Round-by-round "best of / worst of" comparisons.

**Setup**

- 2–50 choices.
- Custom labels for "best" and "worst" (defaults: "Most Important" / "Least Important").
- Option to reverse the label positions.
- Branching on best or worst pick.
- Choice sentiment is available but doesn't feed into MaxDiff scoring.

**Participant experience.** A subset of choices is shown in each round. The participant picks one as "best" and one as "worst," then moves on. Faster and less mentally taxing than full ranking, even with a large item set.

**Report.** Win/loss matrix and dominance chart — for each choice, the percentage of times it was picked as best vs. worst. The strongest options have high "best %" and low "worst %"; the weakest have the inverse.

**Best for.** Large item sets (10+) where you want defensible relative importance. Brand attribute studies, feature prioritization, value-proposition testing.

**Good to know**

- The number of rounds isn't directly exposed as a setting today — it's derived from the choice count.
- The UI prevents picking the same option for both best and worst within a round.

## Open Text

### Free Response

Open-ended text.

**Setup**

- A question prompt.
- Optional follow-up enabled per choice or globally.
- Sentiment and key-phrase extraction happen automatically — no toggle needed.

**Participant experience.** A text input. Participants type freely up to a 7,000-character limit.

**Report**

- Individual response cards with full text and an auto-detected sentiment tag.
- A word cloud / common phrases panel that clusters responses into themes automatically.
- Key phrases ranked by confidence score from the language model.
- Sentiment distribution (% positive / neutral / negative).

**Best for.** Understanding *why* — the drivers behind a choice, the pain points behind a complaint, the language people use to describe a feature.

**Good to know**

- 7,000-character limit is fixed and not configurable per question.
- Sentiment and key phrases are extracted on save — if the text is empty, both stay empty.
- The language analysis runs synchronously; if the provider is briefly unavailable, the response still saves but without enrichment.

### Free Response Followup

A moderated follow-up question sent to a *specific* participant after their initial response.

**Setup**

- You write the question text per participant from inside the report. It's not configured up front.

**Participant experience.** After the initial response is in, the participant receives a notification or email with a link to answer the follow-up. They open the link, type a response, submit. They never see the follow-up as part of the original study flow.

**Report.** Follow-up answers appear nested under the parent response in the report, with their own sentiment and key-phrase extraction. The original response and the follow-up read as a connected conversation.

**Best for.** Probing deeper on the most interesting individual responses. Particularly useful after a Free Response when one or two participants say something unusual that warrants follow-up.

**Good to know**

- Each follow-up consumes 10 answers from your license balance.
- A follow-up that goes unanswered for 3 days is marked timed-out and your answers are refunded automatically.
- This is researcher-initiated — participants never see a follow-up until you send one.
- For automatic follow-up prompts inside the test flow itself, use **Conditional Follow-ups** instead (below).

### Conditional Follow-ups

Not a section type — a feature available on most section types.

**How it works**

- On any section's choice, you can require a follow-up. When a participant selects that choice, an inline text field appears asking them to elaborate.
- This is in-flow — participants see and answer it as part of the same session, no separate notification.
- Distinct from branching: branching routes participants to a different *section* based on their answer; conditional follow-ups gather *additional input* on the same section.

**Best for.** Capturing the "why" right after a quantitative pick. Without losing momentum or requiring you to moderate each one by hand.

**Good to know**

- Configured per-choice, not per-section.
- Inline follow-ups are recorded on the same response record as the parent answer — they don't cost extra answers.

## Scales

### Likert

An ordinal scale measuring agreement, importance, frequency, or similar.

**Setup.** Helio ships 11 preset templates that cover the most common psychometric scales:

| Template | Length | Use for |
|---|---|---|
| Agreement | 5-point | "I would recommend this product" |
| Occurrence | 5-point | "How often do you…" |
| Importance | 5-point | "How important is this feature?" |
| Quality | 5-point | "How would you rate the quality?" |
| Comprehension | 4-point | "Did you understand…" |
| Impression | 5-point | "First impression of…" |
| Expectations | 5-point | "Did this meet expectations?" |
| Usefulness | 5-point | "How useful is…" |
| Difficulty | 5-point | "How difficult was…" |
| Likelihood | 5-point | "How likely are you to…" |
| Custom | Variable | When none of the above fit |

Preset templates carry sentiment baked in (the negative end maps to negative sentiment, the middle to neutral, the positive end to positive). Custom Likert lets you supply your own labels and scale length but you'll need to think about sentiment yourself.

**Participant experience.** A row of radio buttons or labeled options. One selection per participant.

**Report.** Distribution bars colored by sentiment, with a median score and a net-positive alignment score (promoters minus detractors, normalized).

**Best for.** Standardized attitudinal measurement, especially when paired with a UX Metric like Usefulness, Satisfaction, or Comprehension — Helio auto-builds the right Likert scale when you pick the metric.

**Good to know**

- Scale length is locked to the template (most are 5-point; Comprehension is 4-point). To use a 7-point scale, pick Custom.
- Sentiment isn't editable on preset templates.

### Numerical Scale (NPS)

A 0–10 willingness-to-recommend scale.

**Setup**

- The 0–10 range is fixed. No other ranges are supported.
- Optional global follow-up (commonly "Why did you give that score?").

**Participant experience.** A horizontal strip of 11 numbered buttons (0 through 10), typically anchored with "Unlikely" and "Likely" labels at the ends.

**Report**

- Distribution bars colored by NPS classification (detractor / passive / promoter).
- The NPS score itself (% promoters − % detractors).
- Median rating.

The classification mapping is fixed:

- **Detractors:** 0–6
- **Passives:** 7–8
- **Promoters:** 9–10

**Best for.** Loyalty and recommendation intent — and the related **Effort** metric (if you tag the section with the Effort UX Metric, the scoring switches from NPS math to a 0–100 effort score automatically).

**Good to know**

- 0–10 only. If you want a 0–5 or 1–7 numeric scale, use Likert (Custom) instead.
- The sentiment mapping is hardcoded and not editable.

### Matrix

A grid of related questions sharing the same scale.

**Setup**

- Rows are statements or items you want rated.
- Columns are the scale options (e.g., the 5-point Likert agreement scale).
- All rows share the same scale — you can't mix a 5-point row with a 3-point row in the same matrix.
- Pin or randomize row order.

**Participant experience.** A compact table — participants make one selection per row. Less fatiguing than asking N separate Likert questions back to back.

**Report**

- Cross-tabulation: rows × columns with percentage or count per cell.
- Heatmap coloring on the cells to highlight the dominant pattern.
- Column-level aggregates (e.g., "what % said 'Strongly Agree' across all rows?").

**Best for.** Rating several related things on the same scale in one screen. Feature satisfaction, attribute importance, multi-statement agreement.

**Good to know**

- All rows must use the same scale — if you need different scales per row, use separate Likert sections.
- Row text is required; rows can't be auto-generated.

## Usability

### Prototype Test

The richest section type. Embed a Figma prototype and watch participants try to complete a task.

**Setup**

- **Prototype URL** — A Figma share link.
- **Expected path** — The screens you expect participants to visit in order to succeed. Pick them by clicking through your own prototype during setup.
- **Multi-flow grading** — Support multiple alternative success paths in the same section. A participant who succeeds via any of them is graded as a success, with priority given to the most-direct route.
- **Task instructions** — What you're asking the participant to do.
- **Multiple variations** — Run A/B variants of the prototype in a single section.

**Participant experience.** The task instructions display, then the Figma prototype loads in an embedded frame. Participants navigate by clicking hotspots in the prototype. Every click is captured with normalized coordinates; every screen transition is captured with a timestamp.

**Data captured.** Every screen view and every click — plus a grade for each participant: **Direct Success**, **Indirect Success**, or **Failed**.

- **Direct Success** — The participant followed the expected path exactly, no detours.
- **Indirect Success** — The participant reached the goal but with backtracking, extra clicks, or visits to unexpected screens.
- **Failed** — The participant gave up or never reached the goal.

**Report**

- **Heatmap overlays** on each screen, showing where participants clicked.
- **Path / flow diagram** showing the screen-by-screen flow of participants, with drop-off points called out.
- **Per-screen breakdown** — for each expected screen, you see how many participants reached it as a Direct Success, Indirect Success, or Failed there. Plus average clicks, average dwell time, drop-off percentage, and where participants who dropped off ended up instead.
- **Per-grade overview** — overall success rate, average completion time, click counts.

**Best for**

- Validating multi-step user journeys before development.
- Identifying confusing screens (high "Indirect" share = a confusing branch point).
- A/B testing different design directions on the same task.

**Good to know**

- **Phantom starting screens** — sometimes the Figma editor captures a canvas or page node as the "first screen" that participants never actually visit. Helio detects and filters these on both the editor and the report side, but if your "first screen" shows zero views across all participants, that's why.
- **Grading runs as a background job** — heatmaps and per-screen timing populate after a worker processes each response, so brand-new responses may show empty heatmaps for a few seconds.
- **Multi-flow** is the right answer when there's more than one legitimate way to complete the task — you don't have to pick one canonical path.

**Tied UX Metrics**

- **Success** — Direct Success rate.
- **Completion** — Direct + Indirect Success rate.
- **Usability** — Combined success rate weighted by efficiency across multiple Prototype Tests.
- **Engagement** — Pulled from click patterns, weighted by hotspot priority (see Click Test).

### Click Test

A static image with a question like "Where would you click to do X?"

**Setup**

- **Image** — Upload a static design or screenshot.
- **Hotspots** — Define rectangular regions on the image and tag each one with a priority: **Primary**, **Secondary**, or **Tertiary**. Primary is the "ideal" target; Secondary and Tertiary are acceptable alternatives.
- **Multiple variations** — Run A/B variants in a single section.

**Participant experience.** An image with no visible hotspots. The participant clicks wherever they expect — clicks inside any defined hotspot count as hits; clicks elsewhere are misses.

**Report**

- **Heatmap** of clustered clicks rendered directly on the image.
- **Hotspot hit rates** by priority — what % of clicks landed on Primary, Secondary, Tertiary, or missed entirely.
- **Time to first click**.
- **Average clicks per participant.**

**Best for.** Findability tests — does the call-to-action stand out? Is the navigation icon recognizable? Where are users *expecting* to find this thing?

**Good to know**

- There's no built-in click limit; participants can click multiple times. If you need to enforce a single click, frame the task accordingly.
- Hotspot priorities are buckets, not weights — the report shows which priority got hit, not a weighted score (the weighting shows up in derived UX Metrics like Engagement).

**Tied UX Metrics**

- **Success** — Primary hotspot click rate.
- **Engagement** — Weighted across all hotspot priorities.

### Tree Test

A hierarchical menu navigation task.

**Setup**

- **Tree structure** — Build the menu hierarchy. Up to 6 levels deep.
- **Correct destination** — The leaf node you expect participants to find.
- **Task instructions** — What participants are looking for.

**Participant experience.** A collapsible menu tree. Participants expand and collapse categories to navigate, then select a leaf node to indicate where they'd expect to find the task item. Their full path of expansions and clicks is recorded.

**Report**

- **Success rate** — % of participants who landed on the correct leaf.
- **Incorrect destinations** — Where participants went when they got it wrong.
- **Path efficiency** — How direct or wandering their navigation was.
- **Category popularity** — Which top-level categories participants opened first, indicating their first guesses.

**Best for.** Information architecture validation, especially before any visual design exists. Tree Test answers the question: "Will users *find* this thing in our navigation hierarchy, regardless of how the page looks?"

**Good to know**

- Maximum tree depth is 6 levels.
- Per-click timing isn't captured today — you'll see the sequence and total time, but not how long someone hovered on each category.
- Success is binary (right leaf vs. wrong leaf) — there isn't a Direct/Indirect distinction like Prototype Test has.

## Information Architecture

### Card Sort

Participants group cards into categories.

**Setup**

- **Cards** — A list of items participants will sort.
- **Sort type:**
   - **Open** — Participants invent their own category names.
   - **Closed** — You provide the categories; participants drop cards into them.
   - **Hybrid** — Both: predefined categories plus the ability to add new ones.
- **Task instructions**.

**Participant experience.** Drag-and-drop cards into categories (closed/hybrid) or into named groups they create themselves (open).

**Report**

- **Card placement frequency** — for each card, the percentage of participants who put it in each category.
- **Suggested optimal grouping** — derived from card co-occurrence patterns. Useful when you ran an open sort and want to see if natural clusters emerged.
- **Comparison view** — your proposed grouping vs. what participants actually did.

**Best for**

- **Open sort** — Early-stage discovery. What categories do users naturally invent for this content?
- **Closed sort** — Validation. Does my proposed navigation match user expectations?
- **Hybrid** — Both at once.

**Good to know**

- The clustering and optimal-grouping math is more sophisticated for closed sorts than open ones. Open sort outputs lean heavier on the raw frequency tables.

## AI Heuristic Evaluation

### Design Analysis (AI Section)

Not a section you add to a test — a separate workflow that uses AI to evaluate a design against UX heuristics. It produces a report that **looks** like a test report but has no participants. For the full deep dive, use `helio-design-analysis`.

**Setup**

- **Input** — A prototype URL, an asset URL, or an uploaded image.
- **Context** — A description of the ideal user, the goal of the design, the initiative it supports.
- **Metric mapping is fixed** — The AI evaluates against four "master user needs" (Feel, Understand, Do, Trust), each backed by a curated set of UX metrics. You don't pick the metrics; the system picks them.

**Researcher experience (no participants).** Submit the design and context, then wait — the analysis runs in the background and progress updates in real time. When it completes, you get a report broken into the four user-need sections, each with:

- A score (1–5) with a quality label (Very Poor → Very Good).
- A written explanation of strengths and weaknesses.
- Suggested follow-up questions to validate with real users.
- Annotations overlaid on the screenshot pointing at specific issues.

**Best for**

- A heuristic sanity check before running participant tests.
- Quick design critique on a prototype.
- Comparing iterations (v1 vs. v2) or competitor designs.

**Good to know**

- This is a **separate workflow** from test creation — you don't add a Design Analysis section to a study. It's its own entry point.
- The output is one-shot. Re-running means starting over; you can't iteratively refine the analysis the way you'd iterate on a real study with more responses.
- Design Analysis uses its own metric storage, separate from the UX Metrics on participant-driven tests. The two systems don't share scores.
- Each analysis makes multiple AI model calls under the hood, invisible at the answers level.
- This is **not a replacement for user testing**. Use it to find obvious problems early; use participant tests to find real ones.

## Cross-Cutting Notes

### Multivariate (A/B) support

Not every section type supports A/B variations. Quick reference:

| Supports multivariate | Single variation only |
|---|---|
| Preference, Click Test, Prototype Test | Multiple Choice, Rank, Point Allocation, MaxDiff, Likert, NPS, Matrix, Card Sort, Tree Test |

For the single-variation types, you can still A/B test concepts by making each one its own section and using branching to route participants.

### UX Metric pairings

If you tag a section with a UX Metric, Helio will auto-build the section structure needed to compute it. For the full pairing table, use `helio-ux-metrics`.

### Branching

Available on most section types. Configured at the *choice* level: each choice can route participants to a target section or end the study. Branching from a multi-select choice isn't supported — single-select only. For full branching reference, use `helio-branching`.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard gaps) -->

## What this solves

Without a working model of each section type, teams default to Multiple Choice and Likert for everything — missing the moves (MaxDiff for content, Tree Test for IA, Prototype Test for flows) that would actually surface the signal they're looking for. This is the spec so the choice is deliberate.

## When to use

Reach for this skill when the user is:

- Picking which section type matches the question they're asking
- Configuring a section (hotspots, scale length, choice limits, randomization)
- Confused about what comes back in the report for a given section type
- Hitting a section limitation (multi-select branching, partial ranking, etc.) and needs to know whether it's a config issue or a real platform limit

For broader test design (which sections to combine into a study), use `helio-asset-to-test`. For metric attachment (which UX Metric auto-builds which structure), use `helio-ux-metrics`. For conditional routing across sections, use `helio-branching`.

## Failure modes

- **Defaulting to Multiple Choice for everything.** The cheapest section to set up; the easiest to misread. Reach for the section type whose *report view* matches the question you're actually asking.
- **Using Rank for a list of 15+ items.** Participant fatigue spikes after ~10 items. Use MaxDiff instead.
- **Trying to branch on a multi-select Multiple Choice.** Not supported. The platform blocks it because multi-select branching creates ambiguous routing. Split into single-select questions chained by branches if you need this.
- **Setting up a Prototype Test without confirming the expected path inside Figma.** Helio infers expected paths from your own clickthrough during setup — if you skip that step, every participant grades as Failed.
- **Assuming Design Analysis is a section type.** It's a separate workflow with its own entry point. You don't add it to a study; you start it from the AI evaluation surface.

## Where to go next

- For picking the UX Metric to attach: `helio-ux-metrics`
- For building a study end to end: `helio-asset-to-test`
- For conditional routing: `helio-branching`
- For the AI evaluator: `helio-design-analysis`
- For asset handling (image upload, Figma): `helio-assets`
- For recognizing common section combinations: `helio-patterns`

<!-- /ADDED -->

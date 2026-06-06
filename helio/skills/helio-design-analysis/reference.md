# Design Analysis — Reference

**Skill:** `helio-design-analysis`
**Source:** Design Analysis v0.1
**Source last synced:** 2026-05-23

---

<!-- DERIVED FROM: 1bYfLuQqxIYYf5OBzWXskhqpndNXK4rkc-STc-8j1SMU — Design Analysis v0.1 -->

AI-powered heuristic evaluation of a design or prototype. Generates a report that looks like a participant study but has no participants — every score, observation, and suggestion comes from an AI model evaluating your design against UX heuristics.

For an overview of where this fits among Helio's section types, use `helio-section-types`. This doc is the deep dive.

## What It Is — and What It Isn't

**Design Analysis is a separate workflow from regular studies.** You don't add a Design Analysis section to a test — it's a different entry point with its own UI, its own data model, and its own report.

**It's good for:**

- A quick heuristic check before spending budget on participants.
- Critiquing iterations side by side (v1 vs. v2, your design vs. a competitor).
- Catching obvious problems (missing CTAs, unclear hierarchy, dense layouts).

**It's not a replacement for user testing.** AI can flag heuristic issues but can't tell you whether real users will actually struggle, succeed, or convert. Use Design Analysis to *narrow* what you test with participants, not to *replace* testing.

## Setup

You provide a design and a small amount of context. Helio handles the rest.

**Required inputs**

- **The design** — one of:
   - Direct image upload (PNG, JPG, GIF, WebP)
   - Image URL
   - Website URL (Helio captures a screenshot)
   - An asset already in your library
- **Title** — A name for the analysis.
- **Project** — The project this analysis belongs to.

**Audience context (recommended)**

- **Ideal user** — A name and short description of who you're designing for.
- **Demographics** — Gender, age, education, income, country, language, work status.
- **User type** — Consumer or professional.
- **Job & industry** (professional users).
- **Defining attributes** — Ability, activities, responsibilities, opinions, skills.

**Goal & concept context (recommended)**

- **Goal** — What you want this design to accomplish.
- **Concept / Initiative** — The broader effort or idea behind the design.
- **Notes** — Any additional context you want the AI to consider.

The more context you give, the more targeted the analysis. The audience and goal directly shape how the AI interprets what it sees.

## The Four Master User Needs

Every Design Analysis evaluates your design against four broad needs. These are the top-level lenses; each one is backed by a weighted bundle of UX metrics underneath.

### Feel — How do people feel about this?

**Backed by:** Appeal (40%), Desirability (40%), Feeling (20%).
**What it surfaces:** Emotional response, aesthetic draw, attractiveness, the gut-level reaction someone has on first contact.

### Understand — Does this make sense to people?

**Backed by:** Comprehension (40%), Expectations (25%), Usefulness (25%), Usability (10%).
**What it surfaces:** Clarity, learnability, whether labels and structure communicate what they need to.

### Do — Can people complete what they need?

**Backed by:** Success (33%), Completion (33%), Intent (17%), Effort (17%).
**What it surfaces:** Task feasibility, friction points, missing CTAs, unclear paths to action.

### Trust — Can people rely on this?

**Backed by:** Sentiment (30%), Expectations (25%), Usefulness (25%), Loyalty (20%).
**What it surfaces:** Credibility cues, perceived reliability, signals that build or erode confidence.

For the full per-metric reference, use `helio-ux-metrics`.

## How the Analysis Runs

You submit the design and hit go. The analysis runs in the background and the UI shows real-time progress, going through these phases:

1. **Asset processing** — Capture or load the image.
2. **User-need scoring** — The AI evaluates the design against the heuristics for each user need (1–5 scores per heuristic, averaged into an overall need score).
3. **UX metric scoring** — Score each contributing UX metric for the user need.
4. **Explanation generation** — Write the natural-language summary of strengths and weaknesses.
5. **Headline generation** — Generate the per-need summary headline.
6. **Image annotations** — Identify and locate specific issues on the design with bounding boxes, severity levels, and descriptions.

The four user needs run independently and in parallel. Total runtime varies but is usually under a minute.

**Status flow:** Pending → Running → Completed (or Error).

If something fails mid-pipeline, the analysis is marked errored. The cause is logged internally; partial results may still be visible but the report is incomplete.

## What You Get

The completed report has four sections — one per user need — each with:

**A score and quality label.** The same 0–100 / Very Poor → Very Good scale used elsewhere in Helio.

**A written explanation.** Strengths, weaknesses, and how the design ranks on the contributing heuristics. Rendered as formatted HTML.

**Image annotations.** Hotspots overlaid on the design pointing at specific issues with descriptions and severity (low / medium / high / critical). Color-coded by severity.

**Suggested follow-up questions.** Concrete questions you could ask real users to validate or dig into what the AI flagged. These don't auto-convert into a test — you'd manually create a study using them as inspiration.

Navigation between the four user needs is via tabs or keyboard arrow keys.

## Sharing

Each Design Analysis gets a public report URL (a ULID — a 26-character shareable code). Anyone with the link can view the report without a Helio account.

If you need programmatic access, the regular Helio API tokens work — the analysis is available through the same API surface as participant-driven tests.

## Cost

**A flat 4 answers per analysis.** Not per token, not scaled by image size or context length — every Design Analysis costs the same.

This is billed against your account's answers balance, the same balance used by participant responses.

## Plan & Feature Gates

- Design Analysis is a feature-gated product. If you don't see it in your account, check with your admin.
- This is one of Helio's newer features (status and progress tracking shipped in October 2025), so behavior may still be evolving.

## Good to Know

**The analysis is one-shot.** You submit once, the AI runs the full pipeline, and you get the result. There's no iterative refinement, no "ask a follow-up question," no re-scoring with different context. To run it again with adjusted context, you start a new analysis.

**The user-need-to-metric mapping is fixed.** You can't pick which UX metrics matter for your case — the four user needs and their underlying metrics are baked in. This is intentional (the AI's evaluation depends on the heuristics tied to each metric), but it means Design Analysis is more of a structured assessment than a flexible probe.

**It uses its own metric storage.** The scores you see on a Design Analysis don't show up alongside UX metric scores on participant-driven studies. The two systems run in parallel.

**Prompts are managed externally.** The AI prompts driving the pipeline live in a separate prompt-management system. If you're seeing flaky outputs that look like missing prompts, contact your account manager or support.

**Figma is not directly integrated yet.** You can paste a Figma file URL only if it's a published prototype that resolves to a public screenshot — there's no live design-syncing or asset-pulling from Figma like there is for Prototype Tests.

**Heavy AI usage.** Each analysis makes roughly two dozen model calls underneath. This is invisible at the answers level (still 4 answers flat) but worth knowing if you're considering running many analyses in a tight loop.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Considering running an AI heuristic evaluation before a participant test
- Comparing v1 vs v2 of a design, or their design against a competitor
- Setting up Design Analysis context (ideal user, goal, concept) and wondering how it shapes results
- Interpreting a Design Analysis report (the four user needs, the weighted metrics underneath)
- Confused about the difference between Design Analysis (AI evaluator) and AI Audience (synthetic participants)
- Calculating cost (flat 4 answers, not scaled)
- Wondering why Design Analysis scores don't appear alongside participant-driven scores (different data storage)

For real participant-driven UX metric scoring with the same metric names, use `helio-ux-metrics`. For synthetic-participant responses (AI Audience), use `helio-audience-flow`.

## Failure modes

- **Confusing Design Analysis with AI Audience.** Design Analysis = AI evaluates the design (no participants). AI Audience = AI generates synthetic participant responses (still goes through the regular study flow). Different features.
- **Treating Design Analysis as a substitute for user testing.** AI can flag heuristic issues but can't tell you what real users do. Use it to narrow what to test, not to skip testing.
- **Blending AI-derived metric labels with participant-driven scores.** They live in separate data structures. Don't put them on the same chart.
- **Expecting iterative refinement.** Design Analysis is one-shot. Re-run with adjusted context if needed.
- **Trying to customize the user-need-to-metric mapping.** It's fixed by design.
- **Pasting a Figma file URL and expecting live sync.** Only works if the prototype is publicly resolvable to a screenshot. No live integration.

## Where to go next

- For participant-driven UX metrics: `helio-ux-metrics`
- For the AI Audience (different feature): `helio-audience-flow`
- For building a real study from AI-suggested follow-ups: `helio-asset-to-test`
- For synthesis with the "don't blend" caveat: `helio-reading-report`

<!-- /ADDED -->

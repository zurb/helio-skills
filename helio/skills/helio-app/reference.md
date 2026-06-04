# Helio (Platform) — Reference

**Skill:** `helio-app`
**Source:** Helio App v1.3 + Using Helio v0.2 (merged)
**Source last synced:** 2026-05-23
**Notes:** This skill merges two source docs because positioning (Helio App) and capability tour (Using Helio) form one mental model. Reference.md has two DERIVED blocks.

---

<!-- DERIVED FROM: 12IcYGKc-sOPM-4zR-Oo-FdZl0gZLo9wc2b7qJvMiMR4 — Helio App v1.3 -->

## Helio (positioning, plans, Glare workflow)

Helio is how you get data into Glare. The platform runs structured user research at scale — Click Tests, Prototype Tests, Likert scales, Multiple Choice, NPS, MaxDiff, and more — against a real audience, and turns the responses into UX Metric scores that drop straight into the Glare framework. Fast, structured user feedback for product design teams, in the same vocabulary Glare uses.

For what Helio can do at the platform level — every section type, every audience option, the full report surface — see Using Helio. This doc covers positioning, plans, and how Helio sits inside the Glare workflow.

### What this solves

Most product decisions get made on one or two stakeholder opinions and a hunch. The team ships, watches the dashboards, and learns what worked months later — when the trail back to the decision is cold.

Helio replaces the hunch with a metric, fast. You bring a question. Helio brings the audience, runs the test, and returns a signal you can name and use in the next review. No more "we think users will…" — you get what users actually did, plus how they felt about it.

### What Helio measures

Helio's measurement layer is the Glare framework's metric taxonomy, implemented in code. Today Helio covers two of Glare's four families:

- **Behavioral metrics (8)** — what people did. Success, Completion, Usability, Engagement, Effort, Comprehension, Frequency, Intent.
- **Attitudinal metrics (9)** — how people felt. Sentiment, Feeling, Desirability, Loyalty (NPS), Appeal, Usefulness, Expectations, Satisfaction, Brand Score.

Performance and Intelligence — the other two Glare families — are framework concepts not yet implemented in Helio's code.

Every metric returns a 0–100 score and a 5-tier label (Very Good / Good / Average / Poor / Very Poor). Helio also rolls every metric tagged on a study into a single **Overall Score**, the equal-weight average across all of them.

For the per-metric reference, see `helio-ux-metrics`. For how to read the scores, see `helio-reading-report`.

### Where Helio fits

Three product areas, each tuned to a different kind of question:

- **Market Research** — understand a market, segment, or category before committing to a direction.
- **Product Discovery** — test concepts and prototypes against real users before investing build effort.
- **UX Research** — validate workable designs and surface usability problems before launch.

For the section types and audience options that power each, see Using Helio (the DERIVED block below).

### Where Helio doesn't fit

Helio is built for fast, structured, large-N signal. Not every research need lives there.

- **Niche B2B audiences** — the panel skews consumer. For specialized professional segments, bring your own customer list or pair Helio with targeted recruiting.
- **Moderated qualitative interviews** — Helio is unmoderated. When the research question needs follow-up probes and live conversation, pair it with a moderated tool.
- **Production analytics** — Helio measures attitudes and reactions in test, not behavior in production. Use it alongside, not instead of, your analytics stack.
- **Performance and Intelligence metrics** — drop-off rate, time on task, error rate (Performance), and AI-experience quality (Intelligence) are Glare concepts not in Helio today. Source those from your analytics or AI eval tooling and bring them to the Design Review alongside the Helio result.

### Pricing

Pricing is measured in answers, where one answer is one response to one question from one participant. Helio is sold as engagement-based plans rather than a self-serve SaaS.

- **Pilot** — a focused 30-day discovery engagement to uncover design signals, define the UX metrics that matter, run usability tests, and deliver a roadmap. Contact for pricing. 10,000+ answers included.
- **Scale** — $19,999/month. Continuous discovery and testing with a Helio team. Up to 10,000 answers per month. The default path after a successful Pilot.
- **On Demand** — $4,999/month. Test with a Helio researcher who designs and runs focused studies and synthesizes the results. 5,000–10,000 answers depending on cadence.
- **Business** — $1,799/month. Self-managed access to the platform with audience segments. Up to 3,000 answers per month. Best fit for teams running multiple tests on their own.

See [helio.zurb.com/pricing](https://helio.zurb.com/pricing/) for the full breakdown, FAQs, and billing details. For how Helio's internal license / answers balance accounting works, see `helio-licensing`.

### Choosing a plan

Pick the path that matches where the team is:

- **Brand new to Helio, big initiative on the line?** → Pilot
- **Pilot worked, now you need it running continuously?** → Scale
- **Steady research needs, but lighter than a full program?** → On Demand
- **Internal team that wants to drive the platform themselves?** → Business

Every plan starts with a conversation. There is no self-serve signup.

### Getting started

- **New to Helio?** [Book a demo](https://helio.zurb.com/book-a-demo) or [talk to an expert](https://helio.zurb.com/talk-to-an-expert/). The "Run a Free Test" path on the marketing site also goes through this conversation.
- **Already have an account?** Sign in at [my.helio.app/login](https://my.helio.app/login).

If you'd rather drive the platform from your own tooling, Helio also exposes an API, a CLI, and an MCP server for AI assistants. Each has its own skill.

### Helio in the Glare workflow

Glare defines a design signal as four pieces: a user behavior observed, a metric that captures the reaction, the context that explains why it happened, and a direction the team can act on. Helio supplies the first three:

- **The behavior** is whatever you tested — a Click Test, a Prototype Test, a Preference, a Free Response, a MaxDiff, a Likert.
- **The metric** is what Helio computes — any of the 17 UX Metrics, returning a 0–100 score and a Very Good / Good / Average / Poor / Very Poor label.
- **The context** comes from how you sliced the audience and what the followups said.

Your team supplies the fourth piece: the decision the signal is meant to inform.

That makes Helio a natural fit at the Measure step of Glare's Decision Map, where signals get captured, and a ready source of evidence for Design Reviews, where signals get used.

For the full bridge from Helio result to Glare signal, see `helio-reading-report`.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1snPQ7OQY4UKqt7Pakgs2WY_1eqgX-hnbMG6AKtwuXS4 — Using Helio v0.2 -->

## Using Helio (capability tour)

Every Helio study follows the same shape: **build → recruit → read**. Build a sequence of questions, choose how to find participants, then watch responses turn into insight on the report.

### Building a Study

A study in Helio is a sequence of questions and tasks. You can mix any of the formats below in any order, and add logic like branching and follow-ups to shape each participant's path.

**To understand what people choose or prefer**

- **Preference** — Show two or more designs side by side and ask which one wins.
- **Multiple Choice** — Single- or multi-select from a list.
- **Rank** — Drag a list into priority order.
- **Point Allocation** — Give participants a budget to distribute across options.
- **MaxDiff** — Round-by-round "best of / worst of" comparisons.

**To hear what people think in their own words**

- **Free Response** — Open-ended text.
- **Free Response Follow-up** — A moderated follow-up after another question.

**To measure attitudes, feelings, or intent**

- **Likert** — A 5- or 7-point agreement scale.
- **Numerical Scale (NPS)** — A 0–10 willingness-to-recommend scale.
- **Matrix** — A grid that lets you ask several related questions on the same scale.

**To test usability**

- **Prototype Test** — Embed a Figma prototype with one or more expected paths through it. Captures clicks, screen-by-screen paths, time per screen, and grades each participant as Direct Success, Indirect Success, or Failed.
- **Click Test** — Show a static image and ask where participants would click.
- **Tree Test** — Test whether your information architecture works.

**To understand how people organize information**

- **Card Sort** — Open, closed, or hybrid sorting.

For each section type's full spec (configuration, what participants see, what comes back in the report), use `helio-section-types`.

#### Make your study smarter

- **Branching** — Route participants based on what they answered. See `helio-branching`.
- **Conditional follow-ups** — Show a follow-up question only to participants who picked a specific option.
- **Variations (A/B testing)** — Most question types let you run multiple variants in a single section.
- **UX metrics** — Tag questions to UX metrics like usability, satisfaction, or effort. See `helio-ux-metrics`.
- **Multiple languages** — Preview and run studies in different languages.
- **Preview viewports** — See how your study looks on mobile, tablet, and desktop before you launch.

#### Reuse and collaborate

- **Templates** — Save any study as a starting point for future ones. *Custom templates aren't available on the Pro plan.*
- **Copy a study** — Duplicate any study with one click.
- **Projects** — Group related studies together.

Edits autosave; a study can only be edited by one person at a time.

### Recruiting Participants

When you're ready to send your study, you choose where the responses come from. You can combine multiple audiences on one study.

- **Open Audience** — A shareable link. *All plans.*
- **Helio Panel — Basic** — Unfiltered access to Helio's global panel. *All plans.*
- **Helio Panel — Targeted Demographics** — Filtered by gender, age, education, income, country/region. *Pro and up.*
- **Helio Panel — Advanced Segments** — Filtered by custom screener attributes (job title, industry, company size). *Enterprise.*
- **Customer Lists** — Upload your own list; Helio emails them. *Enterprise.*
- **Intercept** — Triggered surveys inline on your own website. *Enterprise.*
- **API** — Submit responses programmatically. *Enterprise.*
- **AI Audience** — Synthetic responses from AI personas. *Enterprise.*

For the full audience flow (launch validation, panel availability, costs, refund rules), use `helio-audience-flow`.

### Reading the Report

The report updates live as responses come in. Each question type has its own view tuned to the kind of data it collects.

**Per-question views:**

- **Multiple Choice** — Percentage breakdown bars; word cloud of explanations.
- **Likert** — Distribution bars colored by sentiment.
- **NPS** — Score distribution and promoter/passive/detractor breakdown.
- **Free Response** — All text responses with common phrases auto-clustered.
- **Rank / Preference / MaxDiff** — Win/loss counts and relative importance.
- **Matrix** — Heatmap across rows and columns.
- **Card Sort** — Card placement frequency; suggested groupings.
- **Point Allocation** — Distribution graphs; per-option totals.
- **Click Test & Prototype** — Click heatmaps overlaid on the design; path visualizations for prototype tasks.
- **Tree Test** — Success rates by branch and the paths participants actually took.

**Filters:**

Filters apply across every question at once. Demographics (age, gender, country, income, education, company), Sentiment (positive / neutral / mixed / negative — *Enterprise*), Response time, Segments, By answer, By variation. For the filter mechanics, use `helio-report-filtering`.

**UX Metrics:**

Tag questions to UX Metrics for composite scores. Each metric produces a 0–100 score and a quality label (Very Good / Good / Average / Poor / Very Poor). Helio rolls every metric tagged on a study into a single Overall Score. For the full per-metric reference, use `helio-ux-metrics`.

**Findings & insights:**

Capture observations as Findings tied to any section or variation. For the Findings workflow, use `helio-findings`.

**AI features:**

- **Common Phrases** — Auto-clustered themes from open-text responses.
- **AI Summary** — Auto-generated test overview.
- **AI Chat** — Conversational Q&A over the test's data. *Admin only today.*

For the AI heuristic evaluation tool (a separate workflow from regular studies), use `helio-design-analysis`.

**Sharing & export:**

- Public report link, CSV export, copy data as text (*Beta*).

### Working with Your Team

- **Comments** — Discuss findings on a study, section, or variation.
- **Projects** — Group related studies.
- **Roles** — Admin, member, viewer-level access.
- **SSO** — Sign in with your company's identity provider. *Enterprise.*
- **Public API** — Pull tests, responses, and report data into your own tools.

### Plans at a glance

- **All plans** — Available to every Helio account.
- **Pro** — Deeper targeting + a few collaboration tools.
- **Enterprise** — Custom audiences (lists, intercept, API, AI), sentiment analysis, SSO, advanced segments.
- **Beta** — Newer features being rolled out.
- **Admin only** — Restricted to account admins.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is asking about Helio at the *platform* level — what it is, what it does, what plans cost, how to engage. It's the orientation entry point.

Drop into a sibling skill when the user is going deep on one surface:

- Section type questions → `helio-section-types`
- Audience questions → `helio-audience-flow`
- Metric questions → `helio-ux-metrics`
- Build workflow → `helio-asset-to-test`
- CLI / MCP → `helio-cli` / `helio-mcp`
- Engineering-side details (controllers, models, feature flags) → `helio-features`
- Reading and synthesizing results → `helio-reading-report`

## Failure modes

- **Conflating marketing plans with internal license tiers.** Helio's marketing plans (Pilot/Scale/On Demand/Business) are the customer-facing offer. The Answers & Licensing doc lists different internal tiers (Trial/Pro/Business 1–3/Scale/Design–Agency–Enterprise/Custom) for the answers-balance accounting model. Both are valid — don't merge them.
- **Treating Helio as a moderated research tool.** Helio is unmoderated. For interview-style research, pair with a moderated tool.
- **Assuming Performance metrics exist in Helio.** The Glare framework defines them; Helio doesn't implement them yet. If a question is about drop-off rate or time-on-task, name that gap explicitly and route to whichever analytics tool actually measures it.

## Where to go next

- For section type depth: `helio-section-types`
- For UX metrics: `helio-ux-metrics`
- For the build workflow: `helio-asset-to-test`
- For synthesis: `helio-reading-report`
- For the broader Glare framework: `glare-getting-started`

<!-- /ADDED -->

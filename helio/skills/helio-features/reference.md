# Helio Features — Reference

**Skill:** `helio-features`
**Source:** Helio Features v0.2
**Source last synced:** 2026-05-23
**Notes:** Source doc had two minor AEO-rubric gaps (Problem opener; Action pointer). Both are addressed in the ADDED sections at the end of this file. This skill was substantially reworked in v0.2 to remove internal codebase references that shouldn't be public — file paths, internal class names, feature flag names, migration numbers, internal constants. The focus is now the customer-facing feature catalog with plan-tier gating.

---

<!-- DERIVED FROM: 1EiBeoXl0EmzDx_Q--lzdydpA6lbtpfCTZRFU22JmE2I — Helio Features v0.2 -->

The feature catalog of Helio, organized by the lifecycle of a test: **create → send → read**. Each feature is annotated with its plan-tier gating where applicable.

Plan-tier annotations:

- **[All plans]** — available on every Helio account
- **[Pro]** — requires Pro tier or higher
- **[Enterprise]** — requires Enterprise tier
- **[Admin]** — restricted to account admins
- **[Beta]** — newer features still rolling out

## 1. Creating a Test

A Helio test is a single composable document. There is no top-level "test type" choice — every test is a sequence of sections, freely mixed.

### Section Types

Each section captures a different kind of input. All sections support optional follow-up questions, branching, and multivariate variations unless noted.

| Section | What it does | What it collects |
|---|---|---|
| Prototype Test | Embeds a Figma prototype with one or more expected paths through it. | Click and hover events, screen-by-screen paths, time per screen, task success (Direct / Indirect / Failed), drop-off points. Supports multiple expected flows. |
| Click Test | Shows a static image and asks participants where they would click. | Click coordinates, click counts, heatmap data. |
| Preference | Shows 2+ image variants and asks which the participant prefers. | Chosen variant; optional follow-up text. |
| Multiple Choice | Single- or multi-select from a list. | Selected choice(s); sentiment tag per choice (positive / neutral / negative). |
| Free Response | Open-ended text. | Text response; optional conditional follow-ups. |
| Likert | Ordinal agreement scale (e.g., 5- or 7-point). | Scale position; sentiment per choice; net positive alignment score. |
| Numerical Scale (NPS) | 0–10 willingness-to-recommend scale. | Numeric score; auto-segmented into detractors (0–6), passives (7–8), promoters (9–10); NPS calculated. |
| MaxDiff | Paired "best of / worst of" comparisons across rounds. | Best and worst picks per round; relative importance scores. |
| Rank | Drag-to-rank ordered list. | Ordered ranking; relative weights. |
| Point Allocation | Distribute a fixed point budget across items. | Points per item; relative value. |
| Card Sort | Open or closed card sorting. | Card-to-category mapping; user-generated categories (open) or placements (closed). |
| Tree Test | Navigate a hierarchical menu to complete a task. | Click path through the tree; success/failure; navigation depth. |
| Matrix | Grid of questions × scale choices. | Rating per row × column. |
| Free Response Followup | Human-moderated follow-up after another question. | Moderator-collected follow-up text; moderation status (open / complete / timed-out). |
| AI Section | Powers the **Design Analysis** feature — an AI heuristic evaluation of a design or prototype. Not a section researchers add by hand. | AI scores (1–5) on UX metrics with explanations. |

For section-by-section spec (configuration, participant experience, report views), use `helio-section-types`.

### Test Configuration

- **Multivariate / A/B variations** — Most section types support multiple variations within a single section. Responses are tracked per variation; participants are alternated between them.
- **Branching** — Conditional logic routes participants based on prior answers (e.g., "if Q1 = X, show Q2; else skip to Q3"). For full branching reference, use `helio-branching`.
- **Conditional follow-ups** — Any choice can trigger a follow-up question shown only to participants who selected it.
- **UX metric tagging** — Sections can be tagged to UX metrics for aggregated scoring (see Report section). For full UX Metrics reference, use `helio-ux-metrics`.
- **Localization** — Tests can be previewed in multiple languages.
- **Preview viewports** — Draft, mobile, tablet, desktop.

### Test Management

- **Autosave** — Edits save to the server automatically as you work.
- **Edit locks** — A test is locked to one user/tab at a time; stale locks (>5 min) can be taken over.
- **Copy test** — Duplicate any test as a starting point.
- **Templates** — Save a test as a reusable template. **[Enterprise]** for shared templates; custom templates are not available on Pro tier.
- **Draft / Preview / Launch** — Tests must pass validation before they can be sent.

## 2. Sending a Test (Audience)

After a test is built, researchers choose how to source participants. Multiple audience types can be combined on a single test.

| Audience | What it is | Targeting | Tier |
|---|---|---|---|
| Open Audience | A shareable public link. Used for social, email, or website distribution. | None (basic demographics collected post-hoc). | **[All plans]** |
| Basic Helio Panel | Unfiltered access to Helio's worldwide panel. | None. | **[All plans]** |
| Targeted Demographics | Helio's panel, filtered by demographic attributes. | Gender, age, education, income, country/region. | **[Pro]** |
| Advanced Segments | Helio's panel, filtered by custom screener-question segments (job title, industry, company size, etc.). | Custom screener attributes. | **[Enterprise]** |
| Customer Lists | Email invitations to a list the researcher uploads. | Per-list participant segments. | **[Enterprise]** |
| Intercept | Inline survey triggered for matching website visitors. | Device, visitor frequency, traffic source, page path, time on page, custom rules. | **[Enterprise]** |
| API Audience | Responses submitted programmatically. | None — server-side integration. | **[Enterprise]** |
| AI Audience | Synthetic participant responses generated by AI for fast iteration. | Configurable via AI persona/prompt. | **[Enterprise]** |

For full audience setup, use `helio-audience-flow`.

### Demographic Filters Available

Gender, age, education, income, country/region, employment status, job title, industry, company size, skills, device type. Available on Targeted and Advanced audiences and as filters on the Report.

## 3. Reading the Report

The Report is where researchers turn collected responses into insight. It supports drill-down per question, cross-cutting filters, and AI-assisted synthesis.

### Per-Question Visualizations

Each section type has its own report view:

- **Multiple Choice** — Percentage breakdown bars; word cloud of explanations.
- **Likert** — Distribution bars with sentiment tags.
- **NPS** — Score distribution and promoter/passive/detractor segmentation.
- **Free Response** — Text responses with auto-clustered common phrases; linked follow-ups.
- **Ranking / Preference** — Win/loss counts per item; visual ranking.
- **Matrix** — Cell-level heatmap; row and column aggregates.
- **Card Sort** — Card placement frequency; suggested groupings.
- **Point Allocation** — Distribution graphs; per-option totals.
- **MaxDiff** — Most/least chosen pair analysis.
- **Click Test / Prototype** — Click heatmap overlaid on the design; hotspot clustering; path visualization (prototype only).
- **Tree Test** — Success rate per branch; optimal path analysis.

### Filters

Applied to all questions simultaneously; the report updates live.

- **Demographics** — Age, gender, country/state/city, income, education, company. **[All plans]**
- **Sentiment** — Positive / neutral / mixed / negative. **[Enterprise]**
- **Response time** — Group by speed.
- **Segments** — By audience segment if applicable.
- **By question** — Filter to participants who gave a specific answer.
- **By variation** — When the section has multivariate variants.
- **By status** — Hidden, flagged, or marked-spam responses. **[Admin]** for some.

For full filtering reference, use `helio-report-filtering`.

### UX Metrics

Helio's measurement layer, derived from the Glare framework.

**Implementation status:** Glare defines four metric families (Attitudinal, Behavioral, Performance, Intelligence). Helio currently implements the first two — 17 metric types total. Performance and Intelligence metrics aren't in Helio today.

**Behavioral (8):** usability, effort, comprehension, engagement, completion, frequency, success, intent
**Attitudinal (9):** sentiment, feeling, desirability, loyalty, appeal, usefulness, expectations, satisfaction, brand_score

**How tagging works:**

- Researcher picks a metric when creating a section. The metric type dictates the section structure — the platform auto-builds the required sections (e.g., Brand Score generates a 3-section template).
- Each metric has section-type requirements enforced by the platform. Researchers cannot freely tag any section with any metric.

**Score computation:**

- Computed live (not stored), so scores recompute whenever filters change.
- Returns score (0–100), threshold label (Very Good / Good / Average / Poor / Very Poor), and a calculation breakdown.

**Composite test score:**

- The platform rolls every metric tagged on a study into a single Overall Score — equal-weight average across all metrics, returned as 0–100.

**Feature gating:**

- UX Metrics are gated by an account-level toggle. If not visible, contact your account manager.

For full per-metric reference, use `helio-ux-metrics`.

### Findings & Insights

- **Findings panel** — User-authored observations linked to specific sections or variations.
- **Search** — Full-text search across findings.
- **Favorites** — Mark insights to filter to them later.

For full Findings reference, use `helio-findings`.

### AI Features

- **AI Chat** — Conversational Q&A over the test's response data. **[Admin]**
- **Common Phrases** — Auto-clustered themes from open-text responses.
- **AI Summary** — Auto-generated test overview where available.

For the AI heuristic evaluator (a separate workflow), use `helio-design-analysis`.

### Responses Panel

- View, search, and inspect individual responses.
- Upvote / heart standout responses.
- Filter by hidden, flagged, or spam status.

### Moderation **[Admin]**

- Flag individual responses as low-quality.
- Mark responses as spam.
- Bulk flag or freeze a participant's data across tests.
- Toggle spam-highlight visibility.

### Sharing & Export

- **CSV export** — Full response data with demographics and per-question breakdowns; configurable fields.
- **Public report link** — Shareable, view-only URL.
- **Copy data as text** — Structured copy of all responses or all question summaries. **[Beta]**
- **Take link** — Direct link to the test for sharing.

### Test Management from the Report

- Send / stop the test.
- Order more responses.
- Edit, preview, copy, or delete the test.
- Save as template.

### Collaboration

- Comments on test, sections, and variations (if enabled).
- Findings authoring and favoriting.
- Response upvotes.

## Cross-Cutting & Account-Level Features

These aren't part of a single test's lifecycle but shape what researchers can do.

- **Projects** — Group related tests.
- **Account roles** — Admin, member, viewer-level access.
- **SSO** — Enterprise SAML / OAuth login. **[Enterprise]**
- **Public API** — Programmatic access to tests, responses, and reports.
- **Webhooks** — Available for select platform events.
- **Audit log** — Account activity audit trail.

## Open Questions / To Verify

Items that may not be fully confirmed against the live product:

- Exact panel size figures.
- Pricing per audience type.
- Which "Beta" / "Internal" capabilities are currently active for any given customer tier.
- Tree Test and Card Sort — confirm current UI completeness.
- Where Design Analysis lives in the UI (separate flow vs. inside test create) and how researchers access it.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem + Action gaps) -->

## What this solves

Customer-facing language for what features exist in Helio and which are gated to which plan tier. Without this catalog, support tickets get misrouted ("is this feature on my plan?"), planning gets confused ("do we need Enterprise for X?"), and feature ambiguity (is this Pro, Enterprise, Beta?) hides real impact.

## When to use

Reach for this skill when the user is:

- Asking "what's available on my plan" or "what plan do I need for X"
- Reading a Helio doc that mentions a feature and wondering if they have access
- Planning a research program and budgeting which features to use across their team
- Confused about whether a feature is Beta or generally available
- Looking for an Admin-only feature and wondering who has access in their org

This is a reference, not a how-to. For how-to flows, use `helio-app` (positioning + plan choice) or `helio-asset-to-test` (build workflow). For per-feature depth, use the specific sibling skill.

## Failure modes

- **Treating the gating annotations as exhaustive.** Individual features can be enabled per-account independently of plan tier. If a feature is missing without explanation, contact your account manager.
- **Citing the Open Questions list as authoritative.** Those items need confirmation against the live product. Verify before relying.
- **Treating tier annotations as immutable.** Plan structures evolve. Always confirm current state against `helio.zurb.com/pricing` or contact sales.

## Where to go next

- For positioning and plan choice: `helio-app`
- For billing accounting (answers, refunds): `helio-licensing`
- For section type details: `helio-section-types`
- For UX metrics: `helio-ux-metrics`
- For audience setup: `helio-audience-flow`
- For the AI heuristic evaluator: `helio-design-analysis`
- For Findings: `helio-findings`
- For report filtering: `helio-report-filtering`
- For participant experience: `helio-participant-experience`

<!-- /ADDED -->

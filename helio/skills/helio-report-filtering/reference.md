# Report Filtering — Reference

**Skill:** `helio-report-filtering`
**Source:** Report Filtering v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had two minor AEO-rubric gaps (Problem opener; Action pointer). Both are addressed in the ADDED sections at the end of this file.

---

<!-- DERIVED FROM: 1s9892SdPp4NeuyZqXclunIYKDawo1qB6S_LZWCGihgg — Report Filtering v0.1 -->

How to slice your data on the Helio report — every filter type, how they combine, and what to know about edge cases.

For broader report context, use `helio-reading-report`.

## How Filters Work

Filters apply to **all questions at once** on the report — set them on the demographic panel or per-question, and the report re-renders with only the matching participants.

Filters combine with **AND** logic across categories (Female + age 25–34 + answered "Yes" to Q3 = participants who match all three). Within a single filter category, multiple selections combine with **OR** (Female + Male = anyone of either gender).

Filters are URL-persistent — your filtered view is shareable as a link. Note that the URL only updates when you load the page, not as you toggle filters, so to share a specific view you need to copy the URL after you've set the filters and refreshed.

## Demographic Filters

| Filter | Type | Source |
|---|---|---|
| **Gender** | Multi-select | Participant-provided or panel attribute |
| **Age** | Bucketed (e.g., 18–24, 25–34) | Participant-provided or panel attribute |
| **Country / State / City** | Multi-select | Geocoded from participant data or panel |
| **Company** | Multi-select | Participant input or custom-list attribute |
| **Income** | Multi-select bucketed | Participant or panel |
| **Education** | Multi-select | Participant or panel |
| **Response time** | Bucketed (< 5s, 5–10s, > 10s, or custom range) | Calculated from response duration |
| **Sentiment** | Multi-select (Positive / Neutral / Negative / Mixed) | Auto-extracted from Free Response text |
| **Segment** | Multi-select | Audience segment (Enroll panel) |

**Where demographics come from depends on the audience:**

- **Open audience** — Collected post-hoc from participants if asked.
- **Helio panel (Basic / Targeted / Advanced)** — Pre-loaded from the panel.
- **Customer Lists** — Whatever you attached to the list, plus optional post-hoc fields.

**Missing data behavior:** Filters exclude participants with no value for that demographic — there's no "unknown" bucket. If you filter by country, anyone whose country wasn't captured won't show up at all in that view.

## Question-Level Filters

Click into any question on the report to filter by how participants answered it. The available options depend on the section type.

| Section type | Filter options |
|---|---|
| **Multiple Choice, Likert, NPS, Tree Test** | Select one or more specific choices |
| **Preference** | Select one or more variations |
| **MaxDiff** | Filter by which option was picked as best / worst, in which round |
| **Card Sort** | Filter by card-to-category placement |
| **Free Response** | Filter by selected phrases extracted from the responses |
| **Click Test** | Filter by individual response (useful when drilling into specific click patterns) |
| **Prototype Test** | Filter by path type: Direct Success, Indirect Success, or Failed |

**Phrase filtering on Free Response** matches the substring case-insensitively. Multiple phrases combine with OR — selecting "easy" and "intuitive" shows participants who said either.

## Status Filters (Admin)

These don't apply to most researchers, but admins can filter responses by status:

- **Hidden** — Responses manually hidden from the standard view.
- **Flagged** — Responses flagged as low quality.
- **Spam** — Responses marked as spam.

## Sentiment Filter Specifics

Sentiment is detected on Free Response text in 6 languages (English, Spanish, French, Italian, German, Portuguese). It's not generated for other section types.

If your study has no Free Response sections, the sentiment filter will return no results — there's nothing to score.

Sentiment is an Enterprise feature. If you don't see the filter in your account, that's why.

## What the UI Shows

- A bottom bar lists every active filter with a remove button per filter.
- The filter panel shows a count of active filters as a badge.
- **Clear individual** — Click the X next to any filter in the bottom bar.
- **Clear all** — "Clear Filters" button resets every selection at once.

What's *not* there today:

- Saved filter sets / presets.
- "Compare cohort A vs. cohort B" side-by-side views.
- An obvious "X participants match these filters" headline (per-question counts update, but the global total isn't displayed prominently).

## Audience Segment Filter

For studies that used Helio's panel with Advanced Segments, the segment filter lets you slice by which segment each participant came from.

If you're using the API to inspect quota data, segment IDs may not match what you see in the UI — they're stored as opaque identifiers internally. Use the API's documented endpoints to map between them.

## The View Flows Modal (Prototype filtering)

For Prototype Tests, the "View Flows" feature lets you build a custom screen sequence and filter to participants whose path matched it. Three match modes:

- **Contains path** — Participants visited the screens in order, consecutively.
- **Includes screens** — Participants visited the screens in order, with gaps allowed.
- **Exact path** — Participants visited exactly those screens in that exact order, no extras.

Use this when the path-type filter (Direct / Indirect / Failed) is too coarse — for example, when you want to see only participants who reached the goal but went through a specific detour.

## Performance & Caching

The report caches data per unique combination of filters. Each set of filters gets its own cached snapshot, so toggling between common filter sets is fast.

**Cache freshness gotcha:** If responses were graded or processed after the cache snapshot was taken (e.g., a Prototype Test response just finished its background grading), the cached view may be stale. Reloading the page typically rebuilds the cache; if not, ask an admin to clear it.

**Performance with many filters:** Each question-level filter adds a query condition. The report stays fast at typical scale (~thousands of responses with a handful of filters), but stacking many question-level filters on a very large response set can slow things down.

## Limits and Edge Cases

- **No hard limit** on number of filters applied, but URL length caps practically limit you to ~50–100 question-level filter values before browsers truncate.
- **Hidden / flagged / spam** filters only apply to response-level status; they don't filter individual section responses within a participant.
- **Demographic data is not refreshable** mid-study — once a participant's demographics are captured, they're fixed for that response.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem + Action gaps) -->

## What this solves

Helio's report is meaningless without the right filter applied — a Good Overall score can hide a Poor segment, and synthesis-grade signals live in cohort-specific cuts. Teams default to reading top-level averages and miss the segment spread that's the actual finding. This skill exists so the slice happens deliberately.

## When to use

Reach for this skill when the user is:

- Slicing report data by demographic, segment, or question answer
- Combining filters and confused about AND vs OR behavior
- Hitting "no participants match" and wondering whether it's a real-zero or missing-data
- Trying to use the sentiment filter and discovering it needs Free Response sections + Enterprise tier
- Filtering Prototype Test paths and needing more than Direct/Indirect/Failed (use View Flows)
- Wishing for saved filter presets or side-by-side cohort views (they don't exist today)
- Sharing a filtered view URL and confused about when the URL actually updates

For synthesizing filtered data into a Glare signal, route to `helio-reading-report`. For UX metric scores recomputing with filters, use `helio-ux-metrics`.

## Failure modes

- **Reading the headline Overall without any filter applied.** Average can hide segment-level findings. Always cut by audience for synthesis.
- **Forgetting missing-data is silently excluded.** A "no Hispanic respondents" finding might actually mean "country wasn't captured for those participants."
- **Sharing a filter URL without refreshing first.** The URL only updates on load. Toggle filters, refresh, then copy.
- **Combining sentiment filter with non-Free-Response sections.** Returns empty. Sentiment only scores Free Response text.
- **Trying to filter individual section responses within a participant using status filters.** Status applies to whole responses, not sections.
- **Comparing cohorts by toggling filters back and forth.** Helio doesn't have a side-by-side view today; for true comparison, use `helio-mcp`'s `compare_segments` tool.

## Where to go next

- For synthesis using filtered data: `helio-reading-report`
- For UX metrics that recompute with filters: `helio-ux-metrics`
- For demographic capture mechanics: `helio-audience-flow`
- For MCP-based cohort comparison: `helio-mcp`

<!-- /ADDED -->

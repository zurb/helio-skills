# Findings & Insights — Reference

**Skill:** `helio-findings`
**Source:** Findings v0.1
**Source last synced:** 2026-05-23

---

<!-- DERIVED FROM: 1PouJK0KPyZLxH54j6gntjirCxHXOzF1jupwzPJRX1K4 — Findings v0.1 -->

How to capture, organize, and share observations from your studies.

**Naming note:** "Finding" and "insight" are used interchangeably across the platform. They refer to the same thing.

## What a Finding Is

A finding is a captured observation — a note tied to something specific in your study (a section, a variation, a particular response, or the study as a whole). Findings turn the raw data on your report into a synthesized story you can share with stakeholders.

Each finding has:

- **Text** — the observation itself (rich text with formatting and inline references).
- **What it's attached to** — a study, a section, a variation, or your account workspace.
- **Tags** — categorization (defaults to "observation").
- **Filter context** — if you set filters on the report when you captured the finding, those filters are snapshotted so you remember the cohort the observation applies to.
- **A favorite flag** — per user; not shared across the team.
- **Optional sharing** — a public URL that doesn't require Helio login.
- **An author and timestamp**.

## Where Findings Live

Findings can attach at any level:

- **Test-level** — observations about the study as a whole.
- **Section-level** — tied to a specific question.
- **Variation-level** — tied to a specific A/B variant in a section.
- **Account-level** — broader observations not tied to a single study (sometimes called "workspace insights").

Each level shows its own counts in the UI — open a study and you'll see the number of findings on that test; open a section and you'll see the subset that attach to that section.

## Capturing a Finding

From the report's Findings panel, hit the "create finding" button. You'll be writing rich text — Helio sanitizes the HTML but allows formatting, inline references to other findings, and attachments.

What gets captured automatically:

- **You** as the author.
- **Timestamp**.
- **The current filter context** on the report — if you filtered to "Female, age 25–34" before capturing the finding, that snapshot stays on the record. The finding doesn't auto-update if you change the filters later; it remembers the cohort you saw at the time of capture.
- **A relative ID** — a friendly per-project sequence number (Finding #1, #2, #3 within a project) so you can reference findings by simple numbers.

Optional:

- **Attach a design or screenshot** (an asset from your library).
- **Tag the finding** for later filtering.
- **Mark it as a favorite** to come back to easily.

## AI-Generated Findings (Status)

You may have seen mentions of "AI-generated findings" elsewhere. **As of today, automatic generation isn't actually wired up.** The Findings system is currently manual — researchers capture observations themselves.

What *does* exist:

- **AI Summary** — auto-generated test overviews, but this is a separate feature for AI Tests (not regular participant studies), and it's not stored as a Finding.
- **Common Phrases** — automatic thematic clustering of Free Response text, but this is a separate panel, not Findings.
- **AI Test Generation** — generates the structure of new tests, not insights from existing ones.

So when you see "AI-generated insight" in the UI, it's most likely a researcher who wrote one up using AI assistance externally, not Helio auto-generating. The infrastructure for first-class AI-generated findings is being built but isn't shipping yet.

## Browsing and Searching

The Findings panel supports:

- **Full-text search** across the text, tags, author, and the section it's tied to.
- **Sort** by Recent, Oldest, A→Z, Z→A, or relative ID.
- **Scope filter:**
   - **All** — every finding in the project.
   - **Mine** — only findings you wrote.
   - **Others'** — findings everyone else wrote.
   - **Shared** — findings in shared projects.
- **Favorites filter** — show only what you've hearted.
- **Tags filter** — narrow by tag.

For account-wide search across many studies, Helio's search is indexed for fast cross-study lookups even with thousands of findings.

## Favorites

The favorite flag is a quick personal-curation tool. Each researcher's favorites are independent — your favorites don't show up when a teammate filters their favorites view.

Use favorites to:

- Mark findings worth coming back to during synthesis.
- Build your shortlist of "things to share in the readout."
- Pin the most-important observations to the top of long lists.

Counters for "favorited" exist at the test, section, variation, and project levels — useful when you have hundreds of findings and want to see which ones got the most attention.

## Sharing Findings

Each finding can be made shareable. Toggle the "share" flag and Helio generates a public URL (a unique share UUID) anyone can open without a Helio account.

Use cases:

- Drop a finding URL into a Slack thread for a quick share.
- Embed a finding in a doc or wiki.
- Send specific findings to stakeholders without exposing the full report.

You can also regenerate a finding's share URL — useful if you've shared something and want to invalidate the old link.

## Comments on Findings

Comments are a separate but related concept — they let teammates discuss observations on a section or study.

Comments support:

- **@-mentions** of teammates, which trigger notifications.
- **Mark as resolved** — close out a thread once it's addressed.
- **Real-time updates** — comments appear live for anyone viewing the section.
- **Email rollups** — @-mentions trigger email notifications, batched in 15-minute windows.

Comments differ from findings in intent:

- A **finding** is an observation you want to capture and possibly share.
- A **comment** is a conversation thread on a section or finding — used for discussion, not for documenting an insight.

## Editing and Deleting

Findings can be edited freely — text, tags, attachments, the section they're tied to. Edits don't create version history; the finding is overwritten with the new content.

Deletion is soft — findings are marked deleted, not removed from the database. They disappear from the UI but can be recovered by an admin if needed.

When a finding is deleted, references *to* it (other findings that mentioned it via inline reference) get cleaned up automatically.

## Findings vs. Report Filters

A subtle interaction worth understanding:

- When you **capture** a finding, the current report filters are snapshotted onto the finding's state.
- When you **view** a finding later, the filters that were active when you captured it don't auto-reapply — you'd need to reapply them manually if you want to see the same view that prompted the finding.

This is by design — a finding stands on its own as a documented observation, independent of how the report is currently filtered. The snapshotted filter context is there for your own reference, so months later you can remember "this finding was specifically about the 25–34 age group."

## Limits and Good to Know

**No max number of findings per test.** Capture as many as you need.

**Findings don't auto-update.** If new responses arrive after you capture a finding, the finding doesn't re-evaluate — it's a snapshot of an observation, not a live calculation.

**No history / versioning.** Edits overwrite. If you need to preserve an earlier version, copy the text elsewhere before editing.

**Findings and comments share infrastructure.** If you're using the public API to pull data, you may see both types of records with a type indicator distinguishing them. You can filter to one or the other in the API.

**Inline references between findings.** A finding can reference another finding by ID — these become links in the rendered text and update if the referenced finding's text changes. Use this to build chains of related observations.

**No CSV export of findings yet.** Findings don't export as part of the standard CSV. To get them out of Helio in bulk, the public API is currently the path.

**Search indexing happens asynchronously.** Newly created findings may take a few seconds to show up in account-wide searches, even though they're immediately visible in the current study's Findings panel.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Capturing observations during report synthesis
- Searching across findings (account-wide search or project-scoped via the panel)
- Asking why "AI-generated findings" don't show up automatically (they don't — manual today)
- Confused about findings vs comments (observation to share vs conversation to resolve)
- Sharing a finding externally and wondering about URL stability and regeneration
- Bulk-exporting findings (API is the path; no CSV today)
- Editing a finding and discovering edits overwrite (no version history)

For the broader synthesis workflow (turning findings into a Glare signal), use `helio-reading-report`. For the moderated follow-up workflow (a different feature with researcher-initiated follow-ups that consume 10 answers each), use `helio-section-types`.

## Failure modes

- **Expecting AI to auto-generate findings.** It doesn't today. Use AI Summary and Common Phrases as adjacent tools, but writing findings is manual.
- **Confusing findings with comments.** Both share the underlying model, but findings are observations and comments are discussion. Use the right one for the intent.
- **Treating filter context as live.** A finding remembers the filters at capture but doesn't re-apply them on later views. Reapply manually if you need the cohort view.
- **Editing a finding expecting to preserve history.** Edits overwrite. Copy elsewhere if you need a record.
- **Sharing a finding URL and forgetting it's a stable public link.** Anyone with the URL can view forever. Regenerate the share URL if you need to invalidate.

## Where to go next

- For synthesizing findings into a Glare signal: `helio-reading-report`
- For moderated follow-up workflow: `helio-section-types`
- For filter context that gets snapshotted: `helio-report-filtering`
- For AI Chat / AI Summary / Common Phrases (adjacent features): `helio-features`
- For broader feature gating and plan tier: `helio-features`

<!-- /ADDED -->

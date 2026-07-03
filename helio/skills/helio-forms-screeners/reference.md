# Forms & Screeners — Reference

**Skill:** `helio-forms-screeners`
**Source:** Forms & Screeners v0.1
**Source last synced:** 2026-06-29

---

<!-- DERIVED FROM: 1wW2_BSgD_8RNuF3FzFwGyCKNW0xY3MtBfb-0MzjYux4 — Forms & Screeners v0.1 -->

Two distinct things in Helio carry the word "screener," and they're easy to confuse. This doc covers both — what they are, how they differ, and when to use which.

## Two Ways to Screen

### 1. Formal Screeners (Form-based)

**What they are:** Pre-membership qualification questions that run when someone signs up to a Customer List via a Helio Form (a landing page or embedded modal).

**Who sees them:** People joining a Customer List — typically a sign-up flow on the researcher's site, not test participants going through a study.

**When they run:** Before someone becomes a list member, not during a study.

**What they do:** Capture qualifying information that gets attached to the participant record so future studies can target them by their answers.

### 2. Inline Screening (Multiple Choice + Branching)

**What it is:** A regular Multiple Choice section at the top of a study, with branching configured to route disqualified participants to an "end of test" with a custom message.

**Who sees it:** Anyone taking the study.

**When it runs:** At the start of the study itself.

**What it does:** Filters participants out of *this specific study* by routing them to a thank-you screen with a "doesn't apply to you" message.

These are different features. Formal Screeners qualify someone for membership in a Customer List; Inline Screening qualifies someone for a single study.

The rest of this doc covers Formal Screeners, since they're a distinct subsystem worth understanding. Inline Screening is just a regular section + a branch — see `helio-branching`.

## Formal Screeners: The Form-Based System

### Forms

A **Form** is a Helio-hosted landing page or embeddable modal that signs people up to a Customer List. Forms belong to Customer Lists; they don't belong directly to tests.

Each Form carries:

- **Branding** — logo, primary color, banner text, landing page text.
- **Demographics collection** — toggles for gender, age, income, education.
- **Verification** — email verification text and success messages.
- **Opt-in** — whether to show, and whether to require, an opt-in checkbox with custom text.
- **Domain & banner** — for embedded mode.
- **Up to 5 screeners** — qualification questions (see below).

A Form can be active or suspended. Suspended forms stop accepting submissions but keep their data.

### Screener Types

Four screener types, each with the same data shape as their non-screener counterparts:

| Screener | What it captures |
|---|---|
| Multiple Choice Screener | Selection from a list — single or multi-select |
| Likert Screener | Scale response (uses the same Likert templates as regular sections) |
| NPS Screener | 0–10 scale |
| Free Response Screener | Open text (single-line or textarea) |

Each screener has:

- **Instructions** — the question text shown to the person filling out the form.
- **Required / optional** — defaults to required.
- **Position** — order within the Form.
- **Choices** (for Multiple Choice, Likert, and NPS) — answer options with optional pinning and randomization.
- **Status** — active or disabled (soft disable, preserves responses).

### What the Form Captures

When someone submits a Form:

1. A **Participant** record is created or matched.
2. Their **demographics** are captured (from any toggled-on fields).
3. Their **screener responses** are stored against their participant ID.
4. They're attached to the **Customer List**.
5. The participant can later be included in studies that target this Customer List.

The submission counts against your account's panelist limit (not your answers balance).

## What Screeners Don't Do (Today)

A few important nots:

**Screeners don't disqualify automatically.** There's no built-in routing that says "if they pick option B, refuse them." Every Form submission becomes a Customer List member. Whether to exclude someone is a downstream filtering decision when you target the list with a study.

**Screeners don't carry branches.** Unlike regular sections, screeners don't route.

**Screeners don't show up in test branching.** Their answers are stored on the Participant record, not on study responses. To act on screener answers, you target a subset of the list when launching a study.

**Free Response screeners can't auto-disqualify.** No keyword matching, no length thresholds — just text capture.

## Setting Up a Form

Forms are configured under Customer Lists in the dashboard:

1. **Customer Lists → New Form** (or edit an existing one).
2. Set the **landing-page branding** — logo, colors, banner text.
3. Configure **demographics collection** — which fields to ask.
4. Add **screener questions** — up to 5, in order.
5. Set **email verification** copy.
6. Configure **opt-in** if needed.
7. Mark the Form **active** to start accepting submissions.

You can use the Form as:

- A **landing page** — Helio hosts a URL anyone can visit to sign up.
- An **embedded modal** — drop a snippet on your own site to trigger the Form inline.

## Targeting Studies by Screener Answers

Once you have a Customer List with screener responses attached to each member, you target a subset when launching a study:

1. Create a study and choose **Customer Lists** as the audience.
2. Pick the Customer List you want to target.
3. Filter members by their screener answers (or by other attributes).
4. Launch.

The study goes only to members who match your criteria.

This is where the "screening" effectively happens — at study launch time, you choose who from the list to invite, based on what they answered when they signed up.

## Disabling vs. Deleting Screeners

If a screener has responses (any Customer List member has answered it), it can't be deleted — only disabled. Disabling preserves existing responses but removes the screener from the active list for new submissions.

This is similar to the "soft delete" pattern used elsewhere in Helio. To clean up old screeners, disable them; admins can permanently delete them if needed.

## When to Use Formal Screeners vs. Inline Screening

| Situation | Use |
|---|---|
| You want to build a long-term audience of qualified people who you study repeatedly | **Formal screeners** on a Customer List Form |
| You're running a single study and need to filter participants at the door | **Inline screening** — a Multiple Choice section + branch to end-of-test |
| You want screener answers to enrich participant records for future use | **Formal screeners** |
| You don't have a Customer List — using Helio's panel or open audience | **Inline screening** (or Targeted Demographics on the Helio panel) |
| Mixing demographics + qualification | **Formal screeners** (Forms also collect demographics) |
| Doing IRB-style consent up front | **Inline screening** — Multiple Choice with "I agree / I do not agree" and branch the latter to end-of-test |

## Limits and Good to Know

**Maximum 5 screeners per Form.** Hard limit; not configurable.

**Free Response screeners stop at text capture.** No validation, no keyword matching.

**One screener response per participant.** A participant can't take the same Form twice and update their answers — the second submission would fail the uniqueness constraint.

**Multi-select Multiple Choice screeners are supported** (unlike inline branching, which requires single-select). Since screeners don't route, multi-select is fine.

**Forms aren't directly connected to Helio's panel.** They're a Customer List concept. If you want to build a qualified audience from Helio's panel, use Advanced Segments instead — that's the panel-side equivalent.

**The Form landing page is Helio-hosted.** Custom domains for Form landing pages exist but require per-account setup. The default is a helio-hosted URL.

## Related

- `helio-audience-flow` — how Customer Lists become audiences for studies.
- `helio-branching` — for inline screening via branching.
- `helio-section-types` — for the underlying section types the screeners mirror.

<!-- /DERIVED -->

---

<!-- ADDED 2026-06-29 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Setting up a Customer List signup Form and configuring its screener questions
- Confused between the two "screener" concepts (Form-based vs Inline)
- Trying to disqualify at test start and wondering which pattern to use
- Hitting the 5-screener-per-Form limit
- Discovering that Form submissions don't auto-disqualify
- Trying to delete a screener with responses and being blocked
- Designing an IRB consent flow (inline pattern with Multiple Choice + branch)

For broader test design where screening is one step, route to `helio-asset-to-test`. For the Customer List audience once the list exists, route to `helio-audience-flow`.

## Failure modes

- **Confusing Formal Screeners with Inline Screening.** They're different features. Formal Screeners live on a Customer List signup Form; Inline Screening lives at the start of a study. Pick based on whether you're building an audience or filtering a study.
- **Expecting Form submissions to auto-disqualify.** They don't. Every submission joins the list; qualification is a launch-time targeting decision.
- **Trying to branch off a screener answer.** Screeners don't route. Use their answers to filter at launch, or use Inline Screening if you need branching at the point of the question.
- **Exceeding the 5-screener limit.** Hard limit. If you need more qualifying questions, ask them in Inline Screening at study start.
- **Trying to delete a screener with responses.** Blocked. Disable it instead.
- **Forgetting that screeners on multi-select Multiple Choice are fine here.** Multi-select branching isn't supported in Inline Screening, but multi-select is fine on formal screeners because they don't route.

## Where to go next

- For Customer List audience config after the list is populated: `helio-audience-flow`
- For branching config (used by Inline Screening): `helio-branching`
- For Multiple Choice / Likert / NPS / Free Response section spec generally: `helio-section-types`
- For the full test-build workflow: `helio-asset-to-test`
- For how these fit into Helio's broader data model: `helio-concepts`

<!-- /ADDED -->

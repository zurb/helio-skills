# Branching Logic — Reference

**Skill:** `helio-branching`
**Source:** Branching v0.1
**Source last synced:** 2026-05-23

---

<!-- DERIVED FROM: 1ki9ZxmM-CUBwE-0gwnBkDm-BBxlgxHo44_AzX3-YSXE — Branching v0.1 -->

How to route participants down different paths through your study based on what they answer.

For context on what branching looks like at the section level, use `helio-section-types`. Most section types support branching — the rules below cover where and how.

## What Branching Does

Branching changes what happens *after* a participant answers a question. Without it, every participant goes through the same sections in order. With it:

- A participant who picks "Yes" jumps to a follow-up section; one who picks "No" skips past it.
- A participant who fails a screening question ends the test early with a custom message.
- A participant who picks a particular variation gets redirected to your own page after completing.

Branching is configured at the **choice level**, not the section level. Each individual choice (or hotspot, or ranked answer) can carry its own routing.

## What Can Trigger a Branch

| Section type | Branchable from | Notes |
|---|---|---|
| **Multiple Choice** | Each choice | Single-select only — see below |
| **Click Test** | Each hotspot | Branch by which hotspot the participant clicks |
| **Rank** | Best **or** worst answer | Configure which via the "branching label" setting |
| **MaxDiff** | Best **or** worst answer | Same as Rank |
| **Tree Test** | Each choice | Branch by which leaf the participant picks |
| **Card Sort, Point Allocation, Matrix** | Each choice | Branch by answer |
| **Prototype Test** | Limited | Most prototype routing happens inside Figma itself |

**Not supported:**

- **Likert, NPS, Preference, Free Response** — these section types don't carry branching.
- **Multi-select Multiple Choice** — branching requires single-select. The system blocks branching when you have a multi-select question because "if they picked A *and* C" creates ambiguous routing.

## What a Branch Can Do

Every branch has an **action** that determines where the participant goes:

| Action | What happens |
|---|---|
| **Jump to a section** | Skip directly to a specific section later in the study. |
| **End the test** | The participant goes straight to the thank-you screen. |
| **End the test with a custom message** | Same as ending the test, but the participant sees a custom message you write (this is how disqualification works — see below). |
| **Redirect to an external URL** | After completing, send the participant to your own URL. Useful for follow-on flows in your product. |
| **Continue to next section** | The default fall-through if no branch is set on the choice. |

**No backward looping.** Branches always go forward in the section order. You can't route a participant back to an earlier section.

**One target per choice.** A choice can only branch to one place — no multi-target or conditional-on-multi-answer routing.

## Disqualification

Helio doesn't have a separate "disqualify" action. Disqualification is just **End the test with a custom message** — typically something like *"Thanks for your time — based on your answers, this study isn't a fit for you."*

The participant sees this message instead of the standard thank-you screen. From their perspective, they're done with the study. There's no visible flag that says "you were disqualified."

## How Targets Stay Stable

Helio identifies branch targets by a **UUID per section**, not by position. This matters because:

- **Reordering sections** doesn't break branches — the UUIDs travel with the sections.
- **Cloning a test (or saving as a template)** preserves branching automatically — all the UUIDs get remapped to the new sections in the clone.

You don't see UUIDs in the UI. The editor shows you "Jump to Question 4" — Helio handles the underlying reference.

## Setting Up Branches in the Editor

Branching configuration lives inside the section editor. The general pattern:

1. Open a section that can branch (e.g., Multiple Choice).
2. For each choice, you'll see an option to set a branch.
3. Pick the action (Jump / End / Redirect) and the target.
4. The editor shows a visual indicator on choices that have branches set.

For Rank and MaxDiff, you'll see a "branching label type" toggle — choose whether the branch fires on the **best** or **worst** answer.

## Validation at Launch

Helio blocks launch if a branch is incomplete (configured but pointing nowhere). The editor highlights these so you can fix them before you can send the test.

What Helio **does not** automatically catch:

- **Orphaned branches** — if you delete a section that another section branched into, the branch becomes an orphan. Helio doesn't surface this — the participant just falls through to the next sequential section instead.
- **Circular references** — not preventable at the data level (forward-only routing limits this, but you can still create unreachable sections).
- **Unreachable sections** — sections nothing branches to and that come after a branch that always fires can sit there with no traffic. No warning today.

If you've been heavily editing a study with branching, do a manual pass to check that every section is still reachable and that no branches point at deleted targets.

## Branching and UX Metrics

A subtle gotcha: if you branch participants past a section that's tagged with a UX Metric, those participants never answer that section — so they don't contribute to the metric's score. Depending on how many participants branch away, this can:

- Drop the metric's response count below a useful threshold.
- Skew the metric toward whoever didn't branch out (which may not be a representative sample).

There's no automatic check for this today. If you're using branching alongside UX Metrics, think about which metrics get answered by which branches.

## Branching and Quotas

**Branched-out participants count toward your quota.** A participant who ends the test early via a disqualification branch still consumes their share of the quota — they answered enough sections to count.

This is by design (you paid for their attention) but can be surprising. If you're running a heavy screener at the top of a study to filter for a specific audience, expect significant quota burn on participants you ultimately disqualify.

There's no separate "qualified vs. disqualified" count in the report today — you'd identify them by filtering on the screener question's answer or by spotting the custom thank-you message they hit.

## Branching and Conditional Follow-ups

Two related-but-distinct features that get confused:

- **Branching** routes participants to a *different section* based on their answer.
- **Conditional follow-ups** show an *inline text field* on the same section based on which choice they picked.

A choice can have one, the other, both, or neither. They serve different purposes — branching shapes the path through the study; conditional follow-ups gather the "why" right after a quantitative pick.

Conditional follow-ups are covered in `helio-section-types`.

## Good to Know

**Single-select is non-negotiable.** Multi-select branching genuinely doesn't exist — there's no roadmap path that adds it without redesigning how branches resolve. If you need to branch on a multi-attribute question, split it into multiple single-select questions and chain them with branches.

**Branches don't impose a maximum depth.** You can chain branches indefinitely (jump to section 4 → which branches to section 9 → which branches to end-of-test). The UI doesn't show a flowchart, so deep chains can become hard to reason about. Sketch the flow outside Helio first if it's complex.

**The branch UI is per-choice, not visual.** If you find yourself wishing for a flowchart, that's a real limitation today — branching is configured one choice at a time, and the "story" of how participants flow through the study lives in your head until you preview the test.

**Hotspot branching is real.** It's easy to miss because the Click Test setup UI focuses on the image and the hotspot regions. But each hotspot can route to a different next section, which is powerful for "did they click the right thing" → different follow-up paths.

**Branches don't fire during preview.** When you preview a test as yourself, you'll see every section regardless of branching. To test branch behavior end-to-end, you need to take the test as a real participant (or use the test's take link with multiple sessions).

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Setting up screening or disqualification (use the "End with custom message" pattern)
- Routing participants to different follow-up sections based on prior answers
- Wondering why their branch isn't firing during preview (it doesn't; you need a real take session)
- Trying to branch on a multi-select Multiple Choice (not supported; split into single-selects)
- Confused about branching vs Conditional Follow-ups (one routes sections, the other gathers inline input)
- Hitting a UX Metric undercount because participants branched past the metric-tagged section
- Surprised that disqualified participants still count toward quota

For inline conditional follow-ups (in-flow text fields on the same section), route to `helio-section-types`.

## Failure modes

- **Testing branches in preview mode.** Doesn't work. Use a real take session.
- **Trying to branch on multi-select.** Not supported. Split the question.
- **Deleting a section that other sections branched to.** The branches go orphan; participants fall through silently. Helio doesn't warn.
- **Tagging a UX Metric on a section that branching routes most participants past.** The metric undercounts and skews toward the non-branched group.
- **Underestimating quota cost of a heavy screener.** Disqualified participants still count. Budget accordingly.
- **Assuming the editor shows the flow visually.** It doesn't — branching is per-choice and lives in your head until preview. Sketch complex flows outside Helio.

## Where to go next

- For inline conditional follow-ups: `helio-section-types`
- For section type spec: `helio-section-types`
- For the build workflow: `helio-asset-to-test`
- For UX metric implications: `helio-ux-metrics`
- For quota counting: `helio-audience-flow`

<!-- /ADDED -->

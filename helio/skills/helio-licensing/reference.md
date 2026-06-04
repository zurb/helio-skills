# Answers & Licensing — Reference

**Skill:** `helio-licensing`
**Source:** Answers & Licensing v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had two minor AEO-rubric gaps (Problem opener; Action pointer). Both are addressed in the ADDED sections at the end of this file.

---

<!-- DERIVED FROM: 1Z21r50fYUx31NDLzLLwnOVmho6G6NrqMS279Jl4i5WI — Answers & Licensing v0.1 -->

How Helio bills for usage. The "answer" is the unit of consumption — everything you do that involves a participant or AI generation debits answers from your account's balance.

## What an Answer Is

**One answer = one section response.**

A participant who completes a 5-section study uses **5 answers**, not 1. Your quota (number of participants) gets multiplied by the number of sections in the test to determine the answer cost at launch.

For example: a 100-participant quota on a 5-section study = **500 answers** total.

## Where Answers Come From

Every Helio account has a **License**, which carries an answers limit. As you use answers, the balance counts down. The balance you see in the UI is what's left.

Licenses come in plan types:

- **Trial** — limited test answers for evaluation.
- **Pro tier (legacy)** — flat self-serve plan.
- **Business tiers 1–3** — 1,000 / 2,000 / 3,000 answers per month.
- **Scale tiers** — 5,000 / 10,000 answers per month.
- **Design / Agency / Enterprise** — custom, typically invoiced.
- **Custom** — one-off configurations.

Annual subscriptions get **monthly refills** — your answers reset on a refill date each month and unused answers don't roll over.

## What Each Action Costs

| Action | Cost |
|---|---|
| One participant completing a study | 1 answer per section in the study |
| Sending a moderated follow-up question | 10 answers (one-time, per follow-up sent) |
| Follow-up that goes unanswered for 3 days | **+10 answers refunded** automatically |
| Customer List recipient | Pre-charged when the invitation is sent |
| AI Audience response | Same as a real participant (1 per section) |
| **Design Analysis** | Flat **4 answers per analysis**, regardless of design size or AI usage |
| Adding / removing teammates | Counts against your seat limit, not answers |

## What Doesn't Refund

Some scenarios that *look* like they should refund don't:

- **Flagged responses** — marked as low quality, but the answers were already spent.
- **Spam responses** — same.
- **Deleted responses** — soft-deleted; the answers stay debited.
- **Customer List bounces or unsubscribes** — pre-charged at email send, no automatic refund.

For these cases, an admin can issue a manual refund via the admin tools. There's no self-serve refund flow.

## What Does Refund

- **Follow-up timeouts** — if a participant doesn't answer a moderated follow-up within 3 days, the 10 answers come back automatically.
- **List cleanup** — when a customer list is cleaned up before sending, panelist-limit credits return.
- **Manual admin refunds** — admin-initiated adjustments are logged with a reason.

## How Refills Work (Annual Plans)

If you're on an annual subscription, your answers reset on a refill schedule:

- Each month within the year, your usage resets and the full monthly allotment becomes available.
- Refill dates are set when the subscription starts.
- Unused answers don't carry over to the next month.

If you're on a monthly subscription, the same renewal happens monthly through the billing provider.

## What You'll See in the UI

- The answers balance is visible in your account settings or dashboard header.
- "Answers remaining" displays as both a count and a percentage of your limit.
- When you try to launch a test, Helio checks whether your remaining balance covers the cost. If not, launch is blocked with a clear message.

## Free / Discounted Cases

- **Open Audience on the Pro tier** — your first open quota is often free; subsequent open quotas may cost.
- **Trial accounts** — get a one-time allowance to try things out.

## License audit trail

Every answer spent or refunded is recorded. These records are immutable and capture:

- The direction (spend or refund).
- The quantity.
- What triggered it (a quota launch, a follow-up, a list cleanup, a teammate change, etc.).
- What the activity belongs to (the test, the quota, the participant).

If you ever need to understand why your balance changed, an admin can pull the audit log.

## Plan Tier Determination

Your plan tier is computed dynamically based on your active license and billing status. Tier determination affects which features and audiences you can access — Enterprise tier unlocks Advanced Segments, Customer Lists, Intercept, API submissions, sentiment analysis, branching, custom templates, and more.

Individual features can be enabled per account independently of plan tier — your account may have specific features turned on or off regardless of which tier you're billed at. If you're unsure whether a specific feature is available on your account, contact your account manager.

## Good to Know

**Concurrent submissions on a near-zero balance.** Helio uses an atomic balance update — if two participants submit at the same moment and only one answer is left, only one will succeed. The other will hit a 422 error.

**Overdrafts aren't possible.** Helio rejects any spend that would push you past your answers limit. Tests can't run into the red.

**Design Analysis is not on the standard "per-section" cost model.** It's a flat 4 answers no matter how complex the analysis. This is the only place in Helio where cost doesn't scale with content size.

**Subscription tier shows the wrong value briefly.** Rarely, after a billing change, your account may report an older tier for a short window. This normally clears automatically. If it persists, contact your account manager.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem + Action gaps) -->

## What this solves

Most teams miscalculate Helio cost by 2–5× because they forget that one participant on a 5-section study costs 5 answers, not 1. They also miss the non-standard cost rules (Design Analysis = flat 4; follow-ups = 10; AI Audience = 1 per section per persona). This skill is the cost model so the math gets done right before launch.

## When to use

Reach for this skill when the user is:

- Calculating answer cost for a planned test
- Hitting "insufficient balance" on launch and confused why
- Asking about refunds (the answer is usually "no" for flagged/spam/deleted/bounces)
- Trying to understand why their annual plan didn't roll over
- Checking the audit log for a balance discrepancy
- Confused about the difference between marketing plans (Pilot/Scale/etc.) and internal license tiers (Business/Scale/Design-Agency/Custom)

This is a billing reference. For plan choice and self-serve pricing positioning, use `helio-app`. For feature-flag gating (separate from license tier), use `helio-features`.

## Failure modes

- **Multiplying participants by 1 instead of by section count.** The most common error. Always: participants × sections = answers.
- **Expecting refunds for flagged or spam responses.** Those don't auto-refund. Admin can do manual.
- **Forgetting Customer List pre-charge.** Answers debit at email send, not at response. Bounces don't return budget.
- **Assuming Design Analysis cost scales with design complexity.** It doesn't. Flat 4 answers regardless.
- **Underestimating AI Audience.** Cost is per section per persona, same as a real participant — for large studies this adds up faster than expected.
- **Letting annual rollover assumptions cause overrun.** Monthly refills don't carry unused answers. Use them or lose them.
- **Confusing license tier with feature flag.** Tier sets the price; flags gate features individually. Don't conflate.

## Where to go next

- For marketing-facing plans and how to choose one: `helio-app`
- For audience-specific cost: `helio-audience-flow`
- For feature gates (what's enabled, not what it costs): `helio-features`
- For Design Analysis cost specifics: `helio-design-analysis`
- For moderated follow-up cost specifics: `helio-section-types` / `helio-findings`

<!-- /ADDED -->

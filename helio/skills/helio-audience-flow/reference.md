# Sending a Study (Audience Flow) — Reference

**Skill:** `helio-audience-flow`
**Source:** Audience Flow v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had one minor AEO-rubric gap (Problem opener). Addressed in the ADDED section at the end of this file.

---

<!-- DERIVED FROM: src-audience-flow-v0.1 — Audience Flow v0.1 -->

How to go from a finished test to participants completing it — the launch flow, audience configuration, and what to know about each recruiting path.

## The Launch Flow

When you're done building, you click **Send Test**. That opens the purchase modal, which is where you pick an audience and confirm.

1. The test must pass launch validation (see below).
2. You choose an audience type. Available options depend on your plan tier.
3. You configure that audience (demographics, segments, customer list, etc.).
4. You set the response count (quota).
5. You confirm payment (if applicable) and launch.
6. The test status flips from Draft to Running and Helio redirects you to the report.

## Launch Validation

Before a test can launch, Helio runs through a set of blockers. If any fail, the launch button is disabled and the editor highlights what's missing.

- The test must have a real name (not blank, not "Untitled").
- At least one question (except for AI tests).
- A valid audience type selected.
- If you picked Advanced Segments, at least one segment must be chosen.
- If you picked Customer Lists, at least one list or segment must be attached.
- Every section needs instructions and at least one variation.
- Sections that use assets (Prototype, Click Test, Preference) must have those assets uploaded.
- Sections that use choices (Multiple Choice, Rank, etc.) must have at least the minimum choices.

## Audience Options in Detail

### Open Audience

A shareable link. No targeting; anyone with the URL can take the test.

**Setup:** Nothing to configure — Helio generates a link you can copy and distribute.
**Cost:** Free on the Pro tier's first open quota. Subsequent opens may cost.
**Best for:** Testing with your own community, social channels, or any participants you already have access to.

### Helio Panel — Basic

Unfiltered access to Helio's panel.

**Setup:**

- Set the response count.
- That's it — no demographics, no targeting.

**Cost:** Tier 1 pricing.
**Best for:** Fast feedback from real people, when "anyone" is the right audience.

### Helio Panel — Targeted Demographics

Helio's panel, filtered by demographics.

**Setup:** Toggle "Targeted" in the audience picker, then pick from:

- Country / Continent
- Gender
- Age
- Income
- Education

When you choose demographics, Helio validates against the panel in real time — if your requested combination × your quota exceeds available panelists, the launch button stays disabled until you adjust.

**Cost:** Tier 2 pricing.
**Best for:** Audience-specific concept testing, persona validation, or any situation where general-population feedback isn't right.
**Plan tier:** Pro and up.

### Helio Panel — Advanced Segments

Helio's panel, filtered by pre-built segments (job title, industry, behaviors, etc.).

**Setup:** Search Helio's segment library. Each segment shows the available panelist count. Pick one or more.
**Cost:** Tier 3 pricing.
**Best for:** Reaching specific roles, industries, or behavioral cohorts that demographics alone can't isolate.
**Plan tier:** Enterprise.

### Customer Lists

Email a study to your own participants — customers, beta users, employees.

**Setup:**

- Upload a CSV with at least an **Email** column. **Full Name** is optional but recommended.
- Customize the invitation email: sender name, sender email, subject, preheader, message body (top and bottom), CTA text, and CTA URL.
- Each recipient gets a unique tracked URL.

**What's tracked per recipient:**

- Email opened, clicked, completed, bounced, or dropped (didn't deliver).
- Open rate, click rate, take rate at the list level.

**Re-invites:** "Order More Customer Lists" sends reminders to participants who haven't taken the study yet.

**Cost:** Standard answers cost. Pre-charged when emails go out; bounces / unsubscribes don't auto-refund.
**Plan tier:** Enterprise.

### Intercept

Triggered surveys for visitors on your own website.

**Setup:**

- Snippet installation and rule configuration (visitor #, device, traffic source, page path, time on page) happens outside the standard launch modal — typically in a separate intercept setup area.

**Cost:** Standard answers cost.
**Best for:** In-context research with your real users on your real product.
**Plan tier:** Enterprise. May require an additional feature enablement on your account.

### API Audience

Submit responses programmatically from your own systems.

**Setup:**

- Get API credentials from your account settings.
- POST responses to Helio's API in the documented format.
- Each submission counts as one response toward your quota.

**Best for:** Embedded research inside your own product where you're handling delivery yourself.
**Plan tier:** Enterprise.

### AI Audience

Generate synthetic participant responses from AI personas.

**Setup:**

- Define one or more personas during test creation. For each persona, fill in:
   - Consumer personas: demographics, activities, opinions, skills, ability.
   - Professional personas: job title, industry, ability, activities, responsibilities, skills.
- Set the response count.

**Cost:** 4 answers per section per persona response — runs higher than participant-driven responses on a per-completion basis.
**Best for:** Rapid early-stage validation of a concept before spending real-participant budget. Useful for "do these questions even make sense?" checks.
**Plan tier:** Enterprise. May require an additional feature enablement on your account.

## Working with audiences from the CLI

Creating a segment or screener is still web-app work. Everything around it is scriptable, and more of it than most people realize.

**Finding the right audience.** `audiences list` takes `--name <partial>` (case-insensitive) and `--recent` (most recently used in a test first), and returns `participants_count`, `tests_count` and `last_used_at` per audience — enough to tell a live segment from an abandoned one without opening the app. `audiences get <id>` confirms a single match.

**Reusing one.** `tests create --audiences <id> <id> ...` attaches existing segments at create time; passing several is how you run a fanout. `audiences clone <id>` copies an audience within its customer list when you want to vary one without disturbing the original. And `tests clone` carries the source test's last audience along with its questions and metrics — often the fastest way to reuse a configuration you didn't build.

**Verifying what's attached.** As of helio-cli v0.7.0 the audience configuration reads back: `tests preview --output json` returns an `.audience` block with the type, target size, attached segments, customer lists, demographic filters, screener, and retake/exclusion settings. Before that, the only proxy was inferring from the spend estimate.

That read-back matters most for **variant sets**. If V1 and V2 ran against different segments or different sizes, the comparison is noise — and nothing in the questions themselves would show it. Diff the `.audience` blocks across variants before launching a set. (`helio-test-review` does this as one of its cross-variant checks.)

## Combining Audiences

A study has **one active quota at a time** — you can't simultaneously launch the same test against Helio's Panel and a Customer List in a single quota.

**However**, after launch you can add additional quotas to the same test (Order More flow). Each quota's responses are tagged with their source, so you can filter the report by audience.

## Pricing Summary

For self-serve Pro pricing tiers, each Helio Panel option has a flat tier price:

| Tier | Audience | Indicative price |
|---|---|---|
| 0 | Open | $0 |
| 1 | Basic Helio Panel | Tier 1 |
| 2 | Targeted Demographics | Tier 2 |
| 3 | Advanced Segments | Tier 3 |

Enterprise pricing is custom and not shown in the UI flow.

All audiences debit from the same account-wide answers balance.

## After Launch

- The test status flips to Running.
- Responses arrive in real time on the report.
- Quotas are considered fulfilled when the response count is met. The test doesn't auto-stop, though — additional responses past the quota are still collected unless you stop the test.
- You can stop a test at any time from the report.

## Good to Know

**Quota counts vs. fulfillment.** "Quota filled" is based on unflagged responses. If responses get flagged as low quality, your effective response count drops below the quota and you may need to order more.

**Panelist availability for targeted audiences.** Helio validates demographic combinations against panel availability in real time. If you're requesting a very narrow slice, you may need to wait or adjust your targeting.

**Customer List pre-charge.** When you send a Customer List invite, the answers are debited when emails go out, not when recipients respond. Bounces and unsubscribes don't auto-refund — you'll need to ask an admin if you need a refund for delivery failures.

**Trial accounts** get their first open quota free; subsequent quotas require an upgrade.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem-opener gap) -->

## What this solves

Audience choice is the biggest cost-and-quality lever in a Helio test, and the one teams default on most often (everyone picks Open). Picking the wrong audience produces "interesting" data from the wrong people — high quota burn, low signal. This skill exists so the choice gets made deliberately.

## When to use

Reach for this skill when the user is:

- Launching a study and stuck choosing among the 8 audience types
- Hitting a launch-blocker validation error
- Considering a Customer List upload (especially around pre-charge / bounce behavior)
- Setting up Intercept and confused about the snippet workflow being outside the standard modal
- Trying to run an AI Audience and wondering about the per-completion cost
- Asking why their narrow targeting won't launch (panel availability check)
- Planning audience fanout — same test, multiple audience cohorts via Order More

For the broader 7-step build workflow, use `helio-asset-to-test`. For filtering the report after launch, use `helio-report-filtering`.

## Failure modes

- **Defaulting to Open Audience.** Free is enticing; uncontrolled audience is rarely the right signal. Pick a target.
- **Forgetting the panelist-availability check.** Narrow targeting can leave the launch button disabled silently.
- **Treating Customer List pre-charge as a refund-after-bounce model.** It isn't. Answers debit at send; bounces don't auto-refund.
- **Underestimating AI Audience cost.** 4 answers per section per persona is significantly more than a real participant on the same test.
- **Stacking audiences in one quota.** You can't. Run them as sequential Order More quotas.
- **Letting flagged responses drop your effective fulfillment below quota.** "Quota filled" counts unflagged only; budget for some loss.

## Audience configurations from real tests

Real audience setups drawn from the corpus catalogued in `helio-patterns`. Five recurring patterns:

### Single niche segment (precise target)

**The hunting-apparel store:** "Hunting Apparel Consumers" as the sole segment. Narrow, specific, expensive per-answer but the only audience that produces meaningful Success signal on a hunting-apparel flow.

### Adjacent audience (proxy target)

**A veteran careers landing page:** Banking, credit-card, credit-union users — *not* literal veterans. Deliberately adjacent. Picked because the panel can reach this segment efficiently and the read still tells you whether the page registers as a careers landing for the right kind of buyer.

### Multi-segment press fanout

**A press-room site:** 7 segments — journalists, bloggers, vloggers, social-media marketers (and variations). Same test, multiple audiences. Lets the team read how the same page lands for each press type and identify the segment least served.

### Audience-fanout testing as a method

**a campaign page run three ways:** Three audiences run side by side — Consumers / SMB Owners / Strangers. The compare-across-segments cut is the test's headline output, not the aggregate.

### Targeted demographics on the panel

**The banking-app prototype:** "Banking consumers, credit card / credit-card-points users, credit union members (US). 100 responses." Targeted demographics + behavioral attributes. Tier 2 pricing; matches the audience to the design's actual buyer type.

## Where to go next

- For the build workflow: `helio-asset-to-test`
- For section types: `helio-section-types`
- For report filtering after launch: `helio-report-filtering`

<!-- /ADDED -->

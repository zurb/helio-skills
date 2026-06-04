# The Participant Experience — Reference

**Skill:** `helio-participant-experience`
**Source:** Participant Experience v0.1
**Source last synced:** 2026-05-23
**Notes:** Source doc had two minor AEO-rubric gaps (Problem opener; Action pointer). Both are addressed in the ADDED sections at the end of this file.

---

<!-- DERIVED FROM: 1_fpHvnll4epixxGRl3SCWC5HJj3NoaPMPL-PUFUr07w — Participant Experience v0.1 -->

What people actually see and do when they take a Helio study. Useful for understanding the participant side of your research, supporting IRB / ethics review, and answering customer questions about how their users will experience an embedded study.

## How Participants Arrive

Every Helio study has a **take link** — a URL like `/t/{test_id}` that loads the participant-facing version of the study.

How a participant lands on that URL depends on the audience type:

| Audience type | How they get there |
|---|---|
| **Open audience** | The link is shared by the researcher (social, email, website embed). |
| **Helio panel** | Emailed to panelists Helio matched to the study. Link includes a panelist ID. |
| **Customer list** | Emailed via Helio with a personalized link tied to the recipient. |
| **Intercept** | Loaded inline on the researcher's own site via an embedded iframe. |
| **API** | No participant-facing flow — responses come in programmatically. |
| **AI audience** | No human participant — AI generates responses synthetically. |

The take link supports query parameters for:

- **Preview mode** — for the researcher to preview without consuming a quota slot.
- **Skip intro** — skip the welcome screen.
- **Jump to a specific section** (for testing branching paths).
- **Language override** — force a specific language for preview.
- **Autofill** — for testing flows quickly.

## What Participants See First

The first screen is typically a **welcome / intro card** with the study's introduction text. Researchers can customize this; the default is a brief description and a "Let's begin" button.

If the study has been configured to skip the intro (`?skipIntro=1`), participants land directly on the first section.

While the first section's assets (images, video) load, Helio shows a "please wait" placeholder. Subsequent sections preload their assets in the background to keep the experience smooth.

## Consent

Helio's standard flow **does not include an explicit consent modal**. The model is "accept by participation" — opening the link and clicking through is treated as implicit consent.

Some audience-specific consent does exist:

- **Helio panel participants** have a standing opt-in from when they joined the panel.
- **Customer list recipients** have implicit consent because you collected their email and added them.
- **Open audience** has no pre-stored consent — anyone with the link can take it.

Some flows do track explicit consent acceptance as a separate flag on the participant record, but it isn't a hard gate in the standard study flow.

**For IRB or regulated environments:** if you need participants to acknowledge specific consent language, the typical pattern is to put a Multiple Choice section at the start of the study with "I agree" / "I do not agree" and branch the "do not agree" path to an end-of-test with a custom message.

## Screening

Helio supports **screeners** — Multiple Choice, Likert, NPS, and Free Response questions that filter participants in or out before the main study begins.

Screeners are configured on the study and run before any regular sections. A participant who fails a screener is routed to a disqualification message and doesn't continue. They still count as having taken the study, but their responses are flagged accordingly.

Practical pattern: put a screener at the top to confirm participants match your target audience (e.g., "Have you used a fitness app in the last 30 days?"), then disqualify off the wrong answer.

## Demographic Collection

Helio collects demographics **after** the participant finishes the study, not before — so demographic data doesn't bias the experience.

Researchers configure which demographics to collect (any combination of):

- Gender
- Age
- Education
- Income

Plus, depending on audience type, Helio may also capture:

- Email and full name (Customer Lists usually pre-populate this).
- Country, state, city (often geolocated from IP for open audiences).
- ZIP code, company (when relevant).

Demographics are presented in a "Tell us about yourself" screen, with all fields optional by default. Participants can skip them.

These fields then populate the [report filtering](#) layer — use `helio-report-filtering` for details.

## Section Flow

By default, sections progress linearly. Participants move section-by-section with a "Next" button.

**Progress indicators:** Phase indicators (page-N-of-M dots) are present but unobtrusive.

**Progress saving:** Helio writes the participant's current section index to `localStorage` in their browser. If they close the tab and come back to the same link on the same browser, they pick up where they left off. There's no formal "save and resume" UI — it's just how the participant flow works.

**Back button:** Allowed in most cases. Going back lets the participant change a prior answer.

**Branching:** Configured by the researcher — participants don't see the branching logic, they just experience the relevant path. See `helio-branching`.

## Per-Section Interaction

What participants see varies by section type:

- **Multiple Choice / Likert / NPS** — radio or checkbox UI with the choices listed.
- **Rank** — drag-and-drop list (touch-friendly on mobile).
- **Point Allocation** — input fields next to each choice with live total validation.
- **Free Response** — text area with character limit (7,000 max).
- **Preference** — carousel of variations with arrow keys / swipe.
- **Click Test** — image with invisible hotspots; participants click anywhere.
- **Prototype Test** — Figma prototype embedded in an iframe.
- **Tree Test** — collapsible menu tree.
- **Card Sort** — drag cards into categories.
- **Matrix** — grid of rows × columns; one selection per row.

Required-answer validation runs on submit — empty text fields or unselected required choices block the "Next" button.

## Timers

Some sections support a timer. When enabled:

- A countdown displays for the participant.
- The countdown only shows when the section has a visual asset (image or video) — text-only sections don't show a timer.
- When the timer expires, the participant can submit; before it expires, the submission is held.

Use timers when you want to enforce a first-impression-only response (e.g., 5-second test on a homepage).

## Mobile vs. Desktop

Helio's participant experience is responsive — sections adapt their layout based on viewport size. Mobile-specific behaviors:

- **Touch-friendly drag** for Rank, Card Sort, and similar drag-based interactions.
- **Send-to-mobile** feature: if the participant lands on a device that's a poor fit for the study (e.g., desktop study opened on mobile), Helio can SMS a link to a more appropriate device.
- **Carrier-charge disclaimer** on the SMS prompt.

**Prototype Tests on mobile** may show the Figma prototype at desktop dimensions inside the iframe — make sure your prototype is designed at the dimensions you want participants to see.

## Accessibility

Helio's participant flow has baseline accessibility:

- Standard form controls (radio, checkbox, select, textarea) are keyboard-navigable.
- Translation keys feed into labels for screen readers.
- Image alts where assets carry alt text.

Limitations to be aware of for accessibility-sensitive research:

- Custom Angular controls (drag-and-drop ranking, card sorting) rely on mouse / touch interaction. Keyboard-only flow may not work for all section types.
- WCAG compliance isn't formally certified. Color contrast, focus indicators, and ARIA labels aren't comprehensively present.
- Video / audio assets don't enforce captions or transcripts — that's on the researcher to provide.

If your study needs to meet specific accessibility requirements, do a pass on each section type as a keyboard-only user before launching.

## Languages

Helio supports localized participant experiences. The participant gets the right language based on:

- The study's configured locale.
- Optional `?language=...` query param override (mostly for preview).
- Auto-detect from browser locale isn't the default — the study's locale wins.

What gets translated:

- UI chrome (Next button, labels, error messages).
- Demographic field labels.
- Default thank-you message.

What **doesn't** get auto-translated:

- Your section instructions.
- Your choice text.
- Your free-response prompts.

For multi-language studies, you'd need to either create separate studies per language or rely on participants who speak the language you wrote the questions in.

Right-to-left layouts aren't specifically supported today.

## Completion

After the last section (and any demographic collection), participants see a **thank-you screen**.

What's on it depends on the researcher's settings:

- **Custom thank-you message** — written by the researcher.
- **Custom logo** — pulled from the account's brand settings.
- **Default message** — if no custom message is set.

After ~2.5 seconds, Helio executes any configured **redirect**:

- **Custom redirect URL** — sends the participant to a page on your site.
- **Kiosk mode** — loops back to the test start (used for in-person research where the next participant should land directly on the study).
- **Helio panel members** — see a link back to their panel dashboard.
- **Open audience** — sees an upsell to join the panel (unless the account is enterprise).

There's no automatic email confirmation sent to the participant at completion — that happens upstream (e.g., the customer list send already confirmed their participation).

## Drop-Off and Abandonment

What happens when a participant doesn't finish:

- **Browser closed mid-test** — Helio shows a "you have unsaved progress" warning before they leave.
- **Progress in localStorage** — they can resume if they return to the same link on the same browser.
- **Partial responses retained** — whatever sections they completed are saved and count toward your quota (unless flagged as low quality).
- **No formal time limit** per study — participants can take as long as they need.

Per-section response time is captured, so you can analyze drop-off patterns on the report — see which sections people spent a long time on or abandoned at.

## Disqualification

A disqualified participant sees a thank-you screen with the custom disqualification message you wrote — typically something like "Thanks — based on your answers, this study isn't a fit." There's no distinct "you've been disqualified" framing unless you write it that way.

From a quota perspective, disqualified participants still count — they answered enough to register as a response. See `helio-branching` for the full picture.

## Identity and Deduplication

Helio's ability to prevent double-submission varies by audience:

- **Helio panel** — strict dedup. Each panelist gets one response per study.
- **Customer list** — one response per recipient (tied to their invitation token).
- **Open audience** — no enforcement. The same person could take the study multiple times on different browsers / devices.
- **API** — depends on whether you pass a `c_id` (custom identifier) to dedupe yourself.

For open audiences where dedup matters, you'd need to handle it on your side (post-survey).

Helio captures IP addresses and geolocates them for demographic enrichment, but doesn't use IP-based dedup.

## Branding

Researchers can customize the participant experience:

- **Account-level logo** — appears on the welcome and thank-you screens.
- **Brand colors** — applied dynamically to the test UI.
- **Custom thank-you message** — your words instead of Helio's default.
- **Custom redirect** — to your URL when done.

Custom take-link domains (white-labeling the `/t/...` URL itself) aren't part of the standard configuration — that requires per-account setup.

## Intercept Specifics

The Intercept audience type embeds the study as an iframe on your own website. The participant experiences:

- The study popping up in-context based on rules you set (visitor #, traffic source, page path, etc.).
- The iframe communicates with your parent page via `postMessage` so you can integrate with your own analytics or trigger events on completion.
- The participant can close the iframe at any time — their partial responses are still saved.

## API Audience and AI Audience

These two audiences don't have a participant experience in the conventional sense:

- **API audience** — your system POSTs responses to Helio's API. There's no participant going through a UI.
- **AI audience** — Helio generates synthetic responses from AI personas. There's no human in the loop at all.

Both produce responses that show up on the report alongside human responses.

## Edge Cases

**JavaScript disabled** — there's no server-rendered fallback. The participant flow requires JS. Modern browsers only.

**Slow connections** — Helio preloads images for the next section to smooth transitions, but Prototype Tests still need the Figma embed to load, which can be slow on poor networks.

**Figma prototype failing to load** — if the embed fails (private prototype, no participant access, Figma downtime), the participant sees a blank section. There's no graceful fallback today. Make sure your prototype is shareable before launching.

**Asset loading errors** — if an image or video can't load, Helio shows an "invalid asset" message and the participant can continue past the section. The response is captured but flagged.

**Helio downtime** — response saves show a retry UI. If multiple retries fail, the participant sees a final error message. Their partial data isn't lost — it can be re-sent if they return.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context; closes AEO scorecard Problem + Action gaps) -->

## What this solves

Researchers regularly answer "what will participants see" from memory or guess — leading to test designs that miss real participant constraints (consent timing, screener UX, drop-off behavior, accessibility limits, dedup rules). This skill is the canonical answer so design decisions account for them.

## When to use

Reach for this skill when the user is:

- Preparing for IRB or ethics review
- Answering customer or stakeholder questions about embedded study UX (intercept iframe, take link behavior)
- Designing a screener and unsure how disqualification UX works
- Auditing accessibility (the doc is honest about WCAG gaps)
- Investigating drop-off / abandonment patterns
- Setting up dedup expectations across audience types
- Configuring completion redirects, kiosk mode, or branded thank-you screens

For test design that accounts for these constraints, route to `helio-asset-to-test`. For audience-specific arrival behavior, use `helio-audience-flow`. For screener routing config, use `helio-branching`.

## Failure modes

- **Assuming Helio has an explicit consent modal.** It doesn't — accept-by-participation is the default. Use a screener pattern for explicit consent.
- **Designing a screener and forgetting disqualified participants still count toward quota.** Budget accordingly.
- **Expecting Helio to enforce dedup on Open audience.** It doesn't. Same person can take the test multiple times.
- **Assuming Prototype Tests scale correctly on mobile.** They may render at desktop dimensions inside the iframe.
- **Relying on Helio for accessibility certification.** WCAG isn't certified; custom controls aren't keyboard-friendly.
- **Translating section instructions automatically.** Helio doesn't — only UI chrome and demographics get translated. Researcher writes the question text.

## Where to go next

- For screener / disqualification config: `helio-branching`
- For section types participants encounter: `helio-section-types`
- For audience arrival paths: `helio-audience-flow`
- For test design implications: `helio-asset-to-test`
- For broader feature gating and plan tier: `helio-features`

<!-- /ADDED -->

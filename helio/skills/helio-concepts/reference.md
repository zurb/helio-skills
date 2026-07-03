# Concepts — Reference

**Skill:** `helio-concepts`
**Source:** Concepts v0.1
**Source last synced:** 2026-06-29
**Notes:** Source doc references internal class names (GenericTest, Insight, LicenseActivity, and so on) that don't belong in a public skill. Those references have been reframed into customer-facing language in the ADDED content below. The DERIVED block preserves the source structure with the same reframing applied inline.

---

<!-- DERIVED FROM: 1sMmcZZ3Cf8qmnfqCr1__-dusYc36qX91EgzDwZacKg8 — Concepts v0.1 -->

The data hierarchy that powers Helio — how accounts, projects, tests, sections, and responses relate. Useful as a mental model for researchers and as an orienting reference for engineers and integrators.

## The Hierarchy

At the highest level, Helio is organized around an account → project → test structure, with several cross-cutting systems hanging off each level.

```
Account (your workspace)
│
├─ License (answers balance, plan tier)
├─ Members (admin / member / viewer)
├─ Brand options (logo, colors)
├─ Figma authentications (team Figma tokens)
│
└─ Project (a folder of related tests)
   │
   └─ Test (a study)
      │
      ├─ Section (a question or task)
      │  │
      │  └─ Variation (an A/B variant of the section)
      │     │
      │     ├─ Choice (answer option, scale point, brand option…)
      │     │  └─ Branch (where to route if picked)
      │     │
      │     └─ Hotspot (Click Test only; clickable region)
      │        └─ Branch (where to route if clicked)
      │
      ├─ Quota (an audience configuration)
      │
      ├─ Finding (researcher-captured observation)
      │
      └─ Response (one participant's complete pass)
         │
         └─ Section Response (their answer to one section)
            ├─ Which choices they picked
            └─ Prototype path (Prototype Test only — views, clicks, gives-up)
```

A study can have many sections; each section can have one or more variations; each variation has the choices or hotspots that participants interact with.

When a participant takes the study, they create a Response containing one Section Response per section they saw — which in turn contains the specific choices they picked, the text they wrote, the clicks they made, or whatever the section type captures.

## What Lives Where

### Account

The top of the tree. An account holds:

- **Members** — users with admin / member / viewer roles.
- **License** — the answers balance and plan tier.
- **Brand options** — logo and color customization that applies to all studies in the account.
- **Figma authentications** — OAuth tokens from anyone on the account who has connected Figma. Used team-wide for prototype syncing.
- **Projects** — the folders that organize tests.
- **Account-level findings** — observations that span across studies.

### Project

A lightweight grouping mechanism. Projects own tests; they exist mostly to keep large accounts organized. A test belongs to exactly one project.

### Test (study)

The unit of research. A test is composed of:

- **Sections** in an ordered list.
- **A quota** (or sometimes multiple) describing the audience.
- **A status** in its lifecycle (see below).
- **Optional configuration** for branding, language, custom redirects, kiosk mode.

### Section

A single question or task. Sections have:

- **A type** (Multiple Choice, Likert, Click Test, etc.) — see `helio-section-types`.
- **Instructions** — the prompt shown to the participant.
- **At least one variation** holding the actual content.
- **Optional UX Metric tagging** — sections that contribute to a UX Metric score.

### Variation

The variant of a section. Most section types support only one variation; Preference, Click Test, and Prototype Test support multiple for A/B testing.

A variation holds:

- The asset (image, prototype URL).
- The choices (for choice-based sections).
- The hotspots (for Click Tests).
- Per-variation configuration (e.g., randomization of choices).

### Choice & Hotspot

The leaf-level interactive elements. A choice is an answer option (in Multiple Choice, Rank, Likert, etc.). A hotspot is a clickable region on a Click Test image.

Both can carry a **Branch** — a routing rule that determines what happens when a participant picks that choice or clicks that hotspot.

## Cross-Cutting Systems

Some Helio concepts don't live in the strict hierarchy — they attach across multiple levels.

### Assets

Assets (images, video, audio) are uploaded once per account and referenced by many variations across many tests. They live in your account's media library.

A Figma file is also an asset of sorts — it's tracked via a Figma reference plus per-screen node identifiers, separately from the regular asset system.

### Findings

Findings are captured observations. They can attach to:

- The test as a whole.
- A specific section.
- A specific variation.
- The account workspace.

Findings carry a snapshot of the report filters that were active when they were captured, so they remember the cohort they were about.

### UX Metrics

Each UX Metric is one-to-many with sections — a metric may require several sections to compute (e.g., Brand Score requires three). When you tag a section with a metric, Helio auto-builds the section structure that metric needs.

UX Metrics aren't stored as scores; they're computed on the fly from responses every time you view the report.

### Branches

Branches attach to both ends flexibly:

- **Source** (branchable): can be a Choice, a Hotspot, or a Variation.
- **Target**: typically a Section, sometimes a sentinel value (end-of-test, external redirect).

This means branching logic lives next to the *answer*, not the section — when participants pick A, they go to Section 5; when they pick B, they go to Section 7.

### Comments

Comments are a related but separate concept from Findings. They attach to sections or tests and support @-mentions, resolution status, and real-time updates.

## Test Lifecycle

A test moves through a small set of states:

```
Draft ──launch──→ Running ──fulfilled──→ Fulfilled
   │                 │                       │
   │                 ├──paused──→ Paused     │
   │                 │              │        │
   │                 │              ←─resume─┘
   │                 │
   │                 └──stop──────→ Stopped
   │
   └──delete──→ (soft-deleted)
```

- **Draft** — being edited. Not collecting responses. Pre-launch validation runs at launch time.
- **Running** — collecting responses against the active quota.
- **Paused** — temporarily not collecting. Can resume back to Running.
- **Fulfilled** — quota met. Doesn't auto-stop; additional responses keep coming unless you stop the test.
- **Stopped** — manually halted. Responses don't come in. Can't resume to a previous quota.

A test can be edited freely in Draft. Once Running, structural edits are constrained.

## Response Lifecycle

When a participant arrives at a take link:

1. A Response record is created (or resumed from browser storage).
2. As they progress through sections, Section Response records are created.
3. For most section types, the choices they picked are captured.
4. For Prototype Tests, every view, click, and quit event is captured as a path.
5. On completion, the Response is marked complete and demographics are captured.

A Response can be:

- **Hidden** — manually removed from the standard view.
- **Flagged** — marked as low quality.
- **Marked spam** — explicitly tagged.
- **Locked** — administratively frozen.

Each of these states affects whether the response counts toward the quota and shows up in the report by default.

## How the AI Workflow Differs

Design Analysis (AI heuristic eval) creates a parallel hierarchy that doesn't follow the same shape:

```
AI Test (the analysis)
│
├─ AI Section (one per master user need: Feel, Understand, Do, Trust)
│  │
│  ├─ Score and explanation
│  ├─ Per-metric AI scoring
│  └─ Image annotation bounding boxes
│
└─ AI Test Asset (the design being analyzed)
```

These are all generated by AI — no participant responses, no quota, no audience. The AI Test produces a report that looks similar to a participant study's report but uses its own metric storage. See `helio-design-analysis`.

## How Billing Connects

The Quota is the bridge between a test and the account's billing:

- When a test is launched, a Quota with a specific audience type is created.
- The Quota carries the cost (answers needed = quota size × section count).
- The account's balance is debited.
- Responses arrive against the Quota; when the unflagged response count meets the quota, the Quota is fulfilled.
- Follow-ups, refunds, and other adjustments create their own accounting entries.

## Identity & Authentication

Most actions in Helio are scoped to a single account context:

- A user can belong to multiple accounts.
- Each account membership carries a role (admin / member / viewer).
- All API calls happen in the context of a specific account.
- Public reports and shared findings can be accessed without authentication via UUID URLs.

Participants don't have user accounts in the standard sense — they're tracked by an internal participant ID, linked to their audience source (panel enrollment, customer list recipient, open-audience visitor, etc.). The Participant record carries IP, geo, and demographic data.

## The Mental Picture, in One Sentence

A **researcher** working on an **account** organizes **tests** into **projects**; each test is a sequence of **sections** (with **variations** and **choices**) that get **launched** against a **quota** (which determines the **audience**); **participants** create **responses** that flow into **reports** filtered by **demographics** and **answers**, with **findings** capturing observations and **UX Metrics** scoring how the experience went.

<!-- /DERIVED -->

---

<!-- ADDED 2026-06-29 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Building a mental model of how Helio's data fits together
- Confused about "why can't I move X across tests" or "why does variation belong to section"
- Debugging a "test won't let me edit this" issue (probably in Running state, needs Draft)
- Asking about the test lifecycle (Draft → Running → Fulfilled)
- Wondering how the AI Design Analysis workflow relates to the regular test workflow
- Planning an API integration and needs to know the shape
- Explaining Helio to a new team member

For any specific depth — section type spec, audience config, UX metrics, findings, branching, assets, AI evaluation — route to the sibling skill. This skill is the orientation layer; the others are the detail.

## Failure modes

- **Trying to structurally edit a Running test.** Most edits require Draft. Stop the test (loses the quota progress) or start a new test.
- **Expecting variations to move across tests.** They don't. A variation belongs to a section, which belongs to a test.
- **Assuming the AI Design Analysis workflow shares participant responses.** It doesn't. It's a parallel hierarchy with its own storage.
- **Reading response counts without filtering out Hidden/Flagged/Spam.** By default these are excluded from the standard view but included in raw counts. Know which count you're looking at.
- **Confusing Findings with Comments.** Findings are observations to share; comments are discussion threads.
- **Assuming quotas can be shared across tests.** They can't. A quota belongs to one test.

## Where to go next

- For section type detail: `helio-section-types`
- For UX metric detail: `helio-ux-metrics`
- For audience / quota detail: `helio-audience-flow`
- For branching detail: `helio-branching`
- For findings detail: `helio-findings`
- For asset handling: `helio-assets`
- For the AI Design Analysis workflow: `helio-design-analysis`
- For Forms & Screeners on Customer List signup: `helio-forms-screeners`
- For the full test-build workflow: `helio-asset-to-test`

<!-- /ADDED -->

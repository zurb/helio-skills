# Helio Marketplace — Changelog

## v0.11.1 — 2026-07-21 — Patch: asset-to-test DERIVED body caught up; Notes framing cleaned

A post-release retrieval test over the five updated skills found the v0.11.0 edits to `helio-asset-to-test` had only touched the ADDED sections — the DERIVED "asset gap" passage still said "The CLI cannot upload screen images." Fixed, along with the Dual-Offer example (image upload now shown via `assets upload`) and a doc bug (`--metrics` → `--ux-metrics`, twice). helio-cli / helio-assets reference Notes reframed from "Amended" to native v1.4 / v0.2 content. helio-asset-to-test 0.1.1 → 0.1.2. Known source-doc question deferred to the next From Asset To Test revision: the Dual-Offer `questions.json` includes a `click_test` entry even though click_test is not API-creatable.

### Plugin metadata

- `marketplace.json` / `plugin.json` version: 0.11.0 → 0.11.1.

## v0.11.0 — 2026-07-21 — Drive docs refreshed; asset-upload staleness cleared across the family

Closes both "Notes" items from v0.10.0. Two new Drive docs landed (composed via the Drive connector): **Assets v0.2** and **Helio CLI v1.4**, both carrying the helio-cli v0.1.1 assets command group. Four more Drive docs were uploaded in the same session for future skills: Figma Syncing v0.1, Glossary v0.1, Test Templates v0.1, From Finding to Test v0.1. Drive-side follow-up: Assets v0.1 and Helio CLI v1.3 should move to Archive (connector can't move files).

### helio-cli 0.3.0 → 0.3.1 · helio-assets 0.2.0 → 0.2.1 (repoints)

- doc_id / drive_url / source_doc_version repointed to Helio CLI v1.4 and Assets v0.2. Both skills are single-source again; the "codebase second source" from v0.10.0 is retired.

### helio-creating-test 0.1.2 → 0.1.3

- Canonical UI-only boundary checklist: the "Asset upload & finding asset IDs" row is now "Video/audio asset upload" — image upload/list/attach is CLI-native; MCP has no asset tools.

### helio-asset-to-test 0.1.0 → 0.1.1

- Step 7 loses the web-app upload detour for image-based tests; "what the workflow doesn't cover" and failure modes rewritten (hotspots, branching, video/audio remain UI-only).

### helio-mcp 0.2.1 → 0.2.2

- Ceilings restated per surface: MCP itself still has no asset tools (verified against the server code — no asset-named tools registered); route image uploads to helio-cli or the web app.

### Plugin metadata

- `marketplace.json` / `plugin.json` version: 0.10.0 → 0.11.0.

## v0.10.0 — 2026-07-21 — CLI assets command group: asset upload leaves the UI-only list

helio-cli v0.1.1 (zurb/helio-cli PR #6) shipped an `assets` command group — `assets list` (`--type`/`--name`/`--limit`/`--offset`), `assets get <id>`, `assets upload <file>` (images only: jpg/jpeg/png/gif, max 10MB, multipart; returns a numeric id with `status: "processing"`, poll `assets get` until `complete`). Uploaded ids attach via `tests add-question --asset-id` / `tests edit-question --asset-id` or `asset_id` in question payloads (free_response). This release syncs the two affected skills, which were updated in the deployed copies on 2026-07-20 and back-ported here.

### helio-cli 0.2.0 → 0.3.0 (second source: CLI codebase)

- Core idea gains the assets surface; "Known ceilings (UI-only)" drops asset upload, narrows to video/audio upload.
- reference.md: `Assets` row in the command surface; new "Assets — upload, list, get" section (validation, polling, numeric ids, attachment paths, list filters); "What the CLI can't do" and failure-modes updated; `asset_id` pointer rewritten (was "get asset IDs from the web app").
- Description gains "assets upload," "assets list," "--asset-id" triggers.
- Verified by subagent retrieval test (6 probes, all correct from the files alone).

### helio-assets 0.1.0 → 0.2.0

- Uploading is now two paths (web app all types; CLI images only), with the polling caveat reconciled against the original "ready as soon as upload finishes" claim.
- Handoffs updated: `helio-cli` added; "asset upload is a UI-only step" phrasing removed.
- Description gains "upload from terminal," "assets upload CLI," "asset id" triggers.

### Notes

- **Drive docs not yet updated.** Both skills now cite a second source (`helio-cli v0.1.1 codebase`) beyond their Drive docs; "Assets v0.1" and "Helio CLI v1.3" on Drive still carry the pre-CLI upload story. A Drive-side refresh (Assets → v0.2, Helio CLI → v1.4) would restore single-source derivation.
- Known remaining staleness elsewhere: `helio-asset-to-test`, `helio-creating-test` (canonical UI-only checklist), and `helio-mcp` still list asset upload as UI-only — queued as a separate task.

### Plugin metadata

- `marketplace.json` / `plugin.json` version: 0.9.0 → 0.10.0.

## v0.9.0 — 2026-07-06 — Test Pattern Playbook merged into helio-patterns (the "when" layer)

A second Claude session analyzed **285 real tests over five months** (Feb–Jul 2026) and produced the Test Pattern Playbook: seven shared templates mapped to the project stage where each earns its place. This release lands it in the doc family and the marketplace.

### New Drive doc

- **Test Pattern Playbook v0.1** — created directly in the Drive folder, scrubbed during the build: customer names → category descriptors (same v0.3.2 pattern), internal `owner_id`s removed, researcher attribution recast as two operating styles (iteration-deep vs first-look volume), account-handoff telemetry generalized.

### helio-patterns 0.2.0 → 0.3.0 (now a merged two-source skill)

- Second DERIVED block: the stage axis (first look / iterate / benchmark) with real use counts; the asset-first template picker (one screen → T2/T3/T5/T6, flow → T1/T7, either → T4); all seven template question tables (type, metric, prompt, required follow-up); the empirical metric-coverage table (20 metrics, 6 carry ~⅔, `expectations` most-deployed at 208 uses); house follow-up rules; method & caveats (61% template fit, ~39% custom).
- ADDED updates: which-block-to-read routing, playbook failure modes (templates aren't cages; click-heavy templates hit the UI-only boundary when automated).
- Description gains stage/template triggers ("what test should I run at this stage," "findability sweep," T1–T7 names).

### helio-creating-test 0.1.1 → 0.1.2

- ADDED cross-reference table: the four conceptual shapes mapped to T1–T7 (A→T5, C→T2, B→T7; concept comparison has no corpus template), plus the four templates the shapes don't cover.

### Notes

- The playbook resolves several of Test Patterns v0.2's "what's NOT in this sample" caveats with 19× the sample.
- Internal-track follow-up (not in this release): T1–T7 as validated `questions.json` payloads in helio-cli for automation.

### Plugin metadata

- `marketplace.json` / `plugin.json` version: 0.8.1 → 0.9.0.

### Verification

All 17 skills pass the validator.

## v0.8.1 — 2026-07-06 — helio-mcp doc_id repoint (Drive v1.3 landed as a new document)

Patch. The Drive-side paste of Helio MCP v1.3 created a **new document** rather than editing v1.2 in place; the v1.2 doc (a source document) was moved to Archive. `helio-mcp` 0.2.0 → 0.2.1: doc_id, drive_url, and DERIVED marker repointed to the new document. Content unchanged. (Helio CLI v1.3 *was* updated in place — a source document verified, no change needed.) Drive-side confirmations: both v1.3 docs live; five Archive candidates from v0.5.0 moved/pending per the docs owner's worklist.

## v0.8.0 — 2026-07-06 — helio-mcp rebuilt against Helio MCP v1.3 + canonical UI-only boundary checklist

Items 3 and 5 of the test-creation improvement plan.

### helio-mcp 0.1.0 → 0.2.0 (Item 3)

Rebuilt against **Helio MCP v1.3**, regenerated from the MCP server codebase. Corrects the v1.2 **"26 tools" claim to the real registered surface: 20 tools + 2 prompts (`analyze_test`, `compare_audiences`) + 1 resource** (`helio://guide/analysis-workflow`). New content:

- Full grouped tool catalog: Discovery (5), Building a draft (5), Launching (3), Reading results (4), AI assessments (3) — with parameter notes per tool.
- `create_test` details: same 10 question types / 11 UX metrics as the CLI, plus `ux_metric_context` and `ux_metric_assets` (the latter has no CLI equivalent).
- The assistant-driven build loop (`create_test` → `add/update/remove_question` / `update_test` → `validate_test` → `send_test`) and the metric-section edit rules (`update_question` without `type`; `update_test` for metric add/remove; `remove_question` refuses metric sections).
- `get_test_report` `include` options and demographic filtering; `get_filtered_responses`; `compare_segments`.
- Capability limits: same UI-only ceilings as the CLI, plus MCP-specific gaps — no dry-run (use `validate_test`) and no walkthrough (use the preview URL).
- Drive-side: v1.3 content drafted from the codebase and handed off for paste into the existing Drive doc (a source document — doc_id unchanged, title → "Helio MCP v1.3").

### Canonical UI-only boundary checklist (Item 5)

- **`helio-creating-test` 0.1.0 → 0.1.1** — reference.md ADDED block gains the one authoritative table of web-app-only steps: asset upload/finding IDs, hotspot drawing, click/tree/prototype sections, branching & conditional follow-ups, audience/screener creation, the 7 prototype-dependent UX metrics, scheduled launch — each with why, workaround, and rough effort. Ends with the working pattern: script the buildable part, finish in the web app, validate/send anywhere.
- Pointers added so the story is told once: `helio-assets` (handoff), `helio-branching` (handoff), `helio-asset-to-test` (How-to-apply step 7). `helio-cli` and `helio-mcp` carry their own DERIVED "what X can't do" sections, consistent with the checklist.

### Plugin metadata

- `marketplace.json` / `plugin.json` version: 0.7.0 → 0.8.0 (descriptions unchanged; skill count unchanged).

### Verification

All 17 skills pass the validator.

## v0.7.0 — 2026-07-06 — helio-cli rebuilt against Helio CLI v1.3 (full command surface + payload schemas)

Items 2 and 4 of the test-creation improvement plan. The v1.2 Drive doc documented 4 of ~20 test commands; v1.3 was regenerated from the CLI codebase (README, built-in guide, `QUESTION_TYPES` / `UX_METRIC_TYPES` validation schemas) and the skill rebuilt against it.

### Changes

- **`helio-cli` 0.1.0 → 0.2.0** — DERIVED block rebuilt from Helio CLI v1.3. New content:
  - The **draft → iterate → launch loop**: `create --dry-run` → `create` → `add-question` / `edit-question` / `remove-question` / `order` / `reorder` / `add-ux-metrics` / `remove-ux-metrics` → `preview` / `walkthrough` (`--interactive`, `--output json`) → `validate` → `send`.
  - The **full command catalog** (setup/diagnostics, browsing, building, schema lookups, reviewing, launching, reading; aliases).
  - **`tests create` flag table** (`--project-name` resolution, `--ux-metric-context`, `--dry-run`, questions via `@file`).
  - **Question payload schemas** (Item 4): JSON example + required/optional fields for all 10 creatable types; the 11 Likert scale types; snake_case/PascalCase acceptance; non-creatable types (`click_test`, `tree_test`, `prototype_task`) flagged UI-only with report-read notes.
  - **UX metric build table**: what each of the 11 creatable metrics auto-builds; the 7 non-creatable metrics named.
  - **"What the CLI can't do"**: no asset upload/listing, no click/tree/prototype creation, no branching, no audience creation, no scheduled launch — with the finish-in-the-web-app pattern.
  - ADDED block: new worked example (iterate on a draft before spending), updated failure modes (don't recreate to edit; walkthrough before send).
- **Drive-side:** the v1.3 content was drafted from the codebase and handed off for paste into the existing Drive doc (a source document — doc_id unchanged, title → "Helio CLI v1.3"). `source_doc_version` and `last_synced` updated accordingly.

### Plugin metadata

- `marketplace.json` / `plugin.json` version: 0.6.0 → 0.7.0 (descriptions unchanged; skill count unchanged).

### Verification

All 17 skills pass the validator.

## v0.6.0 — 2026-07-06 — New design-first hub skill: helio-creating-test (16 → 17)

Additive release. Item 1 of the test-creation improvement plan: the richest test-creation doc in the Drive family — *Creating a Helio Test v0.1* — was the only one not backed by a skill. It now is.

### What's new

- **`helio-creating-test`** (source: Creating a Helio Test v0.1, *Creating a Helio Test v0.1*) — the design-first hub for test creation:
  - The **Hunch → Shape → Test → Signal** arc, with the "we believe…" hunch template and a worked example.
  - The **four house shapes** (marketing page eval, multi-screen flow eval, content prioritization with MaxDiff, concept comparison) plus a shape-picking decision rule.
  - The **metric table** (Helio metric → Glare type), audience shaping and sizing, question types/modes, the four-point **bias check**, and the **required-followup pattern**.
  - **Validate before you spend**: CLI dry-run, web preview, pre-launch checklist (≤ 8 questions).
  - **Templates A/B/C** — ready-to-edit question sets lifted from real Zurb tests.
  - The **surface decision rule**: person → web app, script → CLI, assistant → MCP.
  - Anti-patterns (no hunch, averaged MaxDiff, ignored followups, multi-hunch tests, expiring asset URLs).
  - Customer names in the source (four client engagements) were scrubbed to category descriptors during the build, using the v0.3.2 pattern and matching the descriptors already used in `helio-patterns`.

### Routing

Two hubs, disambiguated by entry point: start from a **hunch** → `helio-creating-test`; start from an **asset/mockup** → `helio-asset-to-test`. Each hands off to the other.

### Handoff updates in existing skills

Added handoffs to `helio-creating-test` from: `helio-patterns`, `helio-asset-to-test`, `helio-section-types`, `helio-concepts`, `helio-cli`, `helio-mcp`.

### Plugin metadata

- `marketplace.json` version: 0.5.0 → 0.6.0; description updated to 17 skills.
- `plugin.json` version: 0.5.0 → 0.6.0; description updated to 17 skills.

### Verification

All 17 skills pass the validator (description length, frontmatter, marker balance, doc-ID matching).

## v0.5.0 — 2026-07-06 — Source-pointer hygiene (patterns v0.2 rebuild, helio-app repoint, reading-report repoint)

Hygiene release. No new skills; every `sources:` pointer now names a doc that exists in the Drive folder with the title claimed. First release of the test-creation improvement plan (Item 6).

### Changes

- **`helio-patterns` 0.1.0 → 0.2.0** — rebuilt against **Helio Test Patterns v0.2 (scrubbed)**, replacing the v0.1 source (a source document). The v0.2 Drive doc is the anonymized revision — customer engagement names became category descriptors, matching the local scrub shipped in v0.3.2. DERIVED block updates: "O2" project prefix dropped in favor of "the 145/the evolving-flow series," cleaner example phrasings in sections 1/5/8, MaxDiff note reworded, tooling notes gain the Node 22 / nvm PATH caveat. No pattern content changed.
- **`helio-app` 0.1.0 → 0.1.1** — fixed doc_id/title mismatch: frontmatter claimed "Helio App v1.3" but pointed at the v1.2 doc (a source document). The skill's DERIVED content matches the v1.3 doc word-for-word, so the pointer was repointed to the real v1.3 doc. No content changes.
- **`helio-reading-report` 0.1.0 → 0.1.1** — resolved the "Drive has v0.1; skill uses v0.2 content from local" workaround: both v0.2 docs now exist in Drive (*Reading a Helio Report v0.2* *Reading a Helio Report v0.2*, *From Helio Test to Glare Signal v0.2* *From Helio Test to Glare Signal v0.2*). Doc_ids repointed, parentheticals dropped from titles, content verified matching. No content changes.

### Drive-side follow-ups (for the Drive Scrub Worklist)

Superseded / orphaned docs still in the main Drive folder, candidates for Archive: *Helio Test Patterns v0.1* (a source document), *Helio App v1.2* (a source document), and the pruned-skill docs *Participant Experience v0.1*, *Answers & Licensing v0.1*, *Helio Features v0.2*. The old local-workaround doc_ids (a source document, a source document) are no longer referenced by any skill.

### Plugin metadata

- `marketplace.json` version: 0.4.0 → 0.5.0
- `plugin.json` version: 0.4.0 → 0.5.0
- Descriptions unchanged (skill count unchanged).

## v0.4.0 — 2026-06-29 — Two new skills (14 → 16)

Additive release. Two new skills added, sourced from Drive docs that weren't yet covered — one for Customer List signup Forms (which contain a distinct "screener" concept easy to confuse with in-study screening), and one for the account → project → test data model.

### What's new

- **`helio-forms-screeners`** (source: Forms & Screeners v0.1) — Two-part coverage:
  - **Formal Screeners**: up to 5 qualification questions attached to a Customer List signup Form (Multiple Choice, Likert, NPS, Free Response). Answers stored on the participant record; disqualification is a downstream targeting decision at study launch, not an auto-reject.
  - **Inline Screening**: the pattern of a Multiple Choice section at the top of a study with a branch to end-of-test — the same "screener" word for a different feature.
  - Also covers when to use each, the 5-per-Form hard limit, and disable-vs-delete rules.

- **`helio-concepts`** (source: Concepts v0.1) — Customer-facing mental model of Helio's data model:
  - The main tree: Account → Project → Test → Section → Variation → Choice/Hotspot → Branch.
  - Cross-cutting systems: Assets, Findings, UX Metrics, Branches, Comments.
  - Test lifecycle (Draft → Running → Fulfilled / Paused / Stopped).
  - Response lifecycle (arrival → per-section capture → complete, plus Hidden / Flagged / Spam states).
  - How the AI Design Analysis workflow runs a parallel hierarchy.
  - How Quotas bridge test and account billing.
  - Internal codebase names in the source doc (class / model names) were reframed into customer-facing language during the skill build.

### Handoff updates in existing skills

- `helio-asset-to-test`: added handoffs to `helio-forms-screeners` (screening at step 5) and `helio-concepts` (data model).
- `helio-audience-flow`: added handoffs to `helio-forms-screeners` (how Customer List members are captured) and `helio-concepts`.
- `helio-branching`: added handoffs to `helio-forms-screeners` (the inline-screening pattern) and `helio-concepts`.

### Plugin metadata

- `marketplace.json` version: 0.3.2 → 0.4.0
- `plugin.json` version: 0.3.2 → 0.4.0
- Descriptions updated to reflect 16 skills and name the two new areas (Concepts, Forms & Screeners).

### Verification

All 16 skills re-pass the validator:

- Description length ≤ 1024 chars
- YAML frontmatter valid
- DERIVED / /DERIVED marker balance
- ADDED / /ADDED marker balance
- Source manifest doc_ids match DERIVED FROM markers

## v0.3.2 — Customer-name scrub

All references to real customer engagements replaced with category descriptors. Public marketplace shouldn't be naming real customer engagements without explicit case-study permission.

### What changed

Seven customer-engagement names were replaced with anonymized category descriptors across 10 files (every skill that had a customer name). The mapping is held privately and is not documented in this public changelog.

Zurb-internal project names (Dual-Offer, a retail PDP series, a campaign page, a continuous-experimentation project, an internal product project, the homepage-baseline project) were left intact — they're Zurb's own work, not customer engagements.

### History

The customer names existed in `helio-patterns` from v0.1.0 (inherited from the source PATTERNS.md doc) and were spread across 6 more skills in v0.3.1. This patch removes them from the working tree. Because the names had already been pushed to the public repo in prior commits, this release is paired with a git history rewrite (squash to a single clean commit + force-push) to scrub history too.

### Plugin metadata

- `marketplace.json` version: 0.3.1 → 0.3.2
- `plugin.json` version: 0.3.1 → 0.3.2

### Verification

All 14 skills re-pass the validator after scrub + cleanup pass.

## v0.3.1 — 2026-05-23 — Worked examples for test creation + synthesis

Content enrichment. Added "Worked examples from real tests" sections to the eight core skills that drive test creation and report synthesis, grounded in the test corpus catalogued in `helio-patterns` (the athletic-apparel homepage, the veteran careers landing page, the B2B data-platform homepage, the hunting-apparel store, a retail PDP variant, the banking-app prototype, the press-room site, the investment-platform).

### What got worked examples

**Test creation:**

- `helio-asset-to-test` — Four shape templates beyond Dual-Offer: the athletic-apparel homepage (Core 5-Q), the veteran careers landing page (with MaxDiff), the hunting-apparel store (multi-screen), the press-room site (satisfaction-as-intent-disclosure)
- `helio-section-types` — Real configurations for Multiple Choice (the athletic-apparel homepage + the B2B data-platform homepage descriptors), Click Test (the hunting-apparel store success), MaxDiff (the veteran careers landing page content), Likert Likelihood (the athletic-apparel homepage), Prototype Test (the banking-app prototype Direct/Indirect/Failed)
- `helio-ux-metrics` — Real score patterns per metric: the hunting-apparel store 12% Success, a retail PDP variant 92/87/38, the athletic-apparel homepage 87 Desirability + 14 NPS, the B2B data-platform homepage 80 Comprehension with jargon tail
- `helio-audience-flow` — Five real audience configurations: the hunting-apparel store niche, the veteran careers landing page adjacent, the press-room site 7-segment fanout, R5 audience-fanout method, the banking-app prototype targeted demographics
- `helio-patterns` — Already had rich real examples throughout; unchanged

**Synthesis:**

- `helio-reading-report` — Four worked synthesis patterns with full one-sentence signals: a retail PDP variant divergence, the hunting-apparel store 12% red flag, the athletic-apparel homepage 87/14 gap, the B2B data-platform homepage stated-vs-behavioral
- `helio-report-filtering` — the press-room site 7-segment filtering workflow + MCP `compare_segments` fallback
- `helio-findings` — Three example finding texts (the athletic-apparel homepage test-level, the hunting-apparel store section-level, the B2B data-platform homepage cross-question)

### Format

All worked examples are in the ADDED sections (not DERIVED), drawn from the test corpus in `helio-patterns`. This keeps the DERIVED content faithful to its source docs while letting the skill content reference verified real test data.

### Verification

All 14 skills re-pass the validator:

- Description length ≤ 1024 chars
- YAML frontmatter valid
- DERIVED / /DERIVED marker balance
- ADDED / /ADDED marker balance
- Source manifest doc_ids match DERIVED FROM markers

### Plugin metadata

- `marketplace.json` version: 0.3.0 → 0.3.1
- `plugin.json` version: 0.3.0 → 0.3.1

## v0.3.0 — 2026-05-23 — Prune non-core skills (17 → 14)

Breaking-shape change. Removed three skills that didn't pertain to creating tests, reading reports, or test structures — they were adding noise rather than helping users get work done.

### What was cut

- **`helio-features`** — feature catalog by plan tier. Sales / admin context, not test-design content. Users who need plan/feature info can use `helio-app` or the website.
- **`helio-licensing`** — billing model, answer math, refund rules. Admin / finance context, not test-related.
- **`helio-participant-experience`** — what participants see, consent timing, IRB / regulated-research context. Tangential to test design.

### What stays (14 skills)

All test-design, test-structure, and report-reading skills:

- Orientation: `helio-app`, `helio-cli`, `helio-mcp`
- Test design: `helio-patterns`, `helio-asset-to-test`, `helio-section-types`, `helio-audience-flow`, `helio-branching`
- Test mechanics: `helio-assets`
- Measurement & synthesis: `helio-ux-metrics`, `helio-report-filtering`, `helio-design-analysis`, `helio-findings`, `helio-reading-report`

### Routing cleanup

All 30+ references to the cut skills were stripped from the surviving 14 skills. Inline mentions (e.g., "For how the answers balance works, see helio-licensing") were either reframed as facts or removed where redundant. Description Do-NOT clauses that listed cut skills were trimmed.

### Plugin metadata

- `marketplace.json` version: 0.2.1 → 0.3.0
- `plugin.json` version: 0.2.1 → 0.3.0

### Verification

All 14 surviving skills re-pass the validator:

- Description length ≤ 1024 chars
- YAML frontmatter valid
- DERIVED / /DERIVED marker balance
- ADDED / /ADDED marker balance
- Source manifest doc_ids match DERIVED FROM markers (bidirectional)

### Worth flagging

If users miss the cut content, the right move is usually to point them at the website rather than re-adding skills. The Helio docs site covers plans/pricing/features for customers; the AEO scorecard for the 3 cut skills is still preserved in `Helio Doc Family — AEO Scorecard v2.docx` for reference.

## v0.2.1 — 2026-05-23 — Internal-info cleanup

Patch release to remove internal technical references from skills that shouldn't be in a public marketplace. No functional changes; the user-facing content is unchanged in substance.

### What got cleaned

**Codebase artifacts removed:**

- File paths (e.g., `app/models/ux_metric.rb`, `app/javascript/dashboard/utils/...`)
- Internal class / module references (e.g., `UxMetric::Result#result`, `GenericTest#ux_metric_score`, `SectionCreator`, `UxMetricUtil.validateSections`, `LicenseActivity`, `CommentInsight`, `EnrollSegment`)
- Internal constants (`BEHAVIORAL_METRIC_TYPES`, `ATTITUDINAL_METRIC_TYPES`)
- Database column names (`answers_limit`, `answers_used`, `seats_limit`, `is_free_open_pro_quota`, `accepted_opt_in`, `has_intercept`, `enroll_segment_ids`, `lock_version`, `is_template`)
- Internal feature flag names (`enterprise_group`, `intercept_group`, `gpt_autosuggest_group`, `ux_metrics_group`, `beta_group`, `internal_group`, `research_repository_group`, `goals_group`)
- Migration numbers
- Internal API paths

**Vendor / tooling names generalized:**

- Honeybadger → "logged internally"
- PromptLayer → "external prompt-management system"
- Algolia → "indexed search"
- AWS Comprehend → unstated
- AWS MediaConvert → "transcoding service"
- AWS S3 / CloudFront → "cloud storage" / "signed-URL CDN"
- Uppy → "drag-drop / file picker uploader"
- GPT-4o → "AI model"
- Stripe → "billing provider"
- `glare-ux-metrics-rb` gem → "the scoring library"
- `cloudfront.key` dev-environment artifact → removed

### Affected skills (11 of 17 had cleanup)

- `helio-assets` (substantial — CloudFront/S3/MediaConvert/Uppy generalized)
- `helio-audience-flow` (feature flag references)
- `helio-design-analysis` (Honeybadger, PromptLayer, GPT-4o, internal API path)
- `helio-features` (major rewrite — file paths, class names, constants, flag names removed; reframed as customer-facing feature catalog with plan-tier gating)
- `helio-findings` (Algolia, Insight/CommentInsight model names)
- `helio-licensing` (column names, feature flag list, LicenseActivity model name, Stripe references)
- `helio-participant-experience` (accepted_opt_in column)
- `helio-patterns` (is_template, enable_branching code-style references)
- `helio-report-filtering` (engineering note about EnrollSegment, AWS Comprehend, handoff)
- `helio-section-types` (GPT-4o reference in Design Analysis subsection)
- `helio-ux-metrics` (gem name, feature flag name)

### What's still intact (vendor disclosure kept)

- Figma OAuth — customer-facing integration; needs to stay
- Account-level tier names (Pro, Enterprise, Beta, Admin) — customer vocabulary
- General architectural facts (the platform uses adaptive streaming, transcoding, etc.) — fact-of-the-feature, not vendor-specific

### Verification

All 17 skills re-pass:

- Description length ≤ 1024 chars (range 594–940 chars)
- YAML frontmatter valid
- DERIVED / /DERIVED marker balance preserved
- ADDED / /ADDED marker balance preserved
- Doc IDs in `sources:` manifest match DERIVED FROM markers

### Plugin metadata

- `marketplace.json` version: 0.2.0 → 0.2.1
- `plugin.json` version: 0.2.0 → 0.2.1

### Worth flagging

A few mentions that *could* be cleaned further but were left as common-knowledge vendor disclosure:

- Specific cloud-region behaviors (none mentioned)
- Authentication providers (Figma OAuth kept — customer needs to know)

If you want any of these scrubbed further, let me know.

## v0.2.0 — 2026-05-23 — All 17 skills built

The remaining 13 skills shipped in this release. Marketplace is now complete relative to the source-doc inventory in Drive folder `the source-doc folder`.

### What's new in this release

**13 new skills:**

| Skill | Source doc | Group |
|---|---|---|
| `helio-cli` | Helio CLI v1.2 | Platform / orientation |
| `helio-mcp` | Helio MCP v1.2 | Platform / orientation |
| `helio-features` | Helio Features v0.2 | Platform / orientation |
| `helio-patterns` | Helio Test Patterns v0.1 | Test lifecycle |
| `helio-audience-flow` | Audience Flow v0.1 | Test lifecycle |
| `helio-branching` | Branching v0.1 | Test lifecycle |
| `helio-assets` | Assets v0.1 | Platform mechanics |
| `helio-licensing` | Answers & Licensing v0.1 | Platform mechanics |
| `helio-participant-experience` | Participant Experience v0.1 | Platform mechanics |
| `helio-report-filtering` | Report Filtering v0.1 | Measurement & synthesis |
| `helio-design-analysis` | Design Analysis v0.1 | Measurement & synthesis |
| `helio-findings` | Findings v0.1 | Measurement & synthesis |
| `helio-reading-report` | Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2 (merged) | Measurement & synthesis |

### Source-doc gaps closed in ADDED sections

Six docs had AEO scorecard Problem-opener and/or Action-pointer gaps. All closed via ADDED sections in their respective skills' `reference.md`:

- `helio-features` — Problem + Action
- `helio-audience-flow` — Problem
- `helio-assets` — Problem + Action
- `helio-licensing` — Problem + Action
- `helio-participant-experience` — Problem + Action
- `helio-report-filtering` — Problem + Action

The other 7 new skills sourced from docs that already scored 20/20 on AEO and didn't need gap-closing additions (helio-cli, helio-mcp, helio-patterns, helio-branching, helio-design-analysis, helio-findings, helio-reading-report).

### Source-doc version note for `helio-reading-report`

The Drive copies of Reading a Helio Report and From Helio Test to Glare Signal are at v0.1. The skill content reflects the v0.2 reconciliations done locally (real Helio threshold scheme, Direct/Indirect/Failed grading, correct Behavioral / Attitudinal family assignments for all 17 metrics, explicit Performance/Intelligence "not implemented" notes). When the docs owner syncs v0.2 content back to Drive, update the skill's `last_synced` dates; if the doc IDs change (e.g., new Drive docs replace the v0.1s), update the source manifest in `SKILL.md` and the DERIVED FROM markers in `reference.md`.

### Verification

All 17 skills pass:

- Description length ≤ 1024 chars (range 613–940 chars; minimum 84 chars headroom)
- YAML frontmatter valid
- DERIVED / /DERIVED marker balance
- ADDED / /ADDED marker balance
- Doc IDs in `sources:` manifest match DERIVED FROM markers in `reference.md`

### Cross-marketplace routing

Several skills route to Glare marketplace skills (`glare-getting-started`, `glare-design-review`, `glare-decision-map`, `glare-ux-metrics`) for methodology-side depth. **This routing is unverified** in actual Claude Code — if cross-marketplace triggers don't fire as expected, the routing language in descriptions needs to be removed or rewritten. Surface this to user during real-world use.

### Plugin metadata

- `marketplace.json` version: 0.1.0 → 0.2.0
- `plugin.json` version: 0.1.0 → 0.2.0

### Decisions still deferred

- **`agent-operations.md` for workflow skills.** `helio-asset-to-test` and `helio-reading-report` are the natural candidates. Not built for v0.2.0 — defer until a real runtime contract emerges. If/when these get AO files, build both together for consistency.
- **`helio-master` orchestrator skill.** Still not built. Defer until routing patterns surface a need — with 17 skills now live, the cross-skill routing density is observable. Revisit after real use.
- **Sibling-copy bundles.** None yet. If/when Helio gets packaged (e.g., `helio-research-essentials`, `helio-engineering-bundle`), mirror Glare's `glare-packages/` pattern.
- **Cross-marketplace routing verification.** Multiple skills route to Glare. Confirm this works in Claude Code before relying on it.

### Known issues / known limits

- Source-doc version mismatch for `helio-reading-report` (Drive has v0.1; skill uses local v0.2). Flagged in the skill's reference header.
- `helio-design-analysis` is one of Helio's newer features (status / progress tracking shipped October 2025). Behavior may still be evolving; verify against live product before relying on the doc as authoritative.
- Several docs flag "Open Questions / To Verify" items (panel size figures, pricing per audience, Tree Test / Card Sort UI completeness, where Design Analysis lives in UI). Not blocking; resolve as the docs owner confirms.

## v0.1.0 — 2026-05-23 — Initial buildout

First release. Marketplace skeleton plus the first four priority skills as worked examples for the patterns laid out in `HELIO-SKILL-BUILDING-CONTEXT.md`.

### What's in this release

**Marketplace structure**

- `.claude-plugin/marketplace.json` — marketplace declaration
- `helio/.claude-plugin/plugin.json` — plugin declaration
- `README.md`, `SKILLS-CATALOG.md`, `HELIO-SKILL-BUILDING-CONTEXT.md`

**Skills built (4 of 17)**

| Skill | Source doc(s) | Notes |
|---|---|---|
| `helio-app` | Helio App v1.3 + Using Helio v0.2 | Merged skill — positioning + capability tour. Two DERIVED blocks. |
| `helio-section-types` | Section Types v0.1 | Foundational reference, largest source doc in the family. |
| `helio-ux-metrics` | UX Metrics v0.1 | Foundational measurement reference — all 17 metrics, sections, thresholds. |
| `helio-asset-to-test` | From Asset To Test v0.1 | Workflow shape — 7-step build-validate-launch. AO file deferred. |

### Source-doc gaps closed in ADDED sections

Per the AEO Scorecard v2, several source docs had Problem-opener and Action-pointer gaps:

- `helio-section-types` — Problem opener + pointer to Using Helio and `helio-asset-to-test`
- `helio-ux-metrics` — Problem opener
- `helio-asset-to-test` — Problem opener

### Plugin metadata

- `marketplace.json` version: 0.1.0 (initial)
- `plugin.json` version: 0.1.0 (initial)

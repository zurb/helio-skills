# Helio Marketplace — Changelog

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

The remaining 13 skills shipped in this release. Marketplace is now complete relative to the source-doc inventory in Drive folder `138Jk13W2CWAOgLWgW9Z5tEmQBpkBkMQ4`.

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

The Drive copies of Reading a Helio Report and From Helio Test to Glare Signal are at v0.1. The skill content reflects the v0.2 reconciliations done locally (real Helio threshold scheme, Direct/Indirect/Failed grading, correct Behavioral / Attitudinal family assignments for all 17 metrics, explicit Performance/Intelligence "not implemented" notes). When Bryan syncs v0.2 content back to Drive, update the skill's `last_synced` dates; if the doc IDs change (e.g., new Drive docs replace the v0.1s), update the source manifest in `SKILL.md` and the DERIVED FROM markers in `reference.md`.

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
- Several docs flag "Open Questions / To Verify" items (panel size figures, pricing per audience, Tree Test / Card Sort UI completeness, where Design Analysis lives in UI). Not blocking; resolve as Bryan confirms.

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

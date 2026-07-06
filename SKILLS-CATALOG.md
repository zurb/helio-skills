# Helio Skills Catalog

Current skills in the Helio marketplace. Last updated 2026-07-06 for v0.9.0.

## Built (17 skills)

The marketplace was trimmed in v0.3.0 from 17 to 14, two skills were added in v0.4.0 (helio-forms-screeners, helio-concepts), and the design-first hub helio-creating-test was added in v0.6.0. Routing for test creation: start from a **hunch** → `helio-creating-test`; start from an **asset** → `helio-asset-to-test`.

### Platform / orientation

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-app` | Helio App v1.3 + Using Helio v0.2 (merged) | ✅ v0.1.1 |
| `helio-cli` | Helio CLI v1.3 | ✅ v0.2.0 |
| `helio-mcp` | Helio MCP v1.3 | ✅ v0.2.1 |
| `helio-concepts` | Concepts v0.1 | ✅ v0.1.0 (new in v0.4.0) |

### Test lifecycle

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-creating-test` | Creating a Helio Test v0.1 | ✅ v0.1.2 (new in v0.6.0; owns the UI-only boundary checklist) |
| `helio-patterns` | Helio Test Patterns v0.2 (scrubbed) + Test Pattern Playbook v0.1 (merged) | ✅ v0.3.0 |
| `helio-asset-to-test` | From Asset To Test v0.1 | ✅ v0.1.0 |
| `helio-section-types` | Section Types v0.1 | ✅ v0.1.0 |
| `helio-audience-flow` | Audience Flow v0.1 | ✅ v0.1.0 |
| `helio-branching` | Branching v0.1 | ✅ v0.1.0 |
| `helio-forms-screeners` | Forms & Screeners v0.1 | ✅ v0.1.0 (new in v0.4.0) |

### Test mechanics

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-assets` | Assets v0.1 | ✅ v0.1.0 |

### Measurement & synthesis

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-ux-metrics` | UX Metrics v0.1 | ✅ v0.1.0 |
| `helio-report-filtering` | Report Filtering v0.1 | ✅ v0.1.0 |
| `helio-design-analysis` | Design Analysis v0.1 | ✅ v0.1.0 |
| `helio-findings` | Findings v0.1 | ✅ v0.1.0 |
| `helio-reading-report` | Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2 (merged) | ✅ v0.1.1 |

## Removed in v0.3.0

These skills were built in v0.1.0 / v0.2.0 but cut in v0.3.0 because they didn't pertain to test design, test structures, or reading reports:

- `helio-features` — feature catalog by plan tier (sales / admin context)
- `helio-licensing` — billing model, answer math, refund rules (admin context)
- `helio-participant-experience` — what participants see, IRB / regulated-research context (tangential to test design)

## Routing summary (current 17 skills)

How skills hand off to each other and to Glare.

### Within Helio marketplace

**Entry points (positioning / orientation):**

- `helio-app` → orients new users; routes to test-design and synthesis skills
- `helio-cli` ↔ `helio-mcp` (the two scripted access surfaces)
- `helio-concepts` → orients on the data model (account → project → test → section → variation → choice → branch); routes to any specific-depth sibling

**Test design chain:**

- `helio-creating-test` (design-first hub: hunch → shape → test → signal; owns the UI-only boundary checklist) ↔ `helio-asset-to-test` (asset-first hub) — entry by starting point
- `helio-creating-test` → `helio-patterns`, `helio-section-types`, `helio-ux-metrics`, `helio-audience-flow`, `helio-forms-screeners`, `helio-branching`, `helio-cli`, `helio-mcp`, `helio-reading-report`
- `helio-asset-to-test` (the build workflow) → `helio-section-types`, `helio-ux-metrics`, `helio-audience-flow`, `helio-branching`, `helio-assets`, `helio-patterns`, `helio-forms-screeners`
- `helio-patterns` ↔ `helio-asset-to-test` (recognize shapes ↔ build to shape)
- `helio-section-types` ↔ `helio-branching` (section spec ↔ routing config)
- `helio-section-types` ↔ `helio-ux-metrics` (sections ↔ metrics that auto-build them)
- `helio-forms-screeners` ↔ `helio-audience-flow` (screener setup ↔ Customer List targeting)
- `helio-forms-screeners` ↔ `helio-branching` (inline screening pattern uses branching)

**Test mechanics:**

- `helio-assets` ↔ `helio-section-types` (asset spec ↔ section that uses it)

**Synthesis:**

- `helio-reading-report` (the synthesis workflow + Glare bridge) → `helio-ux-metrics`, `helio-report-filtering`, `helio-findings`, `helio-patterns`
- `helio-report-filtering` ↔ `helio-reading-report` (slice ↔ synthesize)
- `helio-findings` → `helio-reading-report` (capture ↔ synthesize)
- `helio-design-analysis` (AI evaluator) ↔ `helio-ux-metrics` (same metric names, different scoring source)

### Cross-marketplace routing (to Glare)

These references exist in skill descriptions but are unverified in actual Claude Code routing.

- `helio-app`, `helio-reading-report` → `glare-getting-started`
- `helio-reading-report` → `glare-design-review` (SIGNAL framework for the Design Review handoff)
- `helio-reading-report` → `glare-decision-map` (Measure / Focus / Lead facets)
- `helio-ux-metrics` → `glare-ux-metrics` (broader 4-family framework, including Performance and Intelligence that Helio doesn't implement)

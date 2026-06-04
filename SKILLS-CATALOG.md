# Helio Skills Catalog

Current and planned skills in the Helio marketplace. Last updated 2026-05-23 for v0.2.0.

## Built (17 of 17 content skills)

### Platform / orientation

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-app` | Helio App v1.3 + Using Helio v0.2 (merged) | ✅ v0.1.0 |
| `helio-cli` | Helio CLI v1.2 | ✅ v0.1.0 |
| `helio-mcp` | Helio MCP v1.2 | ✅ v0.1.0 |
| `helio-features` | Helio Features v0.2 | ✅ v0.1.0 |

### Test lifecycle

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-patterns` | Helio Test Patterns v0.1 | ✅ v0.1.0 |
| `helio-asset-to-test` | From Asset To Test v0.1 | ✅ v0.1.0 |
| `helio-section-types` | Section Types v0.1 | ✅ v0.1.0 |
| `helio-audience-flow` | Audience Flow v0.1 | ✅ v0.1.0 |
| `helio-branching` | Branching v0.1 | ✅ v0.1.0 |

### Platform mechanics

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-assets` | Assets v0.1 | ✅ v0.1.0 |
| `helio-licensing` | Answers & Licensing v0.1 | ✅ v0.1.0 |
| `helio-participant-experience` | Participant Experience v0.1 | ✅ v0.1.0 |

### Measurement & synthesis

| Skill | Source doc(s) | Status |
|---|---|---|
| `helio-ux-metrics` | UX Metrics v0.1 | ✅ v0.1.0 |
| `helio-report-filtering` | Report Filtering v0.1 | ✅ v0.1.0 |
| `helio-design-analysis` | Design Analysis v0.1 | ✅ v0.1.0 |
| `helio-findings` | Findings v0.1 | ✅ v0.1.0 |
| `helio-reading-report` | Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2 (merged) | ✅ v0.1.0 |

### Cross-skill orchestration

| Skill | Notes | Status |
|---|---|---|
| `helio-master` | Cross-skill router; deferred until routing patterns surface a need | ⏳ deferred |

## Routing summary

How skills hand off to each other and to Glare. Use this when sanity-checking new skills.

### Within Helio marketplace

**Entry points (positioning / orientation):**

- `helio-app` → routes to all sibling skills depending on the depth needed
- `helio-features` → engineering reference; routes to researcher-facing skills for the same surface
- `helio-cli` ↔ `helio-mcp` (the two scripted access surfaces)

**Test design chain:**

- `helio-asset-to-test` (the 7-step workflow) → `helio-section-types`, `helio-ux-metrics`, `helio-audience-flow`, `helio-branching`, `helio-assets`, `helio-patterns`
- `helio-patterns` ↔ `helio-asset-to-test` (recognize shapes ↔ build to shape)
- `helio-section-types` ↔ `helio-branching` (section spec ↔ routing config)
- `helio-section-types` ↔ `helio-ux-metrics` (sections ↔ metrics that auto-build them)

**Test mechanics:**

- `helio-audience-flow` → `helio-licensing` (audience cost), `helio-participant-experience` (what they see)
- `helio-licensing` ↔ `helio-features` (customer cost ↔ engineering gates)
- `helio-assets` ↔ `helio-section-types` (asset spec ↔ section that uses it)
- `helio-participant-experience` → `helio-branching` (screener disqualification UX)

**Synthesis:**

- `helio-reading-report` (the synthesis workflow + Glare bridge) → `helio-ux-metrics`, `helio-report-filtering`, `helio-findings`, `helio-patterns`
- `helio-report-filtering` ↔ `helio-reading-report` (slice ↔ synthesize)
- `helio-findings` → `helio-reading-report` (capture ↔ synthesize)
- `helio-design-analysis` (AI evaluator) ↔ `helio-ux-metrics` (same metric names, different scoring source)
- `helio-design-analysis` ≠ AI Audience (in `helio-audience-flow`) — disambiguate explicitly

### Cross-marketplace routing (to Glare)

These references exist in skill descriptions but are unverified in actual Claude Code routing. Confirm before relying.

- `helio-app`, `helio-reading-report` → `glare-getting-started`
- `helio-reading-report` → `glare-design-review` (SIGNAL framework for the Design Review handoff)
- `helio-reading-report` → `glare-decision-map` (Measure / Focus / Lead facets)
- `helio-ux-metrics` → `glare-ux-metrics` (broader 4-family framework, including Performance and Intelligence that Helio doesn't implement)

### What's not routing anywhere (intentional)

- `helio-master` orchestrator is deferred. Without it, the entry-point load falls on `helio-app` (orientation) and `helio-reading-report` (synthesis). If users get lost between them, build `helio-master`.

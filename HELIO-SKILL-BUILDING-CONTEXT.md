# Helio Content → Skill Mapper Prompt

**Audience:** A fresh AI session being asked to convert Helio platform content into skills, or a human reviewing the work.
**Last updated:** 2026-05-23
**Marketplace version:** 0.1.0 (initial buildout)

This document captures the pattern, conventions, and current state of the Helio marketplace so the next AI session can pick up the work without re-deriving everything from scratch. Companion to the Glare Content → Skill Mapper Prompt — read that one first if you haven't, because Helio inherits most of the engineering discipline (frontmatter, markers, verification) and just differs on content shape.

---

## TL;DR — what you're being asked to do

Helio is ZURB's user research platform. Its documentation set is shipped as a **Claude Code plugin marketplace** parallel to Glare's: a collection of skills that researchers, designers, PMs, and AI workflows use to operate Helio and read its output. The source of truth for the content is **Google Drive docs** maintained by Bryan in folder `138Jk13W2CWAOgLWgW9Z5tEmQBpkBkMQ4`. Each doc covers a specific aspect of the platform (section types, UX metrics, audience flow, etc.). When Bryan revises a doc, the corresponding skill gets rebuilt to match.

**Your job:**

1. **Detect updates.** Bryan ships new or revised Drive docs. Compare against what's already in the skill.
2. **Rebuild the skill** following the conventions below — preserve what's still accurate, refresh what changed, add what's new.
3. **Bump versions and write a CHANGELOG entry.**
4. **Verify before committing.** Description length, marker balance, frontmatter validity, file integrity.
5. **Be transparent with the user about what changed, what you skipped, and any inconsistencies you found in the source.**

The user is technical, busy, and wants real engagement with decisions rather than blind compliance. Surface things that don't fit the pattern. Ask before doing destructive things (like deprecating sections). Otherwise act and report.

---

## The big picture

### What Helio is

Helio is a fast user research and testing platform for product design teams. It runs Click Tests, Prototype Tests, Likert scales, Multiple Choice, NPS, MaxDiff, and 8 other section types against a real audience (~1M panelists), and produces **UX Metric scores** (0–100, with a consistent 5-tier label: Very Good / Good / Average / Poor / Very Poor) that map directly onto the Glare framework's measurement vocabulary.

Helio implements two of Glare's four UX metric families: **Behavioral (8 metrics)** and **Attitudinal (9 metrics)** — 17 total. Performance and Intelligence metrics are Glare concepts not yet in Helio's code.

The platform is reached three ways, each with its own skill:
- **Web app** — for researchers and teams driving studies by hand
- **CLI** (`@zurb/helio-cli`) — for scripts, cron, CI, version-controlled test definitions
- **MCP server** (hosted at `https://mcp.helio.app/api/mcp`) — for AI assistants (Claude Desktop, Cursor, Claude Code, custom agents)

Helio is sold in engagement-based plans (Pilot, Scale, On Demand, Business). Pricing is measured in "answers" where one answer = one participant completing one section.

### What a "skill" is in this context

A skill is a folder under `helio-marketplace/helio/skills/` containing:

- **`SKILL.md`** — always loaded; carries frontmatter (name, description, version, sources), the core idea, file-loading instructions, application steps, handoffs
- **`reference.md`** — practitioner reference content; loaded when SKILL.md instructs
- **`agent-operations.md`** — *optional;* only for workflow-shaped skills where there's a runtime contract worth promoting (currently a candidate for `helio-asset-to-test` and `helio-reading-report` only)

Skill names follow the pattern `helio-<topic>` (e.g., `helio-section-types`, `helio-ux-metrics`, `helio-audience-flow`).

### How Helio skills differ from Glare skills

Both marketplaces share the engineering discipline (frontmatter spec, DERIVED/ADDED markers, 1024-char description limit, verification checklist). They differ on **content shape**:

- **Glare skills** are built from a strict 7-doc template (Overview / Techniques / Playbook / References / Decisions / Examples / Agent Operations). Each Glare framework *block* has seven source docs that decompose cleanly into a skill.
- **Helio skills** are built from **one source doc each** (with rare exceptions). Most Helio docs are self-contained reference docs or workflow docs. The Glare 7-doc decomposition doesn't apply.

This means Helio's `reference.md` typically has **one DERIVED section** (the full source doc) plus ADDED sections (When to use, Failure modes, etc.) — not six DERIVED sections like Glare.

### Marketplace mechanics

- **`.claude-plugin/marketplace.json`** at the repo root declares the marketplace.
- **`helio/.claude-plugin/plugin.json`** declares the plugin (one plugin per marketplace, named `helio`).
- **`helio/skills/<skill-name>/SKILL.md`** is loaded by Claude Code when the description triggers a match against the user's request.

Skill descriptions have a **hard 1024-character limit**. The Glare validator (Bryan's tooling) will fail above this. Plan trigger phrases carefully.

---

## File and folder architecture

```
/Users/benjaminscott/Desktop/zurb.nosync/skills/
├── glare-marketplace/                          ← existing
├── helio-marketplace/                          ← NEW (Helio)
│   ├── .claude-plugin/
│   │   └── marketplace.json
│   ├── helio/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   │       ├── helio-app/
│   │       │   ├── SKILL.md
│   │       │   └── reference.md
│   │       ├── helio-cli/
│   │       │   ├── SKILL.md
│   │       │   └── reference.md
│   │       ... (17 skills + 1 master)
│   ├── CHANGELOG.md
│   ├── README.md
│   ├── SKILLS-CATALOG.md
│   └── HELIO-SKILL-BUILDING-CONTEXT.md         ← THIS FILE (after first commit)
```

### Sibling copies

Unlike Glare (which has 5 sibling copies: `glare-marketplace-core`, `glare-packages/glare-full`, `glare-packages/glare-decision-map`, `glare-skills-flat`, `glare-skills-hierarchical`), **Helio has no sibling copies yet**. The canonical `helio-marketplace` is the only working copy.

If/when Helio gets bundled or split into packages, mirror the Glare sibling-sync workflow (verify with `diff -rq` after each copy, version-skew flagged).

### Only `helio-marketplace` is a git repo

Treat it the same way as `glare-marketplace`: changes go in canonical first, sync to siblings if any exist, verify with `diff`.

---

## The proposed Helio skill set (17 skills + 1 master)

Mapping the 19 active source docs to skills with two natural consolidations:

### Platform / orientation (4 skills)

| Skill name | Source doc(s) | Triggers on |
|---|---|---|
| `helio-app` | Helio App v1.3 + Using Helio v0.2 (merged) | "What is Helio," positioning, plan selection, capability tour |
| `helio-cli` | Helio CLI v1.2 | Terminal usage, scripting, CI integration |
| `helio-mcp` | Helio MCP v1.2 | AI-assistant access, MCP tool calls |
| `helio-features` | Helio Features v0.2 | Engineering-side feature reference, plan/feature gates |

### Test lifecycle (5 skills)

| Skill name | Source doc(s) | Triggers on |
|---|---|---|
| `helio-patterns` | Helio Test Patterns v0.1 | Test shapes, the core 5-Q template, multi-screen, R3/R5 |
| `helio-asset-to-test` | From Asset To Test v0.1 | Build-validate-launch workflow, the 7-step arc |
| `helio-section-types` | Section Types v0.1 | Every section type — Click, Prototype, Likert, MaxDiff, etc. |
| `helio-audience-flow` | Audience Flow v0.1 | Audience choice, panel filters, custom lists, intercept |
| `helio-branching` | Branching v0.1 | Conditional routing, screeners, disqualification |

### Platform mechanics (3 skills)

| Skill name | Source doc(s) | Triggers on |
|---|---|---|
| `helio-assets` | Assets v0.1 | Images, video, Figma integration, asset lifecycle |
| `helio-licensing` | Answers & Licensing v0.1 | Answers cost, refunds, license tiers, refills |
| `helio-participant-experience` | Participant Experience v0.1 | What participants see, consent, accessibility, IRB context |

### Measurement & synthesis (5 skills)

| Skill name | Source doc(s) | Triggers on |
|---|---|---|
| `helio-ux-metrics` | UX Metrics v0.1 | The 17 metrics, sections required, threshold scheme, Overall Score |
| `helio-report-filtering` | Report Filtering v0.1 | Filter mechanics, cohort slicing, demographic filters |
| `helio-design-analysis` | Design Analysis v0.1 | AI heuristic evaluation, the four master user needs |
| `helio-findings` | Findings v0.1 | Capturing observations, sharing, comments |
| `helio-reading-report` | Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2 (merged) | Synthesis workflow, 30-second scan, divergence reading, one-sentence signal, Glare bridge |

### Cross-skill orchestration (1 skill)

| Skill name | Triggers on |
|---|---|
| `helio-master` | "I'm stuck in Helio," "which skill applies," cross-skill questions, doc-family navigation |

**Total: 17 content skills + 1 master = 18 skills.**

The two merges:
- **`helio-app`** absorbs Using Helio v0.2's capability tour because positioning + capabilities form one mental model. The merged skill's `reference.md` has two DERIVED sections (one per source doc).
- **`helio-reading-report`** absorbs From Helio Test to Glare Signal v0.2 because the mechanical synthesis and the conceptual Glare-bridge are the same conversation. The merged skill has two DERIVED sections.

---

## SKILL.md format

Every `SKILL.md` follows this structure:

```markdown
---
[frontmatter — see Frontmatter Spec below]
---

You are helping the user work with **<topic>** in Helio. <one-sentence positioning>.

## Core idea

[2–4 sentences naming what the doc is about + the foundational structure (e.g., "the 17 UX metrics across two families," "the 14 section types grouped by purpose," "the 7-step build workflow"). Cite the structure as a numbered or bulleted list.]

## Files to read

[Explicit instruction: read `reference.md` (and `agent-operations.md` if it exists). Helio skills usually only have `reference.md`.]

## How to apply

[Numbered steps the Skill follows, ~5–8 items. For reference-shaped skills this might be "1. Read the user's question. 2. Identify which section of reference.md is relevant. 3. Surface the answer with the canonical Helio vocabulary." For workflow skills it's the actual steps of the workflow.]

## Operating rules

[Only for skills with an agent-operations.md. The highest-leverage runtime rules duplicated from agent-operations.md so they bind even without reading that file. For reference-shaped skills, skip this section.]

## What's new in v<X>

[Short release notes for the current version — what changed since last rebuild.]

## Handoffs

[When to route to sibling skills. E.g.: "For section types, use `helio-section-types`. For audience choice, use `helio-audience-flow`. For the broader Glare framework, use `glare-getting-started`."]
```

### What SKILL.md is *not*

- It's not the full reference. That lives in `reference.md`.
- It's not the runtime contract. That lives in `agent-operations.md` if it exists.
- It's not a marketing intro. The Core idea is for orientation; the Handoffs are for routing.

---

## Frontmatter spec

Exact structure (mirrors Glare's pattern):

```yaml
---
name: helio-section-types
description: Use this skill when the user is working with section types in Helio — picking which section type to use for a question, configuring sections, or understanding what each section captures. Triggers — "what section type," "click test," "prototype test," "likert," "MaxDiff," "card sort," "tree test," "matrix," "preference," "rank," "free response," "what's the difference between," "how do I configure a section." Do NOT use when the question is about which UX metric to attach (use `helio-ux-metrics`), how to build a whole test (use `helio-asset-to-test`), or the AI heuristic evaluator (use `helio-design-analysis`). For test shapes that combine sections, use `helio-patterns`.
version: 0.1.0
source_doc_version: v0.1
last_rebuilt: 2026-05-23

sources:
  - doc_id: 165DVFQskrAuCBgYItH0Oz_IxZO3GPHupIFrZZvAyJGs
    title: Section Types v0.1
    drive_url: https://docs.google.com/document/d/165DVFQskrAuCBgYItH0Oz_IxZO3GPHupIFrZZvAyJGs/edit
    last_synced: 2026-05-23
---
```

### Description rules

- **Hard limit: 1024 characters.** The validator fails above this. Always check after edits:
  ```bash
  python3 -c "import yaml; d = yaml.safe_load(open('SKILL.md').read().split('---', 2)[1]); print(len(d['description']))"
  ```
- **Structure:** `Use this skill when the user is...` + `Triggers — "phrase," "phrase," ...` + `Do NOT use when...` + `For <related context>, use \`<sibling-skill>\``
- **Trigger phrases** should match what real users say. Direct quotes in single quotes; concepts as plain phrases. Include both happy-path triggers and diagnostic phrases (e.g., "what does Sentiment mean," "section won't validate").
- **Routing language** at the end tells Claude when to hand off to sibling skills. Keep this current — broken references confuse routing.
- **Cross-marketplace routing** is allowed and encouraged. Helio skills can route to Glare skills (`glare-decision-map`, `glare-measure`, `glare-getting-started`) when the question is methodological rather than platform-mechanical.

### Source manifest

The `sources:` block lists every Drive doc the skill derives from. **Every doc ID in the manifest must match a `DERIVED FROM:` comment in `reference.md`** — they're the binding contract for the future refresh script (which will compare `last_synced` timestamps to Drive's `modifiedTime` to detect staleness).

Most Helio skills have a single source. The two merged skills (`helio-app`, `helio-reading-report`) have two sources each.

### Version semantics

- **`version`** — the skill's version, bumped on any meaningful change. Starts at 0.1.0 for initial builds; first stable release is 1.0.0.
- **`source_doc_version`** — the version of Bryan's source docs this skill reflects (e.g., "v0.1," "v1.2").
- **`last_rebuilt`** — ISO date of the rebuild.

When the marketplace as a whole gets a version bump, all three files need updating: `.claude-plugin/marketplace.json`, `helio/.claude-plugin/plugin.json`, and `CHANGELOG.md`.

---

## Content markers

### DERIVED FROM / /DERIVED

Wraps content that came from a Drive source doc:

```markdown
<!-- DERIVED FROM: <doc_id> — <doc title> -->

## Section content here...

<!-- /DERIVED -->
```

The `doc_id` is the Google Drive document ID. The title is the doc's title verbatim.

**Why this matters:** the future refresh script will detect these markers, compare to the source doc's modified time, and rewrite the content between the markers without touching ADDED sections. Get the IDs right.

For Helio's single-source-per-skill pattern, there's usually just one DERIVED block covering the entire source doc.

### ADDED / /ADDED

Wraps content the skill-builder added (not derived from any source doc):

```markdown
<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

...

<!-- /ADDED -->
```

ADDED content survives source-doc refreshes. Typical ADDED sections for Helio skills:

- **When to use** — the trigger contexts (mirrors the description but in long form)
- **Failure modes** — common ways teams misuse this part of Helio
- **Problem opener (when missing from source)** — the one-sentence "what's broken without this" framing that the AEO scorecard flagged as missing from most reference docs
- **Cross-doc pointers** — explicit handoffs to sibling skills

### Verifying marker balance

```bash
grep -c 'DERIVED FROM' reference.md   # should equal number of source sections (usually 1 for Helio, 2 for merged skills)
grep -c '/DERIVED' reference.md       # should match
grep -c 'ADDED' reference.md          # opening + closing + any inline mentions
```

---

## Reference.md structure

```markdown
# <Skill Topic> — Reference

**Skill:** <Skill name>
**Source:** <Doc title and version>
**Source last synced:** <date>

[Deviation notes if source has inconsistencies — e.g., factual errors flagged by the AEO scorecard.]

<!-- DERIVED FROM: <doc_id> — <doc title> -->

[Full source doc content, structured by source headings.]

<!-- /DERIVED -->

<!-- ADDED <date> (skill-builder context) -->

## When to use

[Trigger contexts in narrative form.]

## Failure modes

[Common misuses.]

## Where to go next

[Cross-doc routing.]

<!-- /ADDED -->
```

---

## Workflow: converting a doc to a skill

Step-by-step for taking a Helio source doc to a shipped skill.

### 1. Read the source doc

Use the Drive MCP `read_file_content` tool with the doc's ID. For docs already in the conversation context (via `<sync_sources>`), the content is already there — no fetch needed.

### 2. Check the AEO scorecard

Look up the doc in `Helio Doc Family — AEO Scorecard v2.docx`. If the doc has gaps (Problem opener missing, Action pointer missing, Strengths/Limits soft), plan to address them in the ADDED sections of `reference.md`.

### 3. Compare to existing skill (if any)

If a previous version of the skill exists, read its `SKILL.md` and `reference.md`. Diff the source doc against the existing DERIVED content. Identify:

- Sections that changed materially (rewrite)
- Sections that are minor edits (line-level)
- Sections that are new (add)
- Sections that need to be deprecated (rare — confirm with user first)
- Pre-existing ADDED content that needs to survive

### 4. Decide file layout

For Helio:
- **Reference-shaped skill** → `SKILL.md` + `reference.md`. No `agent-operations.md`.
- **Workflow-shaped skill** (`helio-asset-to-test`, `helio-reading-report`) → `SKILL.md` + `reference.md` + optionally `agent-operations.md` if there's a runtime contract worth promoting.
- **Merged skill** (`helio-app`, `helio-reading-report`) → `SKILL.md` + `reference.md` with two DERIVED blocks.

### 5. Draft `SKILL.md`

Required sections:

```markdown
---
[frontmatter — see spec above; description ≤1024 chars]
---

You are helping the user work with **<topic>** in Helio. <positioning sentence>.

## Core idea

[2–4 sentences + numbered or bulleted foundational structure]

## Files to read

[Read `reference.md` (and `agent-operations.md` if exists)]

## How to apply

[5–8 numbered steps]

## What's new in v0.1.0

[Initial release notes]

## Handoffs

[Cross-skill routing]
```

Check description length:
```bash
python3 -c "import yaml; d = yaml.safe_load(open('SKILL.md').read().split('---', 2)[1]); print('desc len:', len(d['description']))"
```

If over 1024, trim — drop generic phrases first, keep trigger-rich vocabulary.

### 6. Draft `reference.md`

Header → DERIVED block(s) covering the full source doc → ADDED sections at the end.

If the AEO scorecard flagged a Problem-opener gap, **add the Problem opener at the top of the ADDED sections**, not inside DERIVED (DERIVED reflects what the source actually says).

Example:

```markdown
<!-- ADDED 2026-05-23 (problem opener — source v0.1 is missing this; see AEO Scorecard) -->

## What this solves

Without a working model of every Helio UX metric, teams attach Sentiment to everything (it's the easiest) and miss the metrics that would actually answer the decision. This is the catalog so the choice is deliberate.

<!-- /ADDED -->
```

### 7. Verify the skill

```bash
# Description length
python3 -c "import yaml; d = yaml.safe_load(open('SKILL.md').read().split('---', 2)[1]); print('desc len:', len(d['description']))"

# Marker balance
grep -c 'DERIVED FROM' reference.md
grep -c '/DERIVED' reference.md

# Doc IDs match between sources manifest and DERIVED FROM markers
grep '^  - doc_id:' SKILL.md
grep -oE 'DERIVED FROM: [a-zA-Z0-9_-]+' reference.md

# YAML validity
python3 -c "import yaml; yaml.safe_load(open('SKILL.md').read().split('---', 2)[1])"
```

### 8. Bump versions

- `helio-marketplace/.claude-plugin/marketplace.json` — bump version
- `helio-marketplace/helio/.claude-plugin/plugin.json` — bump version (same number)

Initial release is 0.1.0. First stable is 1.0.0.

### 9. Write CHANGELOG entry

Follow Glare's CHANGELOG format:

- Title with version + date + short descriptor
- 1–2 paragraph context
- "What changed" — bullet list or table
- Plugin metadata version bumps
- Notes on deferred decisions, source-doc quirks, etc.

### 10. Verify and commit

```bash
cd helio-marketplace
git status  # confirm what's staged
git add <files>
git commit -F - <<'EOF'
<commit message>
EOF
```

Commit format: short subject line (skill name + change + version arrow), body with bullets, sources list, follow-up flags.

---

## Verification checklist (before commit)

- [ ] `SKILL.md` description ≤ 1024 chars
- [ ] `SKILL.md` frontmatter parses as valid YAML
- [ ] `sources:` manifest count matches DERIVED FROM marker count
- [ ] All doc IDs in `sources:` manifest appear in DERIVED FROM markers (and vice versa)
- [ ] DERIVED and /DERIVED counts match
- [ ] ADDED and /ADDED counts match
- [ ] No stray references to old version numbers in body text
- [ ] Marketplace + plugin JSONs bumped to new version
- [ ] CHANGELOG entry written
- [ ] If the source doc had an AEO-scorecard gap, the fix is in an ADDED section (not buried inside DERIVED)
- [ ] Any source-doc inconsistencies (typos, contradictions, factual errors) flagged in the reference header or CHANGELOG

---

## State of the world (as of 2026-05-23)

### What exists

- **19 source docs in Drive folder `138Jk13W2CWAOgLWgW9Z5tEmQBpkBkMQ4`** — covering platform/orientation, test lifecycle, mechanics, measurement & synthesis. All have been AEO-rubric scored (see `Helio Doc Family — AEO Scorecard v2.docx`).
- **No Helio skills built yet.** This prompt is the kickoff for the initial buildout. The marketplace folder doesn't exist on disk yet.
- **The Glare marketplace lives at `glare-marketplace/`** with 60 skills at v3.4.0. Helio's marketplace will sit at `helio-marketplace/` parallel to it.

### Pending source-doc gaps from the AEO scorecard

Ten docs have minor gaps that should be addressed when converting to skills. The fix is a one-sentence opener and/or a top-of-doc pointer — placed in ADDED sections of the skill's `reference.md`, not in DERIVED:

| Doc | Gap | Fix to add as ADDED in the skill |
|---|---|---|
| Using Helio v0.2 | Problem; Strengths/Limits; Action | One-sentence Problem opener; "where Helio doesn't fit" parallel to Helio App; pointer to From Asset To Test |
| Helio Features v0.2 | Problem; Action | "Without this map, engineers and researchers describe the same surface in incompatible language"; pointer to Using Helio and Section Types |
| From Asset To Test v0.1 | Problem | "Without a defined workflow, teams skip the test-build steps that matter and produce tests that look thorough but don't answer the question" |
| Section Types v0.1 | Problem; Action | "Teams default to Multiple Choice and Likert and miss the moves that surface the actual signal"; pointer to Using Helio's Building a Study section |
| Audience Flow v0.1 | Problem | "Audience is the biggest cost-and-quality lever; this is how to make the choice deliberately" |
| Assets v0.1 | Problem; Action | "Asset handling failures are quiet — the test still runs but the data is corrupted"; pointer to Section Types |
| Answers & Licensing v0.1 | Problem; Action | "Teams miscalculate cost by 2–5× because one participant on a 5-section study costs 5 answers, not 1"; pointer to Helio App |
| Participant Experience v0.1 | Problem; Action | "Researchers answer 'what will participants see' from memory and miss real participant constraints"; pointer to From Asset To Test |
| UX Metrics v0.1 | Problem | "Teams attach Sentiment to everything; this is the catalog so the choice is deliberate" |
| Report Filtering v0.1 | Problem; Action | "A Good Overall can hide a Poor segment; this is how to slice"; pointer to Reading a Helio Report |

These don't need to wait for source-doc updates from Bryan. Apply them in ADDED sections during skill conversion.

### Decisions deferred

- **Whether Helio gets sibling-copy bundles like Glare does.** Right now there's only the canonical. If/when Helio gets packaged into bundles (e.g., `helio-research-essentials`, `helio-engineering-only`), mirror Glare's `glare-packages/` pattern.
- **`agent-operations.md` for workflow skills.** The two candidates are `helio-asset-to-test` and `helio-reading-report` — both have runtime workflows that could benefit from a promoted runtime contract. Decision deferred to when those skills are built; default to no AO file unless a real need surfaces.
- **`helio-master` skill content.** The orchestrator pattern from Glare (`glare-master`) is a good model but Helio's cross-skill routing is less dense (fewer overlapping concerns than Glare's components-and-blocks structure). May start without `helio-master` and add it only if cross-skill routing gets confusing.
- **Helio + Glare cross-marketplace routing.** Skills in `helio-marketplace` should route to skills in `glare-marketplace` for methodological questions (e.g., "what user need does this serve" → `glare-define-user-needs`). Confirm the cross-marketplace routing actually works in Claude Code before relying on it.

### Known source-doc quirks

- **My Metrics doc was retired during reconciliation.** `_DEPRECATED_Metrics for Helio Testing v0.1.docx` exists in the local working folder; the canonical metric reference is **UX Metrics v0.1** (in Drive). Don't pull from the deprecated doc.
- **Creating a Helio Test v0.1 is also deprecated.** Superseded by the doc family. Don't pull from it.
- **Pricing tiers in Helio App v1.3 (Pilot/Scale/On Demand/Business)** are marketing-facing plans. **Answers & Licensing v0.1's license tiers (Trial/Pro/Business 1–3/Scale/Design–Agency–Enterprise/Custom)** are the underlying license model. Both are valid — the marketing plans are what customers see, the license tiers are the accounting underneath. Don't conflate them.

---

## Worked reference: how `helio-section-types` would look

The most reference-heavy skill in the family. Use this as the template for other reference-shaped Helio skills.

**Path:** `helio-marketplace/helio/skills/helio-section-types/`

**File structure:**
- `SKILL.md` (~80 lines) — frontmatter with 1 source, Core idea (the 14 section types grouped by purpose), Files to read, How to apply (5 steps), What's new, Handoffs
- `reference.md` (~700 lines) — Header + 1 DERIVED block (the full Section Types doc) + 2 ADDED sections (Problem opener; Failure modes)

**Source doc:**
- Section Types v0.1 — `165DVFQskrAuCBgYItH0Oz_IxZO3GPHupIFrZZvAyJGs`

**Description draft (≤1024 chars):**
> Use this skill when the user is working with section types in Helio — picking which to use for a question, configuring sections, or understanding what each captures. Triggers — "what section type," "click test," "prototype test," "likert," "MaxDiff," "card sort," "tree test," "matrix," "preference," "rank," "free response," "what's the difference between," "how do I configure a section." Do NOT use when the question is about which UX metric to attach (use `helio-ux-metrics`), how to build a whole test (use `helio-asset-to-test`), or the AI heuristic evaluator (use `helio-design-analysis`). For test shapes that combine sections, use `helio-patterns`.

---

## Worked reference: how `helio-reading-report` would look (merged skill)

The most complex skill in the family — merges two source docs and has a workflow shape.

**Path:** `helio-marketplace/helio/skills/helio-reading-report/`

**File structure:**
- `SKILL.md` (~120 lines) — frontmatter with 2 sources, Core idea (the synthesis chain: scan → headline → divergence → open text → compare → red flags → one-sentence signal), Files to read, How to apply (the synthesis steps), Operating rules (promoted from the docs' synthesis discipline), What's new, Handoffs
- `reference.md` (~900 lines) — Header + 2 DERIVED blocks (Reading a Helio Report v0.2 + From Helio Test to Glare Signal v0.2) + ADDED sections
- `agent-operations.md` *possibly* — if the synthesis workflow has a runtime contract worth promoting (output schema for the one-sentence signal, confidence vocabulary, escalation triggers). Defer this decision until the skill is built and tested.

**Source docs:**
- Reading a Helio Report v0.2
- From Helio Test to Glare Signal v0.2

---

## Tools you'll need

Operating in this environment, the relevant tools:

- **Drive MCP** — `mcp__6644...search_files`, `read_file_content`, `get_file_metadata`, `list_recent_files`. Used to enumerate folders and fetch source docs.
- **File tools** — `Read`, `Write`, `Edit`, `Glob`, `Grep` for the local working copies.
- **Bash** — for diff, sync, version checks, git operations. Use absolute paths.
- **TaskCreate / TaskUpdate / TaskList** — track multi-step work.
- **AskUserQuestion** — for genuinely ambiguous decisions where the answer changes what you produce significantly (skill granularity, merge boundaries, deprecating sections). Don't use for trivial confirmations.

The validator that catches description length is run manually. Always pre-check with the `python3 yaml.safe_load` snippet before claiming a rebuild is done.

---

## Engagement style with this user

Same as the Glare prompt — repeated here for self-containment:

Things the user values:
- **Real engagement with decisions**, not blind execution. When the source has a contradiction or the pattern is ambiguous, name it and propose a resolution.
- **Forward momentum.** Don't ask multiple-choice clarifying questions for things you can take a sensible default on. Make the call, flag it.
- **Honest accounting.** If you said you did something and didn't quite do it, correct yourself.
- **Verification you can show.** Run actual diffs, validators, length checks. Don't claim it's correct without evidence.
- **Useful surfacing.** If something doesn't fit the pattern (typos, deprecated sections, version drift), surface it.
- **Brevity in chat.** The artifacts can be long; the chat replies should be tight.

Things to avoid:
- Stamping content without engaging the structure
- Adding ADDED sections that duplicate DERIVED content
- Bumping version numbers without writing a CHANGELOG entry
- Touching multiple skills in one "rebuild" without surfacing what's still pending

---

## Open questions worth asking the user (if they come up)

Don't pile these on the user. Surface one at a time when they become blocking.

1. **`agent-operations.md` for workflow skills** — when building `helio-asset-to-test` or `helio-reading-report`, surface whether to promote a runtime contract into its own file or keep everything in `reference.md`.
2. **`helio-master` necessity** — after building the first ~5 skills, surface whether cross-skill routing feels confused enough to warrant a master orchestrator.
3. **Cross-marketplace routing** — confirm that descriptions referencing Glare skills (e.g., "for the methodology, use `glare-getting-started`") actually trigger correctly in Claude Code. If not, drop the cross-references.
4. **Bundle packaging** — when Helio reaches some critical mass of skills (~10+), surface whether to start carving bundles like Glare's `glare-packages/`.
5. **Source-doc refresh script** — Bryan may want a script that compares Drive `modifiedTime` against skill `last_synced` and flags stale skills. Worth scoping if/when source-doc updates become frequent.

---

## What to do first

When a fresh AI session picks this up:

1. **Read this doc.**
2. **Confirm the marketplace folder doesn't already exist.** If it does, skip to step 5.
3. **Create the marketplace skeleton:** `helio-marketplace/.claude-plugin/marketplace.json`, `helio-marketplace/helio/.claude-plugin/plugin.json`, empty `helio-marketplace/helio/skills/`, blank `CHANGELOG.md` and `README.md`.
4. **Pick a skill to build first.** Suggested order:
   - `helio-app` (positioning anchor — useful first stop for new users)
   - `helio-section-types` (foundational reference, longest single doc)
   - `helio-ux-metrics` (foundational measurement reference)
   - `helio-asset-to-test` (workflow anchor)
   - Then expand outward
5. **Follow the conversion workflow** (Section "Workflow: converting a doc to a skill" above).
6. **After ~3 skills are built, sanity-check routing.** Read the descriptions side by side and make sure they don't compete for the same triggers.
7. **Commit and report.**

The doc family is in good shape (AEO scorecard 18+/20 across the board), the source-of-truth lives in one Drive folder, and the conventions inherit cleanly from the Glare marketplace. The main risk is rushing — each skill needs its description tuned and its DERIVED/ADDED structure right. One skill at a time, verify each before moving on.

---
name: helio-concepts
description: Use this skill when the user is asking about how Helio's data model / hierarchy fits together — account → project → test → section → variation → choice/hotspot → branch, plus the cross-cutting systems (assets, findings, UX metrics, quotas). Triggers — "Helio hierarchy," "Helio data model," "account project test," "where does X live in Helio," "what's a variation," "why can't I move X across tests," "test lifecycle," "response lifecycle," "how does the AI workflow fit," "how does billing connect," "Helio mental model," "account vs project vs test," "test status draft running fulfilled." Do NOT use when the user wants section spec (use `helio-section-types`), the test-build workflow (use `helio-asset-to-test`), audience config (use `helio-audience-flow`), report reading (use `helio-reading-report`), or synthesis (use `helio-reading-report`). For any specific feature depth, drop into the relevant sibling skill.
version: 0.1.0
source_doc_version: Concepts v0.1
last_rebuilt: 2026-06-29

sources:
  - doc_id: src-concepts-v0.1
    title: Concepts v0.1
    last_synced: 2026-06-29
---

You are helping the user understand **how Helio is organized** — the account → project → test → section hierarchy, the cross-cutting systems, and the lifecycles of tests and responses.

## Core idea

Helio is organized around a nested hierarchy with a handful of cross-cutting systems attached at various levels.

**The main tree:**

- **Account** (the workspace) — holds License, Members, Brand options, Figma authentications
   - **Project** (folder of related tests)
      - **Test** (a study — sequence of sections)
         - **Section** (a single question or task)
            - **Variation** (an A/B variant of the section)
               - **Choice** (answer option) or **Hotspot** (Click Test region)
                  - **Branch** (routing rule — where to send participants who pick this)
         - **Quota** (audience configuration)
         - **Finding** (researcher-captured observation)
         - **Response** (one participant's complete pass)
            - **Section Response** (their answer to one section)

A study can have many sections; each section can have one or more variations; each variation has the choices or hotspots participants interact with.

**Cross-cutting systems** don't fit strictly in the tree: Assets, Findings, UX Metrics, Branches, Comments. Each attaches at multiple levels.

**Lifecycles matter:** Tests move through Draft → Running → Fulfilled (or Paused / Stopped). Responses move through arrival → per-section capture → complete (or hidden / flagged / spam).

The **AI Design Analysis workflow** creates a parallel hierarchy that doesn't share the participant response model — see `helio-design-analysis`.

## Files to read

Read `reference.md` for the full hierarchy diagram, what each level holds, the cross-cutting systems, test/response lifecycles, how the AI workflow differs, how billing connects, and identity/authentication basics.

## How to apply

1. Identify why the user is asking — building a mental model, debugging a "why can't I do X" question, or planning an integration.
2. For mental-model questions, walk the main hierarchy (account → project → test → section → variation → choice → branch).
3. For "why can't I move / delete / edit X" questions, surface the relevant constraint — variations belong to sections, sections belong to tests, most edits require Draft status.
4. For test-lifecycle questions, walk Draft → Running → Fulfilled / Paused / Stopped.
5. For response-lifecycle questions, walk arrival → capture → completion, plus hidden / flagged / spam states.
6. For AI workflow questions, name that Design Analysis runs its own parallel hierarchy — no participant responses, no quota, its own metric storage.
7. For most specific depth (section types, audience config, UX metrics, findings, etc.), route to the appropriate sibling skill.

## What's new in v0.1.0

Initial release. Sourced from Concepts v0.1. Internal codebase names (class names, model names) were reframed into customer-facing language during the skill build.

## Handoffs

Almost every specific question routes somewhere:

- For **section type spec**: `helio-section-types`
- For **audience configuration** (Quota depth): `helio-audience-flow`
- For **UX Metrics** (how metrics attach to sections): `helio-ux-metrics`
- For **Branches** (how routing is configured): `helio-branching`
- For **Findings** (how observations get captured): `helio-findings`
- For **Assets** (images, video, Figma prototypes): `helio-assets`
- For **the AI Design Analysis parallel workflow**: `helio-design-analysis`
- For **the test-build workflow end to end**: `helio-asset-to-test`
- For **designing a test from a hunch** (shapes, templates, validation): `helio-creating-test`
- For **Forms & Screeners** on Customer List signup: `helio-forms-screeners`
- For **positioning and plans**: `helio-app`

# Helio Marketplace

A Claude Code plugin marketplace for ZURB's [Helio](https://helio.zurb.com) user research platform. Companion to the [Glare marketplace](https://github.com/zurb/glare-marketplace) — Glare is the framework, Helio is the platform that runs the research the framework calls for.

## What's in here

A plugin called `helio` containing skills for every major aspect of operating Helio:

- **Platform / orientation** — what Helio is, the CLI, the MCP server, engineering reference
- **Test lifecycle** — designing, validating, and launching studies
- **Platform mechanics** — assets, audiences, licensing, participant experience
- **Measurement & synthesis** — UX Metrics, filtering reports, AI evaluation, finding capture, signal synthesis

Each skill is a folder under `helio/skills/<skill-name>/` containing:

- `SKILL.md` — always-loaded; carries frontmatter, the core idea, file-loading instructions, application steps, and handoffs to sibling skills
- `reference.md` — practitioner reference content; loaded when SKILL.md instructs
- `agent-operations.md` — *optional;* runtime contract for workflow skills

## Source of truth

All Helio skill content derives from Google Drive docs maintained by Bryan in folder [`138Jk13W2CWAOgLWgW9Z5tEmQBpkBkMQ4`](https://drive.google.com/drive/folders/138Jk13W2CWAOgLWgW9Z5tEmQBpkBkMQ4). When a source doc is updated, the corresponding skill is rebuilt to match.

See `HELIO-SKILL-BUILDING-CONTEXT.md` for the full conversion workflow and conventions.

## Current status

**v0.1.0 (2026-05-23) — initial buildout.** Marketplace skeleton plus the first four skills (`helio-app`, `helio-section-types`, `helio-ux-metrics`, `helio-asset-to-test`). 13 more skills + 1 optional master orchestrator planned.

See `CHANGELOG.md` for what's in this release and `SKILLS-CATALOG.md` for the full skill inventory.

## Related

- [Glare marketplace](../glare-marketplace) — the framework Helio supports
- [Helio docs site](https://helio.zurb.com)
- Helio CLI (`@zurb/helio-cli`)
- Helio MCP server (`https://mcp.helio.app/api/mcp`)

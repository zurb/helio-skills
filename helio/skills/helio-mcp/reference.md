# Helio MCP — Reference

**Skill:** `helio-mcp`
**Source:** Helio MCP v1.2
**Source last synced:** 2026-05-23

---

<!-- DERIVED FROM: 1MG34t7erUX6Lwy4OXfBAR8QludFabaLae359yLQg59Y — Helio MCP v1.2 -->

Helio MCP is the safe, standard way to put AI assistants on top of Glare data. It exposes the entire Helio research platform — every test, response, demographic filter, and AI assessment — to any client that speaks the Model Context Protocol. Claude Desktop, Cursor, Claude Code, custom agents. Twenty-six tools, one contract, auth handled at the protocol layer instead of being pasted into a prompt.

The web app is still there when you want it. The MCP server is there when your assistant should be the one driving.

## When to use MCP (vs CLI vs web)

Three ways to reach Helio. Pick the one that fits the work.

- **MCP** — when an AI assistant should drive the work interactively. Cohort comparisons in chat, concept assessments from a prompt, end-to-end test launches a model can run by itself. Best for exploratory research and ad-hoc analysis where the question evolves.
- **CLI** — when a script or a cron job should drive the work. Nightly pulls, CI checks that gate releases on sentiment, version-controlled test definitions next to the code they evaluate. Best for deterministic, repeatable, auditable runs.
- **Web app** — when a person should drive the work. Initial project setup, careful review of responses, designing tests with a teammate at a screen.

The same Helio API is underneath all three. The choice is about who's driving, not what's available.

## Requirements

- Node.js ≥ 18
- A Helio API token (or OAuth credentials) — generate one at [my.helio.app/account/organization](https://my.helio.app/account/organization)
- An MCP-aware client (Claude Desktop, Cursor, Claude Code, Claude.ai web, or a custom agent)

## Install

Helio MCP ships in two transports. Pick whichever fits your client.

### Local (stdio)

For Claude Desktop, Cursor, and Claude Code, add the server to your MCP config (`~/.cursor/mcp.json`, Claude Desktop settings, or equivalent):

```json
{
  "mcpServers": {
    "helio": {
      "command": "npx",
      "args": ["-y", "@zurb/helio-mcp"],
      "env": {
        "HELIO_API_ID": "your-api-id",
        "HELIO_API_KEY": "your-api-key"
      }
    }
  }
}
```

Restart your assistant. The helio server should appear in your MCP tool list with twenty-six tools available.

### Hosted (HTTP)

For clients that support remote MCP servers — Cursor, Claude.ai web, custom agents — skip the local install and point at the hosted endpoint:

```json
{
  "mcpServers": {
    "helio": {
      "url": "https://mcp.helio.app/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_HELIO_TOKEN"
      }
    }
  }
}
```

This uses the streamable-HTTP MCP transport. Older clients that don't support custom headers on remote servers will need the local stdio path instead.

## Quickstart

Confirm the server is connected by asking your assistant:

```
List my Helio projects.
```

You should get back a list of projects via the `list_projects` tool. From there, every Helio surface is one prompt away.

For the full tool catalog and example prompts, ask your assistant for the `analyze_test` prompt, or open the `helio://guide/analysis-workflow` resource.

## Capabilities

### Full API coverage

Every Helio surface is a tool call. Tests, responses, reports, AI assessments, segment comparison — all addressable in plain English from any MCP-aware assistant.

```
You: "List my Helio projects with 'onboarding' in the name."
→ list_projects(name: "onboarding")
```

### Demographic filters on every report

Slice any test report by `age`, `country`, `segment_id`, `sentiment`, and more — all as arrays, all on the same tool. Discover the available values for any test with one `include` flag.

```
get_test_report(
  test_id: "...",
  include: ["summary", "filter_options"],
  age: ["25-34", "35-44"],
  country: ["US", "CA"]
)
```

### Side-by-side segment comparison

`compare_segments` runs two filtered report calls in parallel and returns a structured diff — the kind of thing you'd otherwise script by hand against the API.

```
compare_segments(
  test_id: "...",
  segment_a: { age: ["18-24"] },
  segment_b: { age: ["55-64"] }
)
```

### One contract, two transports

The same tools, the same Zod-validated schemas, the same Helio API underneath, whether you're running locally over stdio or hitting the hosted endpoint. The server you point at is an implementation detail.

```shell
# local stdio (Claude Desktop, Cursor, Claude Code)
npx -y @zurb/helio-mcp

# hosted HTTP (any MCP client that speaks streamable HTTP)
curl https://mcp.helio.app/api/mcp \
    -H "Authorization: Bearer $HELIO_TOKEN"
```

## Workflows

### Compare cohorts without writing a query

You don't open a dashboard. You ask. The assistant pulls a filtered report for each segment and shows you where they diverged.

```
You: "On test abc-123, compare what 25–34s and 45–54s said about the new
      pricing page. Highlight where sentiment splits."

→ get_test_report(test_id: "abc-123", include: ["summary", "demographics"])
→ compare_segments(test_id: "abc-123",
      segment_a: { age: ["25-34"] },
      segment_b: { age: ["45-54"] })
```

### Score a new concept end to end

Drop in an asset, get back a structured AI assessment with scores, sections, and audience reactions — no UI, no project setup ceremony.

```
You: "Run an assessment on the attached onboarding mockup against our
      'New SaaS users' audience. Tell me where it loses people."

→ create_assessment(title: "Onboarding v3 — first read",
      concept: "...", asset_url: "...")
→ get_assessment(id: "...", include: ["scores", "sections", "audiences"])
```

### Re-run last quarter's study against a fresh audience

Pull the old test definition, clone it with new audience parameters, validate the spend, send it. Four tool calls, one prompt.

```
You: "Take test xyz-789 from last quarter, clone it with a new audience
      of 100 US/CA users aged 25–44, and launch it as 'Checkout · Q3 wave'."

→ get_test(id: "xyz-789")
→ create_test(name: "Checkout · Q3 wave", ..., target_audience_size: 100)
→ validate_test(id: "...")
→ send_test(id: "...")
```

## Where to go next

- `analyze_test` prompt — guided analysis workflow from your assistant
- `helio://guide/analysis-workflow` resource — full tool catalog and example prompts
- GitHub repo — source, issues, releases
- API reference — every endpoint the MCP server wraps

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Connecting Claude Desktop, Cursor, Claude Code, or a custom agent to Helio
- Choosing between the stdio and hosted-HTTP transports
- Hitting "older client doesn't support custom headers" with the hosted transport
- Asking what tools the MCP exposes (the 26-tool surface)
- Comparing the MCP surface to the CLI and web surfaces
- Stuck because their MCP-aware client doesn't see the helio server after config

For scripted (non-interactive) Helio access, route to `helio-cli`. For interactive web-app use, route to `helio-app`.

## Failure modes

- **Pasting API keys into chat instead of the MCP env block.** The whole point of MCP is auth at the protocol layer. If a token is in a prompt, the architecture isn't working.
- **Forgetting to restart the client.** New MCP servers need a client restart to appear.
- **Picking hosted HTTP for a client that doesn't support custom headers on remote servers.** Older clients fail silently. Drop to stdio.
- **Treating MCP as a replacement for CLI in pipelines.** MCP is built for interactive AI workflows. For deterministic scripted runs, use the CLI.

## Where to go next

- For scripted access: `helio-cli`
- For test design workflows the MCP might walk a user through: `helio-asset-to-test`
- For section type depth: `helio-section-types`
- For UX metrics: `helio-ux-metrics`
- For interpreting MCP-returned report data: `helio-reading-report`

<!-- /ADDED -->

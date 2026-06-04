# Helio CLI — Reference

**Skill:** `helio-cli`
**Source:** Helio CLI v1.2
**Source last synced:** 2026-05-23

---

<!-- DERIVED FROM: 1eNqJH7N-FC8sZn1_z5vFxopUS-UizuC7XDHv8xAwO60 — Helio CLI v1.2 -->

Helio CLI is the most robust way to script Glare data collection — by hand, by cron, or by AI agent. It puts the full Helio research platform behind a terminal, with structured JSON output, dry-run validation, predictable exit codes, and test definitions you can version-control alongside the code they evaluate. Anywhere automation or an AI agent needs to call into Glare, the CLI is the contract.

The web app is still there when you want it. The CLI is there when you need to move.

## When to use CLI (vs MCP vs web)

Three ways to reach Helio. Pick the one that fits the work.

- **CLI** — when a script, cron job, or pipeline should drive the work. Nightly pulls, CI checks that gate releases on sentiment, version-controlled test definitions next to the code they evaluate. Best for deterministic, repeatable, auditable runs.
- **MCP** — when an AI assistant should drive the work interactively. Cohort comparisons in chat, concept assessments from a prompt, end-to-end test launches a model can run by itself. Best for exploratory research and ad-hoc analysis where the question evolves.
- **Web app** — when a person should drive the work. Initial project setup, careful review of responses, designing tests with a teammate at a screen.

The same Helio API is underneath all three. The choice is about who's driving, not what's available.

## Requirements

- Node.js ≥ 22
- A Helio API token — generate one at [my.helio.app/account/organization](https://my.helio.app/account/organization)

## Install

```shell
npm install -g @zurb/helio-cli
```

## Authenticate

The CLI accepts credentials two ways. Pick whichever fits the environment.

### Interactive login

For local development:

```shell
helio-cli auth login
```

Credentials are stored in your local config file and reused on every subsequent command.

### Environment variables

For CI, sandboxes, containers, or anywhere a config file would be awkward:

```shell
export HELIO_API_ID=...
export HELIO_API_TOKEN=...
```

Once these are set, every command authenticates without touching disk. This is the recommended path for GitHub Actions, nightly crons, and any internal tool that runs on someone else's machine.

## Quickstart

Confirm auth and list what you already have:

```shell
helio-cli projects list
```

Launch your first test:

```shell
helio-cli tests create \
    --project-id <uuid> \
    --name "My first CLI test" \
    --intro "Quick feedback on a new idea." \
    --target-audience-size 50 \
    --ux-metrics sentiment
```

For a guided walkthrough and full command schemas:

```shell
helio-cli guide
```

## Working with output

### --output json on every command

Add `--output json` to any command and the result becomes a structured payload. Pipe it into `jq`, a data warehouse, a notebook, or a script — every command in the CLI honors the same flag, so your tooling only has to learn one contract.

```shell
helio-cli tests report <uuid> --output json | jq '.questions_summary'
```

### Structured errors and predictable exit codes

When `--output json` is set, errors come back as JSON too. Exit codes stay consistent across commands, so scripts can branch on them without parsing stderr.

```json
{ "error": "Unauthorized", "code": 401 }
```

## --dry-run before you spend

Validate a test payload before it actually runs. Nothing gets created, no incentives are charged, and you get back the same validation errors you would have hit on the real call.

```shell
helio-cli tests create --dry-run --project-id <uuid> --name "Test" --intro "Hi" \
    --target-audience-size 50 --questions '[...]'
```

Wire this into PR checks to catch broken test definitions before merge.

## Use cases

### For developers

You already live in a terminal. Now your research does too. Schedule nightly pulls, gate releases on sentiment thresholds, and version-control your test definitions next to the code they evaluate. Treat user feedback like any other production signal — observable, scriptable, and tied to a build.

Pull the latest report and post it to Slack on a cron:

```shell
helio-cli tests report $TEST_ID --output json \
    | jq '.ux_metrics' \
    | ./post-to-slack.sh
```

### For researchers and PMs

Save a test once, run it a hundred times. Re-run last quarter's onboarding study against a fresh audience — no clicking through screens, no re-typing instructions, no losing the wording you spent two weeks tuning. The test definition is a file you can share, edit in a PR, and replay forever.

Re-launch the onboarding study with a new audience:

```shell
helio-cli tests create \
    --project-id $PROJECT \
    --name "Onboarding · Q3 wave" \
    --intro "$(cat onboarding-intro.txt)" \
    --target-audience-size 100 \
    --ux-metrics sentiment loyalty
```

## Where to go next

- `helio-cli guide` — guided walkthrough and full command schemas
- GitHub repo — source, issues, releases
- API reference — every endpoint the CLI wraps
- Glare framework — the conceptual layer the CLI feeds data into

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-23 (skill-builder context) -->

## When to use

Reach for this skill when the user is:

- Installing or authenticating the CLI
- Looking up the right command for a task (`tests create`, `tests report`, `tests validate`, `tests send`, etc.)
- Scripting Helio inside cron, CI, or a build pipeline
- Piping CLI JSON output to jq, Slack, or a data warehouse
- Wiring `--dry-run` into PR checks
- Comparing the CLI surface to the MCP and web surfaces

For interactive AI workflows over Helio, route to `helio-mcp`. For the end-to-end build workflow (the 7-step arc that uses the CLI in step 7), route to `helio-asset-to-test`.

## Failure modes

- **Confusing the CLI with the MCP.** They share the underlying API but have different driver models. CLI = scripts. MCP = AI assistants.
- **Trying to upload assets via the CLI.** Not supported. Asset upload and hotspot drawing are UI-only today.
- **Forgetting `--dry-run` before a real launch.** Live `tests send` locks the structure and charges answers. Always dry-run first.
- **Pasting tokens into chat history.** Use env vars (`HELIO_API_ID`, `HELIO_API_TOKEN`) instead of inline credentials.
- **Using Node <22.** The CLI shebang resolves to whatever `node` is first in PATH. Run `nvm use 22` (or equivalent) before invoking if your default is older.

## Where to go next

- For AI assistants driving Helio: `helio-mcp`
- For the build workflow: `helio-asset-to-test`
- For section types: `helio-section-types`
- For UX metrics attachment: `helio-ux-metrics`
- For synthesizing report JSON into a Glare signal: `helio-reading-report`

<!-- /ADDED -->

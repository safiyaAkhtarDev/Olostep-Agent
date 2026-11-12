<!-- source: https://docs.olostep.com/cli/reference/jobs -->
# https://docs.olostep.com/cli/reference/jobs

Jobs and monitoring commands - Olostep Docs  

> Documentation Index
> -------------------
> 
> Fetch the complete documentation index at: [/llms.txt](/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

[Olostep Docs home page![light logo](https://mintcdn.com/olostep-58/294AdrknPYBl2RjK/logo/light.svg?fit=max&auto=format&n=294AdrknPYBl2RjK&q=85&s=fad5e5ee72a916722d9ad8279ee7186d)![dark logo](https://mintcdn.com/olostep-58/294AdrknPYBl2RjK/logo/dark.svg?fit=max&auto=format&n=294AdrknPYBl2RjK&q=85&s=dc0971e24a94b91a46d7dd802d74b94f)](https://www.olostep.com/)

English

Search...

⌘K

Search...

Navigation

Command reference

Jobs and monitoring commands

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Command reference

Jobs and monitoring commands
============================

Copy pageCopy page

crawl, batch, monitors, agents and logs: long-running work and its history.

Copy pageCopy page

These commands start work that runs for a while, and read its progress and results. Commands that list results page through them with `--limit` and `--cursor` (or `--offset`): pass the cursor from the previous result to get the next page.

[​

](#crawl)

crawl
----------------------

Crawl a website. `olostep crawl <url>` runs `olostep crawl create`. See [Crawls](/features/crawls).

### 

[​

](#olostep-crawl-list)

olostep crawl list

List your recent crawls.

    olostep crawl list [--limit integer] [--source text] [--offset integer] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--limit`

No

Page size.

`--source`

No

Source filter.

`--offset`

No

Zero-based offset from the previous page.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep crawl list --limit 10
    

### 

[​

](#olostep-crawl-get)

olostep crawl get

Show a crawl’s progress and settings.

    olostep crawl get [--json] [--fields a,b] <crawl_id>
    

**Arguments**

Argument

Description

`crawl_id`

Crawl id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep crawl get <crawl_id>
    

### 

[​

](#olostep-crawl-pages)

olostep crawl pages

Show a page of a crawl’s results. Each page has a Retrieve ID for `olostep content retrieve`.

    olostep crawl pages [--limit integer] [--cursor text] [--json] [--fields a,b] <crawl_id>
    

**Arguments**

Argument

Description

`crawl_id`

Crawl id.

**Flags**

Flag

Required

Description

`--limit`

No

Maximum records in this page.

`--cursor`

No

Opaque next cursor from a previous result.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep crawl pages <crawl_id>
    olostep crawl pages <crawl_id> --limit 100 --json
    

### 

[​

](#olostep-crawl-create)

olostep crawl create

Crawl a website, following links from a start URL up to a page limit.

Uses credits.

    olostep crawl create (--max-pages integer) [--depth integer] [--include-urls string]... [--exclude-urls string]... [--include-external] [--include-subdomain] [--follow-robots-txt] [--ignore-sitemap] [--scrape-options json] [--preview] [--start-url text] [--json] [--fields a,b] [--dry-run] [<start_url>]
    

Shorthand: `olostep crawl <url>`. **Arguments**

Argument

Description

`start_url`

An http(s) URL. Optional; you can pass it as a flag instead.

**Flags**

Flag

Required

Description

`-n`, `--max-pages`

Yes

Maximum pages to crawl.

`--depth`

No

Maximum link depth from the start URL.

`--include-urls`

No

URL patterns to include. Repeat the flag, or separate values with commas.

`--exclude-urls`

No

URL patterns to exclude. Repeat the flag, or separate values with commas.

`--include-external`

No

Follow external links.

`--include-subdomain`

No

Include subdomains.

`--follow-robots-txt`

No

Follow robots.txt.

`--ignore-sitemap`

No

Ignore the sitemap.

`--scrape-options`

No

Scrape options supported by the dashboard. JSON object, or `@file.json`.

`--start-url`

No

Same as the `start_url` argument.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep crawl https://docs.example.com -n 50
    olostep crawl https://example.com -n 200 --depth 3 --include-urls "/blog/**" --exclude-urls "/tag/**"
    

[​

](#batch)

batch
----------------------

Scrape many URLs in one job. See [Batches](/features/batches).

### 

[​

](#olostep-batch-list)

olostep batch list

List your recent batches.

    olostep batch list [--limit integer] [--source text] [--status text] [--search text] [--offset integer] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--limit`

No

Page size.

`--source`

No

Source filter.

`--status`

No

Batch status.

`--search`

No

Search filter.

`--offset`

No

Zero-based offset from the previous page.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep batch list --limit 20
    olostep batch list --status completed --json
    

### 

[​

](#olostep-batch-get)

olostep batch get

Show a batch’s progress and metadata.

    olostep batch get [--json] [--fields a,b] <batch_id>
    

**Arguments**

Argument

Description

`batch_id`

Batch id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep batch get <batch_id>
    

### 

[​

](#olostep-batch-items)

olostep batch items

Show a page of a batch’s items: each input URL and its result.

    olostep batch items [--limit integer] [--cursor text] [--json] [--fields a,b] <batch_id>
    

**Arguments**

Argument

Description

`batch_id`

Batch id.

**Flags**

Flag

Required

Description

`--limit`

No

Maximum records in this page.

`--cursor`

No

Opaque next cursor from a previous result.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep batch items <batch_id> --limit 50
    olostep batch items <batch_id> --cursor <next_cursor>
    

### 

[​

](#olostep-batch-create)

olostep batch create

Create a batch that scrapes a list of URLs. Each item has your own `custom_id` and a `url`. Up to 10,000 items.

Uses credits.

    olostep batch create (--items json) [--country text] [--parser json] [--metadata json] [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--items`

Yes

The URLs to scrape: a JSON list of `{"custom_id": "...", "url": "..."}`, or `@file.json`.

`--country`

No

Optional country.

`--parser`

No

A parser to run on each page: `{"id": "<parser_id>"}`, or `@file.json`.

`--metadata`

No

Batch metadata. JSON object, or `@file.json`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep batch create --items '[{"custom_id":"home","url":"https://example.com"},{"custom_id":"pricing","url":"https://example.com/pricing"}]'
    olostep batch create --items @urls.json --country US
    

### 

[​

](#olostep-batch-update)

olostep batch update

Replace a batch’s metadata.

    olostep batch update (--metadata json) [--preview] [--json] [--fields a,b] [--dry-run] <batch_id>
    

**Arguments**

Argument

Description

`batch_id`

Batch id.

**Flags**

Flag

Required

Description

`--metadata`

Yes

Metadata object. JSON object, or `@file.json`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep batch update <batch_id> --metadata '{"project":"q4-pricing"}'
    

### 

[​

](#olostep-batch-export)

olostep batch export

Start preparing a download of a batch’s results. Check it with `olostep batch export-status`.

    olostep batch export [--preview] [--json] [--fields a,b] [--dry-run] <batch_id>
    

**Arguments**

Argument

Description

`batch_id`

Batch id.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep batch export <batch_id>
    olostep batch export-status <batch_id>
    

### 

[​

](#olostep-batch-export-status)

olostep batch export-status

Check an export’s progress, and get its download URL when it is ready.

    olostep batch export-status [--json] [--fields a,b] <batch_id>
    

**Arguments**

Argument

Description

`batch_id`

Batch id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep batch export-status <batch_id>
    

[​

](#monitors)

monitors
----------------------------

Watch the web for changes on a schedule. See [Monitors](/features/monitors).

### 

[​

](#olostep-monitors-list)

olostep monitors list

List your monitors.

    olostep monitors list [--include-deleted] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--include-deleted`

No

Include deleted monitors.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors list
    

### 

[​

](#olostep-monitors-get)

olostep monitors get

Show a monitor’s settings and current state.

    olostep monitors get [--json] [--fields a,b] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors get <monitor_id>
    

### 

[​

](#olostep-monitors-create)

olostep monitors create

Create a monitor that watches the web for what you describe, on a schedule.

Uses credits.

    olostep monitors create (--query text) [--urls string]... (--frequency text) [--notification json] [--webhook json] [--source-policy json] [--output-schema json] [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--query`

Yes

What to monitor, in plain words.

`--urls`

No

Optional source URLs. Repeat the flag, or separate values with commas.

`--frequency`

Yes

How often to check, in words, such as `every day at 9am` (UTC).

`--notification`

No

Notification channels and event preferences. JSON object, or `@file.json`.

`--webhook`

No

Webhook configuration. JSON object, or `@file.json`.

`--source-policy`

No

Included/excluded URLs and domains. JSON object, or `@file.json`.

`--output-schema`

No

Expected structured output schema. JSON object, or `@file.json`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep monitors create --query "New pricing changes on example.com" --urls https://example.com/pricing --frequency "every day at 9am"
    

### 

[​

](#olostep-monitors-update)

olostep monitors update

Change a monitor’s frequency, notifications, webhook or metadata.

    olostep monitors update [--frequency text] [--notification json] [--webhook json] [--metadata json] [--preview] [--json] [--fields a,b] [--dry-run] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

**Flags**

Flag

Required

Description

`--frequency`

No

How often to check, in words, such as `every day at 9am` (UTC).

`--notification`

No

Notification channels and event preferences. JSON object, or `@file.json`.

`--webhook`

No

Webhook configuration. JSON object, or `@file.json`.

`--metadata`

No

Monitor metadata. JSON object, or `@file.json`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep monitors update <monitor_id> --frequency "every 20 minutes"
    

### 

[​

](#olostep-monitors-pause)

olostep monitors pause

Pause a monitor.

    olostep monitors pause [--preview] [--json] [--fields a,b] [--dry-run] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep monitors pause <monitor_id>
    

### 

[​

](#olostep-monitors-resume)

olostep monitors resume

Resume a paused monitor.

    olostep monitors resume [--preview] [--json] [--fields a,b] [--dry-run] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep monitors resume <monitor_id>
    

### 

[​

](#olostep-monitors-delete)

olostep monitors delete

Delete a monitor.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep monitors delete [--preview] [--json] [--fields a,b] [--dry-run] [--yes] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep monitors delete <monitor_id> --dry-run
    olostep monitors delete <monitor_id> --yes
    

### 

[​

](#olostep-monitors-events)

olostep monitors events

Show a page of a monitor’s run events.

    olostep monitors events [--limit integer] [--cursor text] [--status text] [--json] [--fields a,b] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

**Flags**

Flag

Required

Description

`--limit`

No

Maximum records in this page.

`--cursor`

No

Opaque next cursor from a previous result.

`--status`

No

Run-status filter.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors events <monitor_id> --limit 20
    

### 

[​

](#olostep-monitors-planning)

olostep monitors planning

Show a monitor’s plan and how it runs.

    olostep monitors planning [--json] [--fields a,b] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors planning <monitor_id>
    

### 

[​

](#olostep-monitors-run)

olostep monitors run

Run a monitor now, with its saved settings.

Uses credits.

    olostep monitors run (--monitor-id text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--monitor-id`

Yes

Monitor id.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep monitors run --monitor-id <monitor_id>
    

### 

[​

](#olostep-monitors-run-get)

olostep monitors run-get

Show one monitor run and its structured snapshot.

    olostep monitors run-get [--include-trace] [--json] [--fields a,b] <monitor_id> <run_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

`run_id`

Run id.

**Flags**

Flag

Required

Description

`--include-trace`

No

Include execution trace.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors run-get <monitor_id> <run_id>
    olostep monitors run-get <monitor_id> <run_id> --include-trace --json
    

### 

[​

](#olostep-monitors-logs)

olostep monitors logs

Show recent logs from a monitor’s runs.

    olostep monitors logs [--since integer] [--json] [--fields a,b] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

**Flags**

Flag

Required

Description

`--since`

No

Start time, in milliseconds since the Unix epoch.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors logs <monitor_id>
    

### 

[​

](#olostep-monitors-snapshot)

olostep monitors snapshot

Show the structured snapshot from one monitor run.

    olostep monitors snapshot [--json] [--fields a,b] <monitor_id> <run_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

`run_id`

Run id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors snapshot <monitor_id> <run_id> --json
    

### 

[​

](#olostep-monitors-share)

olostep monitors share

Get a monitor’s public share link. Does not change who can see it.

    olostep monitors share [--json] [--fields a,b] <monitor_id>
    

**Arguments**

Argument

Description

`monitor_id`

Monitor id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep monitors share <monitor_id>
    

[​

](#agents)

agents
------------------------

Run research agents. See [Agents](/features/agents).

### 

[​

](#olostep-agents-list)

olostep agents list

List the research agents available to your team.

    olostep agents list [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep agents list
    

### 

[​

](#olostep-agents-get)

olostep agents get

Show an agent’s details and default inputs.

    olostep agents get [--version text] [--json] [--fields a,b] <agent_id>
    

**Arguments**

Argument

Description

`agent_id`

Agent id.

**Flags**

Flag

Required

Description

`--version`

No

Version.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep agents get <agent_id>
    

### 

[​

](#olostep-agents-runs)

olostep agents runs

List a research agent’s runs.

    olostep agents runs [--json] [--fields a,b] <agent_id>
    

**Arguments**

Argument

Description

`agent_id`

Agent id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep agents runs <agent_id>
    

### 

[​

](#olostep-agents-run)

olostep agents run

Run a research agent with your input values.

Uses credits.

    olostep agents run [--version text] [--input-values json] [--preview] [--json] [--fields a,b] [--dry-run] <agent_id>
    

**Arguments**

Argument

Description

`agent_id`

Agent id.

**Flags**

Flag

Required

Description

`--version`

No

Agent version.

`--input-values`

No

Input values matching the agent’s declared schema. JSON object, or `@file.json`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep agents get <agent_id>
    olostep agents run <agent_id> --input-values @inputs.json
    

### 

[​

](#olostep-agents-run-get)

olostep agents run-get

Show a research agent run’s status and results.

    olostep agents run-get [--json] [--fields a,b] <agent_id> <run_id>
    

**Arguments**

Argument

Description

`agent_id`

Agent id.

`run_id`

Run id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep agents run-get <agent_id> <run_id>
    

### 

[​

](#olostep-agents-request)

olostep agents request

Ask the Olostep team to build a custom research agent for you.

    olostep agents request (--task text) [--model text] [--schedule text] [--budget text] [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--task`

Yes

Requested research workflow.

`--model`

No

Requested model.

`--schedule`

No

Requested schedule.

`--budget`

No

Requested budget.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep agents request --task "Every Monday, find new Series A fintech companies in Europe" --schedule "weekly"
    

[​

](#logs)

logs
--------------------

Read the requests your team made to the Olostep API.

### 

[​

](#olostep-logs-list)

olostep logs list

Show a page of your API request logs. Filter by status, endpoint and method.

    olostep logs list [--days 1|7|30|90] [--page integer] [--size integer] [--status text] [--endpoint text] [--method GET|POST|PUT|PATCH|DELETE] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--days`

No

Lookback window in days. One of: `1`, `7`, `30`, `90`.

`--page`

No

Page number, starting at 1.

`--size`

No

Page size.

`--status`

No

HTTP status filter.

`--endpoint`

No

Endpoint/path filter.

`--method`

No

HTTP method filter. One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep logs list --days 7
    olostep logs list --days 1 --status 429 --method POST
    

### 

[​

](#olostep-logs-export)

olostep logs export

Export your API request logs as JSON or CSV.

    olostep logs export [--days 1|7|30|90] [--format json|csv] [--max-pages integer] [--status text] [--endpoint text] [--method GET|POST|PUT|PATCH|DELETE] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--days`

No

Lookback window in days. One of: `1`, `7`, `30`, `90`.

`--format`

No

Export format. One of: `json`, `csv`.

`--max-pages`

No

Maximum pages of logs to export (1 to 100).

`--status`

No

HTTP status filter.

`--endpoint`

No

Endpoint or path filter.

`--method`

No

HTTP method filter. One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep logs export --days 30 --format csv
    

Was this page helpful?

YesNo
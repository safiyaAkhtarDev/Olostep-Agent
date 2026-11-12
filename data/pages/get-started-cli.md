<!-- source: https://docs.olostep.com/get-started/cli -->
# https://docs.olostep.com/get-started/cli

Olostep CLI - Olostep Docs  

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

Olostep CLI

Olostep CLI

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Olostep CLI

Olostep CLI
===========

Copy pageCopy page

Scrape websites, search the web and manage your Olostep account from the terminal.

Copy pageCopy page

The Olostep CLI is the `olostep` command. It runs Olostep from your terminal, from scripts, and from AI coding agents, signed in to the same Olostep account you use on the dashboard. With the CLI, you can:

*   [Scrape, search, map, crawl, research and extract](/cli/reference/web-data) web data.
*   [Run and inspect jobs](/cli/reference/jobs): batches, crawls, monitors, research agents and request logs.
*   [Manage your account](/cli/reference/account-billing): team, API keys, credits and billing.
*   [Ask the Olostep agent](/cli/reference/cli-commands#olostep-chat) for anything in plain words with `olostep chat`.
*   Print exact JSON with `--json` for scripts and [AI agents](/cli/ai-agents).

[​

](#install)

Install
--------------------------

The CLI needs [Node.js](https://nodejs.org) 20.19 or newer. On macOS or Linux, run:

    curl -fsSL https://cli.olostep.com | sh
    

The script installs the CLI into `~/.olostep` and puts `olostep` on your `PATH`. See [Install and update](/cli/install) for details, updating and uninstalling.

[​

](#quickstart)

Quickstart
--------------------------------

1

Sign in

    olostep login
    

Your browser opens the Olostep sign-in page. Sign in with your Olostep account and return to the terminal.

2

Check your account

    olostep whoami
    

Prints your account, team, plan and credit balance.

3

Scrape a page

    olostep scrape https://example.com -f markdown
    

4

Search the web

    olostep search "best hiking trails"
    

5

Get JSON for a script

    olostep credits balance --json
    

[​

](#common-commands)

Common commands
------------------------------------------

Task

Command

Scrape a page

`olostep scrape https://example.com -f markdown`

Search the web

`olostep search "query"`

List a site’s URLs

`olostep map https://example.com -n 20`

Crawl a site

`olostep crawl https://example.com -n 20`

Research a question

`olostep answer "Compare these products"`

Extract structured data

`olostep extract https://example.com -i "Extract product prices"`

Check your credits

`olostep credits balance`

Save an API key to `.env`

`olostep keys reveal <key> --write-env .env`

Ask the agent

`olostep chat "<request>"`

Find a command

`olostep help <words>`

Every command has help. Help works without signing in:

    olostep --help
    olostep scrape --help
    olostep scrape create --help
    

[​

](#learn-more)

Learn more
--------------------------------

Install and update
------------------

Requirements, updating, and uninstalling.

Authentication
--------------

Sign in, sign out, and tokens for CI.

Usage
-----

Output, `--json`, global flags, environment variables and exit codes.

Use with AI agents
------------------

How coding agents run the CLI, and the `skill` and `tools` commands.

To use Olostep from an MCP client such as Claude, Cursor or VS Code instead of a terminal, see [MCP server](/integrations/mcp-server).

Was this page helpful?

YesNo
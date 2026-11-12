<!-- source: https://docs.olostep.com/features/skills -->
# https://docs.olostep.com/features/skills

Skills - Olostep Docs  

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

Features

Skills

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Skills
======

Copy pageCopy page

Teach your AI coding agents how and when to use Olostep

Copy pageCopy page

A skill is a `SKILL.md` file your AI coding agent reads to know **what** Olostep can do and **when** to use it. Skills work with Claude Code, Cursor, Codex and any other agent that reads skill folders. Skills pair with the [Olostep CLI](/cli/overview) and the [MCP server](/integrations/mcp-server): those give the agent the live _tools_, the skills give it the _know-how_ for when and how to use them. There are two sets of skills:

*   **CLI skills**, served by the Olostep CLI with `olostep skill`.
*   **The hosted skill library** at [olostep.com/skills](https://www.olostep.com/skills/index.md).

[​

](#cli-skills)

CLI skills
--------------------------------

If your agent uses the [Olostep CLI](/cli/overview), give it the CLI’s skills. List them:

    olostep skill list
    

Skill

What it covers

`olostep-cli`

How to use the `olostep` command line: sign-in, `--json`, exit codes, and every command with its flags and JSON output schema.

`credit-usage`

Credit balances, plans, credit expiry and daily usage.

`dashboard`

Dashboard features: account, billing, team, API keys, logs, jobs, parsers, monitors, agents, support and integrations.

Write skills into your agent’s skills folder:

    olostep skill get olostep-cli credit-usage dashboard --write .claude/skills
    

Each skill is written to `<dir>/<name>/SKILL.md`, for example `.claude/skills/olostep-cli/SKILL.md`. Use your agent’s skills folder in place of `.claude/skills`. Read a skill without writing it:

    olostep skill get credit-usage
    olostep skill get credit-usage --json
    

`olostep-cli` is generated from the CLI’s commands, so run the command again after `olostep update` to refresh it. See [Use with AI agents](/cli/ai-agents) and [`olostep skill`](/cli/reference/cli-commands#olostep-skill).

[​

](#the-hosted-skill-library)

The hosted skill library
------------------------------------------------------------

Each skill below is hosted at `https://www.olostep.com/skills/<name>/SKILL.md`. An agent with web access can read the latest version directly. Browse them all at [olostep.com/skills](https://www.olostep.com/skills/index.md).

### 

[​

](#setup)

Setup

Skill

What it does

`setup`

Configure the Olostep MCP server so all other skills work

### 

[​

](#core-web-data)

Core web data

Skill

What it does

`scrape`

Turn one URL into clean markdown / HTML / JSON / text

`search`

Live web search — results, answers, and in-site URL discovery

`answers`

Cited, structured answers from live web data

`crawl`

Autonomously crawl a whole site

`map`

Discover every URL on a site

`batch`

Scrape many URLs in parallel

`extract-schema`

Scrape a page into structured JSON matching a schema

### 

[​

](#build-&-integrate)

Build & integrate

Skill

What it does

`integrate`

Add the Olostep SDK to a project

`docs-to-code`

Scrape API docs and write working code from them

`migrate-code`

Read a migration guide and update local code

### 

[​

](#research-&-debug)

Research & debug

Skill

What it does

`research`

Cited, comparative web research for a decision

`debug-error`

Look up an error message against live GitHub / SO / docs

### 

[​

](#add-a-hosted-skill-to-your-agent)

Add a hosted skill to your agent

Download it into your agent’s skills folder:

    mkdir -p .claude/skills/olostep-scrape
    curl -fsSL https://www.olostep.com/skills/scrape/SKILL.md -o .claude/skills/olostep-scrape/SKILL.md
    

Or tell your agent to fetch `https://www.olostep.com/skills/index.md` and pick the skills it needs.

[​

](#skill-format)

Skill format
------------------------------------

A skill is a folder with a `SKILL.md` file. The file starts with a YAML frontmatter block with `name` and `description`:

    ---
    name: my-skill
    description: What this skill does and when to use it
    ---
    
    # My Skill
    
    ...skill instructions here...
    

[​

](#related)

Related
--------------------------

*   [Olostep CLI](/cli/overview) — scrape, search and manage your account from the terminal
*   [Use with AI agents](/cli/ai-agents) — how coding agents run the CLI
*   [MCP Server](/integrations/mcp-server) — give your agent live Olostep tools

Was this page helpful?

YesNo
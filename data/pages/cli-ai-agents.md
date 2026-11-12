<!-- source: https://docs.olostep.com/cli/ai-agents -->
# https://docs.olostep.com/cli/ai-agents

Use the Olostep CLI with AI agents - Olostep Docs  

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

Use the Olostep CLI with AI agents

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Olostep CLI

Use the Olostep CLI with AI agents
==================================

Copy pageCopy page

How Claude Code, Cursor, Codex and other coding agents run the olostep command.

Copy pageCopy page

AI coding agents can run `olostep` like any other command. The CLI notices when a coding agent runs it and behaves for a program instead of a person.

[​

](#set-it-up)

Set it up
------------------------------

1

Install the CLI and sign in yourself

    curl -fsSL https://cli.olostep.com | sh
    olostep login
    

The agent uses your sign-in on this computer. In CI, set `OLOSTEP_TOKEN` instead. See [Authentication](/cli/authentication#scripts-ci-and-agents).

2

Give the agent the CLI guide

    olostep skill get olostep-cli --write .claude/skills
    

This writes `.claude/skills/olostep-cli/SKILL.md`: how to run the CLI, its exit codes, and every command with its flags and JSON output schema. Use your agent’s skills folder in place of `.claude/skills`.

3

Tell the agent to use --json

Agents should run commands with `--json` and read the JSON. The human output is for people and can change.

[​

](#how-the-cli-behaves-for-an-agent)

How the CLI behaves for an agent
----------------------------------------------------------------------------

The CLI treats a run as an agent’s when there is no terminal, or when one of `CLAUDECODE`, `CURSOR_AGENT`, `CODEX_CI` or `AI_AGENT` is set. Then:

*   `olostep` with no command prints help, not the welcome screen.
*   It never prompts. A command that needs sign-in exits with code `3` and tells the agent, on stderr, to run `olostep login` or set `OLOSTEP_TOKEN`.
*   A command that may delete or overwrite something exits with code `4` unless you pass `--yes`.
*   `olostep keys reveal` never prints a key. Use `--write-env <file>` to save it to a git-ignored env file.
*   `olostep chat` prints replies as plain text (`--plain` is on), and needs a message.
*   No update notice is printed.

Exit code

What the agent should do

`0`

Read the output.

`1`

Read the error on stderr.

`2`

Check the command with `olostep <command> --help`.

`3`

Ask the person to run `olostep login`.

`4`

Confirm with the person, then run again with `--yes`.

`5`

The server could not be reached. Retry later.

[​

](#find-the-right-command)

Find the right command
--------------------------------------------------------

    olostep help monitor pause        # commands whose name or description has every word
    olostep tools --search crawl      # tools that mention "crawl"
    olostep tools crawl_create        # one tool's full input and output schema
    

[​

](#olostep-skill)

`olostep skill`
----------------------------------------

Skills are short instructions for one kind of task. List them, read them, or write them into an agent’s skills folder:

    olostep skill list
    olostep skill get credit-usage
    olostep skill get olostep-cli dashboard --write .claude/skills
    olostep skill get olostep-cli --json
    

Skill

What it covers

`olostep-cli`

How to use the `olostep` command line. Generated from the CLI’s commands.

`credit-usage`

Credit balances, plans, credit expiry and daily usage.

`dashboard`

Dashboard features: account, billing, team, API keys, logs, jobs, parsers, monitors, agents, support and integrations.

`olostep skill list` shows the current list. See [`olostep skill`](/cli/reference/cli-commands#olostep-skill) for the flags.

[​

](#olostep-tools)

`olostep tools`
----------------------------------------

Every CLI command calls a tool on the Olostep server. `olostep tools` lists them, and marks the ones that change things:

    olostep tools
    olostep tools --json
    

[​

](#give-feedback)

Give feedback
--------------------------------------

When a command fails, is missing, or is confusing, the agent can tell the Olostep team. This works without signing in:

    olostep feedback --about tooling --message "crawl create rejected --depth 0"
    

Use `--about tooling` for the CLI itself and `--about product` for Olostep. Never include keys, passwords or personal details.

[​

](#mcp-instead-of-a-terminal)

MCP instead of a terminal
--------------------------------------------------------------

If your agent supports MCP, you can connect it to Olostep directly. See [MCP server](/integrations/mcp-server), or print the setup for your client:

    olostep integrations config --client claude_code
    

Was this page helpful?

YesNo
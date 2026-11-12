<!-- source: https://docs.olostep.com/cli/usage -->
# https://docs.olostep.com/cli/usage

Using the Olostep CLI - Olostep Docs  

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

Using the Olostep CLI

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Olostep CLI

Using the Olostep CLI
=====================

Copy pageCopy page

Command structure, output, JSON, global flags, environment variables and exit codes.

Copy pageCopy page

[​

](#command-structure)

Command structure
----------------------------------------------

    olostep <group> <command> [arguments] [flags]
    

Commands are grouped by what they work on, for example `olostep keys list` or `olostep monitors pause <monitor_id>`. The main web-data commands have a shorthand that runs their create command:

Shorthand

Runs

`olostep scrape <url>`

`olostep scrape create <url>`

`olostep search "<query>"`

`olostep search create "<query>"`

`olostep map <url>`

`olostep map create <url>`

`olostep crawl <url>`

`olostep crawl create <url>`

`olostep answer "<task>"`

`olostep answer create "<task>"`

`olostep extract <url>`

`olostep extract run <url>`

`olostep whoami` is the same as `olostep account info`.

[​

](#get-help)

Get help
----------------------------

    olostep --help                  # every command group
    olostep monitors --help         # the commands in a group
    olostep monitors create --help  # one command's arguments and flags
    olostep help export logs        # find commands by what they do
    

`olostep help <words>` lists the commands whose name or description contains every word. Help works without signing in.

[​

](#output)

Output
------------------------

The CLI picks its output for where it is going:

Where output goes

What you get

A terminal

Formatted Markdown: headings, tables and colors. Red is used only for errors.

A pipe or a file, or `NO_COLOR` is set

The same Markdown as plain text, with no colors.

Any destination, with `--json`

Exact JSON, for scripts and agents.

Errors go to stderr, so piping stdout never mixes them into your data. Colors are also off when `FORCE_COLOR=0` or `TERM=dumb` is set:

    NO_COLOR=1 olostep credits balance
    

### 

[​

](#json)

JSON

Add `--json` to any command that lists it in its help:

    olostep scrape https://example.com -f markdown --json
    

Commands that call Olostep return one JSON object:

    {
      "operation": "<operation>",
      "mode": "executed",
      "data": {},
      "warnings": []
    }
    

Field

Description

`operation`

The operation that ran.

`mode`

One of `read`, `executed`, `dry_run`, `browser` or `unavailable`.

`data`

The result. Its shape depends on the command.

`warnings`

Anything you should know about the result, such as partial data. Empty when there is nothing.

Parse the JSON, not the human-readable output. The human output can change between versions.

### 

[​

](#select-fields)

Select fields

`--fields` keeps only the fields you name. Separate fields with commas, and reach nested fields with a dot. Each field you pick is printed under the path you gave:

    olostep whoami --json --fields mode,warnings
    

    {"mode":"read","warnings":[]}
    

To pick nested fields, look at the full `--json` output once, then name them as `data.<field>`. `--fields` also works without `--json`, and shows only those fields in the table.

### 

[​

](#pipe-into-jq)

Pipe into jq

    olostep credits balance --json | jq '.data'
    olostep crawl pages <crawl_id> --json | jq '.data'
    

[​

](#passing-values)

Passing values
----------------------------------------

Kind of flag

How to pass it

Example

Text or number

After the flag

`--country US`, `--max-pages 50`

Repeatable list

Repeat the flag, or separate with commas

`-f markdown -f html` or `-f markdown,html`

JSON

Inline JSON, or `@` and a file path

`--metadata '{"project":"q3"}'` or `--items @urls.json`

Boolean

The flag alone

`--include-subdomain`

Fixed choice

One of the values shown in help

`--days 7`, `--format csv`

Positional URLs and queries can also be passed as flags, for example `olostep scrape create --url-to-scrape https://example.com` or `olostep search create --query "olostep"`.

[​

](#commands-that-change-things)

Commands that change things
------------------------------------------------------------------

Commands that create, change or delete something, or use credits, say so in their help. They support:

Flag

What it does

`--dry-run`

Shows the call the CLI would make, and sends nothing.

`--preview`

Asks Olostep to preview the change without making it.

`--yes`

Skips the confirmation. Commands that may delete or overwrite need `--yes` when there is no terminal to confirm in. Without it they exit with code `4`.

    olostep monitors delete <monitor_id> --dry-run
    olostep monitors delete <monitor_id> --yes
    

Commands that use credits, such as `scrape`, `search`, `map`, `crawl`, `answer`, `extract`, `batch create`, `monitors create`, `monitors run` and `agents run`, say `This consumes credits` or `consumes credits` in their help.

[​

](#global-flags)

Global flags
------------------------------------

These flags work on every command:

Flag

Description

`-h`, `--help`

Print help for the command and exit.

`--server <url>`

The Olostep CLI server to use. Defaults to `https://cli.olostep.com/mcp`.

`--token <token>`

Use this token instead of the saved sign-in. See [Authentication](/cli/authentication#scripts-ci-and-agents).

`--refresh-tools`

Fetch the current list of commands and their inputs from the server instead of the cached copy.

These flags work on every command that shows them in its help:

Flag

Description

`--json`

Print JSON: for scripts and agents.

`--fields <a,b>`

Only these fields, comma-separated (`a.b` for nested ones).

`--dry-run`

Show the call it would make, and send nothing.

`--preview`

Preview without changing anything.

`--yes`

Don’t ask first (needed without a terminal).

[​

](#environment-variables)

Environment variables
------------------------------------------------------

Variable

Description

`OLOSTEP_TOKEN`

A token to use instead of the saved sign-in. Same as `--token`.

`OLOSTEP_SERVER`

The server URL. Same as `--server`.

`OLOSTEP_HOME`

Where the install script puts the CLI. Defaults to `~/.olostep`. Must be an absolute path.

`NO_COLOR`

Any value turns colors off.

`XDG_CONFIG_HOME`

The CLI keeps its sign-in in `$XDG_CONFIG_HOME/olostep`. Defaults to `~/.config/olostep`.

`CI`

Turns off the update notice.

[​

](#exit-codes)

Exit codes
--------------------------------

Code

Meaning

`0`

Done.

`1`

The command failed. The message is on stderr.

`2`

Wrong command or arguments.

`3`

Sign-in needed. Run `olostep login` or set `OLOSTEP_TOKEN`.

`4`

The command needs `--yes`.

`5`

The server could not be reached.

Was this page helpful?

YesNo
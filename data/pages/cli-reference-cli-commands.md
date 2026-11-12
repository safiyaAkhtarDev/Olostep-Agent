<!-- source: https://docs.olostep.com/cli/reference/cli-commands -->
# https://docs.olostep.com/cli/reference/cli-commands

CLI commands - Olostep Docs  

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

CLI commands

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Command reference

CLI commands
============

Copy pageCopy page

login, logout, whoami, chat, help, tools, skill and update.

Copy pageCopy page

These commands work on the CLI itself: signing in, talking to the Olostep agent, finding commands, and updating.

[​

](#sign-in)

Sign-in
--------------------------

### 

[​

](#olostep-login)

olostep login

Sign in with your Olostep account. Your browser opens the Olostep sign-in page; after you sign in, the CLI saves the sign-in on this computer.

    olostep login
    

See [Authentication](/cli/authentication).

### 

[​

](#olostep-logout)

olostep logout

Sign out on this computer. Olostep revokes this computer’s connection, and the CLI forgets the saved sign-in.

    olostep logout
    

### 

[​

](#olostep-whoami)

olostep whoami

Show your signed-in Olostep account, your team, the team’s plan and its credit balance. Same as `olostep account info`.

    olostep whoami [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep whoami
    olostep whoami --json
    

[​

](#ask-the-agent)

Ask the agent
--------------------------------------

### 

[​

](#olostep-chat)

olostep chat

Ask the Olostep agent for anything in plain words, and it gets it done. With a message, it sends that message and prints the reply. Without one, it opens a conversation in your terminal until you type `/exit`.

    olostep chat ["<message>"] [--json] [--plain] [--new]
    

**Flags**

Flag

Required

Description

`--json`

No

Print the full response as JSON.

`--plain`

No

Print replies as written, and never open the full-screen view. On by default when a coding agent runs the CLI.

`--new`

No

Start a new conversation. Forgets this terminal’s saved conversation reference; the history the agent keeps for you stays.

    olostep chat "How many credits did we use last week?"
    olostep chat "Scrape https://example.com/pricing and list the plans"
    olostep chat --new
    

In the conversation view:

Key

Action

Enter

Send.

Shift+Enter, Alt+Enter, or `\` then Enter

New line.

Ctrl+O

Show or hide tool details.

PageUp, PageDown

Scroll.

Tab

Complete `/help`, `/details`, `/new` and `/exit`.

Escape

Stop waiting for the reply. Work the agent already accepted may still finish.

Ctrl+D

Leave, from an empty prompt.

`olostep chat` without a message needs a terminal. From a script, always pass the message; without one it exits with code `2`.

[​

](#find-commands)

Find commands
--------------------------------------

### 

[​

](#olostep-help)

olostep help

Find commands by what they do. Lists the commands whose name or description contains every word you give.

    olostep help <words>...
    

    olostep help invoices
    olostep help monitor pause
    

### 

[​

](#olostep-tools)

olostep tools

List every tool on the Olostep server, or print one tool’s full description: its input, output and hints. Tools that change something are marked `(changes things)`.

    olostep tools [--search text] [--json] [<tool>]
    

**Arguments**

Argument

Description

`tool`

One tool’s name. Optional.

**Flags**

Flag

Required

Description

`--search`

No

Only tools whose name or description contains this text.

`--json`

No

Print JSON.

    olostep tools --search monitor
    olostep tools scrape_create
    

### 

[​

](#olostep-skill)

olostep skill

List skills, or read the ones you name. A skill is a short set of instructions for one kind of task, written for AI agents. `olostep-cli` is the guide to the CLI itself, generated from its commands.

    olostep skill list
    olostep skill get <name> [name...] [--json] [--write <dir>]
    

**Arguments**

Argument

Description

`action/name...`

`list`, or `get` followed by one or more skill names. With no arguments, lists the skills.

**Flags**

Flag

Required

Description

`--json`

No

Print the skills you name as JSON records.

`--write`

No

Write each skill you name into this skills folder, as `<dir>/<name>/SKILL.md`.

    olostep skill list
    olostep skill get credit-usage
    olostep skill get olostep-cli --write .claude/skills
    

See [Use with AI agents](/cli/ai-agents#olostep-skill).

[​

](#update)

Update
------------------------

### 

[​

](#olostep-update)

olostep update

Update the CLI to its newest version. Runs `curl -fsSL https://cli.olostep.com | sh`.

    olostep update
    

See [Install and update](/cli/install#update).

Was this page helpful?

YesNo
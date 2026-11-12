<!-- source: https://docs.olostep.com/cli/reference/support-integrations -->
# https://docs.olostep.com/cli/reference/support-integrations

Support and integrations commands - Olostep Docs  

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

Support and integrations commands

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Command reference

Support and integrations commands
=================================

Copy pageCopy page

support, integrations, affiliate and feedback.

Copy pageCopy page

Get help, connect other tools to Olostep, and tell the team what you need.

[​

](#support)

support
--------------------------

### 

[​

](#olostep-support-resources)

olostep support resources

Get links to the Olostep docs, support, community and booking a meeting.

    olostep support resources [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep support resources
    

### 

[​

](#olostep-support-contact)

olostep support contact

Send a support request or feedback to the Olostep team.

    olostep support contact (--subject text) (--message text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--subject`

Yes

Subject.

`--message`

Yes

Support request or feedback.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep support contact --subject "Crawl stopped early" --message "Crawl <crawl_id> stopped after 12 of 50 pages."
    

[​

](#integrations)

integrations
------------------------------------

Set up MCP clients and request integrations. See [MCP server](/integrations/mcp-server).

### 

[​

](#olostep-integrations-list)

olostep integrations list

List Olostep integrations and their setup docs.

    olostep integrations list [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep integrations list
    

### 

[​

](#olostep-integrations-config)

olostep integrations config

Print the setup to connect an MCP client to Olostep with sign-in, without exposing any key.

    olostep integrations config (--client claude_code|cursor|codex|chatgpt|claude) [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--client`

Yes

MCP client. One of: `claude_code`, `cursor`, `codex`, `chatgpt`, `claude`.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep integrations config --client claude_code
    olostep integrations config --client cursor
    

### 

[​

](#olostep-integrations-request)

olostep integrations request

Ask the Olostep team for an integration.

    olostep integrations request (--name text) [--url text] [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--name`

Yes

Integration name.

`--url`

No

An http(s) URL.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep integrations request --name "Airtable" --url https://airtable.com
    

[​

](#affiliate)

affiliate
------------------------------

### 

[​

](#olostep-affiliate-dashboard)

olostep affiliate dashboard

Show your affiliate referral link, conversions and commissions.

    olostep affiliate dashboard [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep affiliate dashboard
    

[​

](#feedback)

feedback
----------------------------

### 

[​

](#olostep-feedback)

olostep feedback

Tell the Olostep team what went wrong, what is missing, or what could be better. Works without signing in. Never include keys, passwords or anyone’s personal details.

    olostep feedback (--about tooling|product) (--message text) [--tool text] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--about`

Yes

`tooling` for the CLI (or MCP server) itself, `product` for Olostep.

`--message`

Yes

What happened and what you expected.

`--tool`

No

The command or tool the feedback is about, if any.

Also accepts `--json`, `--fields` and `--dry-run`. See [Global flags](/cli/usage#global-flags).

    olostep feedback --about tooling --message "crawl pages printed no Retrieve IDs" --tool crawl_pages
    olostep feedback --about product --message "I need screenshots in batch results"
    

Was this page helpful?

YesNo
<!-- source: https://docs.olostep.com/cli/reference/web-data -->
# https://docs.olostep.com/cli/reference/web-data

Web data commands - Olostep Docs  

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

Web data commands

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Command reference

Web data commands
=================

Copy pageCopy page

scrape, search, map, answer, extract and content: get data from the web.

Copy pageCopy page

These commands get data from the web. Each one that fetches new data uses credits. To crawl a whole site, see [`olostep crawl`](/cli/reference/jobs#crawl). To scrape many URLs at once, see [`olostep batch`](/cli/reference/jobs#batch). All of them print Markdown in a terminal and JSON with `--json`. See [Output](/cli/usage#output).

[​

](#scrape)

scrape
------------------------

Scrape a single page. `olostep scrape <url>` runs `olostep scrape create`. See [Scrape](/features/scrapes) for the formats and options.

### 

[​

](#olostep-scrape-create)

olostep scrape create

Scrape a page into Markdown, HTML or structured data.

Uses credits.

    olostep scrape create [--formats string]... [--country text] [--wait integer] [--remove-css-selectors text] [--remove-class-names string]... [--parser json] [--llm-extract json] [--screen-size json] [--links-on-page json] [--metadata json] [--preview] [--url-to-scrape text] [--json] [--fields a,b] [--dry-run] [<url_to_scrape>]
    

Shorthand: `olostep scrape <url>`. **Arguments**

Argument

Description

`url_to_scrape`

An http(s) URL. Optional; you can pass it as a flag instead.

**Flags**

Flag

Required

Description

`-f`, `--formats`

No

Output formats, such as `markdown` or `html`. Repeat the flag, or separate values with commas.

`-c`, `--country`

No

Country.

`--wait`

No

Milliseconds to wait before scraping (0 to 60000).

`--remove-css-selectors`

No

CSS selectors to remove from the page.

`--remove-class-names`

No

Classes to remove. Repeat the flag, or separate values with commas.

`--parser`

No

Parser configuration. JSON object, or `@file.json`.

`--llm-extract`

No

LLM extraction configuration. JSON object, or `@file.json`.

`--screen-size`

No

Screenshot viewport. JSON object, or `@file.json`.

`--links-on-page`

No

Link extraction options. JSON object, or `@file.json`.

`--metadata`

No

Request metadata. JSON object, or `@file.json`.

`--url-to-scrape`

No

Same as the `url_to_scrape` argument.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep scrape https://example.com -f markdown
    olostep scrape https://example.com -f markdown,html -c US --wait 2000
    olostep scrape https://example.com -f markdown --json
    

### 

[​

](#olostep-scrape-get)

olostep scrape get

Show a previous scrape by its id.

    olostep scrape get [--json] [--fields a,b] <scrape_id>
    

**Arguments**

Argument

Description

`scrape_id`

Scrape id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep scrape get <scrape_id>
    

[​

](#search)

search
------------------------

Search the web. `olostep search "<query>"` runs `olostep search create`. See [Search](/features/search).

### 

[​

](#olostep-search-create)

olostep search create

Search the web.

Uses credits.

    olostep search create [--options json] [--preview] [--query text] [--json] [--fields a,b] [--dry-run] [<query>]
    

Shorthand: `olostep search "<query>"`. **Arguments**

Argument

Description

`query`

Search query. Optional; you can pass it as a flag instead.

**Flags**

Flag

Required

Description

`--options`

No

Additional public search API options. JSON object, or `@file.json`.

`--query`

No

Same as the `query` argument.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep search "best hiking trails"
    olostep search "olostep web scraping api" --json
    

### 

[​

](#olostep-search-get)

olostep search get

Show a previous search by its id.

    olostep search get [--json] [--fields a,b] <search_id>
    

**Arguments**

Argument

Description

`search_id`

Search id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep search get <search_id>
    

[​

](#map)

map
------------------

List a website’s URLs. `olostep map <url>` runs `olostep map create`. See [Maps](/features/maps).

### 

[​

](#olostep-map-create)

olostep map create

Discover a website’s URLs.

Uses credits.

    olostep map create [--include-urls string]... [--exclude-urls string]... [--search text] [--top-n integer] [--include-subdomain] [--preview] [--url text] [--json] [--fields a,b] [--dry-run] [<url>]
    

Shorthand: `olostep map <url>`. **Arguments**

Argument

Description

`url`

An http(s) URL. Optional; you can pass it as a flag instead.

**Flags**

Flag

Required

Description

`--include-urls`

No

Include URL patterns. Repeat the flag, or separate values with commas.

`--exclude-urls`

No

Exclude URL patterns. Repeat the flag, or separate values with commas.

`--search`

No

Rank URLs by how well they match this query.

`-n`, `--top-n`

No

Maximum number of URLs to return.

`--include-subdomain`

No

Include subdomains.

`--url`

No

Same as the `url` argument.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep map https://example.com -n 20
    olostep map https://example.com --search "pricing" -n 10
    

[​

](#answer)

answer
------------------------

Research a question on the web. `olostep answer "<task>"` runs `olostep answer create`. See [Answers](/features/answers).

### 

[​

](#olostep-answer-create)

olostep answer create

Research a question or task on the web, and get an answer or JSON in the shape you ask for.

Uses credits.

    olostep answer create [--schema json] [--options json] [--preview] [--task text] [--json] [--fields a,b] [--dry-run] [<task>]
    

Shorthand: `olostep answer "<task>"`. **Arguments**

Argument

Description

`task`

Research task. Optional; you can pass it as a flag instead.

**Flags**

Flag

Required

Description

`--schema`

No

Requested JSON schema. JSON object, or `@file.json`.

`--options`

No

Additional answer options. JSON object, or `@file.json`.

`--task`

No

Same as the `task` argument.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep answer "What does Olostep do?"
    olostep answer "What is the latest book by J.K. Rowling?" --schema '{"book_title":"","author":"","release_date":""}' --json
    

### 

[​

](#olostep-answer-get)

olostep answer get

Show a previous answer by its id.

    olostep answer get [--json] [--fields a,b] <answer_id>
    

**Arguments**

Argument

Description

`answer_id`

Answer id.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep answer get <answer_id>
    

[​

](#extract)

extract
--------------------------

Pull structured data out of a page. `olostep extract <url>` runs `olostep extract run`. See [LLM extraction](/features/structured-content/llm-extraction).

### 

[​

](#olostep-extract-run)

olostep extract run

Extract structured data from a page with an instruction in plain words.

Uses credits.

    olostep extract run (--instruction text) [--schema json] [--preview] [--url text] [--json] [--fields a,b] [--dry-run] [<url>]
    

Shorthand: `olostep extract <url>`. **Arguments**

Argument

Description

`url`

An http(s) URL. Optional; you can pass it as a flag instead.

**Flags**

Flag

Required

Description

`-i`, `--instruction`

Yes

What to extract.

`--schema`

No

Optional JSON schema. JSON object, or `@file.json`.

`--url`

No

Same as the `url` argument.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep extract https://example.com -i "Extract product prices"
    olostep extract https://example.com/team -i "List each person's name and role" --json
    

[​

](#content)

content
--------------------------

Read pages you already scraped or crawled, without scraping them again.

### 

[​

](#olostep-content-retrieve)

olostep content retrieve

Get the stored HTML, Markdown or JSON of a page you already scraped or crawled. The `retrieve_id` comes from `scrape create`, `scrape get`, `crawl pages` (the Retrieve ID column) or `batch items`. A scrape id such as `scrape_abc123` works too.

    olostep content retrieve [--formats string]... [--json] [--fields a,b] <retrieve_id>
    

**Arguments**

Argument

Description

`retrieve_id`

The page’s retrieve\_id, such as abc123 (or its scrape id, scrape\_abc123).

**Flags**

Flag

Required

Description

`-f`, `--formats`

No

Formats to return: `html`, `markdown` or `json`. Leave out for every stored format. Repeat the flag, or separate values with commas.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep content retrieve <retrieve_id> -f markdown
    olostep content retrieve scrape_abc123 -f html,markdown --json
    

Was this page helpful?

YesNo
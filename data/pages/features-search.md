<!-- source: https://docs.olostep.com/features/search -->
# https://docs.olostep.com/features/search

Search API - Olostep Docs  

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

Search API

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Search API
==========

Copy pageCopy page

Search the web with natural language and get structured links — Olostep’s AI search API.

Copy pageCopy page

The Olostep `/v1/searches` endpoint lets you search the web with a natural language query and get back a deduplicated list of relevant links with titles and descriptions.

*   Send a query in plain English
*   Get back structured links from across the web
*   Optionally scrape every returned URL in one round-trip and embed `markdown_content` / `html_content` directly into the response
*   Filter by domain, control the result count, and bound the scraping wallclock
*   Search for [people and companies](#people-and-company-search) instead of web pages, with a query in any language or explicit filters

It will search for the query semantically across the web and return results. For API details, see the [Search Endpoint API Reference](/api-reference/searches/create).

[​

](#installation)

Installation
------------------------------------

Python

Node

cURL

Node (API)

Python (API)

    pip install olostep
    

    npm install olostep
    

    # curl is available by default on macOS, Linux, and Windows
    

    npm install node-fetch
    

    pip install requests
    

[​

](#basic-usage)

Basic usage
----------------------------------

Send a natural language query and receive a list of relevant links.

Python

Node

cURL

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    search = client.searches.create("Best Answer Engine Optimization startups")
    
    print(search.id, len(search.links))
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const search = await client.searches.create('Best Answer Engine Optimization startups')
    
    console.log(search.id, search.links.length)
    

    curl -s -X POST "https://api.olostep.com/v1/searches" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Best Answer Engine Optimization startups"
      }'
    

    const res = await fetch('https://api.olostep.com/v1/searches', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: 'Best Answer Engine Optimization startups'
      })
    })
    console.log(await res.json())
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/searches"
    payload = {
      "query": "Best Answer Engine Optimization startups"
    }
    headers = {"Authorization": "Bearer <YOUR_API_KEY>", "Content-Type": "application/json"}
    
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

[​

](#request-parameters)

Request parameters
------------------------------------------------

Field

Type

Required

Default

Description

`query`

string

yes\*

—

The search query in natural language. \*Optional for `people` and `companies` searches when `category.parameters` is sent.

`category`

object

no

`{ "type": "any" }`

What to search: `any` (web), `people` or `companies`. See [People and company search](#people-and-company-search).

`limit`

integer

no

`12`

Maximum number of links to return after deduplication. Must be between `1` and `25`.

`include_domains`

string\[\]

no

`[]`

Restrict results to these domains. Bare hosts only — leading `http(s)://` and trailing slashes are stripped automatically.

`exclude_domains`

string\[\]

no

`[]`

Exclude results from these domains. Bare hosts only — leading `http(s)://` and trailing slashes are stripped automatically.

`scrape_options`

object

no

—

When provided, every returned link is also scraped and its content embedded in the response. See [scrape\_options](#scrape-options) below.

`fast_mode`

boolean

no

`false`

Request a direct, low-latency search using your query verbatim. Default mode performs a broader search pass for wider result coverage.

### 

[​

](#limiting-the-number-of-results)

Limiting the number of results

    {
      "query": "What's going on with OpenAI's Sora shutting down?",
      "limit": 5
    }
    

### 

[​

](#filtering-by-domain)

Filtering by domain

`include_domains` narrows results to a whitelist; `exclude_domains` filters out unwanted sources. They can be combined.

    {
      "query": "OpenAI Sora shutdown analysis",
      "include_domains": ["nytimes.com", "wsj.com", "bbc.com"],
      "exclude_domains": ["pinterest.com"]
    }
    

[​

](#scrape_options)

scrape\_options
-----------------------------------------

Pass `scrape_options` to scrape every returned URL in parallel and embed the rendered content directly on each link. This saves a round-trip per result vs. calling `/v1/searches` and `/v1/scrapes` separately.

    {
      "query": "What's going on with OpenAI's Sora shutting down?",
      "limit": 10,
      "scrape_options": {
        "formats": ["markdown"],
        "remove_css_selectors": "default",
        "timeout": 25
      }
    }
    

Field

Type

Default

Description

`formats`

string\[\]

`["markdown"]`

Output formats to attach to each link. For `/v1/searches`, only `"html"` and `"markdown"` are supported. Pass `["html", "markdown"]` to receive both.

`remove_css_selectors`

string

`"default"`

Forwarded to `/v1/scrapes`. `"default"` strips nav/footer/script/style/svg/dialog noise. Use `"none"` to disable, or pass a JSON-stringified array of selectors to remove.

`timeout`

integer

`25`

Wallclock budget in **seconds** for the entire scrape phase. Must be between `1` and `60`. After this elapses, the search returns immediately — content fields will be `null` for any links that hadn’t finished.

### 

[​

](#behavior)

Behavior

*   All links are scraped **in parallel**. The `timeout` bounds the whole batch, not each individual link.
*   Per-link scrape failures (network errors, individual page timeouts) leave that link’s `markdown_content` / `html_content` as `null` while other links return normally.
*   If the global `timeout` elapses before all scrapes finish, the search responds immediately with the links it has — already-completed scrapes keep their content; in-flight ones come back with `null` content.
*   For `reddit.com/.../comments/...` URLs, the request is automatically routed through the `@olostep/reddit-post` parser and the structured JSON is rendered into clean markdown + basic HTML
*   If the combined inline content exceeds 9MB, content fields are nulled, `result.size_exceeded` is set to `true`, and you can fetch the full payload from `result.json_hosted_url`.

### 

[​

](#example-with-scraping)

Example with scraping

Python

Node

cURL

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    search = client.searches.create(
        query="What's going on with OpenAI's Sora shutting down?",
        limit=5,
        scrape_options={"formats": ["markdown"], "timeout": 25},
    )
    
    for link in search.links:
        print(link["url"], "—", len(link.get("markdown_content") or ""), "chars")
    

    import Olostep, { Format } from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const search = await client.searches.create({
      query: "What's going on with OpenAI's Sora shutting down?",
      limit: 5,
      scrapeOptions: {
        formats: [Format.MARKDOWN],
        timeout: 25
      }
    })
    
    for (const link of search.links) {
      console.log(link.url, '—', (link.markdown_content || '').length, 'chars')
    }
    

    curl -s -X POST "https://api.olostep.com/v1/searches" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "What'"'"'s going on with OpenAI'"'"'s Sora shutting down?",
        "limit": 5,
        "scrape_options": {
          "formats": ["markdown"],
          "timeout": 25
        }
      }'
    

    const res = await fetch('https://api.olostep.com/v1/searches', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: "What's going on with OpenAI's Sora shutting down?",
        limit: 5,
        scrape_options: {
          formats: ['markdown'],
          timeout: 25
        }
      })
    })
    const data = await res.json()
    for (const link of data.result.links) {
      console.log(link.url, '—', (link.markdown_content || '').length, 'chars')
    }
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/searches"
    payload = {
      "query": "What's going on with OpenAI's Sora shutting down?",
      "limit": 5,
      "scrape_options": {
        "formats": ["markdown"],
        "timeout": 25
      }
    }
    headers = {"Authorization": "Bearer <YOUR_API_KEY>", "Content-Type": "application/json"}
    
    response = requests.post(endpoint, json=payload, headers=headers)
    data = response.json()
    for link in data["result"]["links"]:
      print(link["url"], "—", len(link.get("markdown_content") or ""), "chars")
    

[​

](#response)

Response
----------------------------

You will receive a `search` object in response. The `search` object contains an `id`, your original `query`, `credits_consumed`, and a `result` with a list of `links`.

    {
      "id": "search_9bi0sbj9xa",
      "object": "search",
      "created": 1760327323,
      "metadata": {},
      "query": "What's going on with OpenAI's Sora shutting down?",
      "credits_consumed": 10,
      "result": {
        "json_content": "...",
        "json_hosted_url": "https://olostep-storage.s3.us-east-1.amazonaws.com/search_9bi0sbj9xa.json",
        "size_exceeded": false,
        "credits_consumed": 10,
        "links": [
          {
            "url": "https://www.bbc.com/news/articles/c3w3e467ewqo",
            "title": "OpenAI to shut down Sora video platform",
            "description": "OpenAI says it will discontinue its Sora app...",
            "markdown_content": "# OpenAI to shut down Sora video platform\n\nOpenAI says it will discontinue..."
          },
          {
            "url": "https://www.reddit.com/r/OutOfTheLoop/comments/1s2u847/whats_going_on_with_openais_sora_shutting_down/",
            "title": "What's going on with OpenAI's Sora shutting down?",
            "description": "Reddit thread discussing the shutdown.",
            "markdown_content": "# What's going on with OpenAI's Sora shutting down?\n\n*r/OutOfTheLoop · u/rm-minus-r · 1mo ago*\n\n..."
          }
        ]
      }
    }
    

Each link in `result.links` contains:

Field

Type

Description

`url`

string

The URL of the search result.

`title`

string

The title of the result page.

`description`

string

A short snippet describing the result.

`markdown_content`

string

Markdown content of the page. Only present when `scrape_options.formats` includes `"markdown"`. `null` if the scrape failed, was empty, or hit the global timeout.

`html_content`

string

HTML content of the page. Only present when `scrape_options.formats` includes `"html"`. `null` on failure/timeout.

The full result is also available as a hosted JSON file at `result.json_hosted_url` — useful when `result.size_exceeded` is `true`.

[​

](#retrieving-a-past-search)

Retrieving a past search
------------------------------------------------------------

`GET /v1/searches/{search_id}` returns whatever was persisted at search time, including any scraped content. It’s a pure idempotent read — no re-scraping, no re-billing. Older searches without `scrape_options` simply have no per-link content fields.

Python

Node

cURL

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    search = client.searches.get(search_id="search_9bi0sbj9xa")
    print(search.id, len(search.links))
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const search = await client.searches.get('search_9bi0sbj9xa')
    console.log(search.id, search.links.length)
    

    curl -s "https://api.olostep.com/v1/searches/search_9bi0sbj9xa" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

See [Get Search](/api-reference/searches/get) for full details.

[​

](#people-and-company-search)

People and company search
--------------------------------------------------------------

Set `category.type` to `people` or `companies` to search professional profiles or companies instead of web pages. `category` defaults to `{ "type": "any" }`, the web search described above. You can describe what you are looking for in `query`, in any language, pass explicit filters in `category.parameters`, or both. The query is translated into the same filters; when both are sent, the fields in `category.parameters` win.

    {
      "query": "Senior software engineers in Berlin with more than 5 years of experience",
      "category": { "type": "people" }
    }
    

    {
      "category": {
        "type": "companies",
        "parameters": { "location": "Berlin", "size": 200 }
      }
    }
    

With `people` or `companies`, `limit`, `include_domains`, `exclude_domains` and `scrape_options` are ignored (they are still validated). Each search returns up to 25 results.

### 

[​

](#parameters)

Parameters

Field

Type

Applies to

Description

`name`

string

`people`, `companies`

Person name or company name.

`job_title`

string

`people`

Job title, e.g. `"Senior Software Engineer"`.

`location`

string

`people`, `companies`

City, region or country. For companies, the location of the company.

`years_of_experience`

integer

`people`

Years of experience, `0` or more.

`current_employer`

string

`people`

Company the person currently works at.

`size`

integer

`companies`

Company headcount, `1` or more.

`revenue_usd`

integer

`companies`

Company revenue in USD, `0` or more.

String fields must be non-empty. Fields of the other type are ignored.

### 

[​

](#example)

Example

cURL

Node (API)

Python (API)

    curl -s -X POST "https://api.olostep.com/v1/searches" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Senior software engineers in Berlin with more than 5 years of experience",
        "category": { "type": "people" }
      }'
    

    const res = await fetch('https://api.olostep.com/v1/searches', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: 'Senior software engineers in Berlin with more than 5 years of experience',
        category: { type: 'people' }
      })
    })
    const data = await res.json()
    console.log(data.result.parameters, data.result.people.length)
    

    import requests
    
    endpoint = "https://api.olostep.com/v1/searches"
    payload = {
      "category": {
        "type": "companies",
        "parameters": {"location": "Berlin", "size": 200}
      }
    }
    headers = {"Authorization": "Bearer <YOUR_API_KEY>", "Content-Type": "application/json"}
    
    data = requests.post(endpoint, json=payload, headers=headers).json()
    for company in data["result"]["companies"]:
      print(company.get("name"), company.get("linkedin_url"))
    

### 

[​

](#response-2)

Response

The response has the same `search` envelope as a web search. Instead of `result.links`, `result` contains:

Field

Type

Description

`result.people`

object\[\]

Profiles found by a `people` search. Each has a `linkedin_url`, plus fields such as `full_name`, `title`, `location` and `company`.

`result.companies`

object\[\]

Companies found by a `companies` search. Each has a `linkedin_url`, plus fields such as `name`.

`result.parameters`

object

The filters the search ran with: those read from `query`, overridden by `category.parameters`.

    {
      "id": "search_…",
      "object": "search",
      "credits_consumed": 40,
      "result": {
        "people": [
          {
            "full_name": "…",
            "title": "Senior Software Engineer",
            "location": "Berlin, Berlin, Germany",
            "company": { "name": "…", "linkedin_url": "…" },
            "linkedin_url": "https://www.linkedin.com/in/…"
          }
        ],
        "parameters": { "job_title": "Senior Software Engineer", "location": "Berlin", "years_of_experience": 6 },
        "json_content": "…",
        "json_hosted_url": "…",
        "size_exceeded": false,
        "credits_consumed": 40
      }
    }
    

Check `result.parameters` to see how your `query` was read. `GET /v1/searches/{search_id}` returns the same shape.

### 

[​

](#errors)

Errors

People and company searches use the standard Olostep error envelope:

Case

HTTP

`code`

Invalid `category` or parameters, neither `query` nor `category.parameters` sent, or a `query` with no usable filter

`400`

`validation_error` (fields in `metadata.errors`)

Search could not be completed, or `query` could not be translated

`502`

`upstream_error`

Search temporarily overloaded

`503`

`upstream_error`

Failed searches are not charged. Retry `502` and `503` later.

[​

](#storage)

Storage
--------------------------

Stored files for a search are kept for 7 days by default. Pass a `storage` object on `POST /v1/searches` to keep them longer, or indefinitely. The setting covers the hosted JSON file at `result.json_hosted_url` and, when `scrape_options` is set, the content scraped for each link.

Parameter

Type

Default

Description

`storage.expires_in`

`string`

`7d`

How long to keep the stored files. One of `7d`, `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` (indefinite).

Omitting `storage`, or sending `storage` without `expires_in`, uses `7d`. Both the create response and `GET /v1/searches/{search_id}` include the value in effect:

    "storage": { "expires_in": "30d" }
    

cURL

    curl -s -X POST "https://api.olostep.com/v1/searches" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "best open source vector databases",
        "storage": { "expires_in": "30d" }
      }'
    

An invalid value returns `400`:

    {
      "type": "invalid_request_error",
      "message": "Invalid storage.expires_in. Allowed values: \"7d\", \"10d\", \"30d\", \"60d\", \"90d\", \"180d\", \"365d\", \"never\".",
      "code": "invalid_storage_expires_in"
    }
    

[​

](#pricing)

Pricing
--------------------------

Each search costs **5 credits** for the search itself. When `scrape_options` is provided, each scraped page is billed at the standard `/v1/scrapes` rate (typically 1 credit per page; some parsers cost more). The total is returned in `credits_consumed`. Examples:

Request

`credits_consumed`

Search only

`5`

Search + 5 scraped pages (1 credit each)

`10`

`people` or `companies` search with results

`40`

`people` or `companies` search with no results

`0`

A `people` or `companies` search costs a flat **40 credits** when it returns at least one result, and nothing otherwise.

Was this page helpful?

YesNo
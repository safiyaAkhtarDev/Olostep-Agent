<!-- source: https://docs.olostep.com/features/scrapes -->
# https://docs.olostep.com/features/scrapes

Olostep Docs - Scrape endpoint  

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

Scrape

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Scrape
======

Copy pageCopy page

Turn any URL into LLM-ready Markdown, HTML, screenshots, PDFs, or structured JSON.

Copy pageCopy page

Through the Olostep `/v1/scrapes` endpoint you can extract LLM-friendly Markdown, HTML, text, screenshots, or structured JSON from any URL in real time.

*   Outputs clean markdown, structured data, screenshots, or html
*   Extract JSON through [Parsers](/features/structured-content/parsers) or [LLM extraction](/features/structured-content/llm-extraction)
*   Handles dynamic content: js-rendered sites, login flows via actions, PDFs
*   Control how long results are retained with the `storage` parameter

For API details see the [Scrape Endpoint API Reference](/api-reference/scrapes/create).

[​

](#scraping-a-url)

Scraping a URL
----------------------------------------

Use the `/v1/scrapes` endpoint to scrape a single URL and choose output formats.

### 

[​

](#installation)

Installation

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
    

### 

[​

](#usage)

Usage

You can use the endpoint to scrape a single URL and choose output formats. The mandatory parameters are `url_to_scrape` and `formats`. Some other common parameters are `wait_before_scraping` (in milliseconds), `remove_css_selectors` (default, none, or an array of selectors), and `country`.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    result = client.scrapes.create(
        url_to_scrape="https://en.wikipedia.org/wiki/Alexander_the_Great",
        formats=["markdown", "html"],
    )
    
    print(result.markdown_content)
    print(result.html_content)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const result = await client.scrapes.create({
      url: 'https://en.wikipedia.org/wiki/Alexander_the_Great',
      formats: ['markdown', 'html'],
    })
    
    console.log(result.markdown_content)
    console.log(result.html_content)
    

    curl -s -X POST "https://api.olostep.com/v1/scrapes" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url_to_scrape": "https://en.wikipedia.org/wiki/Alexander_the_Great",
        "formats": ["markdown", "html"]
      }'
    

    olostep scrape "https://en.wikipedia.org/wiki/Alexander_the_Great" \
      --formats markdown,html
    

    const endpoint = 'https://api.olostep.com/v1/scrapes'
    const payload = {
      url_to_scrape: 'https://en.wikipedia.org/wiki/Alexander_the_Great',
      formats: ['markdown', 'html']
    }
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    console.log(data)
    

    import requests
    import json
    
    endpoint = "https://api.olostep.com/v1/scrapes"
    payload = {
        "url_to_scrape": "https://en.wikipedia.org/wiki/Alexander_the_Great",
        "formats": ["markdown", "html"]
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

### 

[​

](#response)

Response

The API returns a `scrape` object in response. The `scrape` has a few properties like `id` and `result`. The `result` object has the following fields (according to the `formats` parameter some might be null):

*   `html_content`: the HTML content of the page. Pass `formats: ["html"]` to get this.
*   `markdown_content`: the MD content of the page. Pass `formats: ["markdown"]` to get this.
*   `text_content`: the text content of the page. Pass `formats: ["text"]` to get this.
*   `json_content`: the JSON content of the page. Pass `formats: ["json"]` to get this and also provide a `parser` or `llm_extract` parameter.
*   `screenshot_hosted_url`: the hosted URL of the screenshot.
*   `html_hosted_url`: the hosted URL of the HTML content
*   `markdown_hosted_url`: the hosted URL of the Markdown content
*   `json_hosted_url`: the hosted URL of the JSON content
*   `text_hosted_url`: the hosted URL of the text content
*   `links_on_page`: the links on the page
*   `page_metadata`: the metadata of the page

    {
      "id": "scrape_6h89o8u1kt",
      "object": "scrape",
      "created": 1745673871,
      "metadata": {},
      "retrieve_id": "6h89o8u1kt",
      "url_to_scrape": "https://en.wikipedia.org/wiki/Alexander_the_Great",
      "result": {
        "html_content": "<html...",
        "markdown_content": "## Alexander the Great...",
        "text_content": null,
        "json_content": null,
        "screenshot_hosted_url": null,
        "html_hosted_url": "https://olostep-storage.s3.us-east-1.amazonaws.com/text_6h89o8u1kt.txt",
        "markdown_hosted_url": "https://olostep-storage.s3.us-east-1.amazonaws.com/markDown_6h89o8u1kt.txt",
        "json_hosted_url": null,
        "text_hosted_url": null,
        "links_on_page": [],
        "page_metadata": { "status_code": 200, "title": "" }
      }
    }
    

[​

](#caching)

Caching
--------------------------

To optimize speed, Olostep provides an optional shared caching layer for HTML, Markdown, text, and parsed JSON results.

### 

[​

](#how-it-works)

How it works

When a scrape is requested, Olostep checks if a matching scrape already exists with the same parameters. If a fresh enough match is found, the content is served instantly from Olostep’s storage without launching a new browser scrape.

*   **Shared Cache:** The cache is shared globally. If another request scraped the exact same URL with the exact same configuration within your freshness window, you benefit from the speedup.
*   **Post-processing is still live:** Operations like `llm_extract` and `links_on_page` filters are run _on-the-fly_ on top of the cached document. You only cache the core page retrieval, keeping your structured extractions dynamic.

### 

[​

](#freshness-and-max_age)

Freshness and `max_age`

By default, the production API always performs a live scrape to guarantee real-time accuracy. You can opt-in to caching using the `max_age` parameter.

Parameter

Type

Default

Description

`max_age`

`integer`

`0`

Acceptable content age in **seconds**. If a cached copy exists and is newer than `max_age` seconds, it is served from the cache.

*   **Default API Behavior (`max_age: 0`):** Every API request triggers a fresh scrape.
*   **Default Playground Behavior:** In the dashboard playground, `max_age` defaults to 24 hours (`86400` seconds).
*   **Maximum Age:** The cache has a hard limit of **7 days** (`604800` seconds). Any `max_age` requested above this limit will fallback to a maximum of 7 days.

### 

[​

](#usage-examples)

Usage Examples

Python

Node

cURL

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    # Opt-in to caching: Accept results up to 1 day (86400 seconds) old
    result = client.scrapes.create(
        url_to_scrape="https://example.com",
        formats=["markdown"],
        max_age=86400
    )
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    // Opt-in to caching: Accept results up to 1 day (86400 seconds) old
    const result = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['markdown'],
      maxAge: 86400,
    })
    

    # Opt-in to caching: Accept results up to 1 hour (3600 seconds) old
    curl -X POST "https://api.olostep.com/v1/scrapes" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url_to_scrape": "https://example.com",
        "formats": ["markdown"],
        "max_age": 3600
      }'
    

    const endpoint = 'https://api.olostep.com/v1/scrapes'
    const payload = {
      url_to_scrape: 'https://example.com',
      formats: ['markdown'],
      max_age: 86400 // Accept results up to 1 day (86400 seconds) old
    }
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    console.log(data)
    

    import requests
    import json
    
    endpoint = "https://api.olostep.com/v1/scrapes"
    payload = {
        "url_to_scrape": "https://example.com",
        "formats": ["markdown"],
        "max_age": 86400 # Accept results up to 1 day (86400 seconds) old
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

### 

[​

](#when-is-the-cache-skipped)

When is the cache skipped?

The cache is automatically bypassed (forcing a live scrape) when your request needs:

*   **Interactive sessions:** Requests using `session_id` or loading a custom browser `context`.
*   **Screenshots:** Any request that includes `screenshot` in formats or sets the screenshot option bypasses the cache.
*   **Special file types:** Binary file downloads or raw PDF rendering.
*   **Debugging & Network:** Capturing `network_calls` or using async parser jobs.

[​

](#storage)

Storage
--------------------------

Scrape results are kept for about 7 days by default. Pass a `storage` object to keep a result longer — or indefinitely — so you can fetch it again later. The result, its hosted URLs, and `GET /v1/scrapes/{scrape_id}` stay available for that window. `max_age` controls whether a new request can reuse a cached page. `storage.expires_in` controls how long this scrape’s result stays available. See [Caching](/features/scrapes#caching) for `max_age`. `storage` is available on all plans for `POST /v1/scrapes`.

Parameter

Type

Default

Description

`storage.expires_in`

`string`

about 7 days (when `storage` is omitted)

How long to keep the result. One of `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` (indefinite).

### 

[​

](#usage-2)

Usage

Python

Node

cURL

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    # Keep this scrape for 90 days
    result = client.scrapes.create(
        url_to_scrape="https://example.com/product/reviews",
        formats=["markdown"],
        storage={"expires_in": "90d"},
    )
    
    print(result.id)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    // Keep this scrape for 90 days
    const result = await client.scrapes.create({
      url: 'https://example.com/product/reviews',
      formats: ['markdown'],
      storage: { expires_in: '90d' },
    })
    
    console.log(result.id)
    

    curl -X POST "https://api.olostep.com/v1/scrapes" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url_to_scrape": "https://example.com/product/reviews",
        "formats": ["markdown"],
        "storage": { "expires_in": "90d" }
      }'
    

    const endpoint = 'https://api.olostep.com/v1/scrapes'
    const payload = {
      url_to_scrape: 'https://example.com/product/reviews',
      formats: ['markdown'],
      storage: { expires_in: '90d' }
    }
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    const data = await res.json()
    console.log(data)
    

    import requests
    import json
    
    endpoint = "https://api.olostep.com/v1/scrapes"
    payload = {
        "url_to_scrape": "https://example.com/product/reviews",
        "formats": ["markdown"],
        "storage": {"expires_in": "90d"}
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

[​

](#extracting-links)

Extracting links
--------------------------------------------

Pass a `links_on_page` object in the request to collect the links found on the page. All links are returned as absolute URLs.

    "links_on_page": {
      "include_links": ["/blog/*"],
      "exclude_links": ["*.pdf"],
      "query_to_order_links_by": "pricing"
    }
    

*   `include_links` / `exclude_links`: glob patterns matched against each link’s URL **path**.
*   `query_to_order_links_by`: re-orders the returned links by relevance to this text.

Glob patterns match path segments. A single `*` does **not** cross `/`, so `"/blog/*"` matches `"/blog/post-1"` but **not** the index `"/blog"` itself — and it never matches `"/blog?tag=x"` because query strings are not part of the path. To include the index too, use `"/blog*"` or `"{/blog,/blog/**}"`.

[​

](#scrape-formats)

Scrape Formats
----------------------------------------

Choose one or more output formats via `formats`:

*   `markdown`: LLM-friendly markdown
*   `html`: cleaned HTML
*   `text`: plain text
*   `json`: structured output (via parser or llm\_extract)
*   `raw_pdf`: raw PDF bytes extracted to hosted URL
*   `screenshot`: set via actions to capture a screenshot and return a hosted URL

Output keys are returned inside `result` as `*_content` fields and a `*_hosted_url` as well.

[​

](#extract-structured-data)

Extract structured data
----------------------------------------------------------

You can extract structured JSON in two ways: using Parsers or LLM extraction.

### 

[​

](#using-a-parser-recommended-for-scale)

Using a Parser (recommended for scale)

Define `formats: ["json"]` and provide a parser `id`.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    result = client.scrapes.create(
        url_to_scrape="https://www.google.com/search?q=alexander+the+great&gl=us&hl=en",
        formats=["json"],
        parser="@olostep/google-search",
    )
    
    print(result.json_content)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const result = await client.scrapes.create({
      url: 'https://www.google.com/search?q=alexander+the+great&gl=us&hl=en',
      formats: ['json'],
      parser: '@olostep/google-search',
    })
    
    console.log(result.json_content)
    

    curl -s -X POST "https://api.olostep.com/v1/scrapes" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url_to_scrape": "https://www.google.com/search?q=alexander+the+great&gl=us&hl=en",
        "formats": ["json"],
        "parser": {"id": "@olostep/google-search"}
      }'
    

    olostep scrape "https://www.google.com/search?q=alexander+the+great&gl=us&hl=en" \
      --formats json \
      --payload-json '{"parser":{"id":"@olostep/google-search"}}'
    

    const res = await fetch('https://api.olostep.com/v1/scrapes', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url_to_scrape: 'https://www.google.com/search?q=alexander+the+great&gl=us&hl=en',
        formats: ['json'],
        parser: { id: '@olostep/google-search' }
      })
    })
    console.log(await res.json())
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/scrapes"
    payload = {
      "url_to_scrape": "https://www.google.com/search?q=alexander+the+great&gl=us&hl=en",
      "formats": ["json"],
      "parser": { 
        "id": "@olostep/google-search" 
      }
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>", 
        "Content-Type": "application/json"
    }
    
    res = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(res.json(), indent=2))
    

Olostep has a few pre-built parsers for [popular websites](https://www.olostep.com/store) but you can also create your own parsers through the dashboard or ask our team to do it for you. Parsers are self-healing and will update themselves to the latest version of the website.

### 

[​

](#using-llm-extraction-schema-and/or-prompt)

Using LLM extraction (schema and/or prompt)

Provide `llm_extract` with a JSON Schema (`schema`) and/or a natural language instruction (`prompt`). You can pass both parameters, but if both are provided, `schema` takes precedence. Instead, if you just pass a `prompt`, the LLM will extract the data based on the prompt and will decide the data structure on its own.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import LLMExtract, Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    result = client.scrapes.create(
        url_to_scrape="https://www.berklee.edu/events/stefano-marchese-friends",
        formats=["markdown", "json"],
        llm_extract=LLMExtract(
            schema={
                "type": "object",
                "properties": {
                    "event": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "date": {"type": "string"},
                            "description": {"type": "string"},
                            "venue": {"type": "string"},
                            "address": {"type": "string"},
                            "start_time": {"type": "string"},
                        },
                    }
                },
            }
        ),
    )
    
    print(result.json_content)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const result = await client.scrapes.create({
      url: 'https://www.berklee.edu/events/stefano-marchese-friends',
      formats: ['markdown', 'json'],
      llmExtract: {
        schema: {
          type: 'object',
          properties: {
            event: {
              type: 'object',
              properties: {
                title: { type: 'string' },
                date: { type: 'string' },
                description: { type: 'string' },
                venue: { type: 'string' },
                address: { type: 'string' },
                start_time: { type: 'string' },
              },
            },
          },
        },
      },
    })
    
    console.log(result.json_content)
    

    curl -s -X POST "https://api.olostep.com/v1/scrapes" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url_to_scrape": "https://www.berklee.edu/events/stefano-marchese-friends",
        "formats": ["json"],
        "llm_extract": {
          "prompt": "Extract the event title, date, description, venue, address, and start time from the page."
        }
      }'
    

    olostep scrape "https://www.berklee.edu/events/stefano-marchese-friends" \
      --formats json \
      --payload-json '{"llm_extract":{"prompt":"Extract the event title, date, description, venue, address, and start time from the page."}}'
    

    const res = await fetch('https://api.olostep.com/v1/scrapes', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url_to_scrape: 'https://www.berklee.edu/events/stefano-marchese-friends',
        formats: ['json'],
        llm_extract: {
          prompt: 'Extract the event title, date, description, venue, address, and start time from the page.'
        }
      })
    })
    console.log(await res.json())
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/scrapes"
    payload = {
      "url_to_scrape": "https://www.berklee.edu/events/stefano-marchese-friends",
      "formats": ["markdown", "json"],
      "llm_extract": {
        "schema": {
          "type": "object",
          "properties": {
            "event": {
              "type": "object",
              "properties": {
                "title": {"type": "string"},
                "date": {"type": "string"},
                "description": {"type": "string"},
                "venue": {"type": "string"},
                "address": {"type": "string"},
                "start_time": {"type": "string"}
              }
            }
          }
        }
      }
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    res = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(res.json(), indent=2))
    

Note: in the Python SDK, `result.json_content` is already a dict. In the Node SDK and the raw API it is a JSON string, so parse it (`JSON.parse` / `json.loads`) if you need an object. **Pricing:** `llm_extract` costs 10 credits per scrape. To lower the cost, you can bring your own API keys or enable usage-based pricing. Contact [info@olostep.com](mailto:info@olostep.com) to get access.

[​

](#extract-links-on-the-page)

Extract links on the page
--------------------------------------------------------------

With the `links_on_page` option, you can extract all the links present on the page you scrape. It accepts the following parameters to help filter and order the extracted links:

*   `absolute_links` (boolean, default: `true`): When true, it returns complete URLs (e.g., `https://example.com/page`) instead of relative paths (e.g., `/page`).
*   `query_to_order_links_by` (string): Orders the returned links by their similarity to the provided query text, prioritizing the most relevant matches first.
*   `include_links` (array of strings): Filter extracted links using glob patterns. Use patterns like `*.pdf` to match file extensions, `/blog/*` for specific paths, or full URLs like `https://example.com/*`. Supports wildcards (`*`), character classes (`[a-z]`), and alternation (`{pattern1,pattern2}`).
*   `exclude_links` (array of strings): Exclude specific links using glob patterns, following the same syntax as `include_links`.

[​

](#interacting-with-the-page-with-actions)

Interacting with the page with Actions
----------------------------------------------------------------------------------------

Perform actions before scraping to interact with dynamic sites. Supported actions:

*   `wait` with `milliseconds`
*   `click` with `selector`
*   `fill_input` with `selector` and `value`
*   `scroll` with `direction` and `amount`

It is often useful to use `wait` before/after other actions to allow the page to load.

### 

[​

](#example)

Example

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import FillInputAction, Olostep, WaitAction
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    result = client.scrapes.create(
        url_to_scrape="https://example.com/login",
        formats=["markdown"],
        actions=[
            FillInputAction(selector="input[type=email]", value="john@example.com"),
            WaitAction(milliseconds=500),
            FillInputAction(selector="input[type=password]", value="secret"),
            {"type": "click", "selector": "button[type=\"submit\"]"},
            WaitAction(milliseconds=1500),
        ],
    )
    
    print(result.markdown_content)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const result = await client.scrapes.create({
      url: 'https://example.com/login',
      formats: ['markdown'],
      actions: [
        { type: 'fill_input', selector: 'input[type=email]', value: 'john@example.com' },
        { type: 'wait', milliseconds: 500 },
        { type: 'fill_input', selector: 'input[type=password]', value: 'secret' },
        { type: 'click', selector: 'button[type="submit"]' },
        { type: 'wait', milliseconds: 1500 },
      ],
    })
    
    console.log(result.markdown_content)
    

    curl -s -X POST "https://api.olostep.com/v1/scrapes" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url_to_scrape": "https://example.com/login",
        "formats": ["markdown"],
        "actions": [
          { "type": "fill_input", "selector": "input[type=email]", "value": "john@example.com" },
          { "type": "wait", "milliseconds": 500 },
          { "type": "fill_input", "selector": "input[type=password]", "value": "secret" },
          { "type": "click", "selector": "button[type=\"submit\"]" },
          { "type": "wait", "milliseconds": 1500 }
        ]
      }'
    

    # For complex options like actions, use --payload-file with a JSON file
    olostep scrape "https://example.com/login" \
      --formats markdown \
      --payload-file actions.json
    
    # Where actions.json contains:
    # {
    #   "actions": [
    #     {"type": "fill_input", "selector": "input[type=email]", "value": "john@example.com"},
    #     {"type": "wait", "milliseconds": 500},
    #     {"type": "fill_input", "selector": "input[type=password]", "value": "secret"},
    #     {"type": "click", "selector": "button[type=\"submit\"]"},
    #     {"type": "wait", "milliseconds": 1500}
    #   ]
    # }
    

    const res = await fetch('https://api.olostep.com/v1/scrapes', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url_to_scrape: 'https://example.com/login',
        formats: ['markdown'],
        actions: [
          { type: 'fill_input', selector: 'input[type=email]', value: 'john@example.com' },
          { type: 'wait', milliseconds: 500 },
          { type: 'fill_input', selector: 'input[type=password]', value: 'secret' },
          { type: 'click', selector: 'button[type="submit"]' },
          { type: 'wait', milliseconds: 1500 }
        ]
      })
    })
    console.log(await res.json())
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/scrapes"
    payload = {
      "url_to_scrape": "https://example.com/login",
      "formats": ["markdown"],
      "actions": [
        {"type": "fill_input", "selector": "input[type=email]", "value": "john@example.com"},
        {"type": "wait", "milliseconds": 500},
        {"type": "fill_input", "selector": "input[type=password]", "value": "secret"},
        {"type": "click", "selector": "button[type=\"submit\"]"},
        {"type": "wait", "milliseconds": 1500}
      ]
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>", 
        "Content-Type": "application/json"
    }
    res = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(res.json(), indent=2))
    

The response will include any requested formats (e.g., `markdown_content`).

[​

](#use-cases)

Use Cases
------------------------------

Below are a few practical applications of customers using the `/scrapes` endpoint.

### 

[​

](#content-analysis-&-research)

Content Analysis & Research

*   **Competitive Analysis**: Extract product details, pricing, and features from competitor websites
*   **Market Research**: Analyze landing pages, product descriptions, and customer testimonials
*   **Academic Research**: Gather specific data from scientific publications or research portals
*   **Legal Documentation**: Extract case studies, regulations, or legal precedents from official websites

### 

[​

](#e-commerce-&-retail)

E-commerce & Retail

*   **Dynamic Pricing Strategies**: Get real-time product pricing from competing stores
*   **Product Information Management**: Extract detailed specifications and descriptions
*   **Stock/Inventory Monitoring**: Check product availability at other retailers
*   **Review Analysis**: Gather consumer feedback and sentiment for specific products

### 

[​

](#marketing-&-content-creation)

Marketing & Content Creation

*   **Content Curation**: Extract relevant articles and blog posts for newsletters
*   **SEO Analysis**: Examine competitors’ keyword usage, meta descriptions, and page structure
*   **Lead Generation**: Extract contact information from business directories or company pages
*   **Influencer Research**: Gather engagement metrics and content styles from influencer profiles
*   **Personalised Social Media generation**: Create AI-powered social media marketing by analyzing customers websites

### 

[​

](#data-applications)

Data Applications

*   **AI Training Data Collection**: Gather specific examples for machine learning models
*   **Custom Knowledge Base Building**: Extract documentation or instructions from software sites
*   **Historical Data Archives**: Preserve website content at specific points in time
*   **Structured Data Extraction**: Transform web content into formatted datasets for analysis

### 

[​

](#monitoring-&-alerts)

Monitoring & Alerts

*   **Regulatory Compliance Monitoring**: Track changes to legal or regulatory websites
*   **Crisis Management**: Monitor news sites for mentions of specific events or organizations
*   **Event Tracking**: Extract details about upcoming events from venue or organizer websites
*   **Service Status Monitoring**: Check service status pages for specific platforms or tools

### 

[​

](#publishing-&-media)

Publishing & Media

*   **News Aggregation**: Extract breaking news from official sources
*   **Media Monitoring**: Track specific topics across news sites
*   **Content Verification**: Extract information to fact-check claims or statements
*   **Multimedia Extraction**: Gather embedded videos, images, or audio for media libraries

### 

[​

](#financial-applications)

Financial Applications

*   **Investment Research**: Extract financial statements or annual reports from company websites
*   **Economic Indicators**: Gather economic data from government or financial institution websites
*   **Cryptocurrency Data**: Extract real-time pricing and market cap information
*   **Financial News Analysis**: Monitor financial news sites for specific market signals

### 

[​

](#technical-applications)

Technical Applications

*   **API Documentation Extraction**: Gather technical documentation for reference
*   **Integration Testing**: Extract website elements to verify third-party integrations
*   **Accessibility Testing**: Analyze website structure for compliance with accessibility standards
*   **Web Archive Creation**: Capture full website content for historical preservation

### 

[​

](#integration-scenarios)

Integration Scenarios

*   **CRM Systems**: Enhance customer profiles with data from company websites or Linkedin
*   **Content Management Systems**: Import relevant external content
*   **Business Intelligence Tools**: Supplement internal data with external market information
*   **Project Management Software**: Extract specifications or requirements from client websites
*   **Custom Dashboards**: Display extracted data alongside internal metrics

[​

](#error-handling)

Error Handling
----------------------------------------

All errors follow a shared envelope shape. Check `error.type` and `error.code` to branch programmatically:

    {
      "id": "error_abc123",
      "object": "error",
      "created": 1745673871,
      "url": "https://example.com",
      "metadata": {},
      "error": {
        "type": "...",
        "code": "...",
        "message": "..."
      }
    }
    

HTTP

`error.type`

`error.code`

Meaning

400

`invalid_request_error`

`dns_resolution_failed`

The domain does not exist or the URL has a typo.

400

`invalid_request_error`

`invalid_url`

The URL is malformed.

502

`invalid_request_error`

`tls_error`

The website has an invalid or incompatible TLS/SSL certificate. `error.detail` carries the low-level SSL code.

504

`request_timeout`

`scrape_poll_timeout`

The scrape did not finish within the ~55-second wait budget.

### 

[​

](#dns-failure-400)

DNS failure (400)

The domain does not resolve. Check the URL for typos.

    {
      "error": {
        "type": "invalid_request_error",
        "code": "dns_resolution_failed",
        "message": "The URL contains a typo, or the domain does not exist."
      }
    }
    

### 

[​

](#tls/ssl-error-502)

TLS/SSL error (502)

The target website has a broken or incompatible HTTPS configuration. `error.detail` provides the specific SSL error code for diagnostics; `error.code` is always `tls_error`.

    {
      "error": {
        "type": "invalid_request_error",
        "code": "tls_error",
        "detail": "err_ssl_tlsv1_alert_internal_error",
        "message": "The website closed or rejected the TLS handshake. The server may be misconfigured or use an unsupported SSL/TLS version."
      }
    }
    

### 

[​

](#request-timeout-504)

Request timeout (504)

The scrape did not complete within the wait budget. The page may be slow, bot-protected, or temporarily unavailable. This response is safe to retry.

    {
      "error": {
        "type": "request_timeout",
        "code": "scrape_poll_timeout",
        "message": "Request timed out while waiting for scrape result. The page may be slow, blocked for our fetchers, or temporarily unavailable."
      }
    }
    

[​

](#pricing)

Pricing
--------------------------

Scrape costs 1 credit by default. If you also pass [parsers](/features/structured-content/parsers), the costs vary by parser (1-5 credits). If you use [LLM extract](/features/structured-content/llm-extraction), it costs 10 credits.

Was this page helpful?

YesNo
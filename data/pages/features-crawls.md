<!-- source: https://docs.olostep.com/features/crawls -->
# https://docs.olostep.com/features/crawls

Crawl - Olostep Docs  

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

Crawl

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Crawl
=====

Copy pageCopy page

Crawl a URL and get the content from all subpages

Copy pageCopy page

Through the Olostep `/v1/crawls` endpoint you can crawl a website and get the content from all the pages.

*   Crawl a website and get the content from all subpages (or limit the depth of the crawl)
*   Use special patterns to crawl specific pages (e.g. `/blog/**`)
*   Pass a `webhook_url` to get notified when the crawl is completed
*   Search query to only find specific pages and sort by relevance

For API details see the [Crawl Endpoint API Reference](/api-reference/crawls/create).

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

](#start-a-crawl)

Start a crawl
--------------------------------------

Provide the starting URL, include/exclude URL globs, and `max_pages`. Optional: `max_depth`, `include_external`, `include_subdomain`, `search_query`, `top_n`, `webhook_url`, `timeout`.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    crawl = client.crawls.create(
        start_url="https://olostep.com",
        max_pages=100,
        include_urls=["/**"],
        exclude_urls=["/collections/**"],
        include_external=False,
    )
    
    print(crawl.id, crawl.status)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const crawl = await client.crawls.create({
      url: 'https://olostep.com',
      maxPages: 100,
      includeUrls: ['/**'],
      excludeUrls: ['/collections/**'],
      includeExternal: false,
    })
    
    console.log(crawl.id, crawl.status)
    

    curl -s -X POST "https://api.olostep.com/v1/crawls" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "start_url": "https://olostep.com",
        "max_pages": 100,
        "include_urls": ["/**"],
        "exclude_urls": ["/collections/**"]
      }'
    

    olostep crawl "https://olostep.com" \
      --max-pages 100 \
      --include-url "/**" \
      --exclude-url "/collections/**" \
      --formats markdown,html
    

    const API_URL = 'https://api.olostep.com'
    const res = await fetch(`${API_URL}/v1/crawls`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        start_url: 'https://olostep.com',
        max_pages: 100,
        include_urls: ['/**'],
        exclude_urls: ['/collections/**']
      })
    })
    console.log(await res.json())
    

    import time, json
    
    API_URL = 'https://api.olostep.com'
    API_KEY = '<YOUR_API_KEY>'
    HEADERS = { 
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}' 
    }
    
    data = {
      "start_url": "https://olostep.com",
      "max_pages": 100,
      "include_urls": ["/**"],
      "exclude_urls": ["/collections/**"],
      "include_external": False
    }
    
    res = requests.post(f"{API_URL}/v1/crawls", headers=HEADERS, json=data)
    crawl = res.json()
    print(json.dumps(crawl, indent=2))
    

Since everything in Olostep is an object, you will receive a `crawl` object in response. The `crawl` object has a few properties like `id` and `status`, which you can use to track the crawl.

[​

](#check-crawl-status)

Check crawl status
------------------------------------------------

Poll the crawl to track progress until `status` is `completed`.

Python

Node

cURL

Node (API)

Python (API)

    # Using the crawl object from the previous step
    info = crawl.info()
    print(info.status, info.pages_count)
    
    # Or wait until completed
    crawl.wait_till_done(check_every_n_secs=5)
    

    // Using the crawl object from the previous step
    const info = await crawl.info()
    console.log(info.status, info.pages_count)
    
    // Or wait until completed
    await crawl.waitTillDone({ checkEveryNSecs: 5 })
    

    curl -s -X GET "https://api.olostep.com/v1/crawls/<CRAWL_ID>" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

    const crawlId = '<CRAWL_ID>'
    const status = await fetch(`${API_URL}/v1/crawls/${crawlId}`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    }).then(r => r.json())
    console.log(status)
    

    import time
    
    def get_crawl_info(crawl_id):
        return requests.get(f'{API_URL}/v1/crawls/{crawl_id}', headers=HEADERS).json()
    
    crawl_id = crawl['id']
    while True:
        info = get_crawl_info(crawl_id)
        print(info['status'], info.get('pages_count'))
        if info['status'] == 'completed':
            break
        time.sleep(5)
    

Alternatively, you can pass a `webhook_url` when starting the crawl to be notified when the crawl is completed.

[​

](#list-pages-paginate/stream-with-cursor)

List pages (paginate/stream with cursor)
------------------------------------------------------------------------------------------

Fetch pages and iterate using `cursor` and `limit`. Works while the crawl is `in_progress` or `completed`.

Python

Node

cURL

Node (API)

Python (API)

    # Iterate all pages (auto-waits for crawl completion, handles pagination)
    for page in crawl.pages():
        print(page.url, page.retrieve_id)
    

    // Iterate all pages (auto-waits for crawl completion, handles pagination)
    for await (const page of crawl.pages()) {
      console.log(page.url, page.retrieve_id)
    }
    

    curl -s -G "https://api.olostep.com/v1/crawls/<CRAWL_ID>/pages" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      --data-urlencode "cursor=0" \
      --data-urlencode "limit=10"
    

    let cursor = 0
    while (true) {
      const pages = await fetch(`${API_URL}/v1/crawls/${crawlId}/pages?cursor=${cursor}&limit=10`, {
        headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
      }).then(r => r.json())
      pages.pages.forEach(p => console.log(p.url, p.retrieve_id))
      if (pages.cursor === undefined) break
      cursor = pages.cursor
    }
    

    def get_pages(crawl_id, cursor=None, limit=10, search_query=None):
        params = { 
            'cursor': cursor, 
            'limit': limit
        }
        return requests.get(f'{API_URL}/v1/crawls/{crawl_id}/pages', headers=HEADERS, params=params).json()
    
    cursor = 0
    while True:
        page_batch = get_pages(crawl_id, cursor=cursor, limit=10)
        for page in page_batch['pages']:
            print(page['url'], page['retrieve_id'])
        if 'cursor' not in page_batch:
            break
        cursor = page_batch['cursor']
        time.sleep(5)
    

[​

](#search-query-limit-to-top-n-relevant)

Search query (limit to top N relevant)
--------------------------------------------------------------------------------------

Use `search_query` at start, and optionally filter listing with `search_query`. Limit per-page exploration with `top_n`.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    crawl = client.crawls.create(
        start_url="https://olostep.com",
        max_pages=100,
        include_urls=["/**"],
        search_query="contact us",
        top_n=5,
    )
    
    for page in crawl.pages(search_query="contact us"):
        print(page.url)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const crawl = await client.crawls.create({
      url: 'https://olostep.com',
      maxPages: 100,
      includeUrls: ['/**'],
      searchQuery: 'contact us',
      topN: 5,
    })
    
    for await (const page of crawl.pages()) {
      console.log(page.url)
    }
    

    curl -s -X POST "https://api.olostep.com/v1/crawls" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "start_url": "https://olostep.com",
        "max_pages": 100,
        "include_urls": ["/**"],
        "search_query": "contact us",
        "top_n": 5
      }'
    

    olostep crawl "https://olostep.com" \
      --max-pages 100 \
      --include-url "/**" \
      --search-query "contact us" \
      --top-n 5
    

    await fetch(`${API_URL}/v1/crawls`, { method: 'POST', headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' }, body: JSON.stringify({ start_url: 'https://olostep.com', max_pages: 100, include_urls: ['/**'], search_query: 'contact us', top_n: 5 }) })
    

    data = {
      "start_url": "https://olostep.com",
      "max_pages": 100,
      "include_urls": ["/**"],
      "search_query": "contact us",
      "top_n": 5
    }
    crawl = requests.post(f'{API_URL}/v1/crawls', headers=HEADERS, json=data).json()
    pages = requests.get(f"{API_URL}/v1/crawls/{crawl['id']}/pages", headers=HEADERS, params={'search_query': 'contact us'}).json()
    print(len(pages['pages']))
    

[​

](#retrieve-content)

Retrieve content
--------------------------------------------

Use each page’s `retrieve_id` with `/v1/retrieve` to fetch `html_content` and/or `markdown_content`.

Python

Node

cURL

CLI

Node (API)

Python (API)

    # Retrieve content for each crawled page
    for page in crawl.pages():
        content = page.retrieve(["markdown"])
        print(content.markdown_content)
    

    // Retrieve content for each crawled page
    for await (const page of crawl.pages()) {
      const content = await client.retrieve.get(page.retrieve_id, ['markdown'])
      console.log(content.markdown_content)
    }
    

    curl -s -G "https://api.olostep.com/v1/retrieve" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      --data-urlencode "retrieve_id=<RETRIEVE_ID>"
    

    # `olostep crawl` retrieves content automatically. To fetch a single
    # page by its retrieve_id later:
    olostep scrape-get <RETRIEVE_ID>
    

    const retrieved = await fetch(`${API_URL}/v1/retrieve?retrieve_id=<RETRIEVE_ID>`, { headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' } }).then(r => r.json())
    console.log(retrieved.markdown_content)
    

    def retrieve_content(retrieve_id):
        return requests.get(f"{API_URL}/v1/retrieve", headers=HEADERS, params={"retrieve_id": retrieve_id}).json()
    
    for page in get_pages(crawl['id'], limit=5)['pages']:
        retrieved = retrieve_content(page['retrieve_id'])
        print(retrieved.get('markdown_content'))
    

[​

](#notes)

Notes
----------------------

*   Pagination is cursor-based; repeat requests until `cursor` is absent.
*   Content fields on `/v1/crawls/{crawl_id}/pages` are deprecated; prefer `/v1/retrieve`.
*   Webhooks: set `webhook_url` to receive a POST when the crawl completes.

[​

](#storage)

Storage
--------------------------

Stored files for a crawl are kept for 7 days by default. Pass a `storage` object on `POST /v1/crawls` to keep them longer, or indefinitely. The setting is passed to every page scrape in the crawl, so it covers the content you fetch later with `retrieve_id`.

Parameter

Type

Default

Description

`storage.expires_in`

`string`

`7d`

How long to keep the stored files. One of `7d`, `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` (indefinite).

Omitting `storage`, or sending `storage` without `expires_in`, uses `7d`. Both the create response and `GET /v1/crawls/{crawl_id}` include the value in effect:

    "storage": { "expires_in": "30d" }
    

cURL

    curl -s -X POST "https://api.olostep.com/v1/crawls" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "start_url": "https://example.com",
        "max_pages": 10,
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

Crawl costs 1 credit per page crawled.

Was this page helpful?

YesNo
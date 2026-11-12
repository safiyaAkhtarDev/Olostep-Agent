<!-- source: https://docs.olostep.com/features/maps -->
# https://docs.olostep.com/features/maps

Maps - Olostep Docs  

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

Maps

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Maps
====

Copy pageCopy page

Get all the URLs on a website.

Copy pageCopy page

Through the Olostep `/v1/maps` endpoint you can get all the URLs on a website. This is useful for content discovery, site structure analysis (e.g., SEO), or deciding which URLs you want to scrape next.

*   Get all URLs on a website (including sitemaps and discovered links)
*   Use special patterns to include/exclude paths (e.g. `/blog/**`)
*   Paginate large responses with `cursor` (up to 10MB per response)
*   Limit volume with `top_n`

For API details see the [Map Endpoint API Reference](/api-reference/maps/create).

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

](#usage)

Usage
----------------------

Send a POST request with the website `url`. Optionally pass `include_urls`, `exclude_urls` (glob patterns), and `top_n`.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    sitemap = client.maps.create(url="https://docs.olostep.com")
    
    for url in sitemap.urls():
        print(url)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const map = await client.maps.create({ url: 'https://docs.olostep.com' })
    
    for await (const url of map.urls()) {
      console.log(url)
    }
    

    curl -s -X POST "https://api.olostep.com/v1/maps" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url": "https://docs.olostep.com"
      }'
    

    olostep map "https://docs.olostep.com"
    

    const res = await fetch('https://api.olostep.com/v1/maps', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: 'https://docs.olostep.com' })
    })
    console.log(await res.json())
    

    import requests
    import json
    
    endpoint = "https://api.olostep.com/v1/maps"
    
    payload = {
        "url": "https://docs.olostep.com"
    }
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

The response time is typically within seconds but can take up to 120 seconds for more complex websites. It can extract all URLs from a website, even backlinks and those not present in the Sitemaps. You can also also decide the URLs paths you want to include or exclude from the response. By default the endpoint returns around 100k URLs in a single call (10MB max). If the response includes more data, the API returns a `cursor` parameter which can be used for pagination and getting the subsequent URLs. For more details refer to the [API Reference](/api-reference/maps/create#body-cursor) This endpoint is particularly useful when you need to:

*   Discover all content pages on a website
*   Analyze site structure and hierarchy
*   Prepare URLs for batch processing
*   Decide which specific URLs to scrape

For more fine-grained control over the URLs returned you can use the params `include_urls` and `exclude_urls`.

### 

[​

](#example)

Example

Let’s say that from [www.brex.com](http://www.brex.com) you want to extract all the urls that have the paths after `/product/` e.g `https://www.brex.com/product/api/no-code` but also include `www.brex.com/product`. You can use the following code:

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    sitemap = client.maps.create(
        url="https://www.brex.com/",
        include_urls=["/product", "/product/**"],
        top_n=100000,
    )
    
    for url in sitemap.urls():
        print(url)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const map = await client.maps.create({
      url: 'https://www.brex.com/',
      includeUrls: ['/product', '/product/**'],
      topN: 100000,
    })
    
    for await (const url of map.urls()) {
      console.log(url)
    }
    

    curl -s -X POST "https://api.olostep.com/v1/maps" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url": "https://www.brex.com/",
        "include_urls": ["/product", "/product/**"],
        "top_n": 100000
      }'
    

    olostep map "https://www.brex.com/" \
      --include-url "/product" \
      --include-url "/product/**" \
      --top-n 100000
    

    const endpoint = 'https://api.olostep.com/v1/maps'
    
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        url: 'https://www.brex.com/',
        include_urls: ['/product', '/product/**'],
        top_n: 100000
      })
    })
    console.log(await res.text())
    

    import requests
    
    endpoint = "https://api.olostep.com/v1/maps"
    
    payload = {
        "url": "https://www.brex.com/",
        "include_urls": ["/product", "/product/**"],
        "top_n": 100000
    }
    
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(endpoint, json=payload, headers=headers)
    
    print(response.text)
    

[​

](#conclusion)

Conclusion
--------------------------------

The maps endpoint is a powerful tool for content discovery and site analysis. It provides a comprehensive list of URLs on a website, enabling you to extract content from specific pages or analyze the site structure. This endpoint is particularly useful for SEO professionals, content marketers, AI agents who need to analyze website content or structure.

[​

](#storage)

Storage
--------------------------

Stored files for a map are kept for 7 days by default. Pass a `storage` object on `POST /v1/maps` to keep them longer, or indefinitely. The setting covers the map result and the pages scraped while discovering URLs.

Parameter

Type

Default

Description

`storage.expires_in`

`string`

`7d`

How long to keep the stored files. One of `7d`, `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` (indefinite).

Omitting `storage`, or sending `storage` without `expires_in`, uses `7d`. Both the create response and `GET /v1/maps/{map_id}` include the value in effect:

    "storage": { "expires_in": "30d" }
    

cURL

    curl -s -X POST "https://api.olostep.com/v1/maps" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "url": "https://example.com",
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

Map costs 1 credit. Then for every extra 1000 URLs returned in the response, an additional credit is billed.

Was this page helpful?

YesNo
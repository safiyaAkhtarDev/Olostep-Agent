<!-- source: https://docs.olostep.com/features/answers -->
# https://docs.olostep.com/features/answers

Answers API - Olostep Docs  

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

Answers API

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Answers API
===========

Copy pageCopy page

AI answers backed by live web search, scraping, and crawling — not a stale index.

Copy pageCopy page

Through the Olostep `/v1/answers` endpoint you can search the web with natural language and return AI‑powered answers and data in the JSON shape you want. This lets you ground your products on real-world data and sources, enrich data points or spreadsheets

*   Ask a question or give AI a data point you want to enrich
*   Optional: specify the JSON structure you want back

It will:

*   Search, clean, validate and return the data it found on the Web
*   Return sources used to generate the answer
*   Handle uncertainty with `NOT_FOUND` values when data cannot be verified

For API details, see the [Answers Endpoint API Reference](/api-reference/answers/create). By default we use a generic web index and a cost‑efficient LLM validator. Enterprise customers have access to proprietary industry specific web indexes, exclusive private data (including phone numbers and emails) and custom LLM models most suited for their use case. Contact us for access: [info@olostep.com](mailto:info@olostep.com)

[​

](#use-cases)

Use cases
------------------------------

The answers endpoint can be used to:

*   Ground AI applications on real world data and facts
*   Enrich spreadsheets and data points for Recruting, Finance, Consulting, and Sales

Here’s a demo of an AI powered spreadsheet powered by the Answers endpoint: [https://www.olostep.com/demos/spreadsheet-enrich](https://www.olostep.com/demos/spreadsheet-enrich)

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

Ask a question and pass a JSON schema to guide the output. You can also not pass the `json` parameter and the API will return a json object with the answer text inside the `result` field.

Python

Node

cURL

CLI

Node (API)

Python (API)

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    answer = client.answers.create(
        task="What is the latest book by J.K. Rowling?",
        json_format={"book_title": "", "author": "", "release_date": ""},
    )
    
    print(answer.json_content)
    print(answer.sources)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const answer = await client.answers.create({
      task: 'What is the latest book by J.K. Rowling?',
      jsonFormat: { book_title: '', author: '', release_date: '' },
    })
    
    console.log(answer.json_content)
    console.log(answer.sources)
    

    curl -s -X POST "https://api.olostep.com/v1/answers" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "task": "What is the latest book by J.K. Rowling?",
        "json": {"book_title": "", "author": "", "release_date": ""}
      }'
    

    olostep answer "What is the latest book by J.K. Rowling?" \
      --json-format '{"book_title":"","author":"","release_date":""}'
    

    const res = await fetch('https://api.olostep.com/v1/answers', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        task: 'What is the latest book by J.K. Rowling?',
        json: { book_title: '', author: '', release_date: '' }
      })
    })
    console.log(await res.json())
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/answers"
    payload = {
      "task": "What is the latest book by J.K. Rowling?",
      "json": {"book_title": "", "author": "", "release_date": ""}
    }
    headers = {"Authorization": "Bearer <YOUR_API_KEY>", "Content-Type": "application/json"}
    
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

[​

](#response)

Response
----------------------------

Like other Olostep endpoints, you will receive a `answer` object in response. The `answer` object has a few properties like `id` and `result`.

    {
      "id": "answer_9bi0sbj9xa",
      "object": "answer",
      "created": 1760327323,
      "metadata": {},
      "task": "What is the latest book by J.K. Rowling?",
      "result": {
        "json_content": "{\"book_title\":\"The Hallmarked Man\",\"author\":\"J.K. Rowling (as Robert Galbraith)\",\"release_date\":\"2 September 2025\"}",
        "json_hosted_url": "https://olostep-storage.s3.us-east-1.amazonaws.com/answer_9bi0sbj9xa.json",
        "sources": [
          "https://strikefans.com/the-books/",
          "https://www.facebook.com/groups/496943608606523/posts/1136830134617864/",
          "https://robert-galbraith.com/strike-books/",
          "https://www.novelsuspects.com/series-list/robert-galbraith-cormoran-strike-series-in-order/",
          "https://www.reddit.com/r/books/comments/1na833a/jk_rowlings_new_strike_novel_900_pages_of_romance/",
          "https://www.harrypotter.com/writing-by-jk-rowling",
          "https://stories.jkrowling.com/book-news/",
          "https://deadline.com/2024/09/jk-rowling-writing-futuristic-novel-1236093909/",
          "https://www.reddit.com/r/FantasticBeasts/comments/1cl1shn/jk_rowling_may_2024_ive_got_six_more_books_in_my/",
          "https://www.jkrowling.com/news/"
        ]
      }
    }
    

Your requested answer, formatted according to the `json` parameter, is in `response.result.json_content` and the list of sources in `response.result.sources`. You can parse the stringified JSON to access the structured data.

    {
      "book_title": "The Hallmarked Man",
      "author": "J.K. Rowling",
      "release_date": "September 2, 2025"
    }
    

Sources example:

    [
        "https://www.harrypotter.com/writing-by-jk-rowling",
        "https://stories.jkrowling.com/book-news/",
        "https://deadline.com/2024/09/jk-rowling-writing-futuristic-novel-1236093909/",
        "https://www.reddit.com/r/FantasticBeasts/comments/1cl1shn/jk_rowling_may_2024_ive_got_six_more_books_in_my/",
        "https://www.jkrowling.com/news/"
    ]
    

When you don’t pass the `json` parameter, the API will return a json object with the answer text inside the `result` field.

    {
      "result": "The latest book by J.K. Rowling is The Hallmarked Man."
    }
    

### 

[​

](#flexible-json-parameter)

Flexible `json` parameter

*   Provide a JSON object with empty values as a schema, or a string describing the data you want.
*   If the agent isn’t confident, it returns `NOT_FOUND` for that field.

Python

Node

Python (API)

CLI

    from olostep import Olostep
    
    client = Olostep(api_key="YOUR_REAL_KEY")
    
    answer = client.answers.create(
        task="When will React 30 be released?",
        json_format={"release_date": ""},
    )
    
    print(answer.json_content)
    

    import Olostep from 'olostep'
    
    const client = new Olostep({ apiKey: 'YOUR_REAL_KEY' })
    
    const answer = await client.answers.create({
      task: 'When will React 30 be released?',
      jsonFormat: { release_date: '' },
    })
    
    console.log(answer.json_content)
    

    import requests, json
    
    endpoint = "https://api.olostep.com/v1/answers"
    payload = {
      "task": "When will React 30 be released?", 
      "json": {
        "release_date": ""
      }
    }
    headers = {
      "Authorization": "Bearer <YOUR_API_KEY>",
      "Content-Type": "application/json"
    }
    response = requests.post(endpoint, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    

    olostep answer "When will React 30 be released?" --json-format '{"release_date":""}'
    

This would return:

    {
      "release_date": "NOT_FOUND"
    }
    

[​

](#storage)

Storage
--------------------------

Stored files for a answer are kept for 7 days by default. Pass a `storage` object on `POST /v1/answers` to keep them longer, or indefinitely. The setting covers the answer result and the pages fetched to build it.

Parameter

Type

Default

Description

`storage.expires_in`

`string`

`7d`

How long to keep the stored files. One of `7d`, `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` (indefinite).

Omitting `storage`, or sending `storage` without `expires_in`, uses `7d`. Both the create response and `GET /v1/answers/{answer_id}` include the value in effect:

    "storage": { "expires_in": "30d" }
    

cURL

    curl -s -X POST "https://api.olostep.com/v1/answers" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "task": "What is the latest stable version of PostgreSQL?",
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

Answers costs 20 credits per request.

Was this page helpful?

YesNo
<!-- source: https://docs.olostep.com/features/feedbacks -->
# https://docs.olostep.com/features/feedbacks

Feedbacks - Olostep Docs  

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

Feedbacks

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Feedbacks
=========

Copy pageCopy page

Report a wrong, incomplete, or failed API result. Costs no credits.

Copy pageCopy page

Through the Olostep `/v1/feedbacks` endpoint you can report when the API got something wrong. Call it from an agent or from your own code when a result was wrong, incomplete, slow, failed, or did not match the documentation.

*   Send the `id` of the object the feedback is about so we can trace it to the exact request
*   Tag the report with a category and optional symptom codes
*   Submitting feedback is free, and it works even when your team’s credits are exhausted

For API details see the [Submit Feedback API Reference](/api-reference/feedbacks/create).

[​

](#submit-feedback)

Submit feedback
------------------------------------------

`category` and `note` are required. Include `related_object_id` when you have it: a `scrape_…`, `batch_…`, or similar resource id, or the `error_…` id when the call failed.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    
    payload = {
        "category": "output_quality",
        "issues": ["missing_content", "broken_formatting"],
        "note": "The markdown drops the pricing comparison table; expected all 4 rows.",
        "affected_endpoint": "POST /v1/scrapes",
        "related_object_id": "scrape_abc1234567",
        "url": "https://example.com/pricing"
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        "https://api.olostep.com/v1/feedbacks",
        headers=headers,
        json=payload
    )
    print(json.dumps(response.json(), indent=2))
    

    const res = await fetch('https://api.olostep.com/v1/feedbacks', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer <YOUR_API_KEY>',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        category: 'output_quality',
        issues: ['missing_content', 'broken_formatting'],
        note: 'The markdown drops the pricing comparison table; expected all 4 rows.',
        affected_endpoint: 'POST /v1/scrapes',
        related_object_id: 'scrape_abc1234567',
        url: 'https://example.com/pricing'
      })
    })
    console.log(await res.json())
    

    curl -X POST https://api.olostep.com/v1/feedbacks \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "category": "output_quality",
        "issues": ["missing_content", "broken_formatting"],
        "note": "The markdown drops the pricing comparison table; expected all 4 rows.",
        "affected_endpoint": "POST /v1/scrapes",
        "related_object_id": "scrape_abc1234567",
        "url": "https://example.com/pricing"
      }'
    

### 

[​

](#response)

Response

The response is the stored `feedback` object. There is no list or get endpoint; feedback is read on our side.

    {
      "object": "feedback",
      "id": "feedback_019e70f9-214a-74fc-a1ae-26fd3318be3e",
      "category": "output_quality",
      "issues": ["missing_content", "broken_formatting"],
      "note": "The markdown drops the pricing comparison table; expected all 4 rows.",
      "affected_endpoint": "POST /v1/scrapes",
      "related_object_id": "scrape_abc1234567",
      "url": "https://example.com/pricing",
      "created_at": "2026-10-23T00:00:00.000Z"
    }
    

[​

](#fields)

Fields
------------------------

Field

Required

Notes

`category`

yes

One of `output_quality`, `reliability`, `performance`, `documentation`, `api_usability`, `feature_gap`, `other`

`note`

yes

What went wrong and what you expected instead, up to 4,000 characters

`issues`

no

Up to 20 `snake_case` symptom codes. Documented codes are listed below; any other code of the same shape is accepted

`affected_endpoint`

no

`METHOD /path` with the canonical plural path, for example `POST /v1/scrapes`

`related_object_id`

no

The `id` of the scrape, batch, crawl, answer, or other object, or the `error_…` id when the call failed

`url`

no

The page the feedback is about, such as the URL that was scraped

### 

[​

](#issue-codes)

Issue codes

`missing_content`, `incorrect_content`, `incomplete_content`, `broken_formatting`, `irrelevant_results`, `duplicate_results`, `stale_content`, `request_failed`, `timeout`, `slow_response`, `inconsistent_result`, `docs_mismatch`, `broken_example`, `confusing_schema`, `confusing_error`, `unsupported_website`, `unsupported_format`.

Was this page helpful?

YesNo
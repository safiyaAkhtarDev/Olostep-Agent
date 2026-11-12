<!-- source: https://docs.olostep.com/features/schedules -->
# https://docs.olostep.com/features/schedules

Schedules - Olostep Docs  

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

Schedules

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Schedules
=========

Copy pageCopy page

Schedule API calls to run automatically at specified times

Copy pageCopy page

Through the Olostep `/v1/schedules` endpoint you can schedule API calls to execute automatically at specified times. Schedule one-time executions or recurring tasks using cron expressions or natural language.

*   Schedule one-time executions at a specific datetime
*   Create recurring schedules using cron expressions
*   Use natural language text to automatically generate cron expressions
*   Schedule HTTP endpoints (GET or POST)
*   For POST requests, use short-form Olostep endpoints (automatically prefixed) or full URLs
*   Pass any payload you want - the payload is sent exactly as you specify it
*   Automatically manage schedule lifecycle

For API details see the [Schedule Endpoint API Reference](/api-reference/schedules/create).

[​

](#installation)

Installation
------------------------------------

Python

Node

cURL

    # pip install requests
    
    import requests
    

    // npm install node-fetch
    
    // ESM
    import fetch from 'node-fetch'
    
    // CommonJS
    const fetch = require('node-fetch')
    

    # macOS: builtin curl is fine
    

[​

](#create-a-schedule)

Create a schedule
----------------------------------------------

Create a schedule to execute API calls automatically. You can create one-time schedules or recurring schedules using cron expressions. The `endpoint` can be any URL (not limited to Olostep endpoints), and the `payload` can contain any data you want to send.

### 

[​

](#one-time-schedule)

One-time schedule

Schedule an API call to execute once at a specific datetime.

Python

Node

cURL

    import requests
    import json
    from datetime import datetime, timedelta
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Schedule a scrape to run in 1 hour
    execute_at = (datetime.now() + timedelta(hours=1)).isoformat()
    
    payload = {
        "method": "POST",
        "endpoint": "v1/scrapes",
        "payload": {
            "url_to_scrape": "https://example.com",
            "formats": ["markdown"]
        },
        "execute_at": execute_at,
        "expression_timezone": "UTC"
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{API_URL}/schedules", headers=headers, json=payload)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const execute_at = new Date(Date.now() + 60 * 60 * 1000).toISOString() // 1 hour from now
    
    const res = await fetch(`${API_URL}/schedules`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        method: 'POST',
        endpoint: 'v1/scrapes',
        payload: {
          url_to_scrape: 'https://example.com',
          formats: ['markdown']
        },
        execute_at: execute_at,
        expression_timezone: 'UTC'
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/schedules" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "method": "POST",
        "endpoint": "v1/scrapes",
        "payload": {
          "url_to_scrape": "https://example.com",
          "formats": ["markdown"]
        },
        "execute_at": "2025-01-15T10:00:00Z",
        "expression_timezone": "UTC"
      }'
    

### 

[​

](#recurring-schedule-with-cron-expression)

Recurring schedule with cron expression

Create a recurring schedule using a cron expression. Cron expressions use 6 fields format: minute hour day month day-of-week year.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Schedule a scrape to run every day at 10am UTC
    payload = {
        "method": "POST",
        "endpoint": "v1/scrapes",
        "payload": {
            "url_to_scrape": "https://example.com",
            "formats": ["markdown"]
        },
        "cron_expression": "0 10 * * ? *",
        "expression_timezone": "UTC"
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{API_URL}/schedules", headers=headers, json=payload)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    
    const res = await fetch(`${API_URL}/schedules`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        method: 'POST',
        endpoint: 'v1/scrapes',
        payload: {
          url_to_scrape: 'https://example.com',
          formats: ['markdown']
        },
        cron_expression: '0 10 * * ? *', // Every day at 10am UTC
        expression_timezone: 'UTC'
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/schedules" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "method": "POST",
        "endpoint": "v1/scrapes",
        "payload": {
          "url_to_scrape": "https://example.com",
          "formats": ["markdown"]
        },
        "cron_expression": "0 10 * * ? *",
        "expression_timezone": "UTC"
      }'
    

### 

[​

](#natural-language-scheduling)

Natural language scheduling

Use natural language text to automatically generate cron expressions. The system will convert your text into a valid cron expression.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Schedule using natural language
    payload = {
        "method": "POST",
        "endpoint": "v1/scrapes",
        "payload": {
            "url_to_scrape": "https://example.com",
            "formats": ["markdown"]
        },
        "text": "every 3 minutes",
        "expression_timezone": "UTC"
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{API_URL}/schedules", headers=headers, json=payload)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    
    const res = await fetch(`${API_URL}/schedules`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        method: 'POST',
        endpoint: 'v1/scrapes',
        payload: {
          url_to_scrape: 'https://example.com',
          formats: ['markdown']
        },
        text: 'every Monday at 9am',
        expression_timezone: 'UTC'
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/schedules" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "method": "POST",
        "endpoint": "v1/scrapes",
        "payload": {
          "url_to_scrape": "https://example.com",
          "formats": ["markdown"]
        },
        "text": "every day at 10am",
        "expression_timezone": "UTC"
      }'
    

[​

](#response-format)

Response format
------------------------------------------

When you create a schedule, you’ll receive a schedule object with the following properties:

    {
      "id": "schedule_abc123xyz",
      "object": "schedule"
      "type": "recurring",
      "method": "POST",
      "endpoint": "v1/scrapes",
      "cron_expression": "0 10 * * ? *",
      "expression_timezone": "UTC",
      "created": "2025-01-15T10:00:00.000Z"
    }
    

For one-time schedules, the response includes `execute_at` instead of `cron_expression`:

    {
      "id": "schedule_abc123xyz",
      "object": "schedule"
      "type": "onetime",
      "method": "POST",
      "endpoint": "v1/scrapes",
      "execute_at": "2025-01-15T10:00:00.000Z",
      "expression_timezone": "UTC",
      "created": "2025-01-15T09:00:00.000Z"
    }
    

[​

](#list-schedules)

List schedules
----------------------------------------

Retrieve all schedules for your team. By default, deleted schedules are filtered out. Use the `include_deleted` query parameter to include them.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    response = requests.get(f"{API_URL}/schedules", headers=headers)
    result = response.json()
    print(f"Total schedules: {result['count']}")
    for schedule in result['schedules']:
        print(json.dumps(schedule, indent=2))
    
    # To include deleted schedules:
    # response = requests.get(f"{API_URL}/schedules?include_deleted=true", headers=headers)
    

    const API_URL = 'https://api.olostep.com/v1'
    
    const res = await fetch(`${API_URL}/schedules`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const result = await res.json()
    console.log(`Total schedules: ${result.count}`)
    result.schedules.forEach(s => console.log(s))
    
    // To include deleted schedules:
    // const res = await fetch(`${API_URL}/schedules?include_deleted=true`, { ... })
    

    curl -s -X GET "https://api.olostep.com/v1/schedules" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    
    # To include deleted schedules:
    # curl -s -X GET "https://api.olostep.com/v1/schedules?include_deleted=true" \
    #   -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#get-a-schedule)

Get a schedule
----------------------------------------

Retrieve a single schedule by its ID.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    schedule_id = "schedule_abc123xyz"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    response = requests.get(f"{API_URL}/schedules/{schedule_id}", headers=headers)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const scheduleId = 'schedule_abc123xyz'
    
    const res = await fetch(`${API_URL}/schedules/${scheduleId}`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(await res.json())
    

    curl -s -X GET "https://api.olostep.com/v1/schedules/schedule_abc123xyz" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#delete-a-schedule)

Delete a schedule
----------------------------------------------

Delete a schedule by its ID. This will stop any future executions.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    schedule_id = "schedule_abc123xyz"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    response = requests.delete(f"{API_URL}/schedules/{schedule_id}", headers=headers)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const scheduleId = 'schedule_abc123xyz'
    
    const res = await fetch(`${API_URL}/schedules/${scheduleId}`, {
      method: 'DELETE',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(await res.json())
    

    curl -s -X DELETE "https://api.olostep.com/v1/schedules/schedule_abc123xyz" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#supported-endpoints)

Supported endpoints
--------------------------------------------------

### 

[​

](#olostep-endpoints-short-form)

Olostep endpoints (short form)

For POST requests, you can use short forms for Olostep endpoints. The system will automatically prepend `https://api.olostep.com/` for these:

*   `v1/scrapes` - Schedule web scraping tasks
*   `v1/batches` - Schedule batch processing jobs
*   `v1/crawls` - Schedule website crawling operations
*   `v1/maps` - Schedule map data extraction
*   `v1/answers` - Schedule answer generation

### 

[​

](#full-urls)

Full URLs

You can also provide full URLs for your endpoints. This is required for external APIs or webhooks:

Python

Node

cURL

    import requests
    import json
    from datetime import datetime, timedelta
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Schedule a call to an external API
    payload = {
        "method": "POST",
        "endpoint": "https://api.example.com/webhook",
        "payload": {
            "custom_field": "any value",
            "data": {"nested": "structure"},
            "timestamp": datetime.now().isoformat()
        },
        "execute_at": (datetime.now() + timedelta(hours=1)).isoformat(),
        "expression_timezone": "UTC"
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{API_URL}/schedules", headers=headers, json=payload)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const execute_at = new Date(Date.now() + 60 * 60 * 1000).toISOString()
    
    const res = await fetch(`${API_URL}/schedules`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        method: 'POST',
        endpoint: 'https://api.example.com/webhook',
        payload: {
          custom_field: 'any value',
          data: { nested: 'structure' },
          timestamp: new Date().toISOString()
        },
        execute_at: execute_at,
        expression_timezone: 'UTC'
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/schedules" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "method": "POST",
        "endpoint": "https://api.example.com/webhook",
        "payload": {
          "custom_field": "any value",
          "data": {"nested": "structure"}
        },
        "execute_at": "2025-01-15T10:00:00Z",
        "expression_timezone": "UTC"
      }'
    

The `payload` field accepts any JSON object - you can structure it however you need for your target endpoint.

[​

](#cron-expression-format)

Cron expression format
--------------------------------------------------------

Cron expressions use 6 fields format:

    minute hour day month day-of-week year
    

Examples:

*   `0/3 * * * ? *` - Every 3 minutes
*   `0 10 * * ? *` - Every day at 10:00 AM
*   `0 9 ? * MON *` - Every Monday at 9:00 AM
*   `0 0 1 * ? *` - First day of every month at midnight

Use `?` for day-of-month or day-of-week when not specified.

[​

](#natural-language-examples)

Natural language examples
--------------------------------------------------------------

You can use natural language to describe schedules. The system will automatically convert them to cron expressions:

*   “every 3 minutes” → `0/3 * * * ? *`
*   “every day at 10am” → `0 10 * * ? *`
*   “every Monday at 9am” → `0 9 ? * MON *`
*   “every hour” → `0 * * * ? *`
*   “every week on Monday” → `0 0 ? * MON *`

[​

](#important-notes)

Important notes
------------------------------------------

*   One-time schedules are automatically deleted after execution
*   Recurring schedules continue until manually deleted
*   Timezone must be a valid IANA timezone identifier (e.g., “UTC”, “America/New\_York”, “Europe/London”)
*   The `execute_at` datetime must be in the future
*   Natural language conversion may require retries; the system will attempt up to 3 times
*   When using natural language text (`text` parameter), the timezone defaults to “UTC”
*   Schedules execute the API call with the provided payload exactly as specified - you can pass any JSON structure you need
*   For POST requests, short-form Olostep endpoints (`v1/scrapes`, `v1/batches`, `v1/crawls`, `v1/maps`, `v1/answers`) are automatically prefixed with `https://api.olostep.com/`
*   For other endpoints, provide the full URL
*   The `payload` can contain any data structure - it’s sent as-is to your target endpoint
*   Deleting an already deleted schedule will return a 400 error

[​

](#pricing)

Pricing
--------------------------

Schedules themselves are free. You only pay for the API calls that are executed when the schedule runs. For example, if you schedule a scrape, you’ll be charged 1 credit per execution (or more if using parsers or LLM extraction).

Was this page helpful?

YesNo
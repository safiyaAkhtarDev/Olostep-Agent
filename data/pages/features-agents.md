<!-- source: https://docs.olostep.com/features/agents -->
# https://docs.olostep.com/features/agents

Agents API - Olostep Docs  

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

Agents API

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Agents API
==========

Copy pageCopy page

Build no-code research agents that search, scrape, and crawl the web with Olostep.

Copy pageCopy page

Through the Olostep Agents API you can create autonomous research agents that can automate data pipelines and search tasks on a schedule and deliver structured results.

*   Web research across sites with automated extraction
*   Multi-step workflows with scheduled execution and notifications
*   Output to JSON/CSV/Sheets/DB

For availability and details, contact us at [info@olostep.com](mailto:info@olostep.com) or [Contact Sales](https://www.olostep.com/contact-sales).

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

](#create-an-agent)

Create an agent
------------------------------------------

Create an agent with a natural language prompt and a target model.

Python

Node

cURL

    API_URL = 'https://api.olostep.com/v1/agents' # endpoint available to select customers
    API_KEY = '<YOUR_API_KEY>'
    
    headers = {
      'Authorization': f'Bearer {API_KEY}', 
      'Content-Type': 'application/json'
    }
    
    data = {
      "prompt": """
        Find portfolio companies from https://www.vcsheet.com/funds and 
        write to a Google Sheet with columns (Fund Name, Fund Website URL, 
        Fund LinkedIn URL, Portfolio Company Name, Portfolio Company URL, 
        Portfolio Company LinkedIn URL). Run weekly on Monday at 9:00 AM 
        and email steve@example.com when new companies are added.
      """,
      "model": "gpt-4.1"
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()
    print(result)
    

    const res = await fetch('https://api.olostep.com/v1/agents', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        prompt: 'Find portfolio companies from https://www.vcsheet.com/funds and write to a Google Sheet...',
        model: 'gpt-4.1'
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/agents" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "Find portfolio companies from https://www.vcsheet.com/funds and write to a Google Sheet...",
        "model": "gpt-4.1"
      }'
    

[​

](#capabilities)

Capabilities
------------------------------------

The Olostep agent can:

*   **Web Research**: Automatically search and extract data from websites
*   **Data Organization**: Structure information into spreadsheets, databases, or other formats
*   **Scheduled Execution**: Run tasks on a recurring schedule (daily, weekly, at a predefined time)
*   **Multi-step Workflows**: Perform complex, multi-part research tasks autonomously
*   **Notifications**: Send email alerts when new data is found or tasks complete
*   **Custom Output**: Return data as CSV, JSON, Google Sheet, or directly in your database

[​

](#access)

Access
------------------------

The Agents API is currently available to select customers. To get access:

*   Email us at [info@olostep.com](mailto:info@olostep.com)
*   Or [contact our sales team](https://www.olostep.com/contact-sales)

[​

](#pricing)

Pricing
--------------------------

Agents pricing is variable. It’s billed by outcome. The price is negotiated between the client and the agent. Reach out to [info@olostep.com](mailto:info@olostep.com) for more details

Was this page helpful?

YesNo
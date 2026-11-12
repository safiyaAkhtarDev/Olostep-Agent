<!-- source: https://docs.olostep.com/get-started/authentication -->
# https://docs.olostep.com/get-started/authentication

Authentication - Olostep Docs  

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

Get Started

Authentication

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Get Started

Authentication
==============

Copy pageCopy page

Authenticate to the Olostep search, scraping, and crawling API with API keys.

Copy pageCopy page

The API endpoints require that you authenticate using an API token.

[​

](#generate-a-token)

Generate a token
--------------------------------------------

The token can be generated from the Olostep dashboard. Please create an account [here](https://www.olostep.com/auth/).

[​

](#use-your-token)

Use your token
----------------------------------------

You can authenticate by adding an `Authorization` header to all your HTTP calls. The Authorization header is formatted as such: `Authorization: Bearer <API-TOKEN>` (replace `<API-TOKEN>` with your token. If you don’t have a token, you can generate one for free from the Olostep [dashboard](https://www.olostep.com/dashboard/). Examples:

Python

Node

cURL

    # pip install requests
    
    import requests
    
    endpoint = 'https://api.olostep.com/v1/scrapes/<SCRAPE_ID>'
    headers = {
        'Authorization': 'Bearer <API-TOKEN>',
        'Accept': 'application/json'
    }
    
    response = requests.get(endpoint, headers=headers)
    print(response.status_code)
    print(response.json())
    

    // npm install node-fetch
    
    // ESM
    import fetch from 'node-fetch'
    
    const endpoint = 'https://api.olostep.com/v1/scrapes/<SCRAPE_ID>'
    const res = await fetch(endpoint, {
      headers: {
        'Authorization': 'Bearer <API-TOKEN>',
        'Accept': 'application/json'
      }
    })
    console.log(res.status)
    console.log(await res.json())
    

    curl -L -X GET 'https://api.olostep.com/v1/scrapes/<SCRAPE_ID>' \
      -H 'Accept: application/json' \
      -H 'Authorization: Bearer <API-TOKEN>'
    

[​

](#using-the-cli)

Using the CLI
--------------------------------------

The [Olostep CLI](/cli/overview) doesn’t use an API key. It signs in with your Olostep account:

    curl -fsSL https://cli.olostep.com | sh
    olostep login
    

Your browser opens the Olostep sign-in page. For CI, set `OLOSTEP_TOKEN`. See [CLI authentication](/cli/authentication). To put an API key into a `.env` file for your own code without printing it:

    olostep keys reveal <key> --write-env .env
    

[​

](#using-the-sdks)

Using the SDKs
----------------------------------------

The [Python](/sdks/python) and [Node.js](/sdks/node-js) SDKs read `OLOSTEP_API_KEY` from the environment, or accept the key directly when you construct the client.

Was this page helpful?

YesNo
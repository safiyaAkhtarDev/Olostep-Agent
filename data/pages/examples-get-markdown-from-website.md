<!-- source: https://docs.olostep.com/examples/get-markdown-from-website -->
# https://docs.olostep.com/examples/get-markdown-from-website

Get the Markdown of a Website - Olostep Docs  

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

Examples

Get the Markdown of a Website

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Examples

Get the Markdown of a Website
=============================

Copy pageCopy page

Learn how to extract content as LLM-friendly markdown from any web page.

Copy pageCopy page

[​

](#overview)

Overview
----------------------------

Olostep’s [scrape](/features/scrapes) endpoint allows to extract content from any website. Content in markdown is useful if you want to feed it to an LLM without all the HTML. In this guide we will see how to extract markdown from a website like `https://www.nea.com/team`.

[​

](#prerequisites)

Prerequisites
--------------------------------------

Before getting started, ensure you have the following:

*   A valid Olostep API key. You can get one by signing up at [Olostep](https://www.olostep.com/dashboard).
*   Python installed on your system
*   The `requests` and `json` libraries (these come pre-installed with Python, but you can install them using `pip install requests` if needed)

[​

](#extracting-text-from-a-website)

Extracting Text from a Website
------------------------------------------------------------------------

The following Python script demonstrates how to extract text and markdown content from a website using Olostep’s API.

    import requests
    import json
    
    url = "https://api.olostep.com/v1/scrapes"
    
    payload = {
        "url_to_scrape": "https://www.nea.com/team",
        "country": "US",
        "formats": ["markdown"],
        "wait_before_scraping": 0,
        "remove_css_selectors": "default",
    }
    
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print(json.dumps(response.json(), indent=4))
    

[​

](#example-response)

Example Response
--------------------------------------------

A successful response will look something like this:

    {
        "id": "scrape_63x2e5sf5r",
        "object": "scrape",
        "created": 1740341743,
        "metadata": {},
        "retrieve_id": "63x2e5sf5r",
        "url_to_scrape": "https://www.nea.com/team",
        "result": {
            "html_content": null,
            "markdown_content": "NEA ….",
            "text_content": null,
            "json_content": null,
            "llm_extract": null,
            "screenshot_hosted_url": null,
            "html_hosted_url": null,
            "markdown_hosted_url": "https://olostep-storage.s3.us-east-1.amazonaws.com/markDown_63x2e5sf5r.txt",
            "json_hosted_url": null,
            "text_hosted_url": null,
            "links_on_page": [],
            "page_metadata": {
                "status_code": 200,
                "title": ""
            }
        }
    }
    

[​

](#explanation)

Explanation
----------------------------------

*   `url_to_scrape`: specifies the website URL to extract content from.
*   `formats`: defines the output formats (text in this case).
*   `Authorization`: contains your API key to authenticate the request.
*   The response is formatted as JSON and printed for readability.

[​

](#conclusion)

Conclusion
--------------------------------

Using Olostep, you can easily extract markdown content from any website. This is useful if you want to get content from a website and feed it to an LLM for data extraction and analysis. If you want to extract content at scale from the same website over and over (e.g. monitoring data, price tracking, etc…) we recommend using a [custom parser](/features/structured-content/parsers) to get the content in JSON format.

Was this page helpful?

YesNo
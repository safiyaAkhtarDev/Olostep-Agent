<!-- source: https://docs.olostep.com/features/structured-content/llm-extraction -->
# https://docs.olostep.com/features/structured-content/llm-extraction

Using LLM Extraction - Olostep Docs  

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

Structured Data

Using LLM Extraction

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Structured Data

Using LLM Extraction
====================

Copy pageCopy page

Copy pageCopy page

For websites with changing structures or one-off extraction needs, Olostep offers LLM-powered extraction. This approach:

*   Feeds the content to a Large Language Model
*   Instructs the model to parse and return only the specified data
*   Returns a clean JSON structure containing exactly what you need

    import requests
    import json
    
    def extract_with_llm():
        url = "https://api.olostep.com/v1/scrapes"
    
        headers = {
            "Authorization": "Bearer <API_KEY>",
            "Content-Type": "application/json"
        }
    
        data = {
            "url_to_scrape": "https://www.berklee.edu/events/stefano-marchese-friends",
            "formats": [
                "markdown", 
                "json"
            ],
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
                                "start_time": {"type": "string"},
                            },
                        }
                    },
                }
            },
        }
    
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
    
        # The LLM extract will be available in the result
        print(json.dumps(result, indent=2))
    
        return result
    
    if __name__ == "__main__":
        extract_with_llm()
    

You can either pass the `schema` or a `prompt` to the LLM.

    
    import requests
    import json
    
    def extract_with_llm():
        url = "https://api.olostep.com/v1/scrapes"
    
        headers = {
            "Authorization": "Bearer <API_KEY>",
            "Content-Type": "application/json"
        }
    
        data = {
            "url_to_scrape": "https://www.berklee.edu/events/stefano-marchese-friends",
            "formats": [
                "markdown", 
                "json"
            ],
            "llm_extract": {
                "prompt": "Extract the event title, date, description, venue, address, and start time from the event page."
            },
        }
    
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
    
        # The LLM extract will be available in the result
        print(json.dumps(result, indent=2))
    
        return result
    
    if __name__ == "__main__":
        extract_with_llm()
    

The `prompt` is a natural language string that is passed to the LLM to extract the data. The LLM decides how to extract the data based on the prompt. You can use this when you don’t want to use a `schema`. Sample Response:

    {
        "id": "scrape_94iqy385ty",
        ...
        "result": {
            "json_content":  "{\"event\":{\"title\":\"Stefano Marchese and Friends\",\"date\":\"Wednesday / January 22, 2025\",\"description\":\"Join acclaimed Italian singer-songwriter and educator Stefano Marchese for an unforgettable evening of musical magic as he takes the stage alongside a constellation of extraordinary talent in a concert titled Concerto di Duetti.\",\"venue\":\"David Friend Recital Hall (DFRH)\",\"address\":\"921 Boylston Street Boston MA 02115 United States\",\"start_time\":\"7:30 p.m. (EST)\"}}"
        }
    }
    

json\_content is the stringified JSON content of the event. You can access it as a JSON object by parsing the string.

    import json
    
    event = json.loads(result["json_content"])
    print(event["event"]["title"])
    

Was this page helpful?

YesNo
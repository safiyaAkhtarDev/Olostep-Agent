<!-- source: https://docs.olostep.com/sdks/node-js -->
# https://docs.olostep.com/sdks/node-js

Olostep NodeJS SDK - Olostep Docs  

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

SDKs

Olostep NodeJS SDK

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

SDKs

Olostep NodeJS SDK
==================

Copy pageCopy page

Official NodeJS SDK to search, extract and structure data from the Web

Copy pageCopy page

**NPM Package**: [olostep](https://www.npmjs.com/package/olostep)

[​

](#getting-started)

Getting started
------------------------------------------

    npm install olostep
    

camelCase

snake\_case

    import Olostep from 'olostep';
    
    const client = new Olostep({apiKey: process.env.OLOSTEP_API_KEY});
    
    // Minimal scrape example
    const result = await client.scrapes.create('https://example.com');
    console.log(result.id, result.html_content);
    

    import Olostep from 'olostep';
    
    const client = new Olostep({api_key: process.env.OLOSTEP_API_KEY});
    
    // Minimal scrape example
    const result = await client.scrapes.create('https://example.com');
    console.log(result.id, result.html_content);
    

The NodeJS SDK accepts both **camelCase** and **snake\_case** for all parameters. Use **snake\_case** if you’re building for AI agents, it matches the API’s native field names.

[​

](#usage)

Usage
----------------------

### 

[​

](#scraping)

Scraping

Scrape a single URL with various options:

camelCase

snake\_case

    import Olostep, {Format} from 'olostep';
    
    const client = new Olostep({apiKey: 'your_api_key'});
    
    // Simple scrape
    const scrape = await client.scrapes.create('https://example.com');
    
    // With multiple formats
    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: [Format.HTML, Format.MARKDOWN, Format.TEXT],
      waitBeforeScraping: 1000,
      removeImages: true
    });
    
    // Access the content
    console.log(scrape.html_content);
    console.log(scrape.markdown_content);
    
    // Get scrape by ID
    const fetched = await client.scrapes.get(scrape.id);
    

    import Olostep, {Format} from 'olostep';
    
    const client = new Olostep({api_key: 'your_api_key'});
    
    // Simple scrape
    const scrape = await client.scrapes.create('https://example.com');
    
    // With multiple formats
    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: [Format.HTML, Format.MARKDOWN, Format.TEXT],
      wait_before_scraping: 1000,
      remove_images: true
    });
    
    // Access the content
    console.log(scrape.html_content);
    console.log(scrape.markdown_content);
    
    // Get scrape by ID
    const fetched = await client.scrapes.get(scrape.id);
    

### 

[​

](#batch-processing)

Batch Processing

Process multiple URLs in a single batch:

camelCase

snake\_case

    // Using URL strings (custom IDs auto-generated)
    const batch = await client.batches.create([
      'https://example.com',
      'https://example.org',
      'https://example.net'
    ]);
    
    // Or with explicit custom IDs
    const batch = await client.batches.create([
      {url: 'https://example.com', customId: 'site-1'},
      {url: 'https://example.org', customId: 'site-2'}
    ]);
    
    console.log(`Batch ${batch.id} created with ${batch.total_urls} URLs`);
    
    // Wait for completion
    await batch.waitTillDone({
      checkEveryNSecs: 5,
      timeoutSeconds: 120
    });
    
    // Get batch info
    const info = await batch.info();
    console.log(info);
    
    // Stream individual results
    for await (const item of batch.items()) {
      console.log(item.custom_id);
    }
    

    // Using URL strings (custom IDs auto-generated)
    const batch = await client.batches.create([
      'https://example.com',
      'https://example.org',
      'https://example.net'
    ]);
    
    // Or with explicit custom IDs
    const batch = await client.batches.create([
      {url: 'https://example.com', custom_id: 'site-1'},
      {url: 'https://example.org', custom_id: 'site-2'}
    ]);
    
    console.log(`Batch ${batch.id} created with ${batch.total_urls} URLs`);
    
    // Wait for completion
    await batch.waitTillDone({
      check_every_n_secs: 5,
      timeout_seconds: 120
    });
    
    // Get batch info
    const info = await batch.info();
    console.log(info);
    
    // Stream individual results
    for await (const item of batch.items()) {
      console.log(item.custom_id);
    }
    

### 

[​

](#crawling)

Crawling

Crawl an entire website:

camelCase

snake\_case

    const crawl = await client.crawls.create({
      url: 'https://example.com',
      maxPages: 100,
      maxDepth: 3,
      includeUrls: ['*/blog/*'],
      excludeUrls: ['*/admin/*']
    });
    
    console.log(`Crawl ${crawl.id} started`);
    
    // Wait for completion
    await crawl.waitTillDone({
      checkEveryNSecs: 10,
      timeoutSeconds: 300
    });
    
    // Get crawl info
    const info = await crawl.info();
    console.log(`Crawled ${info.pages_crawled} pages`);
    
    // Stream crawled pages
    for await (const page of crawl.pages()) {
      console.log(page.url, page.status_code);
    }
    

    const crawl = await client.crawls.create({
      url: 'https://example.com',
      max_pages: 100,
      max_depth: 3,
      include_urls: ['*/blog/*'],
      exclude_urls: ['*/admin/*']
    });
    
    console.log(`Crawl ${crawl.id} started`);
    
    // Wait for completion
    await crawl.waitTillDone({
      check_every_n_secs: 10,
      timeout_seconds: 300
    });
    
    // Get crawl info
    const info = await crawl.info();
    console.log(`Crawled ${info.pages_crawled} pages`);
    
    // Stream crawled pages
    for await (const page of crawl.pages()) {
      console.log(page.url, page.status_code);
    }
    

### 

[​

](#site-mapping)

Site Mapping

Generate a sitemap of URLs from a website:

camelCase

snake\_case

    const map = await client.maps.create({
      url: 'https://example.com',
      topN: 100,
      includeSubdomain: true,
      searchQuery: 'blog posts'
    });
    
    console.log(`Map ${map.id} created`);
    
    // Stream URLs
    for await (const url of map.urls()) {
      console.log(url);
    }
    
    // Get map info
    const info = await map.info();
    

    const map = await client.maps.create({
      url: 'https://example.com',
      top_n: 100,
      include_subdomain: true,
      search_query: 'blog posts'
    });
    
    console.log(`Map ${map.id} created`);
    
    // Stream URLs
    for await (const url of map.urls()) {
      console.log(url);
    }
    
    // Get map info
    const info = await map.info();
    

### 

[​

](#ai-powered-answers)

AI-Powered Answers

Get answers from web pages using AI:

camelCase

snake\_case

    import Olostep from 'olostep';
    
    const client = new Olostep({apiKey: 'your_api_key'});
    
    // Simple task: pass a string directly
    const answer = await client.answers.create(
      'What is the main topic of https://example.com?'
    );
    console.log(answer.answer);
    console.log(answer.sources);
    
    // With structured JSON output
    const structured = await client.answers.create({
      task: 'Extract all product names and prices from https://example.com',
      jsonFormat: {
        products: [{name: '', price: ''}]
      }
    });
    console.log(structured.json_content);
    
    // Retrieve a previously created answer by ID
    const fetched = await client.answers.get(answer.id);
    console.log(fetched.answer);
    

    import Olostep from 'olostep';
    
    const client = new Olostep({api_key: 'your_api_key'});
    
    // Simple task: pass a string directly
    const answer = await client.answers.create(
      'What is the main topic of https://example.com?'
    );
    console.log(answer.answer);
    console.log(answer.sources);
    
    // With structured JSON output
    const structured = await client.answers.create({
      task: 'Extract all product names and prices from https://example.com',
      json_format: {
        products: [{name: '', price: ''}]
      }
    });
    console.log(structured.json_content);
    
    // Retrieve a previously created answer by ID
    const fetched = await client.answers.get(answer.id);
    console.log(fetched.answer);
    

### 

[​

](#content-retrieval)

Content Retrieval

Retrieve previously scraped content:

    // Get content in specific format(s)
    const content = await client.retrieve(retrieveId, Format.MARKDOWN);
    console.log(content.markdown_content);
    
    // Multiple formats
    const content = await client.retrieve(retrieveId, [
      Format.HTML,
      Format.MARKDOWN
    ]);
    

### 

[​

](#advanced-options)

Advanced Options

#### 

[​

](#custom-actions)

Custom Actions

Perform browser actions before scraping:

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      actions: [
        {type: 'wait', milliseconds: 2000},
        {type: 'click', selector: '#load-more'},
        {type: 'scroll', distance: 1000},
        {type: 'fill_input', selector: '#search', value: 'query'}
      ]
    });
    

#### 

[​

](#geographic-location)

Geographic Location

Scrape from different countries using predefined country codes or any valid country code string:

camelCase

snake\_case

    import Olostep, {Country} from 'olostep';
    
    const client = new Olostep({apiKey: 'your_api_key'});
    
    // Using predefined enum values (US, DE, FR, GB, SG)
    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      country: Country.DE  // Germany
    });
    
    // Or use any valid country code as a string
    const scrape2 = await client.scrapes.create({
      url: 'https://example.com',
      country: 'jp'  // Japan
    });
    

    import Olostep, {Country} from 'olostep';
    
    const client = new Olostep({api_key: 'your_api_key'});
    
    // Using predefined enum values (US, DE, FR, GB, SG)
    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      country: Country.DE  // Germany
    });
    
    // Or use any valid country code as a string
    const scrape2 = await client.scrapes.create({
      url: 'https://example.com',
      country: 'jp'  // Japan
    });
    

#### 

[​

](#caching)

Caching

By default, every scrape request fetches the page fresh (`max_age: 0`). Pass `maxAge` to reuse a recent result with the same parameters and improve response time. Value is in **seconds**; the maximum is 7 days (`604800`). See [Caching](/features/scrapes#caching) for details.

camelCase

snake\_case

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['markdown'],
      maxAge: 86400 // Accept results up to 1 day old
    });
    

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['markdown'],
      max_age: 86400 // Accept results up to 1 day old
    });
    

#### 

[​

](#storage)

Storage

By default, a scrape result is kept for about 7 days. Pass `storage.expires_in` as `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` to keep it longer. See [Storage](/features/scrapes#storage) for details.

camelCase

snake\_case

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['markdown'],
      storage: { expires_in: '90d' }
    });
    

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['markdown'],
      storage: { expires_in: '90d' }
    });
    

#### 

[​

](#llm-extraction)

LLM Extraction

Extract structured data using LLMs. `schema` is a JSON Schema with an object at the top level:

camelCase

snake\_case

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['json'],
      llmExtract: {
        schema: {
          type: 'object',
          properties: {
            title: { type: 'string' },
            price: { type: 'number' },
            description: { type: 'string' }
          }
        },
        prompt: 'Extract product information from this page'
      }
    });
    

    const scrape = await client.scrapes.create({
      url: 'https://example.com',
      formats: ['json'],
      llm_extract: {
        schema: {
          type: 'object',
          properties: {
            title: { type: 'string' },
            price: { type: 'number' },
            description: { type: 'string' }
          }
        },
        prompt: 'Extract product information from this page'
      }
    });
    

### 

[​

](#client-configuration)

Client Configuration

camelCase

snake\_case

    import Olostep from 'olostep';
    
    const client = new Olostep({
      apiKey: 'your_api_key',
      apiBaseUrl: 'https://api.olostep.com/v1',  // optional
      timeoutMs: 150000,  // 150 seconds (optional)
      retry: {
        maxRetries: 3,
        initialDelayMs: 1000
      },
      userAgent: 'MyApp/1.0'  // optional
    });
    

    import Olostep from 'olostep';
    
    const client = new Olostep({
      api_key: 'your_api_key',
      api_base_url: 'https://api.olostep.com/v1',  // optional
      timeout_ms: 150000,  // 150 seconds (optional)
      retry: {
        max_retries: 3,
        initial_delay_ms: 1000
      },
      user_agent: 'MyApp/1.0'  // optional
    });
    

### 

[​

](#feature-highlights)

Feature highlights

*   Async-first client with full TypeScript support.
*   Type-safe inputs using TypeScript enums and interfaces (Formats, Countries, Actions, etc.).
*   Rich resource namespaces with both shorthand calls (`client.scrapes.create()`) and explicit methods (`client.scrapes.get()`).
*   Shared transport layer with retries, timeouts, and JSON decoding.
*   Comprehensive error hierarchy

Was this page helpful?

YesNo
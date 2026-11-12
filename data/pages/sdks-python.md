<!-- source: https://docs.olostep.com/sdks/python -->
# https://docs.olostep.com/sdks/python

Olostep Python SDK - Olostep Docs  

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

Olostep Python SDK

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

SDKs

Olostep Python SDK
==================

Copy pageCopy page

Official Python SDK to search, extract and structure data from the Web

Copy pageCopy page

**PyPI Package**: [olostep](https://pypi.org/project/olostep/) | **Requirements**: Python 3.11+

[​

](#installation)

Installation
------------------------------------

pip

pip3

poetry

uv

    pip install olostep
    

    pip3 install olostep
    

    poetry add olostep
    

    uv pip install olostep
    

[​

](#authentication)

Authentication
----------------------------------------

Get your API key from the [Olostep Dashboard](https://www.olostep.com/dashboard/).

[​

](#quick-start)

Quick Start
----------------------------------

The SDK provides two client options depending on your use case:

Sync Client (`Olostep`)
-----------------------

Best for: Scripts and simple use cases where you prefer blocking operations.  
  
The sync client provides a simpler, blocking interface that’s easier to get started with if you’re new to async/await.

Async Client (`AsyncOlostep`)
-----------------------------

Best for: Production applications, and handling many concurrent requests.  
  
The async client provides non-blocking operations and is the recommended choice for production applications that need high throughput.

[​

](#sync-client-olostep)

Sync Client (Olostep)
====================================================

The sync client (`Olostep`) provides a blocking interface that’s perfect for scripts and simple use cases.

    from olostep import Olostep
    
    # Provide the API key either via passing in the 'api_key' parameter or
    # by setting the OLOSTEP_API_KEY environment variable
    
    # The sync client handles resource management automatically
    # No explicit close needed - resources are cleaned up after each operation
    client = Olostep(api_key="YOUR_REAL_KEY")
    scrape_result = client.scrapes.create(url_to_scrape="https://example.com")
    

### 

[​

](#basic-web-scraping)

Basic Web Scraping

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Simple scraping
    result = client.scrapes.create(url_to_scrape="https://example.com")
    print(f"Scraped {len(result.html_content)} characters")
    
    # Multiple formats
    result = client.scrapes.create(
        url_to_scrape="https://example.com",
        formats=["html", "markdown"]
    )
    print(f"HTML: {len(result.html_content)} chars")
    print(f"Markdown: {len(result.markdown_content)} chars")
    

### 

[​

](#batch-processing)

Batch Processing

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Process multiple URLs efficiently
    batch = client.batches.create(
        urls=[
            "https://www.google.com/search?q=python",
            "https://www.google.com/search?q=javascript",
            "https://www.google.com/search?q=typescript"
        ]
    )
    
    # Wait for completion and process results
    for item in batch.items():
        content = item.retrieve(["html"])
        print(f"Processed {item.url}: {len(content.html_content)} bytes")
    

### 

[​

](#smart-web-crawling)

Smart Web Crawling

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Crawl with intelligent filtering
    crawl = client.crawls.create(
        start_url="https://www.bbc.com",
        max_pages=100,
        include_urls=["/articles/**", "/blog/**"],
        exclude_urls=["/admin/**"]
    )
    
    for page in crawl.pages():
        content = page.retrieve(["html"])
        print(f"Crawled: {page.url}")
    

### 

[​

](#site-mapping)

Site Mapping

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Extract all links from a website
    maps = client.maps.create(url="https://example.com")
    
    # Get all discovered URLs
    urls = []
    for url in maps.urls():
        urls.append(url)
        if len(urls) >= 10:  # Limit for demo
            break
    
    print(f"Found {len(urls)} URLs")
    

### 

[​

](#ai-powered-answers)

AI-Powered Answers

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Get answers from web pages using AI
    answer = client.answers.create(
        task="What is the main topic of https://example.com?"
    )
    print(f"Answer: {answer.answer}")
    

[​

](#async-client-asyncolostep)

Async Client (AsyncOlostep)
================================================================

The async client (`AsyncOlostep`) is the recommended client for high-performance applications, backend services, and when you need to handle many concurrent requests.

    from olostep import AsyncOlostep
    
    # Provide the API key either via passing in the 'api_key' parameter or
    # by setting the OLOSTEP_API_KEY environment variable
    
    # RESOURCE MANAGEMENT
    # ===================
    # The SDK supports two usage patterns for resource management:
    
    # 1. Context Manager (Recommended for one-off usage):
    #    Automatically handles resource cleanup
    async with AsyncOlostep(api_key="YOUR_REAL_KEY") as client:
        scrape_result = await client.scrapes.create(url_to_scrape="https://example.com")
    # Transport is automatically closed here
    
    # 2. Explicit Close (For long-lived services):
    #    Requires manual resource cleanup
    client = AsyncOlostep(api_key="YOUR_REAL_KEY")
    try:
        scrape_result = await client.scrapes.create(url_to_scrape="https://example.com")
    finally:
        await client.close()  # Manually close the transport
    

### 

[​

](#basic-web-scraping-2)

Basic Web Scraping

    import asyncio
    from olostep import AsyncOlostep
    
    async def main():
        async with AsyncOlostep(api_key="your-api-key") as client:
            # Simple scraping
            result = await client.scrapes.create(url_to_scrape="https://example.com")
            print(f"Scraped {len(result.html_content)} characters")
    
            # Multiple formats
            result = await client.scrapes.create(
                url_to_scrape="https://example.com",
                formats=["html", "markdown"]
            )
            print(f"HTML: {len(result.html_content)} chars")
            print(f"Markdown: {len(result.markdown_content)} chars")
    
    asyncio.run(main())
    

### 

[​

](#batch-processing-2)

Batch Processing

    import asyncio
    from olostep import AsyncOlostep
    
    async def main():
        async with AsyncOlostep(api_key="your-api-key") as client:
            # Process multiple URLs efficiently
            batch = await client.batches.create(
                urls=[
                    "https://www.google.com/search?q=python",
                    "https://www.google.com/search?q=javascript",
                    "https://www.google.com/search?q=typescript"
                ]
            )
    
            # Wait for completion and process results
            async for item in batch.items():
                content = await item.retrieve(["html"])
                print(f"Processed {item.url}: {len(content.html_content)} bytes")
    
    asyncio.run(main())
    

### 

[​

](#smart-web-crawling-2)

Smart Web Crawling

    import asyncio
    from olostep import AsyncOlostep
    
    async def main():
        async with AsyncOlostep(api_key="your-api-key") as client:
            # Crawl with intelligent filtering
            crawl = await client.crawls.create(
                start_url="https://www.bbc.com",
                max_pages=100,
                include_urls=["/articles/**", "/blog/**"],
                exclude_urls=["/admin/**"]
            )
    
            async for page in crawl.pages():
                content = await page.retrieve(["html"])
                print(f"Crawled: {page.url}")
    
    asyncio.run(main())
    

### 

[​

](#site-mapping-2)

Site Mapping

    import asyncio
    from olostep import AsyncOlostep
    
    async def main():
        async with AsyncOlostep(api_key="your-api-key") as client:
            # Extract all links from a website
            maps = await client.maps.create(url="https://example.com")
    
            # Get all discovered URLs
            urls = []
            async for url in maps.urls():
                urls.append(url)
                if len(urls) >= 10:  # Limit for demo
                    break
    
            print(f"Found {len(urls)} URLs")
    
    asyncio.run(main())
    

### 

[​

](#ai-powered-answers-2)

AI-Powered Answers

    import asyncio
    from olostep import AsyncOlostep
    
    async def main():
        async with AsyncOlostep(api_key="your-api-key") as client:
            # Get answers from web pages using AI
            answer = await client.answers.create(
                task="What is the main topic of https://example.com?"
            )
            print(f"Answer: {answer.answer}")
    
    asyncio.run(main())
    

[​

](#sdk-reference)

SDK Reference
--------------------------------------

### 

[​

](#method-structure)

Method Structure

Both SDK clients provide the same clean, pythonic interface organized into logical namespaces:

Namespace

Purpose

Key Methods

`scrapes`

Single URL extraction

`create()`, `get()`

`batches`

Multi-URL processing

`create()`, `info()`, `items()`

`crawls`

Website traversal

`create()`, `info()`, `pages()`

`maps`

Link extraction

`create()`, `urls()`

`answers`

AI-powered extraction

`create()`, `get()`

`retrieve`

Content retrieval

`get()`

Each operation returns stateful objects with ergonomic methods for follow-up operations.

[​

](#error-handling)

Error Handling
----------------------------------------

Catch all SDK errors using the base exception class:

    from olostep import Olostep, Olostep_BaseError
    
    client = Olostep(api_key="your-api-key")
    
    try:
        result = client.scrapes.create(url_to_scrape="https://example.com")
    except Olostep_BaseError as e:
        print(f"Error has occurred: {type(e).__name__}")
        print(f"Error message: {e}")
    

For detailed error handling information, including the full exception hierarchy and granular error handling options, see [Detailed Error Handling](/sdks/python#detailed-error-handling).

[​

](#automatic-retries)

Automatic Retries
----------------------------------------------

The SDK automatically retries on transient errors (network issues, temporary server problems) based on the `RetryStrategy` configuration. You can customize the retry behavior by passing a `RetryStrategy` instance when creating the client:

    from olostep import Olostep, RetryStrategy
    
    retry_strategy = RetryStrategy(
        max_retries=3,
        initial_delay=1.0,
        jitter_min=0.2,
        jitter_max=0.8
    )
    
    client = Olostep(api_key="your-api-key", retry_strategy=retry_strategy)
    result = client.scrapes.create("https://example.com")
    

For detailed retry configuration options and best practices, see [Retry Strategy](/sdks/python#retry-strategy-configuration).

[​

](#advanced-features)

Advanced Features
----------------------------------------------

### 

[​

](#smart-input-coercion)

Smart Input Coercion

The SDK intelligently handles various input formats for maximum convenience:

    from olostep import Olostep, Country
    
    client = Olostep(api_key="your-api-key")
    
    # Formats: string, list, or enum
    client.scrapes.create(url_to_scrape="https://example.com", formats="html")
    client.scrapes.create(url_to_scrape="https://example.com", formats=["html", "markdown"])
    
    # Countries: case-insensitive strings or enums
    client.scrapes.create(url_to_scrape="https://example.com", country="us")
    client.scrapes.create(url_to_scrape="https://example.com", country=Country.US)
    
    # Lists: single values or lists
    client.batches.create(urls="https://example.com")    # Single URL
    client.batches.create(urls=["https://a.com", "https://b.com"])  # Multiple URLs
    

### 

[​

](#advanced-scraping-options)

Advanced Scraping Options

    from olostep import Olostep, Format, Country, WaitAction, FillInputAction
    
    client = Olostep(api_key="your-api-key")
    
    # Full control over scraping behavior
    result = client.scrapes.create(
        url_to_scrape="https://news.google.com/",
        wait_before_scraping=3000,
        formats=[Format.HTML, Format.MARKDOWN],
        remove_css_selectors=["script", ".popup"],
        actions=[
            WaitAction(milliseconds=1500),
            FillInputAction(selector="searchbox", value="olostep")
        ],
        parser="@olostep/google-news",
        country=Country.US,
        remove_images=True
    )
    

### 

[​

](#caching)

Caching

By default, every scrape request fetches the page fresh (`max_age=0`). Pass `max_age` to reuse a recent result with the same parameters and improve response time. Value is in **seconds**; the maximum is 7 days (`604800`). See [Caching](/features/scrapes#caching) for details.

    # Opt-in to caching: accept results up to 1 day (86400 seconds) old
    result = client.scrapes.create(
        url_to_scrape="https://example.com",
        formats=["markdown"],
        max_age=86400
    )
    

### 

[​

](#storage)

Storage

By default, a scrape result is kept for about 7 days. Pass `storage` with `expires_in` set to `10d`, `30d`, `60d`, `90d`, `180d`, `365d`, or `never` to keep it longer. See [Storage](/features/scrapes#storage) for details.

    result = client.scrapes.create(
        url_to_scrape="https://example.com",
        formats=["markdown"],
        storage={"expires_in": "90d"}
    )
    

### 

[​

](#batch-processing-with-custom-ids)

Batch Processing with Custom IDs

    from olostep import Olostep, Country
    
    client = Olostep(api_key="your-api-key")
    
    batch = client.batches.create([
        {"url": "https://www.google.com/search?q=python", "custom_id": "search_1"},
        {"url": "https://www.google.com/search?q=javascript", "custom_id": "search_2"},
        {"url": "https://www.google.com/search?q=typescript", "custom_id": "search_3"}
    ],
    country=Country.US,
    parser="@olostep/google-search"
    )
    
    # Process results by custom ID
    # When using a parser, retrieve JSON content instead of HTML
    for item in batch.items():
        if item.custom_id == "search_2":
            content = item.retrieve(["json"])
            print(f"Search result: {content.json_content}")
    

### 

[​

](#intelligent-crawling)

Intelligent Crawling

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Crawl with intelligent filtering
    crawl = client.crawls.create(
        start_url="https://www.bbc.com",
        max_pages=1000,
        max_depth=3,
        include_urls=["/articles/**", "/news/**"],
        exclude_urls=["/ads/**", "/tracking/**"],
        include_external=False,
        include_subdomain=True,
    )
    
    for page in crawl.pages():
        content = page.retrieve(["html"])
        print(f"Crawled: {page.url}")
    

### 

[​

](#site-mapping-with-filters)

Site Mapping with Filters

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Extract all links with advanced filtering
    maps = client.maps.create(
        url="https://www.bbc.com",
        include_subdomain=True,
        include_urls=["/articles/**", "/news/**"],
        exclude_urls=["/ads/**", "/tracking/**"]
    )
    
    # Get filtered URLs
    urls = []
    for url in maps.urls():
        urls.append(url)
    
    print(f"Found {len(urls)} relevant URLs")
    

### 

[​

](#answers-retrieval)

Answers Retrieval

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # First create an answer
    created_answer = client.answers.create(
        task="What is the main topic of https://example.com?"
    )
    
    # Then retrieve it using the ID
    answer = client.answers.get(answer_id=created_answer.id)
    print(f"Answer: {answer.answer}")
    

### 

[​

](#content-retrieval)

Content Retrieval

    from olostep import Olostep
    
    client = Olostep(api_key="your-api-key")
    
    # Get content by retrieve ID
    result = client.retrieve.get(retrieve_id="ret_123")
    
    # Get multiple formats
    result = client.retrieve.get(retrieve_id="ret_123", formats=["html", "markdown", "text", "json"])
    

[​

](#logging)

Logging
--------------------------

Enable logging to debug issues:

    import logging
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("olostep")
    logger.setLevel(logging.INFO)  # Use DEBUG for verbose output
    

**Log Levels**: `INFO` (recommended), `DEBUG` (verbose), `WARNING`, `ERROR`

[​

](#retry-strategy-configuration)

Retry Strategy Configuration
--------------------------------------------------------------------

The `RetryStrategy` class controls how the Olostep SDK handles transient API errors through automatic retries with exponential backoff and jitter. This helps ensure reliable operation in production environments where temporary network issues, rate limits, and server overload can cause intermittent failures.

### 

[​

](#default-behavior)

Default Behavior

By default, the SDK uses the following retry configuration:

*   **Max retries**: 5 attempts
*   **Initial delay**: 2 seconds
*   **Backoff**: Exponential (2^attempt)
*   **Jitter**: 10-90% of delay (randomized)

This means:

*   Attempt 1: Immediate
*   Attempt 2: ~2-3.6s delay
*   Attempt 3: ~4-7.2s delay
*   Attempt 4: ~8-14.4s delay
*   Attempt 5: ~16-28.8s delay

Maximum duration: ~57 seconds for all retries (worst case)

### 

[​

](#custom-configuration)

Custom Configuration

    from olostep import AsyncOlostep, RetryStrategy
    
    # Create custom retry strategy
    retry_strategy = RetryStrategy(
        max_retries=3,
        initial_delay=1.0,
        jitter_min=0.2,  # 20% minimum jitter
        jitter_max=0.8,  # 80% maximum jitter
    )
    
    # Use with client
    async with AsyncOlostep(
        api_key="your-api-key",
        retry_strategy=retry_strategy
    ) as client:
        result = await client.scrapes.create("https://example.com")
    

### 

[​

](#when-retries-happen)

When Retries Happen

The SDK automatically retries on:

*   **Temporary server issues** (`OlostepServerError_TemporaryIssue`)
*   **Timeout responses** (`OlostepServerError_NoResultInResponse`)

Other errors (authentication, validation, resource not found, etc.) fail immediately without retry.

### 

[​

](#transport-vs-caller-retries)

Transport vs Caller Retries

The SDK has two retry layers:

1.  **Transport layer**: Handles network-level connection failures (DNS, timeouts, etc.)
2.  **Caller layer**: Handles API-level transient errors (controlled by `RetryStrategy`)

Both layers are independent and have separate configuration. The total maximum duration is the sum of both layers.

### 

[​

](#calculating-max-duration)

Calculating Max Duration

    retry_strategy = RetryStrategy(max_retries=5, initial_delay=2.0)
    max_duration = retry_strategy.max_duration()
    print(f"Max call duration: {max_duration:.2f}s")
    

### 

[​

](#configuration-examples)

Configuration Examples

Here are some examples of how to configure the retry strategy for different use cases.

#### 

[​

](#conservative-strategy)

Conservative Strategy

    # Fewer retries, shorter delays
    retry_strategy = RetryStrategy(
        max_retries=3,
        initial_delay=1.0,
        jitter_min=0.2,
        jitter_max=0.8
    )
    # Max duration: ~12.6s
    

#### 

[​

](#aggressive-strategy)

Aggressive Strategy

    # More retries for critical operations
    retry_strategy = RetryStrategy(
        max_retries=10,
        initial_delay=0.5
    )
    # Max duration: ~969.75s
    

#### 

[​

](#no-retries-fail-fast)

No Retries (Fail Fast)

    # Disable retries for immediate failure feedback
    retry_strategy = RetryStrategy(max_retries=0)
    
    client = AsyncOlostep(api_key="your-api-key", retry_strategy=retry_strategy)
    

#### 

[​

](#high-throughput-strategy)

High-Throughput Strategy

    # Optimized for high-volume operations
    retry_strategy = RetryStrategy(
        max_retries=2,
        initial_delay=0.5,
        jitter_min=0.1,
        jitter_max=0.3  # Lower jitter for more predictable timing
    )
    # Max duration: ~1.95s
    

### 

[​

](#understanding-jitter)

Understanding Jitter

Jitter adds randomization to prevent “thundering herd” problems when many clients retry simultaneously. The jitter is calculated as:

    base_delay = initial_delay * (2 ** attempt)
    jitter_range = base_delay * (jitter_max - jitter_min)
    jitter = random.uniform(base_delay * jitter_min, base_delay * jitter_min + jitter_range)
    final_delay = base_delay + jitter
    

For example, with `initial_delay=2.0`, `jitter_min=0.1`, `jitter_max=0.9`:

*   Attempt 0: base=2.0s, jitter=0.2-1.8s, final=2.2-3.8s
*   Attempt 1: base=4.0s, jitter=0.4-3.6s, final=4.4-7.6s
*   Attempt 2: base=8.0s, jitter=0.8-7.2s, final=8.8-15.2s

### 

[​

](#best-practices)

Best Practices

#### 

[​

](#for-production-applications)

For Production Applications

    # Balanced approach for production
    retry_strategy = RetryStrategy(
        max_retries=5,
        initial_delay=2.0,
        jitter_min=0.1,
        jitter_max=0.9
    )
    

#### 

[​

](#for-development/testing)

For Development/Testing

    # Fast feedback for development
    retry_strategy = RetryStrategy(
        max_retries=2,
        initial_delay=0.5,
        jitter_min=0.1,
        jitter_max=0.3
    )
    

#### 

[​

](#for-batch-operations)

For Batch Operations

    # Conservative for large batch jobs
    retry_strategy = RetryStrategy(
        max_retries=3,
        initial_delay=1.0,
        jitter_min=0.2,
        jitter_max=0.8
    )
    

### 

[​

](#monitoring-and-debugging)

Monitoring and Debugging

The SDK logs retry information at the DEBUG level:

    DEBUG: Temporary issue, retrying in 2.34s
    DEBUG: No result in response, retrying in 4.67s
    

Enable debug logging to monitor retry behavior:

    import logging
    logging.getLogger("olostep").setLevel(logging.DEBUG)
    

### 

[​

](#error-handling-2)

Error Handling

When all retries are exhausted, the original error is raised:

    try:
        result = await client.scrapes.create("https://example.com")
    except OlostepServerError_TemporaryIssue as e:
        print(f"Failed after all retries: {e}")
        # Handle the permanent failure
    

### 

[​

](#performance-considerations)

Performance Considerations

*   **Memory**: Each retry attempt uses additional memory for request/response objects
*   **Time**: Total operation time can be significantly longer with retries enabled
*   **API Limits**: Retries count against your API usage limits
*   **Network**: More network traffic due to retry attempts

Choose your retry strategy based on your application’s requirements for reliability vs. performance.

[​

](#detailed-error-handling)

Detailed Error Handling
----------------------------------------------------------

### 

[​

](#exception-hierarchy)

Exception Hierarchy

The Olostep SDK provides a comprehensive exception hierarchy for different failure scenarios. All exceptions inherit from `Olostep_BaseError`. There are three main error types that directly inherit from `Olostep_BaseError`:

1.  **`Olostep_APIConnectionError`** - Network-level connection failures
2.  **`OlostepServerError_BaseError`** - Errors raised (sort of) by the API server
3.  **`OlostepClientError_BaseError`** - Errors raised by the client SDK

### 

[​

](#why-connection-errors-are-separate)

Why Connection Errors Are Separate

`Olostep_APIConnectionError` is separate from server errors because it represents network-level failures that occur before the API can process the request. These are transport layer issues (DNS or HTTP failures, timeouts, connection refused, etc.) rather than API-level errors. HTTP status codes (4xx, 5xx) are considered API responses and are categorized as server errors, even though they indicate problems.

    Olostep_BaseError
    ├── Olostep_APIConnectionError
    ├── OlostepServerError_BaseError
    │   ├── OlostepServerError_TemporaryIssue
    │   │   ├── OlostepServerError_NetworkBusy
    │   │   └── OlostepServerError_InternalNetworkIssue
    │   ├── OlostepServerError_RequestUnprocessable
    │   │   ├── OlostepServerError_ParserNotFound
    │   │   └── OlostepServerError_OutOfResources
    │   ├── OlostepServerError_BlacklistedDomain
    │   ├── OlostepServerError_FeatureApprovalRequired
    │   ├── OlostepServerError_AuthFailed
    │   ├── OlostepServerError_CreditsExhausted
    │   ├── OlostepServerError_InvalidEndpointCalled
    │   ├── OlostepServerError_ResourceNotFound
    │   ├── OlostepServerError_NoResultInResponse
    │   └── OlostepServerError_UnknownIssue
    └── OlostepClientError_BaseError
        ├── OlostepClientError_RequestValidationFailed
        ├── OlostepClientError_ResponseValidationFailed
        ├── OlostepClientError_NoAPIKey
        ├── OlostepClientError_AsyncContext
        ├── OlostepClientError_BetaFeatureAccessRequired
        └── OlostepClientError_Timeout
    

### 

[​

](#recommended-error-handling)

Recommended Error Handling

For most use cases, catch the base error and print the error name:

    from olostep import AsyncOlostep, Olostep_BaseError
    
    try:
        result = await client.scrapes.create(url_to_scrape="https://example.com")
    except Olostep_BaseError as e:
        print(f"Error has occurred: {type(e).__name__}")
        print(f"Error message: {e}")
    

This approach catches all SDK errors and provides clear information about what went wrong. The error name (e.g., `OlostepServerError_AuthFailed`) is descriptive enough to understand the issue.

### 

[​

](#granular-error-handling)

Granular Error Handling

If you need more specific error handling, catch the specific error types directly. **Avoid using `OlostepServerError_BaseError` or `OlostepClientError_BaseError`** - these base classes only indicate who raised the error (server vs client), not who’s responsible for fixing it. This is an implementation detail that doesn’t help with error handling logic. Instead, catch specific error types that indicate the actual problem:

    from olostep import (
        AsyncOlostep,
        Olostep_BaseError,
        Olostep_APIConnectionError,
        OlostepServerError_AuthFailed,
        OlostepServerError_CreditsExhausted,
        OlostepClientError_NoAPIKey,
    )
    
    try:
        result = await client.scrapes.create(url_to_scrape="https://example.com")
    except Olostep_APIConnectionError as e:
        print(f"Network error: {type(e).__name__}")
    except OlostepServerError_AuthFailed:
        print("Invalid API key")
    except OlostepServerError_CreditsExhausted:
        print("Credits exhausted")
    except OlostepClientError_NoAPIKey:
        print("API key not provided")
    except Olostep_BaseError as e:
        print(f"Error has occurred: {type(e).__name__}")
    

[​

](#configuration)

Configuration
--------------------------------------

### 

[​

](#environment-variables)

Environment Variables

Variable

Description

Default

`OLOSTEP_API_KEY`

Your API key

Required

`OLOSTEP_BASE_API_URL`

API base URL

`https://api.olostep.com/v1`

`OLOSTEP_API_TIMEOUT`

Request timeout (seconds)

`150`

[​

](#getting-help)

Getting Help
------------------------------------

*   [Full Documentation](https://docs.olostep.com)
*   [Community Slack](https://join.slack.com/t/olostep-users/shared_invite/zt-2pn2ce0uu-~591qIdhAfJy~LXCWQS5UQ)
*   [Support Email](mailto:info@olostep.com)

[​

](#resources)

Resources
------------------------------

PyPI Package
------------

View on PyPI

Get API Key
-----------

Sign up for free

Was this page helpful?

YesNo
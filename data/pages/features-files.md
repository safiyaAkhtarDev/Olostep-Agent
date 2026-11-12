<!-- source: https://docs.olostep.com/features/files -->
# https://docs.olostep.com/features/files

Files - Olostep Docs  

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

Files

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Files
=====

Copy pageCopy page

Upload and manage JSON files for use as context in API requests

Copy pageCopy page

Through the Olostep `/v1/files` endpoint you can upload JSON files that can be used as context in your API requests. This allows you to provide structured data to enhance your scrapes, answers, and other operations.

*   Upload JSON files up to 200MB
*   Files are automatically validated for proper JSON format
*   Use files as context in scrapes, answers, and other endpoints
*   Files expire after 30 days
*   Secure pre-signed URL upload process

For API details see the [Files Endpoint API Reference](/api-reference/files/create).

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

](#upload-a-file)

Upload a file
--------------------------------------

The file upload process consists of two steps:

1.  **Create upload URL**: Request a pre-signed URL for uploading your file
2.  **Complete upload**: Upload your file to the pre-signed URL, then call the complete endpoint to validate and finalize

### 

[​

](#step-1-create-upload-url)

Step 1: Create upload URL

First, create an upload URL by providing the filename and optional purpose. The `purpose` parameter supports only two values: `"context"` (default) or `"batch"`.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Step 1: Create upload URL
    payload = {
        "filename": "my-data.json",
        "purpose": "context"  # Optional, defaults to "context". Supported values: "context" or "batch"
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(f"{API_URL}/files", headers=headers, json=payload)
    upload_data = response.json()
    
    print(json.dumps(upload_data, indent=2))
    # Response includes: id, upload_url, expires_in
    

    const API_URL = 'https://api.olostep.com/v1'
    
    const res = await fetch(`${API_URL}/files`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        filename: 'my-data.json',
        purpose: 'context'  // Optional, defaults to "context". Supported values: "context" or "batch"
      })
    })
    const uploadData = await res.json()
    console.log(uploadData)
    

    curl -s -X POST "https://api.olostep.com/v1/files" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "filename": "my-data.json",
        "purpose": "context"
      }'
    
    # Example with "batch" purpose:
    curl -s -X POST "https://api.olostep.com/v1/files" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "filename": "batch-data.json",
        "purpose": "batch"
      }'
    

The response includes a pre-signed `upload_url` that expires in 10 minutes:

    {
      "id": "file_abc123xyz789",
      "object": "file.upload",
      "created": 1760329882,
      "upload_url": "https://olostep-files.s3.amazonaws.com/files/...",
      "expires_in": 600
    }
    

### 

[​

](#step-2-upload-file-and-complete)

Step 2: Upload file and complete

Upload your JSON file to the pre-signed URL, then call the complete endpoint to validate and finalize the upload.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # After getting upload_url from Step 1
    file_id = upload_data["id"]
    upload_url = upload_data["upload_url"]
    
    # Prepare your JSON data
    json_data = {
        "users": [
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Smith", "email": "jane@example.com"}
        ]
    }
    
    # Step 2a: Upload file to pre-signed URL
    upload_response = requests.put(
        upload_url,
        data=json.dumps(json_data),
        headers={"Content-Type": "application/json"}
    )
    upload_response.raise_for_status()
    
    # Step 2b: Complete the upload
    complete_response = requests.post(
        f"{API_URL}/files/{file_id}/complete",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    file_info = complete_response.json()
    
    print(json.dumps(file_info, indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    
    // After getting upload_url from Step 1
    const fileId = uploadData.id
    const uploadUrl = uploadData.upload_url
    
    // Prepare your JSON data
    const jsonData = {
      users: [
        { name: 'John Doe', email: 'john@example.com' },
        { name: 'Jane Smith', email: 'jane@example.com' }
      ]
    }
    
    // Step 2a: Upload file to pre-signed URL
    await fetch(uploadUrl, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(jsonData)
    })
    
    // Step 2b: Complete the upload
    const completeRes = await fetch(`${API_URL}/files/${fileId}/complete`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const fileInfo = await completeRes.json()
    console.log(fileInfo)
    

    # Step 2a: Upload file to pre-signed URL
    curl -X PUT "$UPLOAD_URL" \
      -H "Content-Type: application/json" \
      -d @my-data.json
    
    # Step 2b: Complete the upload
    curl -s -X POST "https://api.olostep.com/v1/files/$FILE_ID/complete" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

The complete endpoint validates the JSON file and returns file metadata:

    {
      "id": "file_abc123xyz789",
      "object": "file",
      "created": 1760329882,
      "filename": "my-data.json",
      "bytes": 1024,
      "purpose": "context",
      "status": "completed"
    }
    

[​

](#retrieve-file-metadata-by-id)

Retrieve file metadata by ID
--------------------------------------------------------------------

Retrieve metadata for a file by its ID.

Python

Node

cURL

    file_id = "file_abc123xyz789"
    response = requests.get(
        f"{API_URL}/files/{file_id}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    file_info = response.json()
    print(json.dumps(file_info, indent=2))
    

    const fileId = 'file_abc123xyz789'
    const res = await fetch(`${API_URL}/files/${fileId}`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const fileInfo = await res.json()
    console.log(fileInfo)
    

    curl -s -X GET "https://api.olostep.com/v1/files/$FILE_ID" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#retrieve-file-object-by-id)

Retrieve file object by ID
----------------------------------------------------------------

Get a pre-signed URL to download the JSON content of a completed file. Optionally specify the expiration time for the download URL using the `expires_in` query parameter (defaults to 600 seconds / 10 minutes).

Python

Node

cURL

    file_id = "file_abc123xyz789"
    # Get download URL (default expiration: 600 seconds)
    response = requests.get(
        f"{API_URL}/files/{file_id}/content",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    download_info = response.json()
    download_url = download_info["download_url"]
    
    # Download the file content using the pre-signed URL
    file_response = requests.get(download_url)
    file_content = file_response.json()
    print(json.dumps(file_content, indent=2))
    
    # Example with custom expiration (3600 seconds = 1 hour)
    response = requests.get(
        f"{API_URL}/files/{file_id}/content?expires_in=3600",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    download_info = response.json()
    print(f"Download URL expires in: {download_info['expires_in']} seconds")
    

    const fileId = 'file_abc123xyz789'
    
    // Get download URL (default expiration: 600 seconds)
    const res = await fetch(`${API_URL}/files/${fileId}/content`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const downloadInfo = await res.json()
    const downloadUrl = downloadInfo.download_url
    
    // Download the file content using the pre-signed URL
    const fileRes = await fetch(downloadUrl)
    const fileContent = await fileRes.json()
    console.log(fileContent)
    
    // Example with custom expiration (3600 seconds = 1 hour)
    const customRes = await fetch(`${API_URL}/files/${fileId}/content?expires_in=3600`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const customDownloadInfo = await customRes.json()
    console.log(`Download URL expires in: ${customDownloadInfo.expires_in} seconds`)
    

    # Get download URL (default expiration: 600 seconds)
    curl -s -X GET "https://api.olostep.com/v1/files/$FILE_ID/content" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    
    # Get download URL with custom expiration (3600 seconds = 1 hour)
    curl -s -X GET "https://api.olostep.com/v1/files/$FILE_ID/content?expires_in=3600" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    
    # Download the file using the pre-signed URL
    curl -s "$DOWNLOAD_URL"
    

The response includes a pre-signed `download_url` that expires after the specified time:

    {
      "id": "file_abc123xyz789",
      "object": "file",
      "created": 1760329882,
      "filename": "my-data.json",
      "bytes": 1024,
      "download_url": "https://olostep-files.s3.amazonaws.com/files/...",
      "expires_in": 600
    }
    

[​

](#list-files)

List files
--------------------------------

List all completed files for your team. Optionally filter by purpose (supported values: `"context"` or `"batch"`).

Python

Node

cURL

    # List all files
    response = requests.get(
        f"{API_URL}/files",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    files = response.json()
    print(json.dumps(files, indent=2))
    
    # List files filtered by purpose
    response = requests.get(
        f"{API_URL}/files?purpose=context",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    context_files = response.json()
    print(json.dumps(context_files, indent=2))
    

    // List all files
    const res = await fetch(`${API_URL}/files`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const files = await res.json()
    console.log(files)
    
    // List files filtered by purpose
    const contextRes = await fetch(`${API_URL}/files?purpose=context`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const contextFiles = await contextRes.json()
    console.log(contextFiles)
    

    # List all files
    curl -s -X GET "https://api.olostep.com/v1/files" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    
    # List files filtered by purpose
    curl -s -X GET "https://api.olostep.com/v1/files?purpose=context" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

The response includes a list of files:

    {
      "object": "list",
      "data": [
        {
          "id": "file_abc123xyz789",
          "object": "file",
          "created": 1760329882,
          "filename": "my-data.json",
          "bytes": 1024,
          "purpose": "context",
          "status": "completed"
        }
      ]
    }
    

[​

](#delete-a-file)

Delete a file
--------------------------------------

Delete a file and its associated data from storage.

Python

Node

cURL

    file_id = "file_abc123xyz789"
    response = requests.delete(
        f"{API_URL}/files/{file_id}",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    result = response.json()
    print(json.dumps(result, indent=2))
    

    const fileId = 'file_abc123xyz789'
    const res = await fetch(`${API_URL}/files/${fileId}`, {
      method: 'DELETE',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const result = await res.json()
    console.log(result)
    

    curl -s -X DELETE "https://api.olostep.com/v1/files/$FILE_ID" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#complete-upload-example-context-purpose)

Complete upload example (context purpose)
--------------------------------------------------------------------------------------------

Here’s a complete example that uploads a JSON file with `purpose="context"`:

Python

Node

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Step 1: Create upload URL
    create_response = requests.post(
        f"{API_URL}/files",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"filename": "user-data.json", "purpose": "context"}
    )
    upload_data = create_response.json()
    file_id = upload_data["id"]
    upload_url = upload_data["upload_url"]
    
    # Step 2: Prepare and upload JSON data
    json_data = {
        "users": [
            {"id": 1, "name": "Alice", "role": "admin"},
            {"id": 2, "name": "Bob", "role": "user"}
        ]
    }
    
    upload_response = requests.put(
        upload_url,
        data=json.dumps(json_data),
        headers={"Content-Type": "application/json"}
    )
    upload_response.raise_for_status()
    
    # Step 3: Complete the upload
    complete_response = requests.post(
        f"{API_URL}/files/{file_id}/complete",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    file_info = complete_response.json()
    
    print(f"File uploaded successfully: {file_info['id']}")
    print(f"File size: {file_info['bytes']} bytes")
    

    const API_URL = 'https://api.olostep.com/v1'
    
    // Step 1: Create upload URL
    const createRes = await fetch(`${API_URL}/files`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({ filename: 'user-data.json', purpose: 'context' })
    })
    const uploadData = await createRes.json()
    const fileId = uploadData.id
    const uploadUrl = uploadData.upload_url
    
    // Step 2: Prepare and upload JSON data
    const jsonData = {
      users: [
        { id: 1, name: 'Alice', role: 'admin' },
        { id: 2, name: 'Bob', role: 'user' }
      ]
    }
    
    await fetch(uploadUrl, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(jsonData)
    })
    
    // Step 3: Complete the upload
    const completeRes = await fetch(`${API_URL}/files/${fileId}/complete`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const fileInfo = await completeRes.json()
    
    console.log(`File uploaded successfully: ${fileInfo.id}`)
    console.log(`File size: ${fileInfo.bytes} bytes`)
    

[​

](#upload-batch-file-example)

Upload batch file example
--------------------------------------------------------------

Here’s an example that uploads a JSON file with `purpose="batch"` containing valid batch data that can be used with the `/v1/batches` endpoint:

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    # Step 1: Create upload URL with purpose="batch"
    create_response = requests.post(
        f"{API_URL}/files",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"filename": "batch-items.json", "purpose": "batch"}
    )
    upload_data = create_response.json()
    file_id = upload_data["id"]
    upload_url = upload_data["upload_url"]
    
    # Step 2: Prepare batch JSON data (valid format for /v1/batches endpoint)
    batch_data = {
        "items": [
            {"custom_id": "item-1", "url": "https://www.google.com/search?q=stripe&gl=us&hl=en"},
            {"custom_id": "item-2", "url": "https://www.google.com/search?q=paddle&gl=us&hl=en"},
            {"custom_id": "item-3", "url": "https://www.google.com/search?q=payment+gateway&gl=us&hl=en"}
        ],
        "parser": {"id": "@olostep/google-search"},
        "country": "US"
    }
    
    upload_response = requests.put(
        upload_url,
        data=json.dumps(batch_data),
        headers={"Content-Type": "application/json"}
    )
    upload_response.raise_for_status()
    
    # Step 3: Complete the upload
    complete_response = requests.post(
        f"{API_URL}/files/{file_id}/complete",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    file_info = complete_response.json()
    
    print(f"Batch file uploaded successfully: {file_info['id']}")
    print(f"File size: {file_info['bytes']} bytes")
    print(f"Purpose: {file_info['purpose']}")
    

    const API_URL = 'https://api.olostep.com/v1'
    
    // Step 1: Create upload URL with purpose="batch"
    const createRes = await fetch(`${API_URL}/files`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({ filename: 'batch-items.json', purpose: 'batch' })
    })
    const uploadData = await createRes.json()
    const fileId = uploadData.id
    const uploadUrl = uploadData.upload_url
    
    // Step 2: Prepare batch JSON data (valid format for /v1/batches endpoint)
    const batchData = {
      items: [
        { custom_id: 'item-1', url: 'https://www.google.com/search?q=stripe&gl=us&hl=en' },
        { custom_id: 'item-2', url: 'https://www.google.com/search?q=paddle&gl=us&hl=en' },
        { custom_id: 'item-3', url: 'https://www.google.com/search?q=payment+gateway&gl=us&hl=en' }
      ],
      parser: { id: '@olostep/google-search' },
      country: 'US'
    }
    
    await fetch(uploadUrl, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(batchData)
    })
    
    // Step 3: Complete the upload
    const completeRes = await fetch(`${API_URL}/files/${fileId}/complete`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const fileInfo = await completeRes.json()
    
    console.log(`Batch file uploaded successfully: ${fileInfo.id}`)
    console.log(`File size: ${fileInfo.bytes} bytes`)
    console.log(`Purpose: ${fileInfo.purpose}`)
    

    # Step 1: Create upload URL with purpose="batch"
    curl -s -X POST "https://api.olostep.com/v1/files" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "filename": "batch-items.json",
        "purpose": "batch"
      }'
    
    # Step 2: Upload batch JSON data (save to batch-items.json first)
    # batch-items.json content:
    # {
    #   "items": [
    #     {"custom_id": "item-1", "url": "https://www.google.com/search?q=stripe&gl=us&hl=en"},
    #     {"custom_id": "item-2", "url": "https://www.google.com/search?q=paddle&gl=us&hl=en"},
    #     {"custom_id": "item-3", "url": "https://www.google.com/search?q=payment+gateway&gl=us&hl=en"}
    #   ],
    #   "parser": {"id": "@olostep/google-search"},
    #   "country": "US"
    # }
    
    curl -X PUT "$UPLOAD_URL" \
      -H "Content-Type: application/json" \
      -d @batch-items.json
    
    # Step 3: Complete the upload
    curl -s -X POST "https://api.olostep.com/v1/files/$FILE_ID/complete" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

The uploaded batch file contains a valid JSON structure that matches the `/v1/batches` endpoint format:

*   `items`: Array of objects with `custom_id` and `url` fields
*   `parser`: Optional parser configuration
*   `country`: Optional country code

This file can be used as input for batch processing operations.

[​

](#file-requirements)

File requirements
----------------------------------------------

*   **File format**: Only JSON files are supported (`.json` extension required)
*   **File size**: Maximum 200MB per file
*   **Expiration**: Files expire after 30 days
*   **Upload URL**: Pre-signed URLs expire after 10 minutes
*   **Purpose parameter**: Only supports `"context"` or `"batch"` values (defaults to `"context"`)

[​

](#pricing)

Pricing
--------------------------

File uploads are free. Files are stored securely and automatically expire after 30 days.

Was this page helpful?

YesNo
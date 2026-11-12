<!-- source: https://docs.olostep.com/features/monitors -->
# https://docs.olostep.com/features/monitors

Monitors - Olostep Docs  

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

Monitors

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Features

Monitors
========

Copy pageCopy page

Monitor pages on a schedule and send change alerts

Copy pageCopy page

Through the Olostep `/v1/monitors` endpoint you can create persistent monitors that run on a fixed schedule, detect page changes, and notify you through email, Slack, SMS, or a dedicated webhook.

*   Create a monitor from a natural language `query`
*   Scope sources with `source_policy`
*   Run checks on natural-language schedules (minimum every 10 minutes, UTC)
*   Configure `notification.channels` and optional `webhook` delivery
*   Stream provisioning progress with Server-Sent Events (`?stream=1`)
*   List, inspect, update, pause, resume, and delete monitors
*   Read snapshot events, planning artifacts, run logs, and live agent logs

By default, every monitor run captures a **full snapshot** of the monitored page — a complete picture of its current state at that moment. If you want the monitor to surface only what’s new or changed between runs (deltas) instead of the full state, express that intent in the `query`.

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

](#create-a-monitor)

Create a monitor
--------------------------------------------

Create a monitor with `POST /v1/monitors`. The API validates your input, reserves a monitor record, provisions a shadow agent, generates a workflow spec, queues DAG planning, and creates a recurring schedule.

*   `query` is required — describe what to watch in natural language.
*   `frequency` is optional and defaults to `every hour`. Use scheduling phrases such as `every day at 9am` (schedules run in **UTC**; minimum interval is **10 minutes**).
*   `source_policy` optionally constrains `include_urls`, `exclude_urls`, `include_domains`, and `exclude_domains`.
*   `notification` configures when and how to alert (`events` + `channels`). Channel delivery is resolved at runtime by the monitor pipeline — you do not pass recipients into the DAG.
*   `webhook` is a separate object (`{ "url": "https://…" }`) for HTTP callbacks in addition to `notification.channels`.
*   `output_schema` optionally enforces structured extraction (valid JSON Schema).

The create response is HTTP `202` with `status: provisioning`. The monitor moves to `active` after planning resolves `tracked` targets. Poll `GET /v1/monitors/:monitor_id` or pass `?stream=1` (or `Accept: text/event-stream`) to follow provisioning phases and spec reasoning tokens over SSE.

### 

[​

](#example-request)

Example request

You only need `query` and `frequency`. Notification channels and webhooks can be added later with `POST /v1/monitors/:monitor_id`.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    payload = {
        "query": "Notify me when a new startup launches on Y Combinator Launches",
        "frequency": "every 20 minutes",
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    response = requests.post(f"{API_URL}/monitors", headers=headers, json=payload)
    print(response.status_code)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    
    const res = await fetch(`${API_URL}/monitors`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: 'Notify me when a new startup launches on Y Combinator Launches',
        frequency: 'every 20 minutes',
      }),
    })
    
    console.log(res.status)
    console.log(await res.json())
    

    curl -sS -X POST "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Notify me when a new startup launches on Y Combinator Launches",
        "frequency": "every 20 minutes"
      }'
    

### 

[​

](#response)

Response

Successful creation (non-streaming) returns HTTP `202` with a monitor object. `tracked` is empty until planning finishes; poll `GET /v1/monitors/:monitor_id` until `status` is `active` and `tracked.urls` is populated.

    {
      "id": "monitor_biglavgvq3",
      "object": "monitor",
      "query": "Notify me when a new startup launches on Y Combinator Launches",
      "tracked": {
        "type": null,
        "urls": [],
        "web_query": null
      },
      "source_policy": {},
      "schedule": {
        "frequency": "every 20 minutes",
        "cron": "7/20 * * * ? *",
        "timezone": "UTC",
        "next_run_at": null
      },
      "notification": {
        "events": [],
        "channels": []
      },
      "webhook": null,
      "output_schema": {},
      "status": "provisioning",
      "error_message": null,
      "last_run": null,
      "agent": {
        "id": "agent_forward_deployed_0_fda_nlkxhr5kto"
      },
      "metadata": {},
      "created": 1780063068,
      "updated": 1780063071
    }
    

### 

[​

](#structured-monitor-output)

Structured monitor output

Set `output_schema` when you want extraction results to follow a specific JSON structure. The schema must be valid JSON Schema.

### 

[​

](#provisioning-stream)

Provisioning stream

Add `?stream=1` or send `Accept: text/event-stream` to receive SSE events while the monitor is created:

Event

Description

`phase`

Provisioning step (`running`, `done`, or `failed`)

`reasoning_token`

Incremental spec-design text

`reasoning_reset`

Truncates buffered reasoning after a failed LLM attempt

`complete`

Final monitor object (same shape as the `202` response)

`error`

Terminal failure

[​

](#notifications-and-webhooks)

Notifications and webhooks
----------------------------------------------------------------

Alerts are configured on the monitor record and resolved at runtime — do not embed channel targets in the monitoring `query`.

### 

[​

](#notification)

`notification`

Field

Description

`events`

Which run outcomes should trigger delivery. See [notification events](#notification-events) below. If you set `channels` and omit `events`, defaults to both `changed` and `first_snapshot`.

`channels`

List of `{ "type", "target", "events"? }` objects

#### 

[​

](#notification-events)

Notification events

Use `events` to state **when** you want to be notified. Allowed values:

Event

Meaning

`changed`

Notify when the monitor detects a **change** compared to the previous snapshot (for example new content, updated price, or a diff the pipeline classifies as changed).

`first_snapshot`

Notify when the monitor takes its **first snapshot** — the initial baseline run that stores current content before later comparisons.

You can include one or both. For example, `["changed"]` alerts only on updates after the baseline; `["first_snapshot"]` confirms setup without waiting for a diff; `["changed", "first_snapshot"]` covers both. Per-channel `events` on a channel object uses the same values and overrides the top-level list for that channel only. Supported channel types:

`type`

`target` format

`email`

Valid email address

`slack`

Slack incoming webhook URL

`sms`

E.164 phone number (for example `+14155552671`)

### 

[​

](#webhook)

`webhook`

Separate from `notification.channels`, `webhook.url` receives HTTP POST payloads when the monitor fires your callback URL. You can use both a webhook and channel notifications on the same monitor.

### 

[​

](#examples)

Examples

Email only:

    {
      "query": "Watch for changes on https://example.com/terms",
      "frequency": "every day at 10am",
      "notification": {
        "events": ["changed"],
        "channels": [
          { "type": "email", "target": "legal@example.com" }
        ]
      }
    }
    

Webhook callback:

    {
      "query": "Watch for changes on https://example.com/terms",
      "frequency": "every day at 10am",
      "webhook": {
        "url": "https://hooks.example.com/olostep-monitor"
      }
    }
    

SMS:

    {
      "query": "Alert me when https://status.example.com shows an incident",
      "frequency": "every hour",
      "notification": {
        "channels": [
          { "type": "sms", "target": "+14155552671" }
        ]
      }
    }
    

[​

](#source-policy)

Source policy
--------------------------------------

Use `source_policy` to constrain which URLs and domains the planner may use.

    {
      "source_policy": {
        "include_urls": ["https://example.com/pricing"],
        "exclude_domains": ["ads.example.com"]
      }
    }
    

[​

](#frequencies)

Frequencies
----------------------------------

Set `frequency` in natural language, for example:

*   `every hour` (default when omitted)
*   `every day at 9am`
*   `every weekday at 14:30`

Rules:

*   Must read as scheduling language (not an arbitrary monitor question).
*   Minimum interval: **every 10 minutes**.
*   Schedules are stored and executed in **UTC** (`schedule.timezone` is `UTC`).
*   Maximum length: 50 characters.

The API derives a cron expression from your `frequency` text and exposes it on `schedule.cron`. When the monitor is `active`, `schedule.next_run_at` shows the next run in ISO 8601.

[​

](#list-monitors)

List monitors
--------------------------------------

Retrieve all monitors for your team with `GET /v1/monitors`. By default, deleted monitors are filtered out. Use `?include_deleted=true` to include them.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    
    headers = { "Authorization": f"Bearer {API_KEY}" }
    
    response = requests.get(f"{API_URL}/monitors", headers=headers)
    result = response.json()
    print(f"Total monitors: {result['count']}")
    print(json.dumps(result, indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    
    const res = await fetch(`${API_URL}/monitors`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    const result = await res.json()
    
    console.log(`Total monitors: ${result.count}`)
    console.log(result.monitors)
    

    curl -s -X GET "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

### 

[​

](#response-shape)

Response shape

    {
      "monitors": [
        {
          "id": "monitor_0wj35czpn7",
          "object": "monitor",
          "query": "Watch AirOps blog for new blog posts",
          "tracked": {
            "type": "urls",
            "urls": ["https://www.airops.com/blog"],
            "web_query": null
          },
          "source_policy": {},
          "schedule": {
            "frequency": "every hour",
            "cron": "2 * * * ? *",
            "timezone": "UTC",
            "next_run_at": null
          },
          "notification": {
            "channels": [],
            "events": []
          },
          "webhook": null,
          "output_schema": {},
          "status": "paused",
          "error_message": null,
          "last_run": null,
          "agent": { "id": "agent_forward_deployed_0_fda_x4822l9h3i" },
          "metadata": {},
          "created": 1780062756,
          "updated": 1780063025
        },
        {
          "id": "monitor_biglavgvq3",
          "object": "monitor",
          "query": "Notify me when a new startup launches on Y Combinator Launches",
          "tracked": {
            "type": "urls",
            "urls": ["https://www.ycombinator.com/launches/"],
            "web_query": null
          },
          "source_policy": {},
          "schedule": {
            "frequency": "every 20 minutes",
            "cron": "7/20 * * * ? *",
            "timezone": "UTC",
            "next_run_at": "2026-05-29T14:27:00.000Z"
          },
          "notification": {
            "channels": [],
            "events": []
          },
          "webhook": null,
          "output_schema": {},
          "status": "active",
          "error_message": null,
          "last_run": null,
          "agent": { "id": "agent_forward_deployed_0_fda_nlkxhr5kto" },
          "metadata": {},
          "created": 1780063068,
          "updated": 1780063141
        }
      ],
      "count": 5
    }
    

[​

](#get-a-monitor)

Get a monitor
--------------------------------------

Retrieve a single monitor with `GET /v1/monitors/:monitor_id`. The response includes `last_run` (latest snapshot summary) and `total_count` (snapshot count) unless you pass `include_total_count=false`. Add `include-diagram=true` to include a `mermaid_diagram` of the monitor DAG.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    headers = { "Authorization": f"Bearer {API_KEY}" }
    
    response = requests.get(f"{API_URL}/monitors/{MONITOR_ID}", headers=headers)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(await res.json())
    

    curl -s -X GET "https://api.olostep.com/v1/monitors/monitor_biglavgvq3" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

### 

[​

](#response-shape-2)

Response shape

    {
      "id": "monitor_biglavgvq3",
      "object": "monitor",
      "query": "Notify me when a new startup launches on Y Combinator Launches",
      "tracked": {
        "type": "urls",
        "urls": ["https://www.ycombinator.com/launches/"],
        "web_query": null
      },
      "source_policy": {},
      "schedule": {
        "frequency": "every 20 minutes",
        "cron": "7/20 * * * ? *",
        "timezone": "UTC",
        "next_run_at": "2026-05-29T14:27:00.000Z"
      },
      "notification": {
        "channels": [],
        "events": []
      },
      "webhook": null,
      "output_schema": {},
      "status": "active",
      "error_message": null,
      "last_run": {
        "id": "run_iwsoafcpyx",
        "status": "completed",
        "change_detected": false,
        "ran_at": "2026-05-29T14:03:15.963Z"
      },
      "agent": {
        "id": "agent_forward_deployed_0_fda_nlkxhr5kto"
      },
      "metadata": {},
      "created": 1780063068,
      "updated": 1780063141,
      "total_count": 1
    }
    

[​

](#list-monitor-events)

List monitor events
--------------------------------------------------

Use `GET /v1/monitors/:monitor_id/events` to list snapshot events for a monitor. Pagination:

*   `limit` (default `25`, max `100`)
*   `cursor` (opaque token from `next_cursor`)
*   `count_only=true` returns only `{ "total_count": N }`

Events are returned newest-first. Each item includes a short-lived pre-signed `snapshot_url`.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    headers = { "Authorization": f"Bearer {API_KEY}" }
    
    response = requests.get(
        f"{API_URL}/monitors/{MONITOR_ID}/events?limit=10",
        headers=headers,
    )
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}/events?limit=10`, {
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(await res.json())
    

    curl -s -X GET "https://api.olostep.com/v1/monitors/monitor_biglavgvq3/events?limit=10" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

### 

[​

](#response-shape-3)

Response shape

    {
      "data": [
        {
          "id": "run_iwsoafcpyx",
          "run_id": "run_iwsoafcpyx",
          "created": 1780063395,
          "changed": false,
          "summary": "First snapshot of this monitor has been taken. Stored current content as baseline.",
          "snapshot_url": "https://olostep-monitor-snapshots.s3.amazonaws.com/monitor_biglavgvq3/run_iwsoafcpyx_snapshot.json?X-Amz-Expires=600&..."
        }
      ],
      "has_more": false,
      "next_cursor": null,
      "total_count": 1
    }
    

[​

](#get-monitor-planning)

Get monitor planning
----------------------------------------------------

Use `GET /v1/monitors/:monitor_id/planning` to inspect the FDA workflow spec and planner DAG after provisioning.

    {
      "spec": {
        "saved_at": "2026-05-29T12:00:00.000000+00:00",
        "status": "complete",
        "goal": "Track pricing on example.com",
        "reasoning": "...",
        "constraints": "...",
        "assumptions": "...",
        "input": { "query": "...", "urls": ["https://www.ycombinator.com/launches/"] },
        "output": { "type": "free_text" },
        "chat_history": []
      },
      "dag": {
        "user_query": "...",
        "graph": { "nodes": [], "edges": [] },
        "has_unresolved": false,
        "unresolved": [],
        "validation": { "is_valid": true, "attempts": 1, "history": [] }
      }
    }
    

[​

](#get-a-monitor-run)

Get a monitor run
----------------------------------------------

Use `GET /v1/monitors/:monitor_id/runs/:run_id` for snapshot metadata and parsed agent log events for one execution (`run_id` must start with `run_`).

    {
      "monitor_id": "monitor_biglavgvq3",
      "run_id": "run_v7k2p9m3",
      "snapshot": { "changed": true, "summary": "..." },
      "log_group": "/aws/ecs/olostep-agents/...",
      "events": [
        {
          "id": "...",
          "ts": 1777960800123,
          "message": "Run run_v7k2p9m3 completed. Files uploaded: 2",
          "event": { "type": "run_complete", "run_id": "run_v7k2p9m3", "files_uploaded": 2 }
        }
      ]
    }
    

[​

](#stream-agent-logs)

Stream agent logs
----------------------------------------------

Use `GET /v1/monitors/:monitor_id/agent-logs?stream=1` (or `Accept: text/event-stream`) to tail CloudWatch logs for the monitor’s agent, filtered to this `monitor_id`. Optional query parameter `since` is a millisecond timestamp (default: 30 minutes ago). SSE event types: `ready`, `log`, `heartbeat`, `error`.

[​

](#update-a-monitor)

Update a monitor
--------------------------------------------

Update a monitor with `POST /v1/monitors/:monitor_id`. Supported fields (include only what you want to change):

*   `metadata` — merged with existing keys; empty string values delete keys
*   `frequency` — recreates the internal schedule and sets `status` back to `active`
*   `notification` — replaces the entire notification object
*   `webhook` — pass `null` to remove

Returns `409` while `status` is `provisioning`. When you add `notification.channels` without `events`, the API defaults `events` to `["changed", "first_snapshot"]`.

### 

[​

](#add-email-notification)

Add email notification

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    payload = {
        "notification": {
            "channels": [
                {"type": "email", "target": "you@example.com"}
            ]
        }
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    response = requests.post(
        f"{API_URL}/monitors/{MONITOR_ID}",
        headers=headers,
        json=payload,
    )
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        notification: {
          channels: [{ type: 'email', target: 'you@example.com' }]
        }
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/monitors/monitor_biglavgvq3" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "notification": {
          "channels": [
            { "type": "email", "target": "you@example.com" }
          ]
        }
      }'
    

    {
      "id": "monitor_biglavgvq3",
      "object": "monitor",
      "query": "Notify me when a new startup launches on Y Combinator Launches",
      "tracked": {
        "type": "urls",
        "urls": ["https://www.ycombinator.com/launches/"],
        "web_query": null
      },
      "source_policy": {},
      "schedule": {
        "frequency": "every 20 minutes",
        "cron": "7/20 * * * ? *",
        "timezone": "UTC",
        "next_run_at": "2026-05-29T14:27:00.000Z"
      },
      "notification": {
        "events": ["changed", "first_snapshot"],
        "channels": [
          { "type": "email", "target": "you@example.com" }
        ]
      },
      "webhook": null,
      "output_schema": {},
      "status": "active",
      "error_message": null,
      "last_run": null,
      "agent": { "id": "agent_forward_deployed_0_fda_nlkxhr5kto" },
      "metadata": {},
      "created": 1780063068,
      "updated": 1780064634
    }
    

### 

[​

](#add-webhook)

Add webhook

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    payload = {
        "webhook": { "url": "https://webhook.site/your-unique-id" }
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    response = requests.post(
        f"{API_URL}/monitors/{MONITOR_ID}",
        headers=headers,
        json=payload,
    )
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        webhook: { url: 'https://webhook.site/your-unique-id' }
      })
    })
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/monitors/monitor_biglavgvq3" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "webhook": { "url": "https://webhook.site/your-unique-id" }
      }'
    

    {
      "id": "monitor_biglavgvq3",
      "object": "monitor",
      "query": "Notify me when a new startup launches on Y Combinator Launches",
      "tracked": {
        "type": "urls",
        "urls": ["https://www.ycombinator.com/launches/"],
        "web_query": null
      },
      "source_policy": {},
      "schedule": {
        "frequency": "every 20 minutes",
        "cron": "7/20 * * * ? *",
        "timezone": "UTC",
        "next_run_at": "2026-05-29T14:47:00.000Z"
      },
      "notification": {
        "channels": [
          { "type": "email", "target": "you@example.com" }
        ],
        "events": ["changed", "first_snapshot"]
      },
      "webhook": {
        "url": "https://webhook.site/your-unique-id"
      },
      "output_schema": {},
      "status": "active",
      "error_message": null,
      "last_run": null,
      "agent": { "id": "agent_forward_deployed_0_fda_nlkxhr5kto" },
      "metadata": {},
      "created": 1780063068,
      "updated": 1780065538
    }
    

[​

](#pause-a-monitor)

Pause a monitor
------------------------------------------

Pause a monitor with `POST /v1/monitors/:monitor_id/pause`. Pausing disables the underlying schedule and sets `status` to `paused`. Only monitors with `status: active` can be paused. The request body is empty.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    response = requests.post(
        f"{API_URL}/monitors/{MONITOR_ID}/pause",
        headers={ "Authorization": f"Bearer {API_KEY}" },
    )
    print(response.status_code)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}/pause`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(res.status)
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/monitors/monitor_biglavgvq3/pause" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

On success, returns `200` with the monitor and `status: paused`. `schedule.next_run_at` is `null` while paused.

[​

](#resume-a-monitor)

Resume a monitor
--------------------------------------------

Resume a paused monitor with `POST /v1/monitors/:monitor_id/resume`. Resuming re-enables the schedule and sets `status` back to `active`. Only `paused` monitors can be resumed.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    response = requests.post(
        f"{API_URL}/monitors/{MONITOR_ID}/resume",
        headers={ "Authorization": f"Bearer {API_KEY}" },
    )
    print(response.status_code)
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}/resume`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(res.status)
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/v1/monitors/monitor_biglavgvq3/resume" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#delete-a-monitor)

Delete a monitor
--------------------------------------------

Delete a monitor with `DELETE /v1/monitors/:monitor_id`. Deletion soft-deletes the monitor row (`status: deleted`) and removes its schedule and shadow agent resources.

Python

Node

cURL

    import requests
    import json
    
    API_KEY = "<YOUR_API_KEY>"
    API_URL = "https://api.olostep.com/v1"
    MONITOR_ID = "monitor_biglavgvq3"
    
    response = requests.delete(
        f"{API_URL}/monitors/{MONITOR_ID}",
        headers={ "Authorization": f"Bearer {API_KEY}" },
    )
    print(json.dumps(response.json(), indent=2))
    

    const API_URL = 'https://api.olostep.com/v1'
    const monitorId = 'monitor_biglavgvq3'
    
    const res = await fetch(`${API_URL}/monitors/${monitorId}`, {
      method: 'DELETE',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>' }
    })
    console.log(await res.json())
    

    curl -s -X DELETE "https://api.olostep.com/v1/monitors/monitor_biglavgvq3" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

[​

](#monitor-status)

Monitor status
----------------------------------------

Status

Meaning

`provisioning`

Agent, spec, planner, and schedule are being set up

`active`

Schedule enabled; runs execute on `schedule.frequency`

`paused`

Schedule disabled via `/pause`

`failed`

Provisioning or schedule update failed (`error_message` set)

`deleted`

Soft-deleted via `DELETE`

[​

](#example-use-cases)

Example use cases
----------------------------------------------

Below are common monitor patterns. Each example only needs `query` and `frequency` at creation time; add `notification` and `webhook` later if you want alerts on the first run or on changes.

### 

[​

](#y-combinator-new-launches)

Y Combinator new launches

Watch [Y Combinator Launches](https://www.ycombinator.com/launches/) for newly published startups. After planning, `tracked.type` is `urls` and `tracked.urls` points at the launches page.

Python

Node

cURL

    import requests
    
    API_URL = "https://api.olostep.com/v1"
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json",
    }
    
    requests.post(
        f"{API_URL}/monitors",
        headers=headers,
        json={
            "query": "Notify me when a new startup launches on Y Combinator Launches",
            "frequency": "every 20 minutes",
        },
    )
    

    const API_URL = 'https://api.olostep.com/v1'
    
    await fetch(`${API_URL}/monitors`, {
      method: 'POST',
      headers: { 'Authorization': 'Bearer <YOUR_API_KEY>', 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: 'Notify me when a new startup launches on Y Combinator Launches',
        frequency: 'every 20 minutes',
      }),
    })
    

    curl -sS -X POST "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Notify me when a new startup launches on Y Combinator Launches",
        "frequency": "every 20 minutes"
      }'
    

Add email and webhook delivery after the monitor is `active`:

    curl -s -X POST "https://api.olostep.com/v1/monitors/monitor_biglavgvq3" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "notification": {
          "channels": [{ "type": "email", "target": "you@example.com" }]
        },
        "webhook": { "url": "https://webhook.site/your-unique-id" }
      }'
    

With `channels` set and `events` omitted, the API defaults to `["changed", "first_snapshot"]` so you are notified on the baseline run and whenever a change is detected.

### 

[​

](#competitor-blog-posts-airops-profound)

Competitor blog posts (AirOps, Profound)

Monitor a competitor blog index for new posts. The planner resolves `tracked.urls` to the blog URL (for example `https://www.airops.com/blog` or `https://www.tryprofound.com/blog`).

cURL AirOps

cURL Profound

    curl -sS -X POST "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Watch AirOps blog for new blog posts",
        "frequency": "every hour"
      }'
    

    curl -sS -X POST "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Watch Profound blog for new blog posts",
        "frequency": "every 20 minutes"
      }'
    

After creation, a monitor in this family looks like:

    {
      "id": "monitor_588ck513zd",
      "object": "monitor",
      "query": "Watch Profound blog for new blog posts",
      "tracked": {
        "type": "urls",
        "urls": ["https://www.tryprofound.com/blog"],
        "web_query": null
      },
      "schedule": {
        "frequency": "every 20 minutes",
        "cron": "15/20 * * * ? *",
        "timezone": "UTC",
        "next_run_at": "2026-05-29T15:15:00.000Z"
      },
      "status": "active"
    }
    

Use `events: ["changed"]` on `notification` if you only want alerts when new posts appear, not on the first baseline snapshot.

### 

[​

](#stock-price-threshold-tesla)

Stock price threshold (Tesla)

Monitor a structured data source when the condition is numeric rather than a page diff. The planner sets `tracked.type` to `data_api` and leaves `tracked.urls` empty.

    curl -sS -X POST "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Notify me when Tesla stock price drops below 436$",
        "frequency": "every 12 minutes"
      }'
    

    {
      "id": "monitor_7609p3191t",
      "object": "monitor",
      "query": "Notify me when Tesla stock price drops below 436$",
      "tracked": {
        "type": "data_api",
        "urls": [],
        "web_query": null
      },
      "schedule": {
        "frequency": "every 12 minutes",
        "cron": "2/12 * * * ? *",
        "timezone": "UTC",
        "next_run_at": "2026-05-29T15:02:00.000Z"
      },
      "status": "active"
    }
    

### 

[​

](#openai-api-changelog)

OpenAI API changelog

Get notified when [OpenAI’s API changelog](https://developers.openai.com/api/docs/changelog) lists new features, model releases, or deprecations. Mention the changelog URL in `query` or pin it with `source_policy.include_urls`.

    curl -sS -X POST "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "Notify me when the OpenAI API changelog has new updates or features https://developers.openai.com/api/docs/changelog",
        "frequency": "every hour",
        "notification": {
          "events": ["changed"],
          "channels": [{ "type": "email", "target": "you@example.com" }]
        }
      }'
    

Set `events` to `["changed"]` so you are alerted when the changelog content changes, not only when the first snapshot is stored.

### 

[​

](#managing-multiple-monitors)

Managing multiple monitors

List every monitor for your team to see status, schedules, and resolved targets in one place:

    curl -s -X GET "https://api.olostep.com/v1/monitors" \
      -H "Authorization: Bearer $OLOSTEP_API_KEY"
    

A team running the examples above might see several monitors side by side—blog watches on different cadences, a `data_api` price watch, and a YC launches monitor with email and webhook configured—with `"count": 4` (or more) in the response.

[​

](#common-validation-errors)

Common validation errors
------------------------------------------------------------

The monitor endpoints return clear validation errors for common invalid requests:

*   Missing or empty `query`
*   `frequency` that is not scheduling language, resolves too often (under 10 minutes), or exceeds 50 characters
*   Invalid `source_policy` entries (URL arrays must contain valid `http`/`https` strings)
*   Invalid `notification` shape, unknown `events`, or invalid channel `type` / `target`
*   Invalid `webhook.url` (must be `http` or `https`)
*   Invalid `output_schema` (must be valid JSON Schema)
*   Invalid `monitor_id` or `run_id` format
*   Update while `status` is `provisioning` (`409`)
*   Pause/resume when status is not `active` / `paused`

Example error:

    {
      "error": "Could not interpret 'frequency': \"check every second\". Use scheduling language such as \"every hour\" or \"every day at 9am\"."
    }
    

Was this page helpful?

YesNo
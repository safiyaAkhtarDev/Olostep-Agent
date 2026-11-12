<!-- source: https://docs.olostep.com/balance-billing/balance-and-billing -->
# https://docs.olostep.com/balance-billing/balance-and-billing

Balance & billing - Olostep Docs  

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

Balance & Billing

Balance & billing

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Balance & Billing

Balance & billing
=================

Copy pageCopy page

Check your credit balance and purchase top-ups programmatically.

Copy pageCopy page

Use the user billing endpoints to read your team’s credit balance and buy top-ups with a saved payment method. Both endpoints require authentication with your [API key](/get-started/authentication). Invalid keys return **402**.

[​

](#check-credit-balance)

Check credit balance
----------------------------------------------------

`GET /user/credits/info` returns the authenticated team’s credit balance, a per-lot breakdown, active subscription details, and whether usage is allowed. Use this endpoint to power billing widgets, usage dashboards, or pre-flight checks before running large jobs. For API details see [Get credit info](/api-reference/billing/credits-info).

Python

Node

cURL

    import requests
    
    response = requests.get(
        "https://api.olostep.com/user/credits/info",
        headers={"Authorization": "Bearer <API-TOKEN>"},
    )
    print(response.json())
    

    const res = await fetch("https://api.olostep.com/user/credits/info", {
      headers: { Authorization: "Bearer <API-TOKEN>" },
    })
    console.log(await res.json())
    

    curl -s "https://api.olostep.com/user/credits/info" \
      -H "Authorization: Bearer <API-TOKEN>"
    

### 

[​

](#response)

Response

    {
      "credits": 12500,
      "breakdown": [
        {
          "purchase_kind": "Subscription",
          "allocated_units": 10000,
          "remaining_units": 8500,
          "expiry_date": 1735689600
        },
        {
          "purchase_kind": "Top-up",
          "allocated_units": 5000,
          "remaining_units": 4000,
          "expiry_date": 1743465600
        }
      ],
      "active_subscription": {
        "id": "SUB_PRO",
        "display_name": "Pro",
        "credits": 10000,
        "created_at": 1704067200
      },
      "allow_usage": true
    }
    

Field

Description

`credits`

Total remaining credits across all non-expired lots

`breakdown`

Per-lot detail: type, allocated and remaining units, expiry

`active_subscription`

Current plan (falls back to `SUB_BASE` if none is active)

`allow_usage`

Whether the team can still consume credits

Each lot in `breakdown` has a `purchase_kind` of `Subscription`, `Top-up`, `Manual`, `Setup`, or `Pending`.

[​

](#purchase-a-top-up)

Purchase a top-up
----------------------------------------------

`POST /user/purchase-topup` charges a saved card on Stripe and buys credits in one step. There is no Checkout redirect or embedded payment UI. Pass the credit amount in the request body:

    { "credits": 10000 }
    

Field

Description

`credits`

Number of credits to purchase

Supported values: **10,000**, **20,000**, **80,000**, and **100,000**. For API details see [Purchase top-up](/api-reference/billing/purchase-topup).

Python

Node

cURL

    import requests
    
    response = requests.post(
        "https://api.olostep.com/user/purchase-topup",
        headers={
            "Authorization": "Bearer <API-TOKEN>",
            "Content-Type": "application/json",
        },
        json={"credits": 10000},
    )
    print(response.status_code)
    print(response.json())
    

    const res = await fetch("https://api.olostep.com/user/purchase-topup", {
      method: "POST",
      headers: {
        Authorization: "Bearer <API-TOKEN>",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ credits: 10000 }),
    })
    console.log(res.status)
    console.log(await res.json())
    

    curl -s -X POST "https://api.olostep.com/user/purchase-topup" \
      -H "Authorization: Bearer <API-TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{"credits": 10000}'
    

### 

[​

](#requirements)

Requirements

*   The team must have a Stripe customer with at least one saved card.
*   Only one purchase attempt is allowed every **60 seconds** per team. If you hit the cooldown, the response is **429** with a `Retry-After` header.

### 

[​

](#responses)

Responses

**200** — payment succeeded:

    {
      "success": true,
      "payment_intent_id": "pi_xxx",
      "credits": 10000
    }
    

**202** — payment is still processing. Credits are added once Stripe confirms the payment:

    {
      "success": true,
      "status": "processing",
      "payment_intent_id": "pi_xxx",
      "message": "Payment is processing. Credits will be added once the payment is confirmed.",
      "credits": 10000
    }
    

Credits are issued by the Stripe webhook after payment confirmation, not directly from the HTTP response. Treat **200** as payment success; poll `GET /user/credits/info` if you need to confirm the updated balance.

### 

[​

](#common-errors)

Common errors

Status

Error

When

400

`missing_topup_selector`

`credits` was not sent

400

`invalid_credits`

Credit amount is not in the allowed list

400

`no_stripe_customer`

Team has no Stripe customer

400

`no_payment_method`

No saved card on file

402

`payment_failed`

No saved card completed the charge

429

`purchase_topup_cooldown`

Another purchase was attempted within 60 seconds

503

`payment_status_unknown`

Ambiguous Stripe error; wait before retrying

Was this page helpful?

YesNo
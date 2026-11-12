<!-- source: https://docs.olostep.com/cli/reference/account-billing -->
# https://docs.olostep.com/cli/reference/account-billing

Account and billing commands - Olostep Docs  

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

Command reference

Account and billing commands

[Documentation

](/get-started/welcome)[SDKs

](/sdks/overview)[CLI

](/cli/overview)[Examples

](/examples/get-markdown-from-website)[Integrations

](/integrations/mcp-server)[API Reference

](/api-reference/common/object-oriented)

Command reference

Account and billing commands
============================

Copy pageCopy page

account, team, keys, credits and billing: manage your Olostep account from the terminal.

Copy pageCopy page

These commands manage your Olostep account. They act on the team you are signed in to. Commands that change something accept `--preview` and `--dry-run`, so you can check them first. `olostep whoami` is the same command as `olostep account info`.

[​

](#account)

account
--------------------------

### 

[​

](#olostep-account-info)

olostep account info

Show your signed-in Olostep account, your team, the team’s plan and its credit balance.

    olostep account info [--json] [--fields a,b]
    

Shorthand: `olostep whoami`. Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep whoami
    olostep account info --json
    

[​

](#team)

team
--------------------

Members, roles and invitations.

### 

[​

](#olostep-team-info)

olostep team info

Show your team’s name, payment method, plan and credit balance.

    olostep team info [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep team info
    

### 

[​

](#olostep-team-members)

olostep team members

List the members of your current team, their roles, and your permissions.

    olostep team members [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep team members
    olostep team members --json
    

### 

[​

](#olostep-team-rename)

olostep team rename

Rename your current team.

    olostep team rename (--team-name text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--team-name`

Yes

New team name.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep team rename --team-name "Acme Research"
    

### 

[​

](#olostep-team-invites)

olostep team invites

List your team’s pending invitations.

    olostep team invites [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep team invites
    

### 

[​

](#olostep-team-invite)

olostep team invite

Invite a person to your team by email. Olostep sends them an invitation.

    olostep team invite (--email text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--email`

Yes

Invitee email address.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep team invite --email jane@example.com
    

### 

[​

](#olostep-team-invite-revoke)

olostep team invite-revoke

Revoke a pending team invitation.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep team invite-revoke (--code text) [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--code`

Yes

Invitation code from the invitations list.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep team invites
    olostep team invite-revoke --code <code>
    

### 

[​

](#olostep-team-role)

olostep team role

Change a team member’s role. You can’t change the owner’s role, your own, or the last admin’s.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep team role (--email text) (--role admin|user) [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--email`

Yes

Member email address.

`--role`

Yes

New role. One of: `admin`, `user`.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep team role --email jane@example.com --role admin
    

### 

[​

](#olostep-team-switch-preview)

olostep team switch-preview

Preview joining the team you were invited to, without changing your membership.

    olostep team switch-preview (--invite-code text) [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--invite-code`

Yes

Invitation code.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep team switch-preview --invite-code <invite_code>
    

### 

[​

](#olostep-team-switch)

olostep team switch

Accept an invitation and switch to that team. This may remove your access to your current team.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep team switch (--invite-code text) [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--invite-code`

Yes

Invitation code.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep team switch-preview --invite-code <invite_code>
    olostep team switch --invite-code <invite_code>
    

### 

[​

](#olostep-team-domain-invite)

olostep team domain-invite

Show any team invitation set up for your email’s domain.

    olostep team domain-invite [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep team domain-invite
    

[​

](#keys)

keys
--------------------

API keys for the [Olostep API](/get-started/authentication). The CLI itself does not need one.

### 

[​

](#olostep-keys-list)

olostep keys list

List your API keys: names, metadata and `key_id`s. Never prints key values.

    olostep keys list [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep keys list
    

### 

[​

](#olostep-keys-create)

olostep keys create

Create an API key. Prints its metadata, not the key. To see the key, use `olostep keys reveal` or the dashboard.

    olostep keys create (--api-key-name text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--api-key-name`

Yes

Descriptive key name.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep keys create --api-key-name "production-server"
    

### 

[​

](#olostep-keys-reveal)

olostep keys reveal

Show an API key, or write it to an env file. The key is shown only in an interactive terminal. From a coding agent or a pipe, the CLI never prints it: use `--write-env <file>` to save it as `OLOSTEP_API_KEY` (or the name in `--var`). The file must be ignored by git, unless you pass `--force`.

    olostep keys reveal [--write-env file] [--var value] [--force] <key>
    

**Arguments**

Argument

Description

`key`

Key name or key\_id from keys list.

**Flags**

Flag

Required

Description

`--write-env`

No

Write the key to this env file instead of showing it.

`--var`

No

Variable name for —write-env. Default: `OLOSTEP_API_KEY`.

`--force`

No

Write even if git does not ignore the file.

    olostep keys reveal production-server
    olostep keys reveal production-server --write-env .env
    olostep keys reveal <key_id> --write-env .env.local --var OLOSTEP_KEY
    

### 

[​

](#olostep-keys-revoke)

olostep keys revoke

Revoke an API key by its `key_id`, never by the key itself.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep keys revoke (--key-id text) [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--key-id`

Yes

Opaque key\_id from keys list.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep keys list
    olostep keys revoke --key-id <key_id>
    

### 

[​

](#olostep-keys-manage)

olostep keys manage

Get a link to the API keys page on the Olostep dashboard.

    olostep keys manage [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep keys manage
    

[​

](#credits)

credits
--------------------------

Your balance, usage and rewards. See [Balance and billing](/balance-billing/balance-and-billing).

### 

[​

](#olostep-credits-rewards)

olostep credits rewards

List the credit rewards you can earn and whether you have claimed them.

    olostep credits rewards [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep credits rewards
    

### 

[​

](#olostep-credits-reward-claim)

olostep credits reward-claim

Claim a reward after you have completed what it asks for.

    olostep credits reward-claim (--reward slack_join|x_follow|linkedin_follow|youtube_follow|docs_visit) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--reward`

Yes

Completed reward. One of: `slack_join`, `x_follow`, `linkedin_follow`, `youtube_follow`, `docs_visit`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep credits reward-claim --reward docs_visit
    

### 

[​

](#olostep-credits-balance)

olostep credits balance

Show your team’s credit balance, plan, usage status and when credits expire.

    olostep credits balance [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep credits balance
    olostep credits balance --json
    

### 

[​

](#olostep-credits-history)

olostep credits history

Show your team’s daily credit usage for a UTC date range, including days with missing or partial data. Defaults to the last 30 days.

    olostep credits history [--start-date text] [--end-date text] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--start-date`

No

Inclusive first UTC day, YYYY-MM-DD; defaults to 29 days before end\_date.

`--end-date`

No

Inclusive last UTC day, YYYY-MM-DD; defaults to today. Cannot be in the future.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep credits history
    olostep credits history --start-date 2026-10-01 --end-date 2026-10-28 --json
    

[​

](#billing)

billing
--------------------------

Plans, invoices, payment methods and auto-refill. Payments always happen in the browser; card details never pass through the CLI.

### 

[​

](#olostep-billing-cleanup-abandoned)

olostep billing cleanup-abandoned

Void open invoices and cancel incomplete subscriptions left by abandoned checkouts. Destructive.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep billing cleanup-abandoned [--subscription-id text] [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--subscription-id`

No

Specific incomplete subscription, or omit for eligible abandoned purchases.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep billing cleanup-abandoned --preview
    

### 

[​

](#olostep-billing-subscription)

olostep billing subscription

Show the available subscriptions and your active one.

    olostep billing subscription [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep billing subscription
    

### 

[​

](#olostep-billing-plans)

olostep billing plans

List the subscription plans available to your account.

    olostep billing plans [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep billing plans
    

### 

[​

](#olostep-billing-topups)

olostep billing topups

List the credit top-ups you can buy, in a currency.

    olostep billing topups [--currency text] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--currency`

No

Three-letter currency code, such as `USD`.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep billing topups --currency USD
    

### 

[​

](#olostep-billing-invoices)

olostep billing invoices

List your team’s invoices.

    olostep billing invoices [--limit integer] [--json] [--fields a,b]
    

**Flags**

Flag

Required

Description

`--limit`

No

Invoices per page.

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep billing invoices --limit 10
    

### 

[​

](#olostep-billing-auto-refill)

olostep billing auto-refill

Show your auto-refill settings and saved payment methods.

    olostep billing auto-refill [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep billing auto-refill
    

### 

[​

](#olostep-billing-auto-refill-update)

olostep billing auto-refill-update

Turn auto-refill on or off, or change when and how it buys credits.

    olostep billing auto-refill-update (--enable true|false) [--threshold integer] [--price-id text] [--payment-method-id text] [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--enable`

Yes

Enable auto-refill.

`--threshold`

No

Credit threshold for refill.

`--price-id`

No

Top-up price id.

`--payment-method-id`

No

Saved payment method id.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep billing auto-refill-update --enable true --threshold 1000
    olostep billing auto-refill-update --enable false
    

### 

[​

](#olostep-billing-checkout)

olostep billing checkout

Start a checkout for a paid plan or a top-up. You pay in the browser. `SUB_BASE` is the Free plan and is not a checkout option.

    olostep billing checkout (--plan text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--plan`

Yes

A paid plan or top-up price id from `billing plans` or `billing topups`, such as `SUB_STARTER`.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep billing plans
    olostep billing checkout --plan SUB_STARTER
    

### 

[​

](#olostep-billing-cancel)

olostep billing cancel

Cancel your active subscription.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep billing cancel [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep billing cancel --preview
    olostep billing cancel
    

### 

[​

](#olostep-billing-portal)

olostep billing portal

Get a link to your billing portal.

    olostep billing portal [--preview] [--json] [--fields a,b] [--dry-run]
    

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep billing portal
    

### 

[​

](#olostep-billing-payment-default)

olostep billing payment-default

Make a saved payment method the team’s default.

    olostep billing payment-default (--payment-method-id text) [--preview] [--json] [--fields a,b] [--dry-run]
    

**Flags**

Flag

Required

Description

`--payment-method-id`

Yes

Saved payment method id.

Also accepts `--json`, `--fields`, `--dry-run` and `--preview`. See [Global flags](/cli/usage#global-flags).

    olostep billing auto-refill
    olostep billing payment-default --payment-method-id <payment_method_id>
    

### 

[​

](#olostep-billing-payment-remove)

olostep billing payment-remove

Remove a saved payment method. You may not be able to remove one that auto-refill uses.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep billing payment-remove (--payment-method-id text) [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--payment-method-id`

Yes

Saved payment method id.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep billing payment-remove --payment-method-id <payment_method_id>
    

### 

[​

](#olostep-billing-payment-add)

olostep billing payment-add

Get a link to add a card on the dashboard. Card details never pass through the CLI.

    olostep billing payment-add [--json] [--fields a,b]
    

Also accepts `--json` and `--fields`. See [Global flags](/cli/usage#global-flags).

    olostep billing payment-add
    

### 

[​

](#olostep-billing-pending-cancel)

olostep billing pending-cancel

Cancel an incomplete subscription left by an abandoned checkout.

Asks before it runs; pass `--yes` when there is no terminal.

    olostep billing pending-cancel (--subscription-id text) [--preview] [--json] [--fields a,b] [--dry-run] [--yes]
    

**Flags**

Flag

Required

Description

`--subscription-id`

Yes

Incomplete subscription id.

Also accepts `--json`, `--fields`, `--dry-run`, `--preview` and `--yes`. See [Global flags](/cli/usage#global-flags).

    olostep billing pending-cancel --subscription-id <subscription_id>
    

Was this page helpful?

YesNo
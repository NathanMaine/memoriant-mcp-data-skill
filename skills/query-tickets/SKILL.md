# query-tickets

Query the ticket system via MCP: list open tickets, filter by priority or customer, get ticket details, count by status, and generate ticket summaries.

## Trigger

User says something like:
- `/query-tickets`
- "show open tickets"
- "list high-priority tickets"
- "how many tickets are open?"
- "what tickets does Acme Corp have?"
- "show me all critical tickets"
- "ticket summary for this week"

## What This Skill Does

Provides a conversational interface to the tickets tool on the MCP server. Supports listing, filtering, counting, and detailing support tickets. Generates summaries suitable for support team standups or management reports.

## Step-by-Step Instructions

### Step 1: Determine the Ticket Action

Parse the request:

| Request Pattern | Ticket Action |
|----------------|---------------|
| "show/list [filter] tickets" | list with filters |
| "how many [filter] tickets" | count |
| "ticket #[id]" / "get ticket [id]" | get by ID |
| "tickets for [customer]" | filter by customer |
| "tickets this week / this month" | filter by date range |
| "ticket summary" | aggregate report |
| "escalated / critical tickets" | filter by priority |

### Step 2: Construct the Tickets Tool Call

**List with filters:**
```
Tool: tickets
Input: {
  "action": "list",
  "filters": {
    "status": "open",
    "priority": "high",
    "customer": "<name>",
    "date_from": "<ISO date>",
    "date_to": "<ISO date>"
  },
  "limit": 50
}
```

**Get by ID:**
```
Tool: tickets
Input: {"action": "get", "id": "<ticket-id>"}
```

**Count:**
```
Tool: tickets
Input: {
  "action": "count",
  "filters": {"status": "open"}
}
```

**Search:**
```
Tool: tickets
Input: {"action": "search", "query": "<search term>"}
```

### Step 3: Display Results

**Ticket list:**
```
Open Tickets — High Priority (8 total)
══════════════════════════════════════════════════════════════
  ID     │ Customer        │ Subject                  │ Assigned   │ Age
  #9871  │ Acme Corp       │ API integration failing  │ Bob Lee    │ 3 days
  #9856  │ BuildRight LLC  │ Login errors prod env    │ Alice Wu   │ 5 days
  #9843  │ CloudFirst Inc. │ Data export timeout      │ Bob Lee    │ 8 days
  ...
```

**Single ticket:**
```
Ticket #9871
══════════════════════════════════════════════════════════════
Customer:   Acme Corp
Subject:    API integration failing
Status:     Open
Priority:   High
Assignee:   Bob Lee (bob@company.com)
Created:    2026-03-22 09:14
Updated:    2026-03-24 15:33
Age:        3 days open

Description:
  Customer reports POST /api/v2/sync returning 500 errors since 3/22 update.

Latest Note (2026-03-24):
  Bob Lee: "Identified root cause — rate limit config regression. Fix in progress."
```

**Count result:**
```
Ticket Counts:
  Open:      47
  Pending:   12
  Escalated:  3
  Closed:   234 (last 30 days)
```

### Step 4: Weekly Ticket Summary

When user asks for a "ticket summary", generate:

```
Ticket Summary — Week of 2026-03-18
══════════════════════════════════════════════════════════════
New this week:     23  (↑ 4 from last week)
Resolved:          18  (↓ 2 from last week)
Net change:        +5

Priority Breakdown:
  Critical:   1  (↑ from 0)
  High:       8
  Medium:     12
  Low:         2

Top Customers (by open tickets):
  Acme Corp        3 open tickets
  BuildRight LLC   2 open tickets
  DataFlow Inc.    2 open tickets

Oldest Open Tickets:
  #9801  CloudFirst Inc.  14 days  "Database sync lag"
  #9789  Acme Corp        18 days  "Legacy API deprecation"
```

### Step 5: Customer Ticket View

When filtering by customer, show all tickets with a brief summary:

```
Tickets — Acme Corp (3 open, 12 total)
══════════════════════════════════════════════════════════════
Open:
  #9871  High  "API integration failing"  3 days
  #9799  Med   "User export missing columns"  21 days
  #9756  Low   "Documentation request"  35 days

Recently Closed:
  #9712  "Authentication bug"  Closed 2026-03-10
  #9688  "Performance query"   Closed 2026-02-28
```

### Step 6: Follow-Up Suggestions

After displaying tickets, suggest:
- "Want to cross-reference with CRM account data? Try `/explore-crm Acme Corp`"
- "Want a full customer profile across all systems? Try `/query-data 'complete profile for Acme Corp'`"

## Filter Reference

| Filter | Values | Notes |
|--------|--------|-------|
| status | open, closed, pending, escalated | Default: open |
| priority | low, medium, high, critical | Can combine: "high or critical" |
| customer | any string | Partial match supported |
| assignee | name | Tickets assigned to a specific person |
| date_from | ISO date | Tickets created after this date |
| date_to | ISO date | Tickets created before this date |
| age_days | integer | Tickets open longer than N days |

## Error Handling

| Situation | Response |
|-----------|----------|
| Ticket not found | "Ticket #<id> not found in the ticket system." |
| No tickets match filters | "No tickets found matching your filters. Try widening the search." |
| Tickets tool unavailable | "Ticket system is not available. Check MCP server status." |

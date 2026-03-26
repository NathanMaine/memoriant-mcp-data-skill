# explore-crm

Interactively explore CRM data: look up accounts and contacts, list customers by status or region, search by name, and generate account summaries.

## Trigger

User says something like:
- `/explore-crm`
- "look up customer X in the CRM"
- "show me all active accounts"
- "who is the account rep for Acme Corp?"
- "list prospects in the northeast region"
- "CRM summary for this customer"

## What This Skill Does

Provides a conversational interface to the CRM tool on the MCP server. Supports lookup by name or ID, filtered listing, search, and rich account summary generation. Bridges the gap between plain-language questions and CRM API calls.

## Step-by-Step Instructions

### Step 1: Determine the CRM Action

Parse the user's request to determine the action type:

| Request Pattern | CRM Action |
|----------------|------------|
| "look up [name]", "find [name]", "who is [name]" | lookup by name |
| "list all [status] accounts", "show [region] customers" | filtered list |
| "search for [term]" | search |
| "count [filter]" | count |
| "summary for [name]" | lookup + full summary generation |

### Step 2: Construct the CRM Tool Call

**Lookup by name:**
```
Tool: crm
Input: {"action": "lookup", "entity": "account", "filters": {"name": "<name>"}}
```

**Filtered list:**
```
Tool: crm
Input: {
  "action": "list",
  "entity": "account",
  "filters": {"status": "<active|inactive|prospect>", "region": "<region>"},
  "limit": 20
}
```

**Search:**
```
Tool: crm
Input: {"action": "search", "entity": "account", "query": "<search term>"}
```

**Count:**
```
Tool: crm
Input: {"action": "count", "entity": "account", "filters": {"status": "active"}}
```

### Step 3: Display Results

**Single account lookup:**
```
Account: Acme Corp
══════════════════════════════════════════
CRM ID:          12345
Status:          Active
Account Rep:     Jane Smith (jane@company.com)
Region:          Northeast
Contract Value:  $45,000/year
Tier:            Enterprise
Created:         2024-06-15
Last Activity:   2026-03-22
```

**List results:**
```
Active Accounts — Northeast Region (12 total)
══════════════════════════════════════════════════════
  Name                │ Status   │ Rep          │ Value
  Acme Corp           │ Active   │ Jane Smith   │ $45,000
  BuildRight LLC      │ Active   │ Tom Jones    │ $28,000
  CloudFirst Inc.     │ Active   │ Jane Smith   │ $120,000
  ...
```

**Count result:**
```
Active accounts: 147
Prospects: 43
Inactive: 22
```

### Step 4: Account Summary Generation

When the user asks for a "summary", combine CRM data with a narrative:

```
Account Summary: Acme Corp
══════════════════════════════════════════════════════
Enterprise customer since June 2024. Annual contract value $45,000.
Account is Active with account rep Jane Smith. Based in the Northeast region.
Tier: Enterprise. Last CRM activity: March 22, 2026.

To see open tickets: /query-tickets for Acme Corp
To see order history: /query-data "show orders for Acme Corp"
```

### Step 5: Follow-Up Suggestions

After any CRM result, suggest relevant follow-up queries:
- "Want to see support tickets for this customer? Try `/query-tickets [name]`"
- "Want a full cross-system profile? Try `/query-data 'complete profile for [name]'`"

## Filtering Options

| Filter | Values | Example |
|--------|--------|---------|
| status | active, inactive, prospect | "list active accounts" |
| region | any string | "northeast accounts" |
| rep | rep name | "Jane Smith's accounts" |
| tier | standard, enterprise, partner | "enterprise accounts" |
| value_min | number | "accounts over $50,000" |

## Error Handling

| Situation | Response |
|-----------|----------|
| Account not found | "No account matching '<name>' found in CRM. Try a partial name search." |
| Multiple matches | "Found <N> accounts matching '<name>'. Which did you mean?" (list options) |
| CRM tool unavailable | "CRM tool is not available on the MCP server. Run /discover-schema to check." |

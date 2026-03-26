# discover-schema

Explore and document the schema of connected data sources: list available MCP tools, describe their fields and types, and generate a unified data map.

## Trigger

User says something like:
- `/discover-schema`
- "what data do I have access to?"
- "show me the schema"
- "what fields does the CRM have?"
- "map my data sources"
- "explore my database schema"

## What This Skill Does

Interrogates connected MCP tools to discover their schemas, field types, relationships, and sample data shapes. Produces a unified data map document so users know exactly what questions they can ask.

## Step-by-Step Instructions

### Step 1: Connect to MCP Server

Check if the MCP server is running. If no MCP server URL is configured, ask:
"What is your MCP server URL? (default: http://localhost:8000)"

Store the URL for the session.

### Step 2: List Available Tools

Call the MCP server's tool listing endpoint. Display all registered tools:

```
Available MCP Tools
═══════════════════════════════════════════════════════
  Tool         │ Description
  crm          │ Customer account and contact data
  tickets      │ Support ticket system
  legacy_db    │ Legacy transactional database
```

If no tools are registered, prompt: "No tools found on the MCP server. Check your server configuration."

### Step 3: Describe Each Tool

For each tool, call a schema introspection request (or use the tool's describe/schema action):

**CRM Schema:**
```
Tool: crm
Schema:
  Input fields:
    action    string   required   [lookup, list, count, search]
    entity    string   required   [account, contact, opportunity]
    filters   object   optional
      name    string
      id      string
      status  string   [active, inactive, prospect]
      region  string
    limit     integer  optional   default: 20

  Sample output fields:
    id          string   CRM record ID
    name        string   Company/contact name
    status      string   Account status
    rep         string   Account representative
    value       number   Contract value
    created_at  string   ISO date
    updated_at  string   ISO date
```

**Tickets Schema:**
```
Tool: tickets
Schema:
  Input fields:
    action    string   required   [list, get, count, search]
    filters   object   optional
      customer  string
      status    string   [open, closed, pending, escalated]
      priority  string   [low, medium, high, critical]
      date_from string   ISO date
      date_to   string   ISO date
    limit     integer  optional   default: 50

  Sample output fields:
    id          string   Ticket ID
    subject     string   Ticket title
    status      string
    priority    string
    customer    string
    created_at  string
    updated_at  string
    assignee    string
```

**Legacy DB Schema:**
```
Tool: legacy_db
Schema:
  Input fields:
    action    string   required   [query, describe, list_tables]
    sql       string   conditional  required for action=query
    table     string   conditional  required for action=describe

  Tables:
    orders         (id, customer_name, amount, status, created_at, delivered_at)
    products       (id, name, sku, price, category, stock)
    transactions   (id, order_id, amount, type, timestamp)

  Sample query:
    SELECT * FROM orders WHERE created_at > '2026-01-01' LIMIT 10
```

### Step 4: Detect Relationships

Analyze field names across tools to identify likely joins:

```
Detected Relationships:
  crm.name         ↔  tickets.customer    (customer name join)
  crm.id           ↔  legacy_db.customer_id  (if present)
  tickets.id       ↔  legacy_db.ticket_id    (if present)

Cross-source query example:
  "Get all tickets + orders for customer Acme Corp"
  → crm lookup by name → tickets filter by customer → legacy_db query by customer_name
```

### Step 5: Write Schema Document

Write a complete schema map to `mcp-schema.md`:

```markdown
# MCP Data Source Schema Map
Generated: <ISO datetime>
Server: <URL>

## Available Tools
...full schema descriptions...

## Cross-Source Relationships
...detected joins...

## Example Queries
"What is the current status of Acme Corp?" → crm lookup
"List all open high-priority tickets" → tickets list with filters
"Show orders over $10,000 in Q1 2026" → legacy_db SQL query
"Complete profile for customer X" → crm + tickets + legacy_db
```

### Step 6: Sample Data Preview

Offer to fetch a small sample from each source to validate connectivity:
"Would you like to see 3 sample records from each source? (yes/no)"

If yes, call each tool with `limit: 3` and display results as tables.

## Output Files

- `mcp-schema.md` — full schema map
- Terminal: formatted schema summary

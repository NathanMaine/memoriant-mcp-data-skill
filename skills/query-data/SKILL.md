# query-data

Answer natural language questions by querying one or more connected data sources (CRM, tickets, legacy database) through the MCP server and returning a unified, plain-language answer.

## Trigger

User says something like:
- `/query-data`
- "ask a question about my data"
- "query my CRM"
- "what does the database say about..."
- "look up customer X across all systems"

## What This Skill Does

Takes a natural language question, determines which data sources are relevant, translates the question into the appropriate query for each source (MCP tool call, SQL, or API), executes the queries in parallel, and synthesizes a single coherent answer.

Core value proposition: instead of logging into 5 different systems, ask one question and get one answer.

## Step-by-Step Instructions

### Step 1: Receive the Question

Ask the user: "What would you like to know? Ask in plain English."

Examples:
- "What is the current balance and latest ticket for customer Acme Corp?"
- "Show me all open support tickets for orders placed in the last 30 days"
- "Which customers haven't had any activity in 90+ days?"

### Step 2: Parse Intent and Entities

Extract from the question:
- **Action**: look up, list, count, compare, summarize
- **Entities**: customer names, IDs, date ranges, statuses
- **Data sources needed**: CRM (account data), tickets (support data), legacy DB (transactional data)
- **Filters**: date range, status, region, amount threshold, etc.

### Step 3: Route to Data Sources

Determine which MCP tools to call:

| Data Need | MCP Tool |
|-----------|----------|
| Customer/account info | `crm` tool |
| Support tickets | `tickets` tool |
| Transactional/historical | `legacy_db` tool |
| Cross-system | all three in parallel |

### Step 4: Construct MCP Tool Calls

For each required data source, construct the tool call:

**CRM query:**
```
Tool: crm
Input: {
  "action": "lookup",
  "entity": "account",
  "filters": {"name": "Acme Corp"}
}
```

**Tickets query:**
```
Tool: tickets
Input: {
  "action": "list",
  "filters": {"customer": "Acme Corp", "status": "open"}
}
```

**Legacy DB query:**
```
Tool: legacy_db
Input: {
  "action": "query",
  "sql": "SELECT * FROM orders WHERE customer_name = 'Acme Corp' ORDER BY created_at DESC LIMIT 10"
}
```

### Step 5: Execute Queries

Call all required MCP tools. Handle responses:
- Successful response: extract relevant fields
- Empty response: note "no records found" for that source
- Error response: note the error and continue with other sources

### Step 6: Synthesize the Answer

Combine results from all sources into a single, clear answer. Format appropriate to the question type:

**Lookup question** → narrative summary:
```
Acme Corp (CRM ID: 12345)
  Account Status:  Active
  Account Rep:     Jane Smith
  Contract Value:  $45,000/year

Latest Support Ticket (Ticket #9871):
  Subject:  "API integration failing"
  Status:   Open
  Priority: High
  Created:  2026-03-22

Recent Orders (Legacy DB):
  Order #10234  $12,500  2026-03-15  Delivered
  Order #10198   $8,200  2026-02-28  Delivered
```

**List question** → table format:
Show results in a clean markdown table.

**Count/aggregate question** → summary with number:
"There are 47 open tickets from the last 30 days, across 23 unique customers."

### Step 7: Cite Sources

Always end with a source citation:
```
Sources: CRM (1 record), Tickets (1 open ticket), Legacy DB (2 orders)
Query time: 0.8s
```

## Error Handling

| Situation | Response |
|-----------|----------|
| MCP server not running | "MCP server is not available. Please start it: `python src/server.py`" |
| Tool not found | "The <tool> tool is not registered on the MCP server." |
| Query returns no results | "No records found for your query in <source>." |
| SQL parse error | Show the generated SQL and ask user to clarify the question |

## Output Format

Plain-language answer with structured data inline. No raw JSON in the response unless the user asks for it.

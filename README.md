<p align="center">
  <img src="https://img.shields.io/badge/claude--code-plugin-8A2BE2" alt="Claude Code Plugin" />
  <img src="https://img.shields.io/badge/skills-4-blue" alt="4 Skills" />
  <img src="https://img.shields.io/badge/agents-2-green" alt="2 Agents" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" />
</p>

# Memoriant MCP Data Skill

A Claude Code plugin for conversational data access via the Model Context Protocol (MCP). Ask questions in plain English and get answers from CRM, ticket systems, and databases — all at once, without logging into each system separately.

**No servers. No Docker. Just install and use.**

## Install

```bash
/install NathanMaine/memoriant-mcp-data-skill
```

## Cross-Platform Support

### Claude Code (Primary)
```bash
/install NathanMaine/memoriant-mcp-data-skill
```

### OpenAI Codex CLI
```bash
git clone https://github.com/NathanMaine/memoriant-mcp-data-skill.git ~/.codex/skills/mcp-data
codex --enable skills
```

### Gemini CLI
```bash
gemini extensions install https://github.com/NathanMaine/memoriant-mcp-data-skill.git --consent
```

## Skills

| Skill | Command | What It Does |
|-------|---------|-------------|
| **Query Data** | `/query-data` | Natural language → parallel MCP queries → unified answer |
| **Discover Schema** | `/discover-schema` | Map all connected data sources: fields, types, relationships |
| **Explore CRM** | `/explore-crm` | Lookup, list, filter, and summarize CRM accounts and contacts |
| **Query Tickets** | `/query-tickets` | List, filter, count, and summarize support tickets |

## Agents

| Agent | Best Model | Specialty |
|-------|-----------|-----------|
| **Data Query Agent** | Sonnet 4.6 | Multi-source NL query, parallel tool calls, answer synthesis |
| **Schema Explorer** | Sonnet 4.6 | Schema discovery, relationship detection, data map generation |

## Quick Start

```bash
# Discover what data sources you have
/discover-schema

# Ask a plain-English question across all sources
/query-data

# Look up a specific customer
/explore-crm

# List open high-priority tickets
/query-tickets
```

## The Core Value

Instead of logging into 5 different systems to answer one customer question, ask this plugin one question:

```
"What is the current status, open tickets, and recent orders for Acme Corp?"
```

**Result:**
```
Acme Corp (CRM: Active, $45,000/year, Rep: Jane Smith)

Open Tickets (2):
  #9871  High  "API integration failing"   3 days
  #9799  Med   "Export missing columns"   21 days

Recent Orders:
  Order #10234  $12,500  2026-03-15  Delivered
  Order #10198   $8,200  2026-02-28  Delivered

Sources: CRM (1 record), Tickets (2 open), Legacy DB (2 orders) — 0.8s
```

## MCP Tool Pattern

This plugin follows the MCP (Model Context Protocol) server pattern:

```
User question
  ↓
Natural language parsing (subject, verb, object, filters)
  ↓
Tool routing (crm / tickets / legacy_db / all)
  ↓
Parallel MCP tool calls
  ↓
Response synthesis
  ↓
Unified plain-language answer
```

## Connected Data Sources

| Tool | Data | Example Questions |
|------|------|-------------------|
| `crm` | Accounts, contacts, reps, contracts | "Who is Acme Corp's account rep?" |
| `tickets` | Support tickets, status, priority | "List all critical open tickets" |
| `legacy_db` | Orders, transactions, products | "Show Q1 orders over $10,000" |

## Schema Discovery

```
/discover-schema
```

Outputs `mcp-schema.md` with:
- All available tools and their field types
- Detected cross-source relationships (e.g., `crm.name ↔ tickets.customer`)
- Example queries for each data source
- Sample records to validate connectivity

## Use Cases

- Support team: complete customer picture before a call
- Sales: account status + recent tickets + order history in one view
- Operations: cross-system reporting without manual data assembly
- Engineering: natural language database exploration during development
- Management: aggregate counts and summaries across all systems

## Source Repository

Built from [NathanMaine/mcp-conversational-data-agent](https://github.com/NathanMaine/mcp-conversational-data-agent).

## License

MIT — see [LICENSE](LICENSE) for details.

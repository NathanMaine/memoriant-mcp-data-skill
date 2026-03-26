# Memoriant MCP Data Skill

Conversational data access skills for coding agents via MCP server pattern.

## Available Skills

### query-data
Answer natural language questions by querying multiple data sources (CRM, tickets, legacy database) through MCP tools in parallel and returning a unified plain-language answer.

Skill file: `skills/query-data/SKILL.md`

### discover-schema
Enumerate and document the schema of all connected MCP tools: field types, allowed values, cross-source relationships, and example queries. Writes a persistent `mcp-schema.md`.

Skill file: `skills/discover-schema/SKILL.md`

### explore-crm
Conversational CRM exploration: look up accounts by name or ID, list and filter customers, generate account summaries, and cross-reference with other data sources.

Skill file: `skills/explore-crm/SKILL.md`

### query-tickets
Query the ticket system: list by status/priority/customer, get ticket details, count by filter, and generate weekly summary reports.

Skill file: `skills/query-tickets/SKILL.md`

## Available Agents

### data-query-agent
Multi-source natural language query agent. Parses questions, selects relevant MCP tools, calls them in parallel, and synthesizes unified answers.

Agent file: `agents/data-query-agent.md`

### schema-explorer-agent
Schema discovery and documentation agent. Systematically probes MCP tools, maps fields and relationships, and maintains a live schema document.

Agent file: `agents/schema-explorer-agent.md`

## Install

```bash
# Claude Code (primary)
/install NathanMaine/memoriant-mcp-data-skill

# OpenAI Codex CLI
git clone https://github.com/NathanMaine/memoriant-mcp-data-skill.git ~/.codex/skills/mcp-data
codex --enable skills

# Google Gemini CLI
gemini extensions install https://github.com/NathanMaine/memoriant-mcp-data-skill.git --consent
```

## Source Repository

[NathanMaine/mcp-conversational-data-agent](https://github.com/NathanMaine/mcp-conversational-data-agent)

# Security Policy

## What This Plugin Does

This plugin consists entirely of markdown instruction files (SKILL.md and agent .md files). It contains:
- No executable code
- No shell scripts
- No network calls
- No file system modifications beyond what Claude Code normally does

All MCP server queries, schema discovery, and data synthesis are performed by Claude Code using its standard tools, guided by the skill instructions in this plugin.

## Data Handling

- This plugin routes queries to your locally configured MCP server
- Data returned from MCP tools is displayed in your Claude Code session and not stored by this plugin
- Schema documentation is written to `mcp-schema.md` in your local workspace
- No customer data, CRM records, or ticket data is transmitted outside your network by this plugin
- All network traffic goes from your machine to your MCP server (typically localhost or your internal network)

## MCP Server Security

The security of data accessed through MCP tools depends on your MCP server configuration. This plugin does not:
- Bypass authentication on your MCP server
- Store or cache credentials
- Transmit MCP data to external services

Ensure your MCP server is properly secured (authentication, network binding, TLS if remote).

## SQL Injection Prevention

When the `query-data` and `query-tickets` skills generate SQL for the `legacy_db` tool, the instructions specify parameterized values or explicit escaping for user-provided strings. Review generated SQL before executing against production databases.

## Reporting a Vulnerability

If you discover a security issue, please email nathan@memoriant.com (do not open a public issue).

We will respond within 48 hours and provide a fix timeline.

## Auditing This Plugin

This plugin is easy to audit:
1. All files are markdown — readable in any text editor
2. No `node_modules`, no Python packages, no compiled binaries
3. Review any SKILL.md file to see exactly what instructions are given to the AI
4. The `.claude-plugin/plugin.json` lists all skills and agents declared by this plugin

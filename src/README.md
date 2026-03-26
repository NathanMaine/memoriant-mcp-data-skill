# MCP Conversational Data Access Agent

Instead of having to log into 5 different websites to answer a customer's question,
a support agent can ask this AI one question.
The AI talks to all 5 systems at once and gives back a single, simple answer.

## What This Is

- A skeleton for a Model Context Protocol (MCP) server.
- Exposes toy tools like `crm`, `tickets`, `legacy_db`.
- Lets an LLM-powered client call these tools to answer questions.

This repo focuses on the shape of an MCP server, not any provider-specific details.

## IP-Safety Boundaries

- No global governance gateway or policy engine.
- No special token-limit or routing logic.
- All data sources are toy, local mocks.

## Suggested Layout

- `src/server.py` -- entrypoint for MCP server.
- `src/tools/crm.py` -- simple in-memory fake CRM.
- `src/tools/tickets.py` -- fake ticket store.
- `src/tools/legacy_db.py` -- toy SQLite or in-memory table.

## Quickstart

This skeleton does not include a concrete MCP library to keep it generic.
You can:

- Pick an MCP implementation you like.
- Wire `src/server.py` into that runtime.
- Map functions in `src/tools/*` to MCP tools.

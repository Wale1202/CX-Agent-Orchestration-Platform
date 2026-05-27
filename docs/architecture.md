# Architecture

This document describes the current shape of the system and the planned phases.
It will grow as the project does.

## Big picture

```
┌────────────────┐        ┌──────────────────────┐        ┌──────────────┐
│  React (Vite)  │ ─────▶ │  FastAPI (Python)    │ ─────▶ │  PostgreSQL  │
│  - Chat widget │  HTTP  │  - REST API          │  SQL   │  + pgvector  │
│  - Dashboard   │        │  - Agent orchestrator│        └──────────────┘
└────────────────┘        │  - LLM client (mock) │
                          └──────────────────────┘
```

A customer talks to the agent through the chat widget. The backend handles
the agent loop: retrieving relevant knowledge, calling tools, scoring the
response, and persisting messages. Tickets are created when the agent
escalates.

## LLM abstraction

The agent never talks to a vendor SDK directly. It depends on a single
`LLMClient` interface. Two implementations:

- `MockLLM` — scripted replies, used for local dev and tests. No API key
  needed.
- Real provider — selected by `LLM_PROVIDER` and `LLM_API_KEY` env vars
  (planned: OpenAI and Anthropic).

This keeps tests fast and deterministic and lets the project run with no
external dependencies.

## Phases

1. **Scaffolding** *(current)* — FastAPI skeleton, health check, DB wiring,
   frontend shell, Docker compose.
2. **Conversation loop with mocked agent** — Conversation/Message models,
   chat endpoints, mock agent that echoes a canned reply.
3. **Real LLM + tool calling** — `LLMClient` swap, tool registry, first two
   tools (`lookup_order`, `create_ticket`).
4. **RAG** — Knowledge document ingestion, embeddings in pgvector,
   retrieval-as-a-tool.
5. **Scoring + escalation** — Sentiment / urgency / confidence on each turn,
   auto-escalation rules, ticket creation.
6. **Agent dashboard** — Conversation list, ticket queue, basic metrics.
7. **Polish** — Architecture diagram, ADRs, seed script, demo.

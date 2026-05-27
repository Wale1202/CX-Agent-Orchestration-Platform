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

## Data model

Six tables — kept deliberately small. See `backend/app/models/` for the
authoritative definitions; the diagram below is just a sketch.

```
Customer ─┬─< Order
          ├─< Conversation ──< Message
          └─< Ticket  >── Conversation

KnowledgeBaseArticle   (standalone for now; chunks/embeddings land in Phase 4)
```

A few choices worth flagging:

- **Categorical fields are plain `String` columns**, not Postgres enums.
  The Pydantic schemas constrain values via `Literal` types at the API
  boundary. This lets us add new sentiment labels, ticket categories, etc.
  without a migration.
- **Scoring fields on `Conversation`** (`sentiment`, `urgency`,
  `confidence_score`) are nullable. They stay `None` until the agent has
  scored at least one turn, which avoids fabricating defaults.
- **`tags` on `KnowledgeBaseArticle`** is a Postgres `text[]` column.
  Simpler than a join table for the kind of keyword filtering the MVP needs.
- **Schema is created via `Base.metadata.create_all()`** from a FastAPI
  lifespan hook. This is a dev shortcut; Alembic migrations are the planned
  replacement before this runs against real users.

## Phases

1. **Scaffolding + data model** *(current)* — FastAPI skeleton, health check,
   ORM models, Pydantic schemas, seed data, Docker compose.
2. **Conversation loop with mocked agent** — chat endpoints, mock agent
   that echoes a canned reply, message persistence.
3. **Real LLM + tool calling** — `LLMClient` swap, tool registry, first two
   tools (`lookup_order`, `create_ticket`).
4. **RAG** — Knowledge document ingestion, embeddings in pgvector,
   retrieval-as-a-tool.
5. **Scoring + escalation** — Sentiment / urgency / confidence on each turn,
   auto-escalation rules, ticket creation.
6. **Agent dashboard** — Conversation list, ticket queue, basic metrics.
7. **Polish** — Architecture diagram, ADRs, seed script, demo.

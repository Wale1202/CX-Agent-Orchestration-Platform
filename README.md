# CX Agent Orchestration Platform

A minimal conversational AI customer-support platform. It demonstrates how an
LLM-powered agent can handle real support conversations end-to-end: answering
from a knowledge base, calling tools (e.g. order lookup), scoring sentiment
and urgency, and escalating to a human ticket when it can't help.

Built as a portfolio project to showcase backend, AI integration, and full-stack
skills relevant to contact-center / customer-experience platforms.

---

## What it does (target scope)

- Customer chats with an AI agent through a web widget.
- The agent retrieves answers from a knowledge base (RAG) and calls tools when
  needed (look up an order, check refund status, create a ticket).
- Every agent turn is scored for sentiment, urgency, and confidence.
- If the agent can't help or the customer is frustrated, the conversation
  escalates and a support ticket is created.
- A separate dashboard lets a human agent view conversations, sentiment, and
  the ticket queue.

This repository currently contains the **initial scaffolding** — the FastAPI
app skeleton, database wiring, frontend shell, and Docker setup. Features will
be added in phases (see `docs/architecture.md`).

---

## Stack

| Layer    | Choice                                              |
|----------|-----------------------------------------------------|
| Backend  | Python 3.11, FastAPI, SQLAlchemy 2.0, Pydantic v2   |
| Database | PostgreSQL 16 (with `pgvector` for RAG later)       |
| Frontend | React 18, TypeScript, Vite                          |
| AI       | Pluggable LLM client (mock by default, OpenAI/Anthropic via env) |
| Testing  | Pytest                                              |
| DevOps   | Docker + docker-compose                             |

---

## Project layout

```
.
├── backend/         FastAPI app, models, agent, tests
├── frontend/        Vite + React + TypeScript app
├── docs/            Architecture notes and decisions
├── docker-compose.yml
└── README.md
```

---

## Running locally

The easiest way to start everything is Docker:

```bash
docker compose up --build
```

That brings up three services:

- `db` — PostgreSQL on `localhost:5432`
- `backend` — FastAPI on `http://localhost:8000`
- `frontend` — Vite dev server on `http://localhost:5173`

Verify the backend is healthy:

```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

### Running the backend without Docker

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # then edit if needed
uvicorn app.main:app --reload
```

### Running the frontend without Docker

```bash
cd frontend
npm install
npm run dev
```

---

## Environment variables

See `backend/.env.example` and `frontend/.env.example`. Defaults work
out-of-the-box with `docker compose up`.

Key backend variables:

- `DATABASE_URL` — Postgres connection string
- `LLM_PROVIDER` — `mock` (default), `openai`, or `anthropic`
- `LLM_API_KEY` — only required when `LLM_PROVIDER` is not `mock`

The platform runs entirely on the mock LLM by default, so no API key is
required to demo the project.

---

## Tests

```bash
cd backend
pytest
```

---

## Status

This is an early-stage portfolio project under active development. See
`docs/architecture.md` for the planned phases and current progress.

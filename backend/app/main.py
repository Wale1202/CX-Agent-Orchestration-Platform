from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health
from app.config import settings
from app.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Dev shortcut — create tables if they don't exist. Replace with Alembic
    # before this app handles real users.
    init_db()
    yield


app = FastAPI(
    title="CX Agent Orchestration Platform",
    description="LLM-powered customer support agent with tools, RAG, and escalation.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])

"""Pydantic schemas for API request and response bodies.

Schemas are split per resource. Each module exposes a ``*Create`` shape for
inputs and a ``*Read`` shape for outputs. Read schemas use
``from_attributes=True`` so they can be built directly from ORM objects.
"""

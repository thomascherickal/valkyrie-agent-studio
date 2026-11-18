"""FastAPI route for generating custom agents from plain-English prompts."""

from __future__ import annotations

from dataclasses import asdict
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from valkyrie.agent_generator import generate_agent_from_english

router = APIRouter(prefix="/api/agents", tags=["agent-generator"])


class CreateFromPromptRequest(BaseModel):
    """Plain-English prompt request for custom agent synthesis."""

    prompt: str
    role: str = "Custom Agents"
    name: str | None = None


@router.post("/create-from-prompt")
def create_agent_from_prompt(req: CreateFromPromptRequest) -> dict[str, object]:
    """Generate YAML IR, Python, tests, docs, and Rust code from English."""
    try:
        bundle = generate_agent_from_english(req.prompt, role=req.role, name=req.name)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return asdict(bundle)

"""FastAPI route for generating custom agents from plain-English prompts."""

from __future__ import annotations

from dataclasses import asdict
import os
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from valkyrie.agent_generator import generate_agent_from_english, write_generated_agent
from valkyrie.ir_schema import load_ir_from_yaml

router = APIRouter(prefix="/api/agents", tags=["agent-generator"])


class CreateFromPromptRequest(BaseModel):
    """Plain-English prompt request for custom agent synthesis."""

    prompt: str
    role: str = "Custom Agents"
    name: str | None = None


def custom_agents_dir() -> Path:
    """Where created agents are saved. Set VALKYRIE_CUSTOM_DIR to move it."""
    default = Path(__file__).resolve().parents[2] / "custom-agents"
    return Path(os.environ.get("VALKYRIE_CUSTOM_DIR") or default)


@router.post("/create-from-prompt")
def create_agent_from_prompt(req: CreateFromPromptRequest) -> dict[str, object]:
    """Generate YAML IR, Python, tests, docs, and Rust code from English, and save them to disk."""
    try:
        bundle = generate_agent_from_english(req.prompt, role=req.role, name=req.name)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    write_generated_agent(bundle, custom_agents_dir())
    return asdict(bundle)


@router.get("/custom")
def list_custom_agents() -> dict[str, list[dict[str, str]]]:
    """List the agents saved by create-from-prompt, so the GUI can restore them after a restart."""
    agents: list[dict[str, str]] = []
    for ir_file in sorted(custom_agents_dir().glob("*/agent.ir.yaml")):
        ir = load_ir_from_yaml(ir_file.read_text())
        agents.append({"id": ir.id, "name": ir.name, "description": ir.description, "tool": ir.tools[0].name})
    return {"agents": agents}

"""FastAPI route for generating custom agents from plain-English prompts."""

from __future__ import annotations

from dataclasses import asdict
import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from valkyrie import tracing
from valkyrie.agent_generator import generate_agent_from_english, write_generated_agent
from valkyrie.ir_schema import load_ir_from_yaml
from valkyrie.storage import custom_agents_dir, delete_custom_agent, drop_custom_edits

router = APIRouter(prefix="/api/agents", tags=["agent-generator"])


class CreateFromPromptRequest(BaseModel):
    """Plain-English prompt request for custom agent synthesis."""

    prompt: str
    role: str = "Custom Agents"
    name: str | None = None


@router.post("/create-from-prompt")
def create_agent_from_prompt(req: CreateFromPromptRequest) -> dict[str, object]:
    """Generate YAML IR, Python, tests, docs, and Rust code from English, and save them to disk."""
    try:
        bundle = generate_agent_from_english(req.prompt, role=req.role, name=req.name)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    write_generated_agent(bundle, custom_agents_dir())
    tracing.step("agent.create", f"created custom agent {bundle.agent_id}", agent_id=bundle.agent_id, name=bundle.name)
    drop_custom_edits(bundle.agent_id)  # a regenerated agent starts from its new original, not an old edit
    return asdict(bundle)


@router.get("/custom")
def list_custom_agents() -> dict[str, list[dict[str, str]]]:
    """List the agents saved by create-from-prompt, so the GUI can restore them after a restart."""
    agents: list[dict[str, str]] = []
    for ir_file in sorted(custom_agents_dir().glob("*/agent.ir.yaml")):
        ir = load_ir_from_yaml(ir_file.read_text())
        agents.append({"id": ir.id, "name": ir.name, "description": ir.description, "tool": ir.tools[0].name})
    return {"agents": agents}


@router.delete("/custom/{agent_id}")
def delete_agent(agent_id: str) -> dict[str, str]:
    """Remove a saved custom agent, with its edits and saved implementations."""
    if not re.fullmatch(r"[a-z0-9-]+", agent_id):
        raise HTTPException(status_code=400, detail="Invalid agent id")
    if not delete_custom_agent(agent_id):
        raise HTTPException(status_code=404, detail=f"No custom agent {agent_id}")
    tracing.step("agent.delete", f"deleted custom agent {agent_id}", agent_id=agent_id)
    return {"deleted": agent_id}

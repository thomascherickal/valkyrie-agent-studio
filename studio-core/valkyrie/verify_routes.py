"""Verify an agent before Deploy to Rust, and save a verified agent as a new Custom Agent."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from valkyrie import tracing
from valkyrie.agent_copy import NAME_MAX, copy_agent, copy_edits, slug
from valkyrie.agent_impls import CUSTOM_ROLE_ID, agent_dir, load_spec
from valkyrie.storage import custom_agents_dir, edits_dir
from valkyrie.verify import verify_agent

router = APIRouter(prefix="/api/agents/{role_id}/{agent_id}", tags=["verify"])


class SaveVerifiedBody(BaseModel):
    """The name the verified copy is saved under."""

    name: str = Field(min_length=1, max_length=NAME_MAX)


def _verify(role_id: str, agent_id: str) -> dict[str, Any]:
    try:
        return verify_agent(role_id, agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/verify")
def verify(role_id: str, agent_id: str) -> dict[str, Any]:
    """Check every Python version of the agent: syntax, blocked code, and runs on awkward input."""
    result = _verify(role_id, agent_id)
    tracing.step("verify", f"verified {agent_id}: {'passed' if result['ok'] else 'problems found'}", "ok" if result["ok"] else "error",
                 agent=agent_id, problems=result["problem_count"], warnings=result["warning_count"], versions=len(result["checks"]))
    return result


@router.post("/save-verified")
def save_verified(role_id: str, agent_id: str, body: SaveVerifiedBody) -> dict[str, Any]:
    """Verify again (never trusting the client), then copy the agent and its edits into Custom Agents under a new name."""
    name = body.name.strip()
    new_id = slug(name)
    if not new_id:
        raise HTTPException(status_code=400, detail="Give the agent a name with letters or numbers")
    result = _verify(role_id, agent_id)
    if not result["ok"]:
        raise HTTPException(status_code=409, detail=f"Not saved: {result['problem_count']} problem(s) found. Verify the agent and fix them first.")
    destination = custom_agents_dir() / new_id
    if destination.exists():
        raise HTTPException(status_code=409, detail=f"A custom agent named {new_id} already exists. Choose another name.")
    copy_agent(agent_dir(role_id, agent_id), destination, agent_id, new_id, name)
    edits = copy_edits(edits_dir() / role_id / agent_id, edits_dir() / CUSTOM_ROLE_ID / new_id, agent_id, new_id)
    saved = load_spec(CUSTOM_ROLE_ID, new_id)
    tracing.step("agent.save-verified", f"saved a verified copy of {agent_id} as {new_id}", source=agent_id, agent_id=new_id, edits_copied=edits)
    return {"id": saved.agent_id, "name": saved.name, "description": saved.description, "tool": saved.tool, "input_key": saved.input_key,
            "output_key": saved.output_key, "sample": saved.sample, "role_id": CUSTOM_ROLE_ID, "edits_copied": edits}

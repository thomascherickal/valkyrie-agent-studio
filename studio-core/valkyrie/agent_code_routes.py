"""View, edit, save and revert each agent's Python.

The original agent.py is never written. Edits are saved apart, in edits_dir()/<role>/<agent>.py,
and reverting deletes the edit, so the original is always there to go back to.
"""

from __future__ import annotations

import os
from pathlib import Path
import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from valkyrie.agent_generator_routes import custom_agents_dir
from valkyrie.python_runner import validate_python_source

router = APIRouter(prefix="/api/agents", tags=["agent-code"])

CUSTOM_ROLE_ID = "custom-agents"
MAX_CODE_CHARS = 100_000
_ID = re.compile(r"[a-z0-9-]+")
_REPO = Path(__file__).resolve().parents[2]


class CodeBody(BaseModel):
    """The edited source to save."""

    code: str = Field(max_length=MAX_CODE_CHARS)


def edits_dir() -> Path:
    """Where edited code is saved. Set VALKYRIE_EDITS_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_EDITS_DIR") or _REPO / "agent-edits")


def _original(role_id: str, agent_id: str) -> Path:
    """The agent's untouched agent.py. Both ids are checked before any path is built from them."""
    if not (_ID.fullmatch(role_id) and _ID.fullmatch(agent_id)):
        raise HTTPException(status_code=400, detail="Invalid agent id")
    base = custom_agents_dir() if role_id == CUSTOM_ROLE_ID else _REPO / "agents" / role_id
    path = base / agent_id / "agent.py"
    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"No agent {agent_id} in {role_id}")
    return path


def _view(role_id: str, agent_id: str) -> dict[str, object]:
    original = _original(role_id, agent_id).read_text()
    edit = edits_dir() / role_id / f"{agent_id}.py"
    edited = edit.is_file()
    return {
        "role_id": role_id,
        "agent_id": agent_id,
        "original": original,
        "code": edit.read_text() if edited else original,
        "edited": edited,
    }


@router.get("/{role_id}/{agent_id}/code")
def get_agent_code(role_id: str, agent_id: str) -> dict[str, object]:
    """The original code, and the saved edit when there is one."""
    return _view(role_id, agent_id)


@router.put("/{role_id}/{agent_id}/code")
def save_agent_code(role_id: str, agent_id: str, body: CodeBody) -> dict[str, object]:
    """Save an edit. Code that matches the original is not an edit, so any saved edit is dropped."""
    original = _original(role_id, agent_id).read_text()
    try:
        compile(body.code, "agent.py", "exec")
        validate_python_source(body.code)
    except (SyntaxError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    edit = edits_dir() / role_id / f"{agent_id}.py"
    if body.code == original:
        edit.unlink(missing_ok=True)
    else:
        edit.parent.mkdir(parents=True, exist_ok=True)
        edit.write_text(body.code)
    return _view(role_id, agent_id)


@router.delete("/{role_id}/{agent_id}/code")
def revert_agent_code(role_id: str, agent_id: str) -> dict[str, object]:
    """Revert to the original by deleting the saved edit."""
    _original(role_id, agent_id)
    (edits_dir() / role_id / f"{agent_id}.py").unlink(missing_ok=True)
    return _view(role_id, agent_id)

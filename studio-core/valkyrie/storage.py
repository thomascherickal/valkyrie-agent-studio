"""Where the studio keeps what you create: custom agents and edits to agent code. Both are gitignored."""

from __future__ import annotations

import os
from pathlib import Path
import shutil

REPO = Path(__file__).resolve().parents[2]


def custom_agents_dir() -> Path:
    """Where created agents are saved. Set VALKYRIE_CUSTOM_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_CUSTOM_DIR") or REPO / "custom-agents")


def edits_dir() -> Path:
    """Where edits and saved implementations go. Set VALKYRIE_EDITS_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_EDITS_DIR") or REPO / "agent-edits")


def logs_dir() -> Path:
    """Where the trace log is written. Set VALKYRIE_LOG_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_LOG_DIR") or REPO / "logs")


def drop_custom_edits(agent_id: str) -> bool:
    """Delete the saved edits of a custom agent. True when there were any."""
    folder = edits_dir() / "custom-agents" / agent_id
    existed = folder.is_dir()
    shutil.rmtree(folder, ignore_errors=True)
    return existed


def delete_custom_agent(agent_id: str) -> bool:
    """Delete a saved custom agent and its edits. False when there is no such agent."""
    folder = custom_agents_dir() / agent_id
    if not (folder / "agent.ir.yaml").is_file():
        return False
    shutil.rmtree(folder)
    drop_custom_edits(agent_id)
    return True

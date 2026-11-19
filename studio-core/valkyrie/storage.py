"""Where the studio keeps what it ships (the agents/ folder) and what you create (custom agents, edits, logs, .env).

In development both are the repo. In a packaged app the agents/ folder is read-only inside the bundle, and everything
you create goes to a per-user folder instead. Set VALKYRIE_HOME to choose that folder.
"""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[2]
FROZEN = bool(getattr(sys, "frozen", False))
# The folder that holds agents/: the repo, or where PyInstaller unpacks the packaged app.
BUNDLE = Path(getattr(sys, "_MEIPASS", REPO))
APP_FOLDER = "valkyrie-studio"


def user_data_dir() -> Path:
    """The per-user data folder for this operating system."""
    home = Path.home()
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA") or home / "AppData" / "Roaming") / APP_FOLDER
    if sys.platform == "darwin":
        return home / "Library" / "Application Support" / APP_FOLDER
    return Path(os.environ.get("XDG_DATA_HOME") or home / ".local" / "share") / APP_FOLDER


def home_dir() -> Path:
    """Where what you create lives: VALKYRIE_HOME, else the repo (development), else the per-user folder (packaged)."""
    return Path(os.environ["VALKYRIE_HOME"]) if os.environ.get("VALKYRIE_HOME") else user_data_dir() if FROZEN else REPO


def agents_dir() -> Path:
    """The agents/ folder that ships with the studio. Read only."""
    return BUNDLE / "agents"


def custom_agents_dir() -> Path:
    """Where created agents are saved. Set VALKYRIE_CUSTOM_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_CUSTOM_DIR") or home_dir() / "custom-agents")


def edits_dir() -> Path:
    """Where edits and saved implementations go. Set VALKYRIE_EDITS_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_EDITS_DIR") or home_dir() / "agent-edits")


def logs_dir() -> Path:
    """Where the trace log is written. Set VALKYRIE_LOG_DIR to move it."""
    return Path(os.environ.get("VALKYRIE_LOG_DIR") or home_dir() / "logs")


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

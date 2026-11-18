"""Load KEY=VALUE pairs from a .env file into the environment, so saved API keys reach the API.

ponytail: a small parser for the common cases (comments, export, quotes, inline comments).
Swap in python-dotenv if you need multi-line values or variable expansion.
"""

from __future__ import annotations

import os
from pathlib import Path
import re

_KEY = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_REPO = Path(__file__).resolve().parents[2]


def env_file_path() -> Path:
    """The .env file at the repo root. Set VALKYRIE_ENV_FILE to use another file."""
    return Path(os.environ.get("VALKYRIE_ENV_FILE") or _REPO / ".env")


def parse_env(text: str) -> dict[str, str]:
    """Parse .env text. Lines that are not KEY=VALUE are skipped."""
    pairs: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.removeprefix("export ").lstrip().partition("=")
        key, value = key.strip(), value.strip()
        if not sep or not _KEY.fullmatch(key):
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        else:
            value = value.split(" #", 1)[0].rstrip()
        pairs[key] = value
    return pairs


def load_env_file(path: Path | None = None) -> list[str]:
    """Set the file's variables that are not already set. A real environment variable always wins.

    Returns the names that were set, never the values.
    """
    path = path or env_file_path()
    if not path.is_file():
        return []
    loaded: list[str] = []
    for key, value in parse_env(path.read_text(encoding="utf-8")).items():
        if value and key not in os.environ:
            os.environ[key] = value
            loaded.append(key)
    return loaded

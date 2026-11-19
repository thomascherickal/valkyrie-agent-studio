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


_FROM_FILE: set[str] = set()  # names this module set from the file, so a reload may change them


def load_env_file(path: Path | None = None) -> list[str]:
    """Set the file's variables. A variable from your real environment always wins and is never changed.

    Calling it again picks up edits: a changed value replaces the one loaded earlier and a blanked or removed
    one is unset. Returns the names that changed, never the values.
    """
    path = path or env_file_path()
    pairs = parse_env(path.read_text(encoding="utf-8")) if path.is_file() else {}
    changed: list[str] = []
    for key in sorted(_FROM_FILE - pairs.keys()):  # removed from the file
        _FROM_FILE.discard(key)
        os.environ.pop(key, None)
        changed.append(key)
    for key, value in pairs.items():
        if key in os.environ and key not in _FROM_FILE:
            continue
        if value and os.environ.get(key) != value:
            os.environ[key] = value
            _FROM_FILE.add(key)
            changed.append(key)
        elif not value and key in _FROM_FILE:
            _FROM_FILE.discard(key)
            os.environ.pop(key, None)
            changed.append(key)
    return changed

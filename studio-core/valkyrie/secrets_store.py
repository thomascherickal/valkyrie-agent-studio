"""Saving keys and choices to the .env file, and showing a key without revealing it.

A key is shown as its first 10 characters followed by asterisks. A short key shows fewer characters, so that at
least its last 4 are never visible.
"""

from __future__ import annotations

import os
from pathlib import Path

from valkyrie.env_file import env_file_path, load_env_file

SHOWN = 10
MAX_STARS = 20
MAX_VALUE = 512
KEY_VARS = {"gemini": "GEMINI_API_KEY", "openrouter": "OPENROUTER_API_KEY", "opencode": "OPENCODE_API_KEY"}
ALLOWED = {
    *KEY_VARS.values(),
    "VALKYRIE_MODEL_PROVIDER", "VALKYRIE_GEMINI_EFFORT",
    "VALKYRIE_GEMINI_MODEL", "VALKYRIE_OPENROUTER_MODEL", "VALKYRIE_OPENCODE_MODEL",
}


def mask(key: str) -> str:
    """The first 10 characters of a key, then asterisks. Empty for no key."""
    shown = key[: min(SHOWN, max(len(key) - 4, 0))]
    return shown + "*" * min(len(key) - len(shown), MAX_STARS)


def key_preview(provider: str) -> str:
    return mask(os.environ.get(KEY_VARS[provider], ""))


def set_env_value(name: str, value: str, path: Path | None = None) -> None:
    """Set one variable in the .env file (adding it if needed), keep every other line, then load the file.

    Only the keys and choices the Secrets tab manages are allowed. A value cannot contain whitespace. An empty
    value clears the setting.
    """
    if name not in ALLOWED:
        raise ValueError(f"{name} cannot be changed here")
    if any(ch.isspace() for ch in value) or len(value) > MAX_VALUE:
        raise ValueError("A value cannot contain spaces or line breaks, or be longer than 512 characters")
    path = path or env_file_path()
    lines = path.read_text(encoding="utf-8").splitlines() if path.is_file() else []
    out: list[str] = []
    done = False
    for line in lines:
        key, sep, _ = line.removeprefix("export ").lstrip().partition("=")
        if sep and key.strip() == name:
            if not done:
                out.append(f"{name}={value}")
                done = True
            continue  # a repeated line for the same name is dropped
        out.append(line)
    if not done:
        out.append(f"{name}={value}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    try:
        path.chmod(0o600)  # keys: readable by you only
    except OSError:
        pass
    load_env_file(path)

"""Shared fixtures: keep a real GEMINI_API_KEY from leaking into tests and triggering live calls."""

from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def _custom_agents_in_tmp(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Created agents are saved to disk, so tests must never write into the repo."""
    monkeypatch.setenv("VALKYRIE_CUSTOM_DIR", str(tmp_path / "custom-agents"))
    monkeypatch.setenv("VALKYRIE_EDITS_DIR", str(tmp_path / "agent-edits"))


@pytest.fixture(autouse=True)
def _no_ambient_gemini_key(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("GEMINI_API_KEY", "OPENROUTER_API_KEY", "OPENCODE_API_KEY"):
        monkeypatch.delenv(name, raising=False)

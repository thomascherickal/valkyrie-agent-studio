"""Shared fixtures: keep a real GEMINI_API_KEY from leaking into tests and triggering live calls."""

import pytest


@pytest.fixture(autouse=True)
def _no_ambient_gemini_key(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("GEMINI_API_KEY", "OPENROUTER_API_KEY", "OPENCODE_API_KEY"):
        monkeypatch.delenv(name, raising=False)

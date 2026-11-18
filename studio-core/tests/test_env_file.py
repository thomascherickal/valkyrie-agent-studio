"""Tests for loading a .env file into the environment."""

import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from valkyrie.api_server import app
from valkyrie.env_file import env_file_path, load_env_file, parse_env
from valkyrie.llm_router import LLMRouter


@pytest.fixture(autouse=True)
def _isolated_environ(monkeypatch: pytest.MonkeyPatch) -> None:
    """Loading writes to os.environ, so work on a copy that is restored after each test."""
    monkeypatch.setattr(os, "environ", os.environ.copy())


def test_parse_handles_comments_export_quotes_and_inline_comments() -> None:
    text = """
# a comment
GEMINI_API_KEY=abc123
export OPENROUTER_API_KEY = "or key with spaces"
OPENCODE_API_KEY='single'
URL=https://x.test/path?a=1&b=2
WITH_COMMENT=value # not part of it
QUOTED_HASH="keep # this"
EMPTY=
NOT_A_PAIR
1BAD=nope
BAD KEY=nope
"""
    assert parse_env(text) == {
        "GEMINI_API_KEY": "abc123",
        "OPENROUTER_API_KEY": "or key with spaces",
        "OPENCODE_API_KEY": "single",
        "URL": "https://x.test/path?a=1&b=2",
        "WITH_COMMENT": "value",
        "QUOTED_HASH": "keep # this",
        "EMPTY": "",
    }


def test_load_sets_missing_values_and_never_overrides_the_real_environment(tmp_path: Path) -> None:
    env = tmp_path / ".env"
    env.write_text("NEW_ONE=from-file\nALREADY_SET=from-file\nBLANK=\n")
    os.environ["ALREADY_SET"] = "from-shell"
    assert load_env_file(env) == ["NEW_ONE"]  # names only, never values
    assert os.environ["NEW_ONE"] == "from-file"
    assert os.environ["ALREADY_SET"] == "from-shell"
    assert "BLANK" not in os.environ


def test_a_missing_file_is_fine(tmp_path: Path) -> None:
    assert load_env_file(tmp_path / "nope.env") == []


def test_default_path_is_the_repo_root(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VALKYRIE_ENV_FILE")
    assert env_file_path().name == ".env"
    assert (env_file_path().parent / "studio-core").is_dir()


def test_the_api_loads_the_file_at_startup_so_keys_reach_the_router(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    env = tmp_path / "keys.env"
    env.write_text("GEMINI_API_KEY=from-the-file\n")
    monkeypatch.setenv("VALKYRIE_ENV_FILE", str(env))
    assert LLMRouter().api_key is None
    with TestClient(app) as started:  # entering the context runs startup
        assert started.get("/health").status_code == 200
        assert LLMRouter().api_key == "from-the-file"

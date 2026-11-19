"""Tests for saving keys to .env, masking them, and the saved selections."""

import os
from pathlib import Path
import stat

import pytest

from valkyrie import selection
from valkyrie.fallback import candidates
from valkyrie.ir_schema import ModelConfig
from valkyrie.secrets_store import MAX_VALUE, key_preview, mask, set_env_value


def test_a_key_shows_its_first_ten_characters_and_then_asterisks() -> None:
    assert mask("") == ""
    assert mask("AQ.Ab8RN6JABCDEFGHIJKLMNOPQRSTUVWXYZ123456") == "AQ.Ab8RN6J" + "*" * 20
    assert mask("sk-or-v1-abcdef") == "sk-or-v1-a" + "*" * 5
    assert mask("abcdefgh") == "abcd" + "*" * 4  # a short key never shows its last 4 characters
    assert mask("abc") == "***"
    assert set(mask("x" * 100)[10:]) == {"*"} and len(mask("x" * 100)) == 30  # the length is not given away


def test_the_preview_comes_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    assert key_preview("gemini") == ""
    monkeypatch.setenv("GEMINI_API_KEY", "AIzaSy-0123456789-secret")
    assert key_preview("gemini").startswith("AIzaSy-012") and "secret" not in key_preview("gemini")


def test_saving_adds_or_replaces_one_line_and_keeps_everything_else(tmp_path: Path) -> None:
    env = tmp_path / ".env"
    env.write_text("# my notes\nOTHER=1\nexport GEMINI_API_KEY=old\nGEMINI_API_KEY=duplicate\n\nVALKYRIE_MODEL_PROVIDER=ollama\n")
    set_env_value("GEMINI_API_KEY", "newkey123", env)
    set_env_value("OPENCODE_API_KEY", "oc_abc", env)
    assert env.read_text() == "# my notes\nOTHER=1\nGEMINI_API_KEY=newkey123\n\nVALKYRIE_MODEL_PROVIDER=ollama\nOPENCODE_API_KEY=oc_abc\n"
    assert os.environ["GEMINI_API_KEY"] == "newkey123" and os.environ["OPENCODE_API_KEY"] == "oc_abc"  # loaded at once
    set_env_value("GEMINI_API_KEY", "", env)  # an empty value removes the key from use
    assert "GEMINI_API_KEY" not in os.environ and "GEMINI_API_KEY=\n" in env.read_text()


def test_the_file_is_created_with_owner_only_access(tmp_path: Path) -> None:
    env = tmp_path / "new" / "folder" / ".env"
    set_env_value("VALKYRIE_GEMINI_MODEL", "gemini-4-hydrogen", env)
    assert env.read_text() == "VALKYRIE_GEMINI_MODEL=gemini-4-hydrogen\n"
    assert stat.S_IMODE(env.stat().st_mode) == 0o600


def test_a_file_that_cannot_change_mode_is_still_written(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(Path, "chmod", lambda self, mode: (_ for _ in ()).throw(OSError("not supported")))
    env = tmp_path / ".env"
    set_env_value("VALKYRIE_MODEL_PROVIDER", "gemini", env)
    assert env.read_text() == "VALKYRIE_MODEL_PROVIDER=gemini\n"


def test_only_known_names_and_safe_values_are_accepted(tmp_path: Path) -> None:
    env = tmp_path / ".env"
    with pytest.raises(ValueError, match="cannot be changed here"):
        set_env_value("PATH", "/evil", env)
    for bad in ("two words", "line\nbreak", "tab\tbed", "x" * (MAX_VALUE + 1)):
        with pytest.raises(ValueError, match="cannot contain spaces"):
            set_env_value("GEMINI_API_KEY", bad, env)
    assert not env.exists()  # nothing was written


def test_the_default_path_is_the_env_file_setting(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VALKYRIE_ENV_FILE", str(tmp_path / "chosen.env"))
    set_env_value("VALKYRIE_MODEL_PROVIDER", "openrouter")
    assert (tmp_path / "chosen.env").read_text() == "VALKYRIE_MODEL_PROVIDER=openrouter\n"


def test_selection_defaults_and_choices(monkeypatch: pytest.MonkeyPatch) -> None:
    assert selection.selected_model("gemini") == "gemini-4-hydrogen" and selection.selected_model("opencode") == "big-pickle"
    assert selection.selected_effort() == "low" and selection.selected_effort("high") == "high" and selection.default_provider() == "gemini"
    monkeypatch.setenv("VALKYRIE_OPENCODE_MODEL", "mimo-v2.6-flash-free")
    monkeypatch.setenv("VALKYRIE_GEMINI_EFFORT", "medium")
    monkeypatch.setenv("VALKYRIE_MODEL_PROVIDER", "openrouter")
    assert selection.selected_model("opencode") == "mimo-v2.6-flash-free" and selection.chosen_model("gemini") is None
    assert selection.selected_effort("high") == "medium" and selection.default_provider() == "openrouter"
    monkeypatch.setenv("VALKYRIE_GEMINI_EFFORT", "extreme")  # not a valid level: the default is used
    assert selection.selected_effort("high") == "high"


def test_the_fallback_chain_uses_the_chosen_models_and_effort_first(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VALKYRIE_GEMINI_MODEL", "gemini-4-neon")
    monkeypatch.setenv("VALKYRIE_GEMINI_EFFORT", "high")
    monkeypatch.setenv("VALKYRIE_OPENCODE_MODEL", "my-opencode-pick")
    monkeypatch.setenv("VALKYRIE_OPENROUTER_MODEL", "big-pickle")  # also a free opencode name: must not repeat inside openrouter's own list
    found = [(c.provider, c.model, c.thinking_level) for c in candidates(ModelConfig())]
    assert found[0] == ("gemini", "gemini-4-hydrogen", "low") and found[1] == ("gemini", "gemini-4-neon", "high")
    assert found[2][:2] == ("opencode", "my-opencode-pick") and found[3][:2] == ("opencode", "big-pickle")
    assert [m for p, m, _ in found if p == "openrouter"] == ["big-pickle", "openrouter/free", "google/gemma-4-31b-it:free"]

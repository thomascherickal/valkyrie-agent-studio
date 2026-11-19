"""Tests for the packaged-app paths and the API entry point."""

from pathlib import Path
import runpy
import sys

import pytest

from valkyrie import serve, storage


def test_in_development_everything_lives_in_the_repo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VALKYRIE_HOME", raising=False)
    for name in ("VALKYRIE_CUSTOM_DIR", "VALKYRIE_EDITS_DIR", "VALKYRIE_LOG_DIR", "VALKYRIE_ENV_FILE"):
        monkeypatch.delenv(name)
    assert storage.home_dir() == storage.REPO and storage.agents_dir() == storage.REPO / "agents"
    assert storage.custom_agents_dir() == storage.REPO / "custom-agents" and storage.logs_dir() == storage.REPO / "logs"
    assert storage.edits_dir() == storage.REPO / "agent-edits"


def test_a_packaged_app_reads_agents_from_the_bundle_and_writes_to_a_user_folder(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv("VALKYRIE_HOME", raising=False)
    monkeypatch.delenv("VALKYRIE_LOG_DIR")
    monkeypatch.setattr(storage, "FROZEN", True)
    monkeypatch.setattr(storage, "BUNDLE", tmp_path / "bundle")
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "data"))
    monkeypatch.setattr(sys, "platform", "linux")
    assert storage.agents_dir() == tmp_path / "bundle" / "agents"
    assert storage.home_dir() == tmp_path / "data" / "valkyrie-studio"
    assert storage.logs_dir() == tmp_path / "data" / "valkyrie-studio" / "logs"
    monkeypatch.setenv("VALKYRIE_HOME", str(tmp_path / "mine"))  # you can always choose the folder
    assert storage.home_dir() == tmp_path / "mine"


def test_the_user_folder_follows_each_operating_system(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    monkeypatch.delenv("XDG_DATA_HOME", raising=False)
    monkeypatch.delenv("APPDATA", raising=False)
    expected = {
        "linux": tmp_path / ".local" / "share" / "valkyrie-studio",
        "darwin": tmp_path / "Library" / "Application Support" / "valkyrie-studio",
        "win32": tmp_path / "AppData" / "Roaming" / "valkyrie-studio",
    }
    for platform, folder in expected.items():
        monkeypatch.setattr(sys, "platform", platform)
        assert storage.user_data_dir() == folder, platform
    monkeypatch.setenv("APPDATA", str(tmp_path / "roaming"))
    assert storage.user_data_dir() == tmp_path / "roaming" / "valkyrie-studio"


def test_the_env_file_lives_in_the_home_folder(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from valkyrie.env_file import env_file_path

    monkeypatch.delenv("VALKYRIE_ENV_FILE")
    monkeypatch.setenv("VALKYRIE_HOME", str(tmp_path))
    assert env_file_path() == tmp_path / ".env"


def test_serve_runs_the_app_on_localhost_and_the_port_can_be_chosen(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[object, dict[str, object]]] = []
    monkeypatch.setattr("uvicorn.run", lambda app, **kw: calls.append((app, kw)))
    serve.main()
    monkeypatch.setenv("VALKYRIE_PORT", "9123")
    serve.main()
    assert calls[0][0] is serve.app and calls[0][1] == {"host": "127.0.0.1", "port": 8000, "log_level": "info"}
    assert calls[1][1]["port"] == 9123
    runpy.run_module("valkyrie.serve", run_name="__main__")  # the `python -m` entry
    assert len(calls) == 3

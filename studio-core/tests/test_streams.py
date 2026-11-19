"""Tests for the live trace stream and the provider key status."""

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from valkyrie import command_centre_routes
from valkyrie.api_server import app

client = TestClient(app)


def test_the_trace_stream_sends_the_current_traces_then_every_change(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(command_centre_routes, "STREAM_CHECK_S", 0.02)
    client.post("/api/command-centre/start/stream-a")
    with client.websocket_connect("/ws/traces") as ws:
        first = ws.receive_json()["traces"]
        assert {"agent_id": "stream-a", "state": "running", "steps": ["initialized", "running"]} in first
        client.post("/api/command-centre/stop/stream-a")  # a change arrives without asking again
        second = ws.receive_json()["traces"]
        assert next(t for t in second if t["agent_id"] == "stream-a")["state"] == "stopped"
    # leaving the stream open and idle for a few checks sends nothing more, and closing it ends the server loop
    with client.websocket_connect("/ws/traces") as ws:
        ws.receive_json()
        ws.send_text("still here")


def test_providers_report_which_keys_are_set_without_revealing_them(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    body = client.get("/api/providers").json()
    assert body["env_file"] == "no-such.env"
    assert [(p["id"], p["env_var"], p["key_set"]) for p in body["providers"]] == [
        ("gemini", "GEMINI_API_KEY", False), ("openrouter", "OPENROUTER_API_KEY", False), ("opencode", "OPENCODE_API_KEY", False),
    ]
    env = tmp_path / "keys.env"
    env.write_text("OPENCODE_API_KEY=secret-value\n")
    monkeypatch.setenv("VALKYRIE_ENV_FILE", str(env))
    res = client.post("/api/providers/reload")
    assert res.json()["changed"] == ["OPENCODE_API_KEY"] and "secret-value" not in res.text
    assert [p["key_set"] for p in res.json()["providers"]] == [False, False, True]
    env.write_text("")
    client.post("/api/providers/reload")  # the key leaves with the file
    assert client.get("/api/providers").json()["providers"][2]["key_set"] is False

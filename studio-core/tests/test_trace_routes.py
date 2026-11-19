"""Tests for the trace API: listing, clearing and the live stream."""

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from valkyrie import trace_routes
from valkyrie.api_server import app
from valkyrie.tracing import STORE, Tracer

client = TestClient(app)


@pytest.fixture(autouse=True)
def _empty_store() -> None:
    STORE.clear()


def test_list_returns_new_events_and_where_to_continue_from(tmp_path: Path) -> None:
    empty = client.get("/api/trace/events").json()
    assert empty["events"] == [] and empty["last_id"] == 0 and empty["log_file"] == str(tmp_path / "logs" / "trace.jsonl")
    a = Tracer("one", run="r1").step("s1", "first")
    Tracer("two", run="r2").step("s2", "second")
    everything = client.get("/api/trace/events").json()
    assert [e["stage"] for e in everything["events"]] == ["s1", "s2"] and everything["last_id"] == a["id"] + 1
    assert [e["stage"] for e in client.get(f"/api/trace/events?after={a['id']}").json()["events"]] == ["s2"]
    assert [e["stage"] for e in client.get("/api/trace/events?run=r1").json()["events"]] == ["s1"]
    assert client.get(f"/api/trace/events?after={a['id'] + 1}").json()["last_id"] == a["id"] + 1  # nothing new: same place


def test_clear_empties_the_pane_but_not_the_log_file(tmp_path: Path) -> None:
    Tracer("x").step("s", "kept on disk")
    assert client.delete("/api/trace/events").json() == {"cleared": 1}
    assert client.get("/api/trace/events").json()["events"] == []
    assert "kept on disk" in (tmp_path / "logs" / "trace.jsonl").read_text()


def test_the_stream_sends_what_exists_then_every_new_event(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(trace_routes, "STREAM_CHECK_S", 0.02)
    Tracer("a", run="r").step("early", "already there")
    with client.websocket_connect("/ws/trace") as ws:
        assert [e["stage"] for e in ws.receive_json()["events"]] == ["early"]
        client.post("/api/command-centre/start/stream-agent")  # an action elsewhere shows up without asking
        got = ws.receive_json()["events"]
        assert got[-1]["stage"] == "command-centre.start" and got[-1]["detail"]["agent_id"] == "stream-agent"
        ws.send_text("still here")
    with client.websocket_connect(f"/ws/trace?after={got[-1]['id']}") as ws:  # resume after the last seen id
        Tracer("a", run="r").step("late", "after resume")
        assert [e["stage"] for e in ws.receive_json()["events"]] == ["late"]

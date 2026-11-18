"""Tests for Command Centre REST routes."""

from fastapi.testclient import TestClient

from valkyrie.api_server import app

client = TestClient(app)


def test_command_centre_routes() -> None:
    s1 = client.post("/api/command-centre/start/01-prd-architect")
    assert s1.status_code == 200
    assert s1.json()["state"] == "running"

    s2 = client.post("/api/command-centre/start/02-pr-code-reviewer")
    assert s2.status_code == 200

    traces = client.get("/api/command-centre/traces")
    assert traces.status_code == 200
    assert len(traces.json()["traces"]) >= 2

    stop1 = client.post("/api/command-centre/stop/01-prd-architect")
    assert stop1.status_code == 200
    assert stop1.json()["state"] == "stopped"

    stop_all = client.post("/api/command-centre/admin/stop-all")
    assert stop_all.status_code == 200
    assert stop_all.json()["stopped"] >= 1


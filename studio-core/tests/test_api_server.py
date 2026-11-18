"""Tests for FastAPI Studio server."""

from fastapi.testclient import TestClient

from valkyrie.api_server import app
from valkyrie.ir_schema import AgentIR, dump_ir_to_yaml

client = TestClient(app)


def test_health_endpoint() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["default_model"] == "gemini-4-hydrogen"
    assert resp.json()["thinking_level"] == "low"


def test_run_agent_llm_and_python_modes() -> None:
    ir = AgentIR(
        id="api-test",
        name="API Test",
        role="Engineering",
        description="Test",
        system_prompt="Help",
        output_schema={"answer": "string"},
    )
    resp = client.post(
        "/api/agents/run",
        json={"ir_yaml": dump_ir_to_yaml(ir), "prompt": "hi"},
    )
    assert resp.status_code == 200
    assert resp.json()["mode"] == "llm"
    assert resp.json()["eval_passed"] is True

    ir_py = ir.model_copy(update={"custom_python_enabled": True})
    resp_py = client.post(
        "/api/agents/run",
        json={
            "ir_yaml": dump_ir_to_yaml(ir_py),
            "prompt": "hi",
            "custom_python": "def run_agent(p): return {'ok': True}",
            "payload": {},
        },
    )
    assert resp_py.status_code == 200
    assert resp_py.json()["mode"] == "python"

    resp_bad_py = client.post(
        "/api/agents/run",
        json={
            "ir_yaml": dump_ir_to_yaml(ir_py),
            "prompt": "hi",
            "custom_python": "import os\ndef run_agent(p): return {}",
            "payload": {},
        },
    )
    assert resp_bad_py.status_code == 400


def test_run_and_deploy_invalid_yaml() -> None:
    assert client.post("/api/agents/run", json={"ir_yaml": "- bad", "prompt": "x"}).status_code == 400
    assert client.post("/api/agents/deploy-rust", json={"ir_yaml": "- bad"}).status_code == 400


def test_deploy_rust_endpoint() -> None:
    ir = AgentIR(
        id="deploy-test",
        name="Deploy Test",
        role="DevOps",
        description="Test",
        system_prompt="Deploy",
    )
    resp = client.post("/api/agents/deploy-rust", json={"ir_yaml": dump_ir_to_yaml(ir)})
    assert resp.status_code == 200
    assert resp.json()["crate_name"] == "valkyrie_deploy_test"


def test_catalog_and_websocket_traces() -> None:
    resp = client.get("/api/agents")
    assert resp.status_code == 200
    roles = resp.json()["roles"]
    assert len(roles) == 12
    assert sum(len(r["agents"]) for r in roles) == 120

    with client.websocket_connect("/ws/traces") as ws:
        data = ws.receive_json()
        assert data["agent_id"] == "01-prd-architect"
        assert data["state"] == "running"


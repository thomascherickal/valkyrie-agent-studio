"""Tests for /api/agents/create-from-prompt route."""

from fastapi.testclient import TestClient

from valkyrie.api_server import app

client = TestClient(app)


def test_create_agent_from_prompt_endpoint() -> None:
    ok = client.post(
        "/api/agents/create-from-prompt",
        json={"prompt": "Audit Terraform plans for wildcard IAM roles", "role": "Security"},
    )
    assert ok.status_code == 200
    data = ok.json()
    assert data["agent_id"] == "audit-terraform-plans-for"
    assert "agent_id" in data["agent_py"]
    assert "id:" in data["ir_yaml"]
    assert "tokio" in data["cargo_toml"]

    bad = client.post("/api/agents/create-from-prompt", json={"prompt": "  "})
    assert bad.status_code == 400

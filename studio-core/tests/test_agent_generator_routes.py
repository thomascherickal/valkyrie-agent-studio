"""Tests for /api/agents/create-from-prompt route."""

import pytest
from fastapi.testclient import TestClient

from valkyrie.agent_generator_routes import custom_agents_dir
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


def test_created_agents_are_saved_and_listed() -> None:
    assert client.get("/api/agents/custom").json() == {"agents": []}  # nothing saved yet, no directory

    client.post("/api/agents/create-from-prompt", json={"prompt": "Summarize billing spikes", "name": "Billing Watch"})
    client.post("/api/agents/create-from-prompt", json={"prompt": "Audit IAM roles"})
    client.post("/api/agents/create-from-prompt", json={"prompt": "Audit IAM roles"})  # same id: overwritten, not duplicated

    agents = client.get("/api/agents/custom").json()["agents"]
    assert [a["id"] for a in agents] == ["audit-iam-roles", "billing-watch"]
    assert agents[1] == {
        "id": "billing-watch",
        "name": "Billing Watch",
        "description": "Summarize billing spikes",
        "tool": "run_billing_watch",
    }
    saved = custom_agents_dir() / "billing-watch"
    assert (saved / "agent.py").is_file() and (saved / "rust" / "src" / "main.rs").is_file()


def test_custom_agents_dir_defaults_to_the_repo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VALKYRIE_CUSTOM_DIR")
    assert custom_agents_dir().name == "custom-agents"
    assert (custom_agents_dir().parent / "studio-core").is_dir()  # the repo root

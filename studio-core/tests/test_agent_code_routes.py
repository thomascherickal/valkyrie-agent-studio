"""Tests for viewing, editing, saving and reverting each agent's Python."""

import hashlib
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from valkyrie.agent_code_routes import edits_dir
from valkyrie.agent_generator_routes import custom_agents_dir
from valkyrie.api_server import app

client = TestClient(app)
ROLE, AGENT = "01-product-management", "01-prd-architect"
URL = f"/api/agents/{ROLE}/{AGENT}/code"
ORIGINAL_FILE = Path(__file__).resolve().parents[2] / "agents" / ROLE / AGENT / "agent.py"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_view_save_and_revert_a_catalog_agent_without_touching_the_original() -> None:
    before = digest(ORIGINAL_FILE)
    first = client.get(URL).json()
    assert first["original"] == first["code"] == ORIGINAL_FILE.read_text()
    assert first["edited"] is False and first["agent_id"] == AGENT

    new_code = first["original"].replace('"confidence": 0.96', '"confidence": 0.5')
    saved = client.put(URL, json={"code": new_code}).json()
    assert saved["edited"] is True and saved["code"] == new_code and saved["original"] == first["original"]
    assert (edits_dir() / ROLE / f"{AGENT}.py").read_text() == new_code
    assert client.get(URL).json()["code"] == new_code  # still there on the next view

    reverted = client.delete(URL).json()
    assert reverted["edited"] is False and reverted["code"] == first["original"]
    assert not (edits_dir() / ROLE / f"{AGENT}.py").exists()
    assert digest(ORIGINAL_FILE) == before  # the original was never written
    assert client.delete(URL).json()["edited"] is False  # reverting again is harmless


def test_saving_the_original_text_is_not_an_edit() -> None:
    original = client.get(URL).json()["original"]
    client.put(URL, json={"code": original + "\n# tweak"})
    again = client.put(URL, json={"code": original}).json()
    assert again["edited"] is False
    assert not (edits_dir() / ROLE / f"{AGENT}.py").exists()


def test_bad_code_is_rejected_with_the_reason() -> None:
    syntax = client.put(URL, json={"code": "def run_agent(:"})
    assert syntax.status_code == 400 and "line 1" in syntax.json()["detail"]
    forbidden = client.put(URL, json={"code": "import os\n"})
    assert forbidden.status_code == 400 and "Forbidden" in forbidden.json()["detail"]
    assert client.put(URL, json={"code": "x" * 100_001}).status_code == 422
    assert client.get(URL).json()["edited"] is False  # nothing was saved


def test_unknown_and_invalid_ids() -> None:
    assert client.get(f"/api/agents/{ROLE}/no-such-agent/code").status_code == 404
    assert client.get(f"/api/agents/no-such-role/{AGENT}/code").status_code == 404
    for bad in ("/api/agents/Bad_Role/x/code", f"/api/agents/{ROLE}/Bad.Agent/code"):
        assert client.get(bad).status_code == 400
        assert client.put(bad, json={"code": "x = 1"}).status_code == 400
        assert client.delete(bad).status_code == 400


def test_custom_agents_have_the_same_original_and_edit_flow() -> None:
    client.post("/api/agents/create-from-prompt", json={"prompt": "Audit IAM roles"})
    url = "/api/agents/custom-agents/audit-iam-roles/code"
    original_file = custom_agents_dir() / "audit-iam-roles" / "agent.py"
    before = digest(original_file)
    assert client.get(url).json()["original"] == original_file.read_text()
    assert client.put(url, json={"code": "def run_agent(payload):\n    return {}\n"}).json()["edited"] is True
    assert client.delete(url).json()["edited"] is False
    assert digest(original_file) == before


def test_a_custom_agent_cannot_shadow_a_catalog_agent_with_the_same_id() -> None:
    client.post("/api/agents/create-from-prompt", json={"prompt": "01 prd architect"})
    custom = client.get(f"/api/agents/custom-agents/{AGENT}/code").json()
    catalog = client.get(URL).json()
    assert custom["original"] != catalog["original"]
    assert catalog["original"] == ORIGINAL_FILE.read_text()
    client.put(f"/api/agents/custom-agents/{AGENT}/code", json={"code": "x = 1\n"})
    assert client.get(URL).json()["edited"] is False  # the edit landed on the custom agent only


def test_edits_dir_defaults_to_the_repo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VALKYRIE_EDITS_DIR")
    assert edits_dir().name == "agent-edits"
    assert (edits_dir().parent / "studio-core").is_dir()  # the repo root

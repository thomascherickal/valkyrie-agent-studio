"""Tests for viewing, editing, checking, saving and reverting each agent's Python implementations."""

import hashlib
import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from valkyrie.agent_impl_routes import edits_dir
from valkyrie.api_server import app

client = TestClient(app)
ROLE, AGENT = "01-product-management", "01-prd-architect"
BASE = f"/api/agents/{ROLE}/{AGENT}"
AGENT_DIR = Path(__file__).resolve().parents[2] / "agents" / ROLE / AGENT


def tree_hash(folder: Path) -> str:
    digest = hashlib.sha256()
    for f in sorted(p for p in folder.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        digest.update(f.name.encode() + f.read_bytes())
    return digest.hexdigest()


def impl(name: str) -> dict:
    return client.get(f"{BASE}/implementations/{name}").json()


def test_every_agent_lists_its_three_builtin_implementations() -> None:
    items = client.get(f"{BASE}/implementations").json()["implementations"]
    assert [(i["id"], i["kind"], i["edited"]) for i in items] == [
        ("rules", "builtin", False), ("pipeline", "builtin", False), ("hybrid", "builtin", False)]
    rules = impl("rules")
    assert rules["original"] == rules["code"] and rules["label"] == "Rules" and "def run_agent" in rules["code"]
    assert impl("pipeline")["original"] != rules["original"]


def test_edit_and_revert_each_builtin_without_touching_its_original() -> None:
    before = tree_hash(AGENT_DIR)
    for name in ("rules", "pipeline", "hybrid"):
        original = impl(name)["original"]
        mine = original.replace('"confidence"', '"my_confidence"', 1) if name != "hybrid" else original + "\n# mine\n"
        saved = client.put(f"{BASE}/implementations/{name}", json={"code": mine}).json()
        assert saved["edited"] is True and saved["code"] == mine and saved["original"] == original
        assert (edits_dir() / ROLE / AGENT / f"{name}.py").read_text() == mine
        assert impl(name)["code"] == mine  # still there on the next view

        reverted = client.delete(f"{BASE}/implementations/{name}").json()
        assert reverted["edited"] is False and reverted["code"] == original
        assert not (edits_dir() / ROLE / AGENT / f"{name}.py").exists()
        assert client.delete(f"{BASE}/implementations/{name}").json()["edited"] is False  # harmless twice
    assert tree_hash(AGENT_DIR) == before  # nothing under agents/ was written


def test_saving_the_original_text_is_not_an_edit() -> None:
    original = impl("rules")["original"]
    client.put(f"{BASE}/implementations/rules", json={"code": original + "\n# x"})
    assert client.put(f"{BASE}/implementations/rules", json={"code": original}).json()["edited"] is False
    assert not (edits_dir() / ROLE / AGENT / "rules.py").exists()


def test_bad_code_is_rejected_with_the_reason_and_line() -> None:
    syntax = client.put(f"{BASE}/implementations/rules", json={"code": "x = 1\ndef run_agent(:\n"})
    assert syntax.status_code == 400 and "SyntaxError" in syntax.json()["detail"] and "(line 2)" in syntax.json()["detail"]
    forbidden = client.put(f"{BASE}/implementations/rules", json={"code": "import os\n"})
    assert forbidden.status_code == 400 and "Forbidden construct" in forbidden.json()["detail"]
    assert client.put(f"{BASE}/implementations/rules", json={"code": "x" * 100_001}).status_code == 422
    assert client.get(f"{BASE}/implementations").json()["implementations"][0]["edited"] is False  # nothing saved


def test_save_new_implementations_next_to_the_originals() -> None:
    code = "def run_agent(payload):\n    return {'prd_markdown': 'mine', 'implementation': 'mine'}\n"
    created = client.post(f"{BASE}/implementations", json={"name": "My Strict Version", "code": code}).json()
    assert created["impl"] == "saved-my-strict-version" and created["kind"] == "saved" and created["label"] == "My Strict Version"
    assert created["original"] == "" and created["code"] == code

    ids = [i["id"] for i in client.get(f"{BASE}/implementations").json()["implementations"]]
    assert ids == ["rules", "pipeline", "hybrid", "saved-my-strict-version"]  # the three originals are still there
    assert client.post(f"{BASE}/implementations", json={"name": "my strict version!", "code": code}).status_code == 409
    assert client.post(f"{BASE}/implementations", json={"name": "  ", "code": code}).json()["detail"] == "Give the implementation a name"
    assert client.post(f"{BASE}/implementations", json={"name": "Bad", "code": "def (:"}).status_code == 400

    updated = client.put(f"{BASE}/implementations/saved-my-strict-version", json={"code": code + "# v2\n"}).json()
    assert updated["code"].endswith("# v2\n") and updated["edited"] is False
    assert client.delete(f"{BASE}/implementations/saved-my-strict-version").json() == {"deleted": "saved-my-strict-version"}
    assert client.get(f"{BASE}/implementations/saved-my-strict-version").status_code == 404
    assert len(client.get(f"{BASE}/implementations").json()["implementations"]) == 3


def test_unknown_and_invalid_ids() -> None:
    assert client.get(f"/api/agents/{ROLE}/no-such-agent/implementations").status_code == 404
    assert client.get(f"{BASE}/implementations/nope").status_code == 404
    assert client.get(f"{BASE}/implementations/saved-ghost").status_code == 404
    assert client.get(f"{BASE}/implementations/saved-Bad_Slug").status_code == 404
    for bad in ("/api/agents/Bad_Role/x/implementations", f"/api/agents/{ROLE}/Bad.Agent/explanation"):
        assert client.get(bad).status_code == 400


def test_check_reports_load_and_run_errors_with_lines() -> None:
    good = client.post(f"{BASE}/check", json={"code": impl("rules")["code"]}).json()
    assert good["ok"] is True and good["warnings"] == [] and good["output"]["implementation"] == "rules"

    missing_key = client.post(f"{BASE}/check", json={"code": "def run_agent(payload):\n    return {'x': 1}\n"}).json()
    assert missing_key["ok"] is True and missing_key["warnings"] == ['The result has no "prd_markdown" key.']

    runtime = client.post(f"{BASE}/check", json={"code": "def run_agent(payload):\n    return 1 / 0\n"}).json()
    assert runtime == {"ok": False, "error": "ZeroDivisionError: division by zero (line 2)", "line": 2, "warnings": []}
    syntax = client.post(f"{BASE}/check", json={"code": "def run_agent(:"}).json()
    assert syntax["ok"] is False and "SyntaxError" in syntax["error"] and syntax["line"] is None
    assert client.post(f"{BASE}/check", json={"code": "import os"}).json()["error"].startswith("ValueError: Forbidden")


def test_explanation_is_served_for_each_agent() -> None:
    info = client.get(f"{BASE}/explanation").json()
    assert info["title"] == "PRD Architect" and info["words"] >= 100
    assert [s["heading"] for s in info["sections"]][0] == "What this agent does"


def test_each_agent_lists_the_extra_data_it_needs_with_a_worked_example() -> None:
    fields = client.get(f"{BASE}/fields").json()["fields"]
    assert [f["key"] for f in fields] == ["target_users", "success_metric", "constraints", "launch_quarter"]
    assert all(set(f) == {"key", "label", "kind", "example"} and f["example"] for f in fields)
    assert client.get("/api/agents/Bad_Role/x/fields").status_code == 400
    assert client.get(f"/api/agents/{ROLE}/no-such-agent/fields").status_code == 404


def run_body(impl_id: str | None, **extra: object) -> dict:
    ir = {"id": AGENT, "name": "PRD Architect", "role": "Product Management", "description": "d", "system_prompt": "s",
          "output_schema": {"result": "string"}}
    return {"ir_yaml": json.dumps(ir), "prompt": "p", "payload": {"feature_brief": "Goal: faster login"},
            "role_id": ROLE, "agent_id": AGENT, "impl": impl_id, **extra}


def test_run_executes_the_selected_implementation_and_uses_your_saved_edit() -> None:
    for name in ("rules", "pipeline", "hybrid"):
        res = client.post("/api/agents/run", json=run_body(name)).json()
        assert res["mode"] == "python" and res["impl"] == name and res["output"]["implementation"] == name and res["cost_usd"] == 0.0

    mine = impl("rules")["original"].replace('"implementation": "rules"', '"implementation": "rules-edited"')
    client.put(f"{BASE}/implementations/rules", json={"code": mine})
    assert client.post("/api/agents/run", json=run_body("rules")).json()["output"]["implementation"] == "rules-edited"
    client.delete(f"{BASE}/implementations/rules")
    assert client.post("/api/agents/run", json=run_body("rules")).json()["output"]["implementation"] == "rules"


def test_run_reports_errors_in_the_implementation() -> None:
    client.post(f"{BASE}/implementations", json={"name": "Broken", "code": "def run_agent(payload):\n    return payload['nope']\n"})
    bad = client.post("/api/agents/run", json=run_body("saved-broken"))
    assert bad.status_code == 400 and bad.json()["detail"] == "saved-broken: KeyError: 'nope' (line 2)"
    assert client.post("/api/agents/run", json=run_body("saved-ghost")).status_code == 404
    assert client.post("/api/agents/run", json={**run_body("rules"), "agent_id": None}).status_code == 400


def test_agents_you_create_get_the_same_three_implementations_and_explanation() -> None:
    client.post("/api/agents/create-from-prompt", json={"prompt": "Summarize billing spikes risks and next actions", "name": "Billing Watch"})
    base = "/api/agents/custom-agents/billing-watch"
    assert [i["id"] for i in client.get(f"{base}/implementations").json()["implementations"]] == ["rules", "pipeline", "hybrid"]
    res = client.post("/api/agents/run", json={**run_body("pipeline"), "role_id": "custom-agents", "agent_id": "billing-watch",
                                               "payload": {"task_input": "A risk: spend rose 40%. We need to cap it."}}).json()
    assert res["output"]["implementation"] == "pipeline" and "## Input coverage" in res["output"]["result"]
    assert [f["key"] for f in client.get(f"{base}/fields").json()["fields"]] == ["context", "owner", "deadline"]
    assert client.get(f"{base}/explanation").json()["words"] >= 100


def test_edits_dir_defaults_to_the_repo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VALKYRIE_EDITS_DIR")
    assert edits_dir().name == "agent-edits" and (edits_dir().parent / "studio-core").is_dir()

"""Tests for running unsaved code, regenerating and deleting custom agents, and picking up key changes."""

import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from valkyrie.api_server import app
from valkyrie.env_file import load_env_file
from valkyrie.storage import REPO, custom_agents_dir, delete_custom_agent, drop_custom_edits, edits_dir

client = TestClient(app)
CUSTOM = "/api/agents/custom-agents/billing-watch"
CREATE = {"prompt": "Summarize billing spikes", "name": "Billing Watch"}
IR = (REPO / "agents/02-software-engineering/10-rust-port-advisor/agent.ir.yaml").read_text()


def run_body(**extra: object) -> dict:
    return {"ir_yaml": IR, "prompt": "x", **extra}


def make_agent() -> None:
    assert client.post("/api/agents/create-from-prompt", json=CREATE).status_code == 200


def test_run_can_use_the_code_in_the_editor_without_saving_it() -> None:
    make_agent()
    mine = "def run_agent(p):\n    return {'mine': p['task_input'].upper()}\n"
    body = run_body(role_id="custom-agents", agent_id="billing-watch", impl="rules", payload={"task_input": "hi"})
    assert client.post("/api/agents/run", json={**body, "code": mine}).json()["output"] == {"mine": "HI"}
    assert client.post("/api/agents/run", json=body).json()["output"]["implementation"] == "rules"  # the saved one
    assert client.get(f"{CUSTOM}/implementations/rules").json()["edited"] is False  # nothing was saved


def test_regenerating_an_agent_drops_its_old_edits_and_deleting_removes_everything() -> None:
    make_agent()
    code = client.get(f"{CUSTOM}/implementations/rules").json()["code"] + "\n# my edit\n"
    assert client.put(f"{CUSTOM}/implementations/rules", json={"code": code}).json()["edited"] is True
    make_agent()  # same id again
    assert client.get(f"{CUSTOM}/implementations/rules").json()["edited"] is False
    client.put(f"{CUSTOM}/implementations/rules", json={"code": code})
    assert client.delete("/api/agents/custom/billing-watch").json() == {"deleted": "billing-watch"}
    assert not (custom_agents_dir() / "billing-watch").exists()
    assert not (edits_dir() / "custom-agents" / "billing-watch").exists()
    assert client.get("/api/agents/custom").json() == {"agents": []}
    assert client.delete("/api/agents/custom/billing-watch").status_code == 404
    assert client.delete("/api/agents/custom/Bad_Id").status_code == 400


def test_storage_helpers_report_whether_anything_existed() -> None:
    assert delete_custom_agent("nothing") is False and drop_custom_edits("nothing") is False


def test_editing_the_env_file_changes_keys_without_a_restart(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    env = tmp_path / "keys.env"
    monkeypatch.setenv("VALKYRIE_ENV_FILE", str(env))
    monkeypatch.setenv("SHELL_WINS", "shell")
    for name in ("RELOAD_A", "RELOAD_B", "RELOAD_C"):
        monkeypatch.delenv(name, raising=False)
    env.write_text("RELOAD_A=one\nRELOAD_B=two\nSHELL_WINS=file\nRELOAD_C=\n")
    assert load_env_file() == ["RELOAD_A", "RELOAD_B"] and os.environ["SHELL_WINS"] == "shell"
    assert load_env_file() == []  # nothing changed
    env.write_text("RELOAD_A=changed\nRELOAD_C=three\n")  # B removed
    assert client.post("/api/agents/run", json=run_body(payload={})).status_code == 200  # a run reloads the file
    assert os.environ["RELOAD_A"] == "changed" and os.environ["RELOAD_C"] == "three" and "RELOAD_B" not in os.environ
    env.write_text("RELOAD_A=\n")  # blanked: unset, and C removed from the file: unset
    assert sorted(load_env_file()) == ["RELOAD_A", "RELOAD_C"]
    assert "RELOAD_A" not in os.environ and "RELOAD_C" not in os.environ

"""Tests that a run, and every other action, leaves a full step-by-step trace."""

import pytest
from fastapi.testclient import TestClient

from valkyrie import run_routes
from valkyrie.api_server import app
from valkyrie.fallback import AllProvidersFailed
from valkyrie.storage import REPO
from valkyrie.tracing import STORE

client = TestClient(app)
AGENT = REPO / "agents/01-product-management/02-roadmap-prioritizer"
IR = (AGENT / "agent.ir.yaml").read_text()
ROLE, AGENT_ID = "01-product-management", "02-roadmap-prioritizer"


@pytest.fixture(autouse=True)
def _empty_store() -> None:
    STORE.clear()


def run(**extra: object):
    return client.post("/api/agents/run", json={"ir_yaml": IR, "prompt": "hello", **extra})


def stages() -> list[str]:
    return [e["stage"] for e in STORE.since()]


def test_a_model_run_without_keys_traces_every_step() -> None:
    res = run(agent_id=AGENT_ID, payload={"x": "secret-looking value"})
    assert res.status_code == 200 and res.json()["mode"] == "llm"
    assert stages() == ["run.start", "env", "ir", "prompt", "route", "provider.simulated", "eval", "run.done"]
    events = STORE.since()
    assert len({e["run"] for e in events}) == 1 and events[0]["agent"] == AGENT_ID
    assert events[0]["detail"]["payload"] == {"x": "secret-looking value"} and events[0]["detail"]["mode"] == "model"
    assert events[2]["detail"]["model"] == "gemini-4-hydrogen" and events[3]["detail"]["prompt"] == "hello"
    assert events[-1]["detail"]["cost_usd"] >= 0 and events[-1]["ms"] >= events[0]["ms"]


def test_a_bad_definition_is_traced_and_refused() -> None:
    res = client.post("/api/agents/run", json={"ir_yaml": "not: [valid", "prompt": "p"})
    assert res.status_code == 400
    last = STORE.since()[-1]
    assert last["stage"] == "ir.error" and last["status"] == "error" and last["detail"]["http_status"] == 400


def test_when_no_provider_answers_the_run_fails_with_502_and_the_reason(monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(*args: object) -> None:
        raise AllProvidersFailed([{"provider": "gemini", "model": "m", "error": "HTTP 500"}])

    monkeypatch.setattr(run_routes, "invoke_with_fallback", boom)
    res = run()
    assert res.status_code == 502 and "gemini m: HTTP 500" in res.json()["detail"]
    assert stages()[-1] == "run.error" and STORE.since()[-1]["detail"]["http_status"] == 502


def test_an_implementation_run_traces_the_code_the_sandbox_and_the_stages_it_reports() -> None:
    res = run(role_id=ROLE, agent_id=AGENT_ID, impl="pipeline", payload={"feature_brief": "SSO"})
    assert res.status_code == 200
    got = stages()
    assert got[:6] == ["run.start", "env", "ir", "code", "sandbox.start", "sandbox.end"]
    assert got.count("stage") == 6 and "result" in got and got[-1] == "run.done"
    stage_events = [e for e in STORE.since() if e["stage"] == "stage"]
    assert [e["message"] for e in stage_events][:2] == ["stage validate", "stage calculate"]
    assert STORE.since()[3]["detail"]["source"] == "saved"
    assert {e["message"] for e in STORE.since() if e["stage"] == "result"} >= {"completeness", "metrics", "missing"}


def test_unsaved_editor_code_is_traced_as_such() -> None:
    mine = "def run_agent(p):\n    return {'ok': True}\n"
    assert run(role_id=ROLE, agent_id=AGENT_ID, impl="rules", code=mine).json()["output"] == {"ok": True}
    code_step = next(e for e in STORE.since() if e["stage"] == "code")
    assert code_step["detail"]["source"] == "editor" and "unsaved" in code_step["message"]
    sandbox = next(e for e in STORE.since() if e["stage"] == "sandbox.start")
    assert sandbox["detail"]["code_chars"] == len(mine) and sandbox["detail"]["code_lines"] == 3


def test_a_sandbox_error_is_traced_with_its_line() -> None:
    res = run(role_id=ROLE, agent_id=AGENT_ID, impl="rules", code="def run_agent(p):\n    return p['nope']\n")
    assert res.status_code == 400 and "rules: KeyError" in res.json()["detail"]
    failure = next(e for e in STORE.since() if e["stage"] == "sandbox.error")
    assert failure["status"] == "error" and failure["detail"]["line"] == 2
    assert stages()[-1] == "run.error"


def test_running_an_implementation_needs_its_ids() -> None:
    assert run(impl="rules").status_code == 400
    assert STORE.since()[-1]["stage"] == "run.error"


def test_custom_python_runs_are_traced_too() -> None:
    enabled = IR.replace("custom_python_enabled: false", "custom_python_enabled: true")
    ok = client.post("/api/agents/run", json={"ir_yaml": enabled, "prompt": "p", "custom_python": "def run_agent(p):\n    return {'v': 1}\n"})
    assert ok.json()["output"] == {"v": 1} and "sandbox.end" in stages()
    STORE.clear()
    bad = client.post("/api/agents/run", json={"ir_yaml": enabled, "prompt": "p", "custom_python": "def run_agent(p):\n    return 3\n"})
    assert bad.status_code == 400 and "dict" in bad.json()["detail"]
    ignored = client.post("/api/agents/run", json={"ir_yaml": IR, "prompt": "p", "custom_python": "def run_agent(p):\n    return {}\n"})
    assert ignored.json()["mode"] == "llm"  # custom Python is only used when the definition enables it


def test_other_actions_are_traced_as_system_steps() -> None:
    base = f"/api/agents/{ROLE}/{AGENT_ID}"
    code = client.get(f"{base}/implementations/rules").json()["code"]
    client.put(f"{base}/implementations/rules", json={"code": code + "\n# edit\n"})
    client.post(f"{base}/check", json={"code": code})
    client.delete(f"{base}/implementations/rules")
    client.post(f"{base}/implementations", json={"name": "Mine", "code": code})
    client.delete(f"{base}/implementations/saved-mine")
    client.post("/api/agents/create-from-prompt", json={"prompt": "Summarize billing", "name": "Billing Watch"})
    client.delete("/api/agents/custom/billing-watch")
    client.post("/api/providers/reload")
    client.post("/api/command-centre/start/a1")
    client.post("/api/command-centre/stop/a1")
    client.post("/api/command-centre/admin/stop-all")
    assert stages() == ["editor.save", "editor.check", "editor.revert", "editor.delete", "agent.create", "agent.delete",
                        "providers.reload", "command-centre.start", "command-centre.stop", "command-centre.stop-all"]
    assert {e["run"] for e in STORE.since()} == {"system"}
    assert STORE.since()[1]["status"] == "ok"
    bad = client.post(f"{base}/check", json={"code": "def run_agent(p):\n    return p['x']\n"})
    assert bad.json()["ok"] is False and STORE.since()[-1]["status"] == "error"

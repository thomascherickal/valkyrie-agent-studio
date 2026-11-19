"""Tests for the verify and save-verified routes and the agent copy."""

from fastapi.testclient import TestClient

from valkyrie.agent_copy import slug
from valkyrie.api_server import app
from valkyrie.storage import custom_agents_dir, edits_dir
from valkyrie.tracing import STORE

client = TestClient(app)
ROLE, AGENT = "01-product-management", "02-roadmap-prioritizer"
BASE = f"/api/agents/{ROLE}/{AGENT}"


def test_verify_reports_each_version_and_traces_the_outcome() -> None:
    STORE.clear()
    body = client.post(f"{BASE}/verify").json()
    assert body["ok"] is True and [c["impl"] for c in body["checks"]] == ["rules", "pipeline", "hybrid"]
    assert STORE.since()[-1]["stage"] == "verify" and STORE.since()[-1]["status"] == "ok" and STORE.since()[-1]["detail"]["versions"] == 3
    client.put(f"{BASE}/implementations/pipeline", json={"code": "def run_agent(p):\n    return p['nope']\n"})
    failing = client.post(f"{BASE}/verify").json()
    assert failing["ok"] is False and failing["checks"][1]["problems"] and STORE.since()[-1]["status"] == "error"


def test_verify_refuses_bad_ids() -> None:
    assert client.post("/api/agents/Bad_Role/x/verify").status_code == 400
    assert client.post(f"/api/agents/{ROLE}/no-such/verify").status_code == 404


def test_slug_makes_a_safe_id() -> None:
    assert slug("My Verified Agent!") == "my-verified-agent" and slug("  --  ") == "" and slug("../../etc") == "etc"
    assert len(slug("x" * 100)) == 40 and not slug("a" * 39 + "-b").endswith("-")


def test_saving_a_verified_agent_copies_it_and_its_edits_under_the_new_name() -> None:
    saved_code = client.get(f"{BASE}/implementations/rules").json()["code"] + "\n# my tweak\n"
    client.put(f"{BASE}/implementations/rules", json={"code": saved_code})
    client.post(f"{BASE}/implementations", json={"name": "Mine", "code": saved_code})
    res = client.post(f"{BASE}/save-verified", json={"name": "  Roadmap Plus  "})
    assert res.status_code == 200
    body = res.json()
    assert body["id"] == "roadmap-plus" and body["name"] == "Roadmap Plus" and body["role_id"] == "custom-agents" and body["edits_copied"] is True
    assert body["input_key"] == "initiatives" and body["output_key"] and body["tool"] == "compute_rice_score" and body["sample"]
    folder = custom_agents_dir() / "roadmap-plus"
    ir = (folder / "agent.ir.yaml").read_text()
    assert "id: roadmap-plus" in ir and "name: Roadmap Plus" in ir and "Roadmap Prioritizer" not in ir
    assert "02-roadmap-prioritizer" not in (folder / "agent.py").read_text() and '"roadmap-plus"' in (folder / "agent.py").read_text()
    assert "valkyrie_roadmap_plus" in (folder / "rust" / "Cargo.toml").read_text()
    copied = edits_dir() / "custom-agents" / "roadmap-plus"
    assert "# my tweak" in (copied / "rules.py").read_text() and (copied / "saved" / "mine.py").is_file()
    assert (edits_dir() / ROLE / AGENT / "rules.py").is_file()  # the original agent's edits are untouched
    listed = {a["id"]: a for a in client.get("/api/agents/custom").json()["agents"]}
    assert listed["roadmap-plus"]["input_key"] == "initiatives"
    assert client.post("/api/agents/custom-agents/roadmap-plus/verify").json()["ok"] is True  # the copy itself passes


def test_a_copy_without_edits_and_a_copy_of_a_custom_agent_work() -> None:
    first = client.post(f"{BASE}/save-verified", json={"name": "Plain Copy"}).json()
    assert first["edits_copied"] is False and not (edits_dir() / "custom-agents" / "plain-copy").exists()
    again = client.post("/api/agents/custom-agents/plain-copy/save-verified", json={"name": "Second Generation"}).json()
    assert again["id"] == "second-generation" and again["input_key"] == "initiatives"


def test_a_name_that_is_taken_empty_or_symbols_only_is_refused_and_nothing_is_created() -> None:
    client.post(f"{BASE}/save-verified", json={"name": "Taken"})
    taken = client.post(f"{BASE}/save-verified", json={"name": "Taken"})
    assert taken.status_code == 409 and "already exists" in taken.json()["detail"]
    assert client.post(f"{BASE}/save-verified", json={"name": "!!!"}).status_code == 400
    assert client.post(f"{BASE}/save-verified", json={"name": ""}).status_code == 422
    assert [p.name for p in custom_agents_dir().iterdir()] == ["taken"]


def test_an_agent_that_fails_verification_cannot_be_saved() -> None:
    client.put(f"{BASE}/implementations/rules", json={"code": "def run_agent(p):\n    return p['nope']\n"})
    res = client.post(f"{BASE}/save-verified", json={"name": "Broken"})
    assert res.status_code == 409 and "problem(s) found" in res.json()["detail"]
    assert not (custom_agents_dir() / "broken").exists()
    assert client.post("/api/agents/Bad_Role/x/save-verified", json={"name": "A"}).status_code == 400
    assert client.post(f"/api/agents/{ROLE}/no-such/save-verified", json={"name": "A"}).status_code == 404

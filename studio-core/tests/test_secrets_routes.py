"""Tests for the Secrets tab's API."""

from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient

from valkyrie import key_check, model_catalog
from valkyrie.api_server import app
from valkyrie.tracing import STORE

client = TestClient(app)
KEY = "AIzaSy-0123456789-abcdefghijklmnop"


@pytest.fixture(autouse=True)
def _fresh() -> None:
    model_catalog.clear_cache()
    STORE.clear()


def entry(provider: str) -> dict:
    return next(e for e in client.get("/api/secrets").json()["secrets"] if e["id"] == provider)


def test_with_no_keys_the_tab_says_output_is_simulated_and_shows_the_choices() -> None:
    body = client.get("/api/secrets").json()
    assert body["simulated"] is True and body["default_provider"] == "gemini" and body["efforts"] == ["low", "medium", "high"]
    assert body["default_providers"] == ["gemini", "openrouter", "opencode", "ollama"]
    assert [(e["id"], e["label"], e["key_set"], e["preview"], e["model"], e["effort"]) for e in body["secrets"]] == [
        ("gemini", "Gemini", False, "", "gemini-4-hydrogen", "low"),
        ("openrouter", "OpenRouter", False, "", "openrouter/free", None),
        ("opencode", "OpenCode", False, "", "big-pickle", None),
    ]
    assert body["env_path"].endswith("no-such.env") and len(body["fallback"]) == 3


def test_saving_a_key_writes_the_env_file_and_only_ever_returns_a_masked_preview(tmp_path: Path) -> None:
    res = client.put("/api/secrets/gemini", json={"key": f"  {KEY}  "})
    assert res.status_code == 200 and res.json()["key_set"] is True and res.json()["preview"] == "AIzaSy-012" + "*" * 20
    assert KEY not in res.text and KEY not in client.get("/api/secrets").text and KEY not in str(STORE.since())
    assert (tmp_path / "no-such.env").read_text() == f"GEMINI_API_KEY={KEY}\n"  # surrounding spaces were trimmed
    assert client.get("/api/secrets").json()["simulated"] is False
    assert STORE.since()[-1]["stage"] == "secrets.save" and STORE.since()[-1]["detail"]["changed"] == ["key"]
    cleared = client.put("/api/secrets/gemini", json={"key": ""}).json()
    assert cleared["key_set"] is False and cleared["preview"] == "" and client.get("/api/secrets").json()["simulated"] is True


def test_models_and_effort_are_saved_per_provider() -> None:
    assert client.put("/api/secrets/opencode", json={"model": "mimo-v2.6-flash-free"}).json()["model"] == "mimo-v2.6-flash-free"
    saved = client.put("/api/secrets/gemini", json={"model": "gemini-4-neon", "effort": "high"}).json()
    assert saved["model"] == "gemini-4-neon" and saved["effort"] == "high"
    assert entry("gemini")["effort"] == "high" and entry("opencode")["model"] == "mimo-v2.6-flash-free"
    assert client.put("/api/secrets/gemini", json={}).json()["effort"] == "high"  # nothing to change
    assert STORE.since()[-1]["message"] == "saved nothing for gemini"


def test_bad_requests_are_refused() -> None:
    assert client.put("/api/secrets/nobody", json={"key": "x"}).status_code == 404
    assert client.get("/api/secrets/nobody/models").status_code == 404
    assert client.post("/api/secrets/nobody/test", json={}).status_code == 404
    assert client.put("/api/secrets/gemini", json={"effort": "extreme"}).status_code == 400
    assert client.put("/api/secrets/opencode", json={"effort": "low"}).status_code == 400  # effort is Gemini's thinking level
    bad = client.put("/api/secrets/gemini", json={"key": "two words"})
    assert bad.status_code == 400 and "cannot contain spaces" in bad.json()["detail"]
    assert client.put("/api/secrets/gemini", json={"model": "has space"}).status_code == 400


def test_the_default_provider_is_chosen_from_the_list() -> None:
    assert client.put("/api/secrets/default-provider", json={"provider": "openrouter"}).json()["default_provider"] == "openrouter"
    assert client.put("/api/secrets/default-provider", json={"provider": "nobody"}).status_code == 400
    assert client.get("/api/secrets").json()["default_provider"] == "openrouter"


def test_model_lists_come_from_the_catalog_and_gemini_adds_its_effort_levels(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(model_catalog, "TRANSPORT", httpx.MockTransport(lambda r: httpx.Response(200, json={"data": [{"id": "big-pickle"}]})))
    opencode = client.get("/api/secrets/opencode/models").json()
    assert [m["id"] for m in opencode["models"]] == ["big-pickle"] and opencode["efforts"] == [] and opencode["source"] == "live"
    gemini = client.get("/api/secrets/gemini/models").json()
    assert gemini["efforts"] == ["low", "medium", "high"] and gemini["source"] == "built-in"  # no key yet


def test_test_key_uses_the_typed_key_or_the_saved_one(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        key = request.headers["authorization"].removeprefix("Bearer ")
        return httpx.Response(200, json={"choices": [{"message": {"content": "pong"}}]}) if key == "oc_good" else httpx.Response(401, json={"error": "no"})

    monkeypatch.setattr(key_check, "TRANSPORT", httpx.MockTransport(handler))
    assert client.post("/api/secrets/opencode/test", json={"key": "oc_good", "model": "big-pickle"}).json()["ok"] is True
    failed = client.post("/api/secrets/opencode/test", json={"key": "oc_bad"}).json()
    assert failed["ok"] is False and failed["status"] == 401 and failed["model"] == "big-pickle" and failed["causes"]
    client.put("/api/secrets/opencode", json={"key": "oc_good"})
    assert client.post("/api/secrets/opencode/test", json={}).json()["ok"] is True  # the saved key
    assert seen[-1].headers["authorization"] == "Bearer oc_good"


def test_testing_with_no_key_says_so_without_calling_anyone(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(key_check, "TRANSPORT", httpx.MockTransport(lambda r: pytest.fail("no request should be made")))
    body = client.post("/api/secrets/gemini/test", json={"model": "gemini-4-neon"}).json()
    assert body["ok"] is False and body["message"] == "No key to test." and body["model"] == "gemini-4-neon" and body["causes"]
    assert client.post("/api/secrets/gemini/test", json={"key": "   "}).json()["message"] == "No key to test."
    assert client.post("/api/secrets/gemini/test", json={}).json()["model"] == "gemini-4-hydrogen"

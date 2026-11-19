"""Tests for the model lists in the Secrets tab's drop downs."""

import httpx
import pytest

from valkyrie import model_catalog
from valkyrie.model_catalog import catalog
from valkyrie.tracing import STORE

GEMINI = {"models": [
    {"name": "models/gemini-4-hydrogen", "displayName": "Gemini 4 Hydrogen", "supportedGenerationMethods": ["generateContent"]},
    {"name": "models/embed-1", "supportedGenerationMethods": ["embedContent"]},
    {"name": "models/gemini-4-neon", "supportedGenerationMethods": ["generateContent"]},
]}
OPENROUTER = {"data": [
    {"id": "vendor/paid", "name": "Paid", "pricing": {"prompt": "0.001", "completion": "0.002"}},
    {"id": "vendor/free:free", "name": "Free", "pricing": {"prompt": "0", "completion": "0"}},
    {"id": "vendor/no-pricing"},
    {"id": "vendor/odd-pricing", "pricing": {"prompt": "n/a", "completion": "n/a"}},
]}
OPENCODE = {"data": [
    {"id": "gpt-5", "name": "GPT-5", "cost": {"text": {"input": {"price": 1}, "output": {"price": 8}}}},
    {"id": "big-pickle", "name": "Big Pickle", "cost": {"text": {"input": {"price": 0}, "output": {"price": 0}}}},
    {"id": "no-cost-info"},
]}


@pytest.fixture(autouse=True)
def _fresh(monkeypatch: pytest.MonkeyPatch) -> list[httpx.Request]:
    model_catalog.clear_cache()
    STORE.clear()
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        host = request.url.host
        body = GEMINI if "googleapis" in host else OPENROUTER if "openrouter" in host else OPENCODE
        return httpx.Response(200, json=body)

    monkeypatch.setattr(model_catalog, "TRANSPORT", httpx.MockTransport(handler))
    return seen


def test_gemini_lists_only_models_that_can_generate_text_and_sends_the_key_in_a_header(_fresh: list[httpx.Request]) -> None:
    result = catalog("gemini", "the-key")
    assert [m["id"] for m in result["models"]] == ["gemini-4-hydrogen", "gemini-4-neon"] and result["source"] == "live"
    assert result["models"][0]["label"] == "Gemini 4 Hydrogen" and result["models"][1]["label"] == "models/gemini-4-neon"
    assert _fresh[0].headers["x-goog-api-key"] == "the-key" and "the-key" not in str(_fresh[0].url)


def test_openrouter_and_opencode_put_free_models_first() -> None:
    assert [(m["id"], m["free"]) for m in catalog("openrouter")["models"]] == [
        ("vendor/free:free", True), ("vendor/no-pricing", False), ("vendor/odd-pricing", False), ("vendor/paid", False)]
    assert [(m["id"], m["free"]) for m in catalog("opencode")["models"]] == [("big-pickle", True), ("gpt-5", False), ("no-cost-info", False)]


def test_results_are_cached_for_ten_minutes(_fresh: list[httpx.Request], monkeypatch: pytest.MonkeyPatch) -> None:
    clock = [1000.0]
    monkeypatch.setattr(model_catalog.time, "monotonic", lambda: clock[0])
    catalog("opencode")
    clock[0] += model_catalog.TTL_S - 1
    catalog("opencode")
    assert len(_fresh) == 1
    clock[0] += 2  # past the ten minutes
    catalog("opencode")
    assert len(_fresh) == 2


def test_gemini_without_a_key_shows_the_built_in_model_and_says_how_to_get_the_list(_fresh: list[httpx.Request]) -> None:
    result = catalog("gemini")
    assert result["source"] == "built-in" and [m["id"] for m in result["models"]] == ["gemini-4-hydrogen"] and "Add a Gemini key" in result["note"]
    assert _fresh == []  # nothing was requested


def test_when_the_provider_cannot_be_reached_the_built_in_free_models_are_shown(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(model_catalog, "TRANSPORT", httpx.MockTransport(lambda request: httpx.Response(503, text="down")))
    result = catalog("openrouter")
    assert result["source"] == "built-in" and "HTTPStatusError" in result["note"]
    assert [m["id"] for m in result["models"]] == ["google/gemma-4-31b-it:free", "openrouter/free"] and all(m["free"] for m in result["models"])
    assert STORE.since()[-1]["stage"] == "catalog.fallback" and STORE.since()[-1]["status"] == "warn"
    assert catalog("opencode")["source"] == "built-in"  # the same failure for another provider


def test_a_key_in_the_error_text_is_not_kept(monkeypatch: pytest.MonkeyPatch) -> None:
    def leaky(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("could not connect to https://x.test/models?key=SUPERSECRET123")

    monkeypatch.setattr(model_catalog, "TRANSPORT", httpx.MockTransport(leaky))
    catalog("gemini", "SUPERSECRET123")
    assert "SUPERSECRET123" not in str(STORE.since())

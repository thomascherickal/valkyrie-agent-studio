"""Tests for Test Key: one real request, and the causes listed when it fails."""

import json

import httpx
import pytest

from valkyrie import key_check
from valkyrie.key_check import check_key, diagnose
from valkyrie.tracing import STORE

GEMINI_OK = {"candidates": [{"content": {"parts": [{"text": "pong"}]}}]}
CHAT_OK = {"choices": [{"message": {"content": "pong"}}]}


def serve(monkeypatch: pytest.MonkeyPatch, handler) -> list[httpx.Request]:
    seen: list[httpx.Request] = []

    def wrapped(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return handler(request)

    monkeypatch.setattr(key_check, "TRANSPORT", httpx.MockTransport(wrapped))
    return seen


@pytest.fixture(autouse=True)
def _empty() -> None:
    STORE.clear()


def test_a_working_gemini_key_succeeds_with_the_key_in_a_header(monkeypatch: pytest.MonkeyPatch) -> None:
    seen = serve(monkeypatch, lambda r: httpx.Response(200, json=GEMINI_OK))
    result = check_key("gemini", "AIza-secret", "gemini-4-hydrogen")
    assert result["ok"] is True and result["causes"] == [] and result["status"] == 200 and result["message"] == "The key works."
    assert str(seen[0].url).endswith("gemini-4-hydrogen:generateContent") and seen[0].headers["x-goog-api-key"] == "AIza-secret"
    assert json.loads(seen[0].content)["generationConfig"]["maxOutputTokens"] == 512  # room to think and still answer
    assert "AIza-secret" not in json.dumps(result) and "AIza-secret" not in str(STORE.since())
    assert STORE.since()[-1]["stage"] == "secrets.test" and STORE.since()[-1]["status"] == "ok"


def test_working_hosted_keys_use_a_bearer_token_on_the_providers_own_address(monkeypatch: pytest.MonkeyPatch) -> None:
    seen = serve(monkeypatch, lambda r: httpx.Response(200, json=CHAT_OK))
    assert check_key("openrouter", "sk-or-1", "openrouter/free")["ok"] and check_key("opencode", "oc_1", "big-pickle")["ok"]
    assert str(seen[0].url) == "https://openrouter.ai/api/v1/chat/completions" and seen[0].headers["authorization"] == "Bearer sk-or-1"
    assert str(seen[1].url) == "https://opencode.ai/zen/v1/chat/completions" and json.loads(seen[1].content)["model"] == "big-pickle"


@pytest.mark.parametrize("status,expect", [
    (400, "malformed"), (401, "invalid, expired or revoked"), (402, "no credits"), (403, "model access"),
    (404, "does not exist"), (429, "rate limit or quota"),
])
def test_each_failure_status_lists_its_likely_causes(monkeypatch: pytest.MonkeyPatch, status: int, expect: str) -> None:
    serve(monkeypatch, lambda r: httpx.Response(status, json={"error": {"message": "provider says no"}}))
    result = check_key("opencode", "oc_key", "big-pickle")
    assert result["ok"] is False and result["status"] == status and "provider says no" in result["message"]
    assert any(expect in cause for cause in result["causes"]) and STORE.since()[-1]["status"] == "error"


def test_server_errors_and_unexpected_statuses_are_described(monkeypatch: pytest.MonkeyPatch) -> None:
    serve(monkeypatch, lambda r: httpx.Response(503, text="overloaded"))
    assert "outage" in check_key("openrouter", "k", "m")["causes"][0]
    serve(monkeypatch, lambda r: httpx.Response(418, text="teapot"))
    assert "unexpected status (418)" in check_key("openrouter", "k", "m")["causes"][0]


def test_a_timeout_and_an_unreachable_provider_are_told_apart(monkeypatch: pytest.MonkeyPatch) -> None:
    def slow(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("slow")

    serve(monkeypatch, slow)
    timed = check_key("gemini", "k", "m")
    assert timed["status"] is None and timed["message"] == "timed out" and "30 seconds" in timed["causes"][0]

    def down(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("no route to host")

    serve(monkeypatch, down)
    gone = check_key("gemini", "k", "m")
    assert gone["ok"] is False and "cannot be reached" in gone["causes"][0] and gone["message"] == "no answer"


def test_a_success_with_no_text_is_a_failure_with_its_own_cause(monkeypatch: pytest.MonkeyPatch) -> None:
    for body in ({"choices": [{"message": {"content": "  "}}]}, {"choices": []}, {"unexpected": True}, {"choices": [{"message": {"content": 5}}]}):
        serve(monkeypatch, lambda r, body=body: httpx.Response(200, json=body))
        result = check_key("opencode", "k", "m")
        assert result["ok"] is False and "returned no text" in result["causes"][0]
    serve(monkeypatch, lambda r: httpx.Response(200, text="<html>not json</html>"))
    assert check_key("opencode", "k", "m")["ok"] is False


def test_the_key_is_removed_from_messages_the_provider_echoes_back(monkeypatch: pytest.MonkeyPatch) -> None:
    serve(monkeypatch, lambda r: httpx.Response(401, json={"error": {"message": "Incorrect API key provided: oc_SECRETVALUE_123"}}))
    result = check_key("opencode", "oc_SECRETVALUE_123", "big-pickle")
    assert "oc_SECRETVALUE_123" not in json.dumps(result) and "***" in result["message"]
    assert "oc_SECRETVALUE_123" not in str(STORE.since())


def test_diagnose_prefers_the_transport_problem_over_a_status() -> None:
    assert "30 seconds" in diagnose(500, "", True, False, False)[0]
    assert "cannot be reached" in diagnose(None, "", False, True, False)[0]
    assert "no text" in diagnose(200, "", False, False, True)[0]

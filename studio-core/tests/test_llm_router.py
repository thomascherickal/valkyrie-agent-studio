"""Tests for unified LLM Router (Gemini 4 Hydrogen Low & Ollama)."""

import httpx
import pytest

from valkyrie.ir_schema import ModelConfig
from valkyrie.llm_router import LLMRouter, calculate_cost_usd


def test_cost_calculation() -> None:
    assert calculate_cost_usd("ollama", 1_000_000, 1_000_000) == 0.0
    cost = calculate_cost_usd("gemini", 1_000_000, 1_000_000, cached_tokens=500_000)
    # 500k uncached * 1.50/M + 500k cached * 0.075/M + 1M output * 7.50/M
    assert cost == round(0.75 + 0.0375 + 7.50, 8)


def test_router_deterministic_fallback_without_key() -> None:
    router = LLMRouter()
    cfg = ModelConfig()
    res = router.invoke(cfg, "System", "Hello world")
    assert res.provider == "gemini"
    assert res.model == "gemini-4-hydrogen"
    assert res.thinking_level == "low"
    assert "Hello world" in res.content


def test_router_reads_key_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "env-key")
    assert LLMRouter().api_key == "env-key"
    assert LLMRouter(api_key="explicit").api_key == "explicit"  # an explicit key wins

    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        body = {"candidates": [{"content": {"parts": [{"text": "ok"}]}}]}
        return httpx.Response(200, json=body)

    LLMRouter(transport=httpx.MockTransport(handler)).invoke(ModelConfig(), "S", "U")
    assert "gemini-4-hydrogen:generateContent?key=env-key" in seen[0]


def _compat_reply(request: httpx.Request, seen: list[httpx.Request]) -> httpx.Response:
    seen.append(request)
    return httpx.Response(200, json={"choices": [{"message": {"content": "hi"}}]})


@pytest.mark.parametrize(
    ("provider", "env", "url"),
    [
        ("openrouter", "OPENROUTER_API_KEY", "https://openrouter.ai/api/v1/chat/completions"),
        ("opencode", "OPENCODE_API_KEY", "https://opencode.ai/zen/v1/chat/completions"),
    ],
)
def test_hosted_providers(monkeypatch: pytest.MonkeyPatch, provider: str, env: str, url: str) -> None:
    cfg = ModelConfig(provider=provider, model="acme/free-model")
    sim = LLMRouter().invoke(cfg, "S", "U")  # no key: deterministic simulation, never a network call
    assert (sim.provider, sim.model, sim.cost_usd) == (provider, "acme/free-model", 0.0)

    monkeypatch.setenv(env, "k")
    seen: list[httpx.Request] = []
    res = LLMRouter(transport=httpx.MockTransport(lambda r: _compat_reply(r, seen))).invoke(cfg, "S", "U")
    assert str(seen[0].url) == url
    assert seen[0].headers["authorization"] == "Bearer k"
    assert b'"model":"acme/free-model"' in seen[0].content.replace(b" ", b"")
    assert (res.provider, res.model, res.content, res.cost_usd) == (provider, "acme/free-model", "hi", 0.0)


def test_ollama_never_receives_the_gemini_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "secret")
    seen: list[httpx.Request] = []
    router = LLMRouter(transport=httpx.MockTransport(lambda r: _compat_reply(r, seen)))
    router.invoke(ModelConfig(provider="ollama"), "S", "U")
    assert "authorization" not in seen[0].headers


def test_hosted_provider_requires_a_model() -> None:
    with pytest.raises(ValueError, match="Set a model ID for provider openrouter"):
        ModelConfig(provider="openrouter")
    with pytest.raises(ValueError, match="Set a model ID for provider opencode"):
        ModelConfig(provider="opencode", model="")


def test_router_mock_http_gemini_and_ollama() -> None:
    def gemini_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "candidates": [{"content": {"parts": [{"text": "Gemini OK"}]}}],
                "usageMetadata": {
                    "promptTokenCount": 100,
                    "candidatesTokenCount": 50,
                    "cachedContentTokenCount": 20,
                },
            },
        )

    gemini_router = LLMRouter(api_key="test-key", transport=httpx.MockTransport(gemini_handler))
    g_res = gemini_router.invoke(ModelConfig(), "Sys", "User")
    assert g_res.content == "Gemini OK"
    assert g_res.cached_tokens == 20

    def ollama_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": "Ollama OK"}}],
                "usage": {"prompt_tokens": 30, "completion_tokens": 15},
            },
        )

    ollama_router = LLMRouter(transport=httpx.MockTransport(ollama_handler))
    o_res = ollama_router.invoke(ModelConfig(provider="ollama"), "Sys", "User")
    assert o_res.provider == "ollama"
    assert o_res.content == "Ollama OK"
    assert o_res.cost_usd == 0.0


"""Tests for unified LLM Router (Gemini 4 Hydrogen Low & Ollama)."""

import httpx

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


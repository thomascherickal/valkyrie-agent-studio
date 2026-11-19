"""The `model(prompt)` helper that sandboxed agent code can call. It runs here, on the server, with your keys."""

from __future__ import annotations

import os

from valkyrie import tracing
from valkyrie.fallback import AllProvidersFailed, invoke_with_fallback, usable
from valkyrie.ir_schema import ModelConfig
from valkyrie.llm_router import LLMRouter

SYSTEM = "You are a careful domain expert. Follow the requested structure exactly and keep every figure as given."
PROVIDERS = ("gemini", "ollama", "openrouter", "opencode")


def server_model(prompt: str) -> str | None:
    """Ask the provider chain (Gemini, then OpenCode and OpenRouter free models). None when nothing can answer.

    None means the agent uses its drafted report. It happens with no key set, an unknown provider or every provider failing.
    Provider and model come from VALKYRIE_MODEL_PROVIDER (default gemini) and VALKYRIE_MODEL_ID (needed for
    openrouter and opencode as the first choice: pick a model id from their catalog).
    """
    provider = os.environ.get("VALKYRIE_MODEL_PROVIDER", "gemini")
    tracing.step("model.call", "the agent code called model(prompt)", prompt_chars=len(prompt), prompt=prompt, provider=provider)
    if provider not in PROVIDERS:
        tracing.step("model.none", f"unknown provider {provider}: using the drafted report", "warn")
        return None
    model_id = os.environ.get("VALKYRIE_MODEL_ID")
    config = ModelConfig(provider=provider, model=model_id) if model_id else ModelConfig(provider=provider)
    router = LLMRouter()
    if not usable(router, config):
        tracing.step("model.none", "no provider has a key: using the drafted report", "warn")
        return None
    try:
        answer = invoke_with_fallback(router, config, SYSTEM, prompt)
    except AllProvidersFailed:
        tracing.step("model.none", "no provider answered: using the drafted report", "warn")
        return None
    return answer.content

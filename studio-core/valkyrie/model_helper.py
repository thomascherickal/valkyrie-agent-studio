"""The `model(prompt)` helper that sandboxed agent code can call. It runs here, on the server, with your keys."""

from __future__ import annotations

import os

from valkyrie.ir_schema import ModelConfig
from valkyrie.llm_router import LLMRouter

SYSTEM = "You are a careful domain expert. Follow the requested structure exactly and keep every figure as given."


def server_model(prompt: str) -> str | None:
    """Ask the configured provider. None when it has no key, so a run without keys never touches the network.

    Provider and model come from VALKYRIE_MODEL_PROVIDER (default gemini) and VALKYRIE_MODEL_ID (needed for
    openrouter and opencode: pick a model id from their catalog).
    """
    provider = os.environ.get("VALKYRIE_MODEL_PROVIDER", "gemini")
    router = LLMRouter()
    if provider not in ("gemini", "ollama", "openrouter", "opencode") or not router.has_key(provider):
        return None
    model_id = os.environ.get("VALKYRIE_MODEL_ID")
    config = ModelConfig(provider=provider, model=model_id) if model_id else ModelConfig(provider=provider)
    return router.invoke(config, SYSTEM, prompt).content

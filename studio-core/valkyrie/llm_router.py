"""Unified LLM Router for Gemini 4 Hydrogen (Low Effort) and local Ollama."""

from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Any
import httpx

from valkyrie.ir_schema import ModelConfig

INPUT_COST_PER_M = 1.50
OUTPUT_COST_PER_M = 7.50
CACHE_READ_COST_PER_M = 0.075

# Hosted OpenAI-compatible providers: (base URL, env var holding the API key).
# ponytail: URLs are fixed constants. Move them into ModelConfig if a self-hosted gateway is needed.
HOSTED_COMPAT = {
    "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY"),
    "opencode": ("https://opencode.ai/zen/v1", "OPENCODE_API_KEY"),
}


@dataclass(frozen=True)
class LLMResponse:
    """Normalized response from any configured LLM provider."""

    content: str
    provider: str
    model: str
    thinking_level: str
    input_tokens: int
    output_tokens: int
    cached_tokens: int
    cost_usd: float


def calculate_cost_usd(
    provider: str,
    input_tokens: int,
    output_tokens: int,
    cached_tokens: int = 0,
) -> float:
    """Compute USD cost. Gemini is the only priced provider; Ollama, OpenRouter and OpenCode are tracked as free."""
    if provider != "gemini":
        return 0.0
    uncached_input = max(0, input_tokens - cached_tokens)
    cost = (
        (uncached_input / 1_000_000) * INPUT_COST_PER_M
        + (cached_tokens / 1_000_000) * CACHE_READ_COST_PER_M
        + (output_tokens / 1_000_000) * OUTPUT_COST_PER_M
    )
    return round(cost, 8)


class LLMRouter:
    """Routes agent prompts to Gemini 4 Hydrogen (default), local Ollama, OpenRouter or OpenCode."""

    def __init__(self, api_key: str | None = None, transport: httpx.BaseTransport | None = None) -> None:
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.transport = transport

    def _key(self, provider: str) -> str | None:
        """The API key for a provider. Ollama is local and takes none."""
        if provider == "gemini":
            return self.api_key
        return os.environ.get(HOSTED_COMPAT[provider][1]) if provider in HOSTED_COMPAT else None

    def has_key(self, provider: str) -> bool:
        """True when a call to this provider can be made: it has a key, is local Ollama, or a test transport is set."""
        return provider == "ollama" or self.transport is not None or bool(self._key(provider))

    def build_payload(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        """Build provider-specific request payload."""
        if config.provider != "gemini":
            return {
                "model": config.ollama_model if config.provider == "ollama" else config.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "temperature": config.temperature,
                "max_tokens": config.max_tokens,
            }
        # Gemini's REST API has no top-level thinking fields: the level goes in generationConfig.thinkingConfig.
        return {
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "generationConfig": {
                "temperature": config.temperature,
                "maxOutputTokens": config.max_tokens,
                "thinkingConfig": {"thinkingLevel": config.thinking_level},
            },
        }

    def invoke(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> LLMResponse:
        """Invoke the configured LLM, or return a deterministic local simulation when no API key is set."""
        key = self._key(config.provider)
        if config.provider != "ollama" and not key and self.transport is None:
            in_tok = max(1, len(system_prompt.split()) + len(user_prompt.split()))
            out_tok = 24
            return LLMResponse(
                content=f"[{config.model}:{config.thinking_level}] Processed: {user_prompt[:80]}",
                provider=config.provider,
                model=config.model,
                thinking_level=config.thinking_level,
                input_tokens=in_tok,
                output_tokens=out_tok,
                cached_tokens=0,
                cost_usd=calculate_cost_usd(config.provider, in_tok, out_tok, 0),
            )

        payload = self.build_payload(config, system_prompt, user_prompt)
        with httpx.Client(transport=self.transport, timeout=60.0) as client:
            if config.provider != "gemini":
                base = config.ollama_base_url if config.provider == "ollama" else HOSTED_COMPAT[config.provider][0]
                headers = {"Authorization": f"Bearer {key}"} if key else {}
                resp = client.post(f"{base.rstrip('/')}/chat/completions", json=payload, headers=headers)
                resp.raise_for_status()
                data = resp.json()
                text = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})
                in_tok = int(usage.get("prompt_tokens", 10))
                out_tok = int(usage.get("completion_tokens", 10))
                return LLMResponse(
                    content=text,
                    provider=config.provider,
                    model=payload["model"],
                    thinking_level="none",
                    input_tokens=in_tok,
                    output_tokens=out_tok,
                    cached_tokens=0,
                    cost_usd=0.0,
                )

            # The key goes in a header, never in the URL, so it cannot show up in a logged address or an error.
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{config.model}:generateContent"
            resp = client.post(url, json=payload, headers={"x-goog-api-key": self.api_key or ""})
            resp.raise_for_status()
            data = resp.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            usage = data.get("usageMetadata", {})
            in_tok = int(usage.get("promptTokenCount", 10))
            out_tok = int(usage.get("candidatesTokenCount", 10))
            cached_tok = int(usage.get("cachedContentTokenCount", 0))
            return LLMResponse(
                content=text,
                provider="gemini",
                model=config.model,
                thinking_level=config.thinking_level,
                input_tokens=in_tok,
                output_tokens=out_tok,
                cached_tokens=cached_tok,
                cost_usd=calculate_cost_usd("gemini", in_tok, out_tok, cached_tok),
            )


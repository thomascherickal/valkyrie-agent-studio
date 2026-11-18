"""Unified LLM Router for Gemini 4 Hydrogen (Low Effort) and local Ollama."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import httpx

from valkyrie.ir_schema import ModelConfig

INPUT_COST_PER_M = 1.50
OUTPUT_COST_PER_M = 7.50
CACHE_READ_COST_PER_M = 0.075


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
    """Compute USD cost for Gemini 4 Hydrogen or zero-cost local Ollama."""
    if provider == "ollama":
        return 0.0
    uncached_input = max(0, input_tokens - cached_tokens)
    cost = (
        (uncached_input / 1_000_000) * INPUT_COST_PER_M
        + (cached_tokens / 1_000_000) * CACHE_READ_COST_PER_M
        + (output_tokens / 1_000_000) * OUTPUT_COST_PER_M
    )
    return round(cost, 8)


class LLMRouter:
    """Routes agent prompts to Gemini 4 Hydrogen (Low) or local Ollama."""

    def __init__(self, api_key: str | None = None, transport: httpx.BaseTransport | None = None) -> None:
        self.api_key = api_key
        self.transport = transport

    def build_payload(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        """Build provider-specific request payload."""
        if config.provider == "ollama":
            return {
                "model": config.ollama_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "temperature": config.temperature,
                "max_tokens": config.max_tokens,
            }
        return {
            "model": config.model,
            "thinking_level": config.thinking_level,
            "reasoning_effort": config.thinking_level,
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "generationConfig": {
                "temperature": config.temperature,
                "maxOutputTokens": config.max_tokens,
            },
        }

    def invoke(self, config: ModelConfig, system_prompt: str, user_prompt: str) -> LLMResponse:
        """Invoke the configured LLM, or return a deterministic local simulation when no API key is set."""
        if config.provider == "gemini" and not self.api_key and self.transport is None:
            in_tok = max(1, len(system_prompt.split()) + len(user_prompt.split()))
            out_tok = 24
            return LLMResponse(
                content=f"[gemini-4-hydrogen:{config.thinking_level}] Processed: {user_prompt[:80]}",
                provider="gemini",
                model=config.model,
                thinking_level=config.thinking_level,
                input_tokens=in_tok,
                output_tokens=out_tok,
                cached_tokens=0,
                cost_usd=calculate_cost_usd("gemini", in_tok, out_tok, 0),
            )

        payload = self.build_payload(config, system_prompt, user_prompt)
        with httpx.Client(transport=self.transport, timeout=15.0) as client:
            if config.provider == "ollama":
                url = f"{config.ollama_base_url.rstrip('/')}/chat/completions"
                resp = client.post(url, json=payload)
                resp.raise_for_status()
                data = resp.json()
                text = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})
                in_tok = int(usage.get("prompt_tokens", 10))
                out_tok = int(usage.get("completion_tokens", 10))
                return LLMResponse(
                    content=text,
                    provider="ollama",
                    model=config.ollama_model,
                    thinking_level="none",
                    input_tokens=in_tok,
                    output_tokens=out_tok,
                    cached_tokens=0,
                    cost_usd=0.0,
                )

            url = (
                f"https://generativelanguage.googleapis.com/v1beta/models/"
                f"{config.model}:generateContent?key={self.api_key or ''}"
            )
            resp = client.post(url, json=payload)
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


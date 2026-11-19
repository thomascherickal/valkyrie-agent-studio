"""Provider fallback. Gemini answers first. If it cannot, OpenCode free models try next, then OpenRouter free models.

Every attempt, skip and failure is a trace step, so the Command Centre shows exactly how an answer was reached.
With no keys at all, the router's offline simulation answers, as before, and the trace says so.
"""

from __future__ import annotations

import os
import time

import httpx

from valkyrie import tracing
from valkyrie.ir_schema import ModelConfig
from valkyrie.llm_router import LLMResponse, LLMRouter
from valkyrie.selection import chosen_model, selected_effort, selected_model

# Free models, in the order they are tried. Override with a comma list in VALKYRIE_OPENCODE_MODELS or
# VALKYRIE_OPENROUTER_MODELS. ponytail: static defaults; the catalogs change, so keep them in step with the live lists.
FREE_MODELS: dict[str, tuple[str, ...]] = {
    "opencode": ("big-pickle", "deepseek-v4.1-flash-free", "mimo-v2.6-flash-free"),
    "openrouter": ("openrouter/free", "google/gemma-4-31b-it:free"),
}
MODEL_VARS = {"opencode": "VALKYRIE_OPENCODE_MODELS", "openrouter": "VALKYRIE_OPENROUTER_MODELS"}
CHAIN = ("gemini", "opencode", "openrouter")


class AllProvidersFailed(RuntimeError):
    """Every provider with a key was tried and none answered. `attempts` says what each one said."""

    def __init__(self, attempts: list[dict[str, str]]) -> None:
        self.attempts = attempts
        super().__init__("No provider answered: " + "; ".join(f"{a['provider']} {a['model']}: {a['error']}" for a in attempts))


def free_models(provider: str) -> tuple[str, ...]:
    configured = os.environ.get(MODEL_VARS[provider], "")
    return tuple(m.strip() for m in configured.split(",") if m.strip()) or FREE_MODELS[provider]


def candidates(primary: ModelConfig) -> list[ModelConfig]:
    """The configurations to try, in order: your choice first, then the rest of the chain with your chosen or free models."""
    found = [primary]
    for provider in CHAIN:
        if provider == "gemini":  # the model and effort chosen in the Secrets tab, else the defaults
            found.append(primary.model_copy(update={"provider": "gemini", "model": selected_model("gemini"), "thinking_level": selected_effort(primary.thinking_level)}))
        else:  # the model you chose comes first, then the free models
            models = [m for m in (chosen_model(provider), *free_models(provider)) if m]
            found.extend(primary.model_copy(update={"provider": provider, "model": m}) for m in models)
    seen: set[tuple[str, str]] = set()
    return [c for c in found if not ((c.provider, c.model) in seen or seen.add((c.provider, c.model)))]


def describe(exc: Exception) -> str:
    """A short, key-free reason an attempt failed."""
    if isinstance(exc, httpx.HTTPStatusError):
        text = exc.response.text.strip().replace("\n", " ")
        text = f": {text}" if text else ""
        return str(tracing.redact(f"HTTP {exc.response.status_code}{text[:300]}"))
    if isinstance(exc, httpx.TimeoutException):
        return "timed out"
    return str(tracing.redact(f"{type(exc).__name__}: {exc}"))


def usable(router: LLMRouter, primary: ModelConfig) -> bool:
    """True when at least one provider in the chain could answer for real (it has a key, or is local)."""
    return any(router.has_key(c.provider) for c in candidates(primary))


def invoke_with_fallback(router: LLMRouter, primary: ModelConfig, system: str, prompt: str) -> LLMResponse:
    """Ask the chain in order and return the first real answer. Raises AllProvidersFailed if none answers."""
    tracing.step("route", "provider chain", chain=[f"{c.provider}:{c.model}" for c in candidates(primary)])
    if not usable(router, primary):
        tracing.step("provider.simulated", "no provider has a key, so the answer is simulated offline", "warn",
                     hint="Put GEMINI_API_KEY, OPENCODE_API_KEY or OPENROUTER_API_KEY in .env and reload keys.")
        return router.invoke(primary, system, prompt)
    attempts: list[dict[str, str]] = []
    skipped: set[str] = set()
    for config in candidates(primary):
        if not router.has_key(config.provider):
            if config.provider not in skipped:
                skipped.add(config.provider)
                tracing.step("provider.skip", f"{config.provider} skipped: no API key set", "warn", provider=config.provider)
            continue
        started = time.perf_counter()
        tracing.step("provider.attempt", f"{config.provider} · {config.model}", provider=config.provider, model=config.model,
                     system_chars=len(system), prompt_chars=len(prompt), temperature=config.temperature, max_tokens=config.max_tokens)
        try:
            answer = router.invoke(config, system, prompt)
            if not answer.content.strip():
                raise ValueError("the provider returned an empty answer")
        except Exception as exc:  # noqa: BLE001  ponytail: any failure means try the next provider
            reason = describe(exc)
            attempts.append({"provider": config.provider, "model": config.model, "error": reason})
            tracing.step("provider.fail", f"{config.provider} · {config.model} failed", "error", error=reason,
                         provider=config.provider, model=config.model, ms_taken=round((time.perf_counter() - started) * 1000, 1))
            continue
        tracing.step("provider.ok", f"{answer.provider} · {answer.model} answered", "ok", provider=answer.provider, model=answer.model,
                     input_tokens=answer.input_tokens, output_tokens=answer.output_tokens, cost_usd=answer.cost_usd,
                     ms_taken=round((time.perf_counter() - started) * 1000, 1), response=answer.content)
        if attempts:
            tracing.step("fallback", f"answered by {answer.provider} after {len(attempts)} failed attempt(s)", "warn", failed=attempts)
        return answer
    tracing.step("provider.exhausted", "every provider with a key failed", "error", failed=attempts)
    raise AllProvidersFailed(attempts)

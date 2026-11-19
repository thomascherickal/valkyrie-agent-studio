"""The model slugs each provider offers, for the Secrets tab's drop downs. Live from the provider when it can be
reached (free models first), otherwise the built-in free models. Results are cached for ten minutes."""

from __future__ import annotations

import time
from typing import Any

import httpx

from valkyrie import tracing
from valkyrie.fallback import FREE_MODELS
from valkyrie.selection import DEFAULT_MODELS

TTL_S = 600.0
TRANSPORT: httpx.BaseTransport | None = None  # tests put a mock here
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models?pageSize=200"
OPENROUTER_URL = "https://openrouter.ai/api/v1/models"
OPENCODE_URL = "https://opencode.ai/zen/v1/models"
_cache: dict[str, tuple[float, dict[str, Any]]] = {}


def clear_cache() -> None:
    _cache.clear()


def _get(url: str, headers: dict[str, str] | None = None) -> Any:
    with httpx.Client(transport=TRANSPORT, timeout=15.0) as client:
        response = client.get(url, headers=headers or {})
        response.raise_for_status()
        return response.json()


def _zero(value: Any) -> bool:
    try:
        return float(value) == 0.0
    except (TypeError, ValueError):
        return False


def _gemini(key: str) -> list[dict[str, Any]]:
    data = _get(GEMINI_URL, {"x-goog-api-key": key})["models"]
    return [{"id": m["name"].removeprefix("models/"), "label": m.get("displayName", m["name"]), "free": False}
            for m in data if "generateContent" in m.get("supportedGenerationMethods", [])]


def _openrouter(_: str) -> list[dict[str, Any]]:
    return [{"id": m["id"], "label": m.get("name", m["id"]),
             "free": _zero(m.get("pricing", {}).get("prompt")) and _zero(m.get("pricing", {}).get("completion"))}
            for m in _get(OPENROUTER_URL)["data"]]


def _opencode(_: str) -> list[dict[str, Any]]:
    models = []
    for m in _get(OPENCODE_URL)["data"]:
        text = m.get("cost", {}).get("text", {})
        free = _zero(text.get("input", {}).get("price")) and _zero(text.get("output", {}).get("price"))
        models.append({"id": m["id"], "label": m.get("name", m["id"]), "free": free})
    return models


LIVE = {"gemini": _gemini, "openrouter": _openrouter, "opencode": _opencode}


def _builtin(provider: str) -> list[dict[str, Any]]:
    ids = FREE_MODELS.get(provider, (DEFAULT_MODELS[provider],))
    return [{"id": i, "label": i, "free": provider != "gemini"} for i in ids]


def catalog(provider: str, key: str = "") -> dict[str, Any]:
    """{models: [{id, label, free}], source: "live" | "built-in", note}. Free models come first."""
    cache_key = f"{provider}:{bool(key)}"
    cached = _cache.get(cache_key)
    if cached and time.monotonic() - cached[0] < TTL_S:
        return cached[1]
    note = ""
    if provider == "gemini" and not key:
        models, source, note = _builtin(provider), "built-in", "Add a Gemini key to load its model list."
    else:
        try:
            models, source = LIVE[provider](key), "live"
        except Exception as exc:  # noqa: BLE001  ponytail: any failure means show the built-in list and say why
            models, source, note = _builtin(provider), "built-in", f"Could not load the live list ({type(exc).__name__}); showing the built-in models."
            tracing.step("catalog.fallback", f"{provider} model list unavailable", "warn", error=str(tracing.redact(str(exc))))
    result = {"provider": provider, "models": sorted(models, key=lambda m: (not m["free"], m["id"])), "source": source, "note": note}
    _cache[cache_key] = (time.monotonic(), result)
    return result

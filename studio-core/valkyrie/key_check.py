"""Check a key (the Test Key button): send one tiny real request with a provider's key and, when it fails, list the likely causes."""

from __future__ import annotations

import time
from typing import Any

import httpx

from valkyrie import tracing
from valkyrie.ir_schema import ModelConfig
from valkyrie.llm_router import HOSTED_COMPAT, LLMRouter

TRANSPORT: httpx.BaseTransport | None = None  # tests put a mock here
PROMPT = "Reply with the single word: pong"
GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
TIMEOUT_S = 30.0

CAUSES: dict[int, list[str]] = {
    400: ["The request was rejected as malformed: the model slug may be wrong or not supported by this key.",
          "For Gemini, a 400 can also mean the key itself is not valid."],
    401: ["The key is invalid, expired or revoked.",
          "The key belongs to a different provider (check you pasted it in the right field).",
          "The key was pasted with extra characters or was cut short."],
    402: ["The account has no credits left: top up its balance.",
          "The model is pay-as-you-go and the account has no payment method."],
    403: ["The key is valid but not allowed to use this model: enable model access in the provider's console.",
          "The provider blocks your region, or the API is not enabled for the project (Gemini: the Generative Language API)."],
    404: ["The model slug does not exist or has been retired: pick another from the list.",
          "The provider's address changed."],
    429: ["The rate limit or quota is used up: wait and try again, or choose another model.",
          "A free model may be limited upstream (OpenCode: the free usage limit; OpenRouter: the free model is busy)."],
}


def diagnose(status: int | None, text: str, timed_out: bool, unreachable: bool, empty: bool) -> list[str]:
    """The likely causes of a failed test, most likely first."""
    if timed_out:
        return ["The provider took longer than 30 seconds: it may be down or the network is slow.", "Try again, or choose a faster model."]
    if unreachable:
        return ["The provider cannot be reached: no internet, a DNS problem, or a proxy or firewall is blocking it.",
                "Check the connection and any VPN, then try again."]
    if empty:
        return ["The request worked but the model returned no text: the model may spend its output on thinking.",
                "Choose another model, or a lower effort for Gemini."]
    if status in CAUSES:
        return CAUSES[status]
    if status is not None and status >= 500:
        return ["The provider is having an outage (a server error): wait and try again.", "Check the provider's status page."]
    return [f"The provider answered with an unexpected status ({status}).", "Read the message below and check the key and model."]


def _answer(provider: str, data: Any) -> str:
    try:
        text = data["candidates"][0]["content"]["parts"][0]["text"] if provider == "gemini" else data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return ""
    return text if isinstance(text, str) else ""


def _clean(text: str, key: str) -> str:
    """A short message without the key."""
    text = text.replace(key, "***") if key else text
    return str(tracing.redact(" ".join(text.split())[:300]))


def check_key(provider: str, key: str, model: str) -> dict[str, Any]:
    """Run one request. Returns {ok, status, ms, message, causes}. The key is never part of the result."""
    config = ModelConfig(provider=provider, model=model, max_tokens=512)  # type: ignore[arg-type]
    payload = LLMRouter().build_payload(config, "You are a connection test.", PROMPT)
    if provider == "gemini":
        url, headers = f"{GEMINI_BASE}/{model}:generateContent", {"x-goog-api-key": key}
    else:
        url, headers = f"{HOSTED_COMPAT[provider][0]}/chat/completions", {"Authorization": f"Bearer {key}"}
    started = time.perf_counter()
    status: int | None = None
    text, answer, timed_out, unreachable = "", "", False, False
    try:
        with httpx.Client(transport=TRANSPORT, timeout=TIMEOUT_S) as client:
            response = client.post(url, json=payload, headers=headers)
        status, text = response.status_code, response.text
        if 200 <= status < 300:
            try:
                answer = _answer(provider, response.json())
            except ValueError:  # a success status with a body that is not JSON
                answer = ""
    except httpx.TimeoutException:
        timed_out = True
    except httpx.HTTPError:
        unreachable = True
    ms = round((time.perf_counter() - started) * 1000, 1)
    ok = bool(answer.strip())
    result = {"ok": ok, "status": status, "ms": ms, "provider": provider, "model": model,
              "message": "The key works." if ok else _clean(text, key) or ("timed out" if timed_out else "no answer"),
              "causes": [] if ok else diagnose(status, text, timed_out, unreachable, status is not None and 200 <= status < 300)}
    tracing.step("secrets.test", f"tested the {provider} key: {'succeeded' if ok else 'failed'}", "ok" if ok else "error",
                 provider=provider, model=model, http_status=status, ms_taken=ms, message=result["message"])
    return result

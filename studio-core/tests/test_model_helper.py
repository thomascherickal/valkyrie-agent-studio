"""Tests for the `model(prompt)` helper and for reading blank fields out of pasted text."""

import time
from types import SimpleNamespace

import pytest

from valkyrie.agent_impls import load_spec, render
from valkyrie.llm_router import LLMRouter
from valkyrie.model_helper import server_model
from valkyrie.python_runner import _model_call, run_custom_python

CALL = "def run_agent(p):\n    return {'answer': model(p['q'])}\n"
KEY = "01-product-management/02-roadmap-prioritizer"


def test_sandbox_model_is_none_without_a_model_and_returns_text_with_one() -> None:
    assert run_custom_python(CALL, {"q": "hi"}).output == {"answer": None}
    assert run_custom_python(CALL, {"q": "hi"}, model=lambda p: p.upper()).output == {"answer": "HI"}


def test_model_call_wrapper_directly() -> None:
    """The wrapper runs under the sandbox tracer, where coverage cannot see it, so check it here too."""
    clock = [100.0]
    assert _model_call(lambda p: p + "!", clock)("a") == "a!" and clock[0] >= 100.0
    assert _model_call(None, clock)("a") is None and _model_call(lambda p: "", clock)("a") is None

    def boom(prompt: str) -> str:
        raise RuntimeError("down")

    assert _model_call(boom, clock)("a") is None


def test_sandbox_model_failures_and_blank_text_mean_no_answer() -> None:
    def boom(prompt: str) -> str:
        raise RuntimeError("network down")

    assert run_custom_python(CALL, {"q": "x"}, model=boom).output == {"answer": None}
    assert run_custom_python(CALL, {"q": "x"}, model=lambda p: "  ").output == {"answer": None}


def test_a_slow_model_call_does_not_use_up_the_time_limit() -> None:
    slow = "def run_agent(p):\n    a = model('x')\n    n = 0\n    for i in range(50):\n        n += i\n    return {'a': a, 'n': n}\n"

    def wait(prompt: str) -> str:
        time.sleep(0.4)
        return "late"

    res = run_custom_python(slow, {}, time_limit=0.2, model=wait)
    assert res.ok and res.output["a"] == "late"


def test_has_key_for_each_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    router = LLMRouter()
    assert router.has_key("ollama") and not router.has_key("gemini") and not router.has_key("opencode")
    monkeypatch.setenv("OPENCODE_API_KEY", "k")
    assert router.has_key("opencode")


def test_server_model_does_nothing_without_a_key_and_uses_the_provider_with_one(monkeypatch: pytest.MonkeyPatch) -> None:
    assert server_model("hello") is None  # no key: no network
    seen: list[tuple[str, str]] = []

    def fake(self: LLMRouter, config, system: str, prompt: str) -> SimpleNamespace:  # noqa: ANN001
        seen.append((config.provider, config.model))
        return SimpleNamespace(content="written by a model")

    monkeypatch.setattr(LLMRouter, "invoke", fake)
    monkeypatch.setenv("GEMINI_API_KEY", "k")
    assert server_model("hello") == "written by a model" and seen == [("gemini", "gemini-4-hydrogen")]
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setenv("VALKYRIE_MODEL_PROVIDER", "openrouter")
    monkeypatch.setenv("VALKYRIE_MODEL_ID", "vendor/free-model")
    assert server_model("hello") == "written by a model" and seen[-1] == ("openrouter", "vendor/free-model")
    monkeypatch.setenv("VALKYRIE_MODEL_PROVIDER", "unknown")
    assert server_model("hello") is None


def test_hybrid_uses_the_model_and_the_review_catches_a_bad_answer() -> None:
    spec = load_spec(*KEY.split("/"))
    code = render(spec, "hybrid")
    data = {spec.input_key: spec.sample}
    plain = run_custom_python(code, data).output
    assert plain["model_used"] is False and plain["review"] == []
    bad = run_custom_python(code, data, model=lambda prompt: "Just ship it.").output
    assert bad["model_used"] is True and bad["review"] and bad["confidence"] < 0.9
    good = run_custom_python(code, data, model=lambda prompt: prompt.split("Keep every figure exactly as drafted:\n")[1]).output
    assert good["model_used"] is True and good["review"] == []


def test_blank_fields_are_read_from_the_pasted_text_and_supplied_data_wins() -> None:
    spec = load_spec(*KEY.split("/"))
    code = render(spec, "rules")
    text = "Backlog item: SSO\nReach: 5,000 users; Impact = 3\n| effort | 2 person-months |\nConfidence: 80%"
    res = run_custom_python(code, {spec.input_key: text}).output
    assert res["missing"] == [] and res["completeness"] == 1.0
    assert run_custom_python(code, {spec.input_key: "Backlog item: SSO"}).output["completeness"] == 0.0
    own = run_custom_python(code, {spec.input_key: text, "reach": "100"}).output
    assert own["metrics"] != res["metrics"]

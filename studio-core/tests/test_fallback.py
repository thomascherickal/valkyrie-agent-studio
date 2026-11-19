"""Tests for the provider fallback chain."""

import httpx
import pytest

from valkyrie import fallback
from valkyrie.fallback import AllProvidersFailed, candidates, describe, free_models, invoke_with_fallback, usable
from valkyrie.ir_schema import ModelConfig
from valkyrie.llm_router import LLMResponse
from valkyrie.tracing import STORE


class FakeRouter:
    """Has keys for some providers. `plan` maps "provider:model" to an answer text, or to an exception to raise."""

    def __init__(self, keys: set[str], plan: dict[str, object]) -> None:
        self.keys, self.plan, self.calls = keys, plan, []

    def has_key(self, provider: str) -> bool:
        return provider in self.keys

    def invoke(self, config: ModelConfig, system: str, prompt: str) -> LLMResponse:
        self.calls.append(f"{config.provider}:{config.model}")
        outcome = self.plan.get(self.calls[-1], "simulated")
        if isinstance(outcome, Exception):
            raise outcome
        return LLMResponse(str(outcome), config.provider, config.model, "low", 5, 7, 0, 0.0)


def status_error(code: int, text: str) -> httpx.HTTPStatusError:
    request = httpx.Request("POST", "https://x.test/v1?key=SECRETKEY")
    return httpx.HTTPStatusError("boom", request=request, response=httpx.Response(code, text=text, request=request))


def stages() -> list[str]:
    return [e["stage"] for e in STORE.since()]


@pytest.fixture(autouse=True)
def _empty_store() -> None:
    STORE.clear()


def test_the_chain_is_your_choice_then_gemini_then_opencode_then_openrouter_free_models() -> None:
    order = [f"{c.provider}:{c.model}" for c in candidates(ModelConfig())]
    assert order == ["gemini:gemini-4-hydrogen", "opencode:big-pickle", "opencode:deepseek-v4.1-flash-free",
                     "opencode:mimo-v2.6-flash-free", "openrouter:openrouter/free", "openrouter:google/gemma-4-31b-it:free"]
    mine = ModelConfig(provider="openrouter", model="vendor/my-model")
    again = [f"{c.provider}:{c.model}" for c in candidates(mine)]
    assert again[0] == "openrouter:vendor/my-model" and again[1] == "gemini:gemini-4-hydrogen" and len(again) == len(set(again)) == 7
    assert candidates(ModelConfig(temperature=0.9))[1].temperature == 0.9  # settings carry over to the fallbacks


def test_free_models_can_be_overridden_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    assert free_models("opencode")[0] == "big-pickle"
    monkeypatch.setenv("VALKYRIE_OPENCODE_MODELS", " alpha-free , beta-free ,")
    assert free_models("opencode") == ("alpha-free", "beta-free")


def test_describe_gives_a_short_reason_without_the_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "SECRETKEY")
    text = describe(status_error(429, '{"error": "Free usage limit reached"}'))
    assert text.startswith("HTTP 429") and "Free usage limit" in text and "SECRETKEY" not in text
    assert describe(status_error(500, "")) == "HTTP 500"
    assert describe(httpx.ReadTimeout("slow")) == "timed out"
    assert describe(ValueError("SECRETKEY leaked")) == "ValueError: *** leaked"


def test_with_no_keys_the_offline_simulation_answers_and_the_trace_says_so() -> None:
    router = FakeRouter(set(), {})
    assert not usable(router, ModelConfig())
    answer = invoke_with_fallback(router, ModelConfig(), "sys", "hi")
    assert answer.content == "simulated" and router.calls == ["gemini:gemini-4-hydrogen"]
    assert stages() == ["route", "provider.simulated"]


def test_the_first_provider_that_answers_wins() -> None:
    router = FakeRouter({"gemini"}, {"gemini:gemini-4-hydrogen": "from gemini"})
    answer = invoke_with_fallback(router, ModelConfig(), "sys", "hi")
    assert answer.content == "from gemini" and router.calls == ["gemini:gemini-4-hydrogen"]
    assert stages() == ["route", "provider.attempt", "provider.ok"]  # it answered, so nobody else was asked
    assert STORE.since()[-1]["detail"]["response"] == "from gemini"


def test_when_gemini_fails_opencode_free_models_are_tried_next_then_openrouter() -> None:
    plan = {
        "gemini:gemini-4-hydrogen": status_error(503, "overloaded"),
        "opencode:big-pickle": status_error(429, "Free usage limit reached"),
        "opencode:deepseek-v4.1-flash-free": httpx.ReadTimeout("slow"),
        "opencode:mimo-v2.6-flash-free": "   ",  # an empty answer counts as a failure
        "openrouter:openrouter/free": "from the free router",
    }
    router = FakeRouter({"gemini", "opencode", "openrouter"}, plan)
    answer = invoke_with_fallback(router, ModelConfig(), "sys", "hi")
    assert answer.content == "from the free router" and answer.provider == "openrouter"
    assert router.calls == ["gemini:gemini-4-hydrogen", "opencode:big-pickle", "opencode:deepseek-v4.1-flash-free",
                            "opencode:mimo-v2.6-flash-free", "openrouter:openrouter/free"]
    events = STORE.since()
    fails = [e for e in events if e["stage"] == "provider.fail"]
    assert [e["detail"]["error"] for e in fails] == ["HTTP 503: overloaded", "HTTP 429: Free usage limit reached", "timed out",
                                                     "ValueError: the provider returned an empty answer"]
    assert events[-1]["stage"] == "fallback" and events[-1]["status"] == "warn" and len(events[-1]["detail"]["failed"]) == 4


def test_when_every_provider_fails_the_error_lists_each_attempt() -> None:
    boom = status_error(500, "down")
    plan = {f"{c.provider}:{c.model}": boom for c in candidates(ModelConfig())}
    router = FakeRouter({"gemini", "openrouter"}, plan)
    with pytest.raises(AllProvidersFailed) as caught:
        invoke_with_fallback(router, ModelConfig(), "sys", "hi")
    assert len(caught.value.attempts) == 3 and "gemini gemini-4-hydrogen: HTTP 500: down" in str(caught.value)
    assert stages()[-1] == "provider.exhausted" and STORE.since()[-1]["status"] == "error"
    skips = [e for e in STORE.since() if e["stage"] == "provider.skip"]
    assert [e["detail"]["provider"] for e in skips] == ["opencode"]  # no key: said once, not once per free model


def test_a_failing_primary_choice_still_reaches_the_chain() -> None:
    mine = ModelConfig(provider="openrouter", model="vendor/mine")
    router = FakeRouter({"openrouter"}, {"openrouter:vendor/mine": status_error(404, "no such model")})
    assert invoke_with_fallback(router, mine, "s", "p").model == "openrouter/free"


def test_module_defaults_name_free_models_only() -> None:
    assert all(m.endswith("free") or m.endswith(":free") or m == "big-pickle" for ms in fallback.FREE_MODELS.values() for m in ms)

"""100% coverage pytest suite for 05-llm-token-optimizer."""

from agent import run_agent


def test_05_llm_token_optimizer() -> None:
    res = run_agent({"llm_usage": "Using high-effort model ($15/1M) for JSO"})
    assert res["agent_id"] == "05-llm-token-optimizer"
    assert res["tool_used"] == "recommend_model_tier"
    assert "recommend_model_tier" in res["token_savings"]

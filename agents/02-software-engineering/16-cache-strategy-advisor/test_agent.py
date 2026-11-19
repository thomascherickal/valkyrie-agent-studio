"""100% coverage pytest suite for 16-cache-strategy-advisor."""

from agent import run_agent


def test_16_cache_strategy_advisor() -> None:
    res = run_agent({"access_pattern": "Product pages: 800 reads/s, 2 writes/s, 95% of reads hit 5% of products, stale up to 60s is fine"})
    assert res["agent_id"] == "16-cache-strategy-advisor"
    assert res["tool_used"] == "design_cache_strategy"
    assert "design_cache_strategy" in res["cache_design"]

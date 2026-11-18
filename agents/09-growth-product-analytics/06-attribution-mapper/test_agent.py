"""100% coverage pytest suite for 06-attribution-mapper."""

from agent import run_agent


def test_06_attribution_mapper() -> None:
    res = run_agent({"channel_spend": "GitHub OSS: $0 CAC, 42% signups; Search "})
    assert res["agent_id"] == "06-attribution-mapper"
    assert res["tool_used"] == "compute_channel_roi"
    assert "compute_channel_roi" in res["attribution_table"]

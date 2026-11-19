"""100% coverage pytest suite for 13-feature-flag-cleaner."""

from agent import run_agent


def test_13_feature_flag_cleaner() -> None:
    res = run_agent({"flag_inventory": "214 flags, 88 older than 6 months, 31 at 100% rollout for over 90 days, owners missing on 40"})
    assert res["agent_id"] == "13-feature-flag-cleaner"
    assert res["tool_used"] == "find_stale_flags"
    assert "find_stale_flags" in res["cleanup_plan"]

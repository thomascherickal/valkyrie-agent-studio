"""100% coverage pytest suite for 19-code-owner-mapper."""

from agent import run_agent


def test_19_code_owner_mapper() -> None:
    res = run_agent({"commit_history": "payments/ last 12 months: 3 authors left, 1 remaining (62% of commits); search/ has no commits in 9 months"})
    assert res["agent_id"] == "19-code-owner-mapper"
    assert res["tool_used"] == "map_code_owners"
    assert "map_code_owners" in res["owners_map"]

"""100% coverage pytest suite for 20-developer-journey-mapper."""

from agent import run_agent


def test_20_developer_journey_mapper() -> None:
    res = run_agent({"journey_notes": "Finds us via search, 4 doc pages to first call, key approval takes a day, production needs a security review"})
    assert res["agent_id"] == "20-developer-journey-mapper"
    assert res["tool_used"] == "map_developer_journey"
    assert "map_developer_journey" in res["journey_map"]

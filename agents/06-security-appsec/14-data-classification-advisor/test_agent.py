"""100% coverage pytest suite for 14-data-classification-advisor."""

from agent import run_agent


def test_14_data_classification_advisor() -> None:
    res = run_agent({"data_inventory": "Customer DB with emails and payment tokens; analytics warehouse with pseudonymous IDs; public marketing site"})
    assert res["agent_id"] == "14-data-classification-advisor"
    assert res["tool_used"] == "classify_data"
    assert "classify_data" in res["classification_map"]

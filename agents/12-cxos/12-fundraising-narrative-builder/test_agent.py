"""100% coverage pytest suite for 12-fundraising-narrative-builder."""

from agent import run_agent


def test_12_fundraising_narrative_builder() -> None:
    res = run_agent({"company_facts": "B2B workflow SaaS, 4.1M ARR growing 160% a year, 118% net retention, raising 20M Series B, 24 months of runway wanted"})
    assert res["agent_id"] == "12-fundraising-narrative-builder"
    assert res["tool_used"] == "build_fundraise_story"
    assert "build_fundraise_story" in res["investor_narrative"]

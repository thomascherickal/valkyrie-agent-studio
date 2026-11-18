"""100% coverage pytest suite for 09-org-design-modeler."""

from agent import run_agent


def test_09_org_design_modeler() -> None:
    res = run_agent({"org_chart": "42 engineers, 4 managers, 1 platform tea"})
    assert res["agent_id"] == "09-org-design-modeler"
    assert res["tool_used"] == "analyze_org_topology"
    assert "analyze_org_topology" in res["org_recommendations"]

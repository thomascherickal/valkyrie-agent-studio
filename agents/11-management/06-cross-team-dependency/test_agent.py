"""100% coverage pytest suite for 06-cross-team-dependency."""

from agent import run_agent


def test_06_cross_team_dependency() -> None:
    res = run_agent({"squad_milestones": "UI team needs /ws/traces from Core by No"})
    assert res["agent_id"] == "06-cross-team-dependency"
    assert res["tool_used"] == "map_critical_path"
    assert "map_critical_path" in res["dependency_risks"]

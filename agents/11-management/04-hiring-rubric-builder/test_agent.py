"""100% coverage pytest suite for 04-hiring-rubric-builder."""

from agent import run_agent


def test_04_hiring_rubric_builder() -> None:
    res = run_agent({"role_level": "Senior Rust/Python Systems Engineer — Ar"})
    assert res["agent_id"] == "04-hiring-rubric-builder"
    assert res["tool_used"] == "build_rubric_grid"
    assert "build_rubric_grid" in res["rubric_md"]

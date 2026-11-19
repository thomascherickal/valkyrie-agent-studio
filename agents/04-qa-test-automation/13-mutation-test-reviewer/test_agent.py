"""100% coverage pytest suite for 13-mutation-test-reviewer."""

from agent import run_agent


def test_13_mutation_test_reviewer() -> None:
    res = run_agent({"mutation_report": "pricing.py: 240 mutants, 168 killed, 72 survived; survivors mostly in boundary checks and rounding"})
    assert res["agent_id"] == "13-mutation-test-reviewer"
    assert res["tool_used"] == "review_mutation_survivors"
    assert "review_mutation_survivors" in res["survivor_actions"]

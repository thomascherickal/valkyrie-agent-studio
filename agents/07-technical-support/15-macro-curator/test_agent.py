"""100% coverage pytest suite for 15-macro-curator."""

from agent import run_agent


def test_15_macro_curator() -> None:
    res = run_agent({"macro_usage": "312 macros; 40 used 80% of the time; 120 not used in a year; CSAT 3 points lower when macro 'Reset steps' is used"})
    assert res["agent_id"] == "15-macro-curator"
    assert res["tool_used"] == "curate_macros"
    assert "curate_macros" in res["macro_plan"]

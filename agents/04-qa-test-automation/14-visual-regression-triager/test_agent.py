"""100% coverage pytest suite for 14-visual-regression-triager."""

from agent import run_agent


def test_14_visual_regression_triager() -> None:
    res = run_agent({"screenshot_diffs": "48 diffs on checkout: 30 are 1px font anti-aliasing, 12 show the new button colour, 6 show a missing icon"})
    assert res["agent_id"] == "14-visual-regression-triager"
    assert res["tool_used"] == "triage_visual_diffs"
    assert "triage_visual_diffs" in res["visual_triage"]

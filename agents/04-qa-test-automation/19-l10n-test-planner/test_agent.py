"""100% coverage pytest suite for 19-l10n-test-planner."""

from agent import run_agent


def test_19_l10n_test_planner() -> None:
    res = run_agent({"locale_list": "Launching in German, Japanese, Arabic and Brazilian Portuguese; currency, dates and addresses vary"})
    assert res["agent_id"] == "19-l10n-test-planner"
    assert res["tool_used"] == "plan_locale_tests"
    assert "plan_locale_tests" in res["l10n_plan"]

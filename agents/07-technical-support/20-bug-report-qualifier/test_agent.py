"""100% coverage pytest suite for 20-bug-report-qualifier."""

from agent import run_agent


def test_20_bug_report_qualifier() -> None:
    res = run_agent({"customer_report": "Invoice PDF shows wrong tax for Canadian customers since March; two accounts affected; screenshot attached"})
    assert res["agent_id"] == "20-bug-report-qualifier"
    assert res["tool_used"] == "qualify_bug_report"
    assert "qualify_bug_report" in res["qualified_bug"]

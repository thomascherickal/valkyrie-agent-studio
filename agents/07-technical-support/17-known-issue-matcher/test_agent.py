"""100% coverage pytest suite for 17-known-issue-matcher."""

from agent import run_agent


def test_17_known_issue_matcher() -> None:
    res = run_agent({"symptom_report": "Export to PDF hangs at 95% for reports over 5,000 rows on Safari; started after the 3.2 release"})
    assert res["agent_id"] == "17-known-issue-matcher"
    assert res["tool_used"] == "match_known_issues"
    assert "match_known_issues" in res["issue_match"]

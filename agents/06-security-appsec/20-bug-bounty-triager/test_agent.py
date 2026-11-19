"""100% coverage pytest suite for 20-bug-bounty-triager."""

from agent import run_agent


def test_20_bug_bounty_triager() -> None:
    res = run_agent({"bounty_report": "Researcher reports stored XSS in the profile bio field on app.example.com, proof of concept attached"})
    assert res["agent_id"] == "20-bug-bounty-triager"
    assert res["tool_used"] == "triage_bounty_report"
    assert "triage_bounty_report" in res["bounty_verdict"]

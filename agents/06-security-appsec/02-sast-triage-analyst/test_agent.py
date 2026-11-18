"""100% coverage pytest suite for 02-sast-triage-analyst."""

from agent import run_agent


def test_02_sast_triage_analyst() -> None:
    res = run_agent({"sast_finding": "CWE-78 in dev_script.py vs parameterized"})
    assert res["agent_id"] == "02-sast-triage-analyst"
    assert res["tool_used"] == "assess_reachability"
    assert "assess_reachability" in res["triage_verdict"]

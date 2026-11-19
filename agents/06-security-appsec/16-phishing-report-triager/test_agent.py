"""100% coverage pytest suite for 16-phishing-report-triager."""

from agent import run_agent


def test_16_phishing_report_triager() -> None:
    res = run_agent({"reported_email": "Subject Urgent payroll update; link to payr0ll-portal.example; sent to 240 staff; 12 clicked, 3 entered passwords"})
    assert res["agent_id"] == "16-phishing-report-triager"
    assert res["tool_used"] == "triage_phishing"
    assert "triage_phishing" in res["phishing_verdict"]

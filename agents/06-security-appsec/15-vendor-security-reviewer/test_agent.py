"""100% coverage pytest suite for 15-vendor-security-reviewer."""

from agent import run_agent


def test_15_vendor_security_reviewer() -> None:
    res = run_agent({"vendor_answers": "Vendor stores customer emails, SOC 2 Type I only, no pen test in 2 years, subprocessors listed, 99.5% SLA"})
    assert res["agent_id"] == "15-vendor-security-reviewer"
    assert res["tool_used"] == "review_vendor_security"
    assert "review_vendor_security" in res["vendor_risk"]

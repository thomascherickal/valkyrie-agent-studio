"""100% coverage pytest suite for 08-accessibility-auditor."""

from agent import run_agent


def test_08_accessibility_auditor() -> None:
    res = run_agent({"html_snippet": "<div onclick='open()'>Deploy</div> witho"})
    assert res["agent_id"] == "08-accessibility-auditor"
    assert res["tool_used"] == "audit_wcag_aa"
    assert "audit_wcag_aa" in res["a11y_issues"]

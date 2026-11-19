"""100% coverage pytest suite for 19-event-taxonomy-auditor."""

from agent import run_agent


def test_19_event_taxonomy_auditor() -> None:
    res = run_agent({"event_list": "signup, Sign_Up, user_signed_up, click_btn, ButtonClicked, plan_upgraded, upgrade; 340 events, 60 unused"})
    assert res["agent_id"] == "19-event-taxonomy-auditor"
    assert res["tool_used"] == "audit_event_names"
    assert "audit_event_names" in res["taxonomy_audit"]

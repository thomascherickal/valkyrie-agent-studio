"""100% coverage pytest suite for 13-duplicate-ticket-merger."""

from agent import run_agent


def test_13_duplicate_ticket_merger() -> None:
    res = run_agent({"ticket_list": "9 tickets about login loops on iOS 17.4 since the 2.8 release; 4 from the same company; 2 mention the same error code"})
    assert res["agent_id"] == "13-duplicate-ticket-merger"
    assert res["tool_used"] == "find_duplicate_tickets"
    assert "find_duplicate_tickets" in res["merge_plan"]

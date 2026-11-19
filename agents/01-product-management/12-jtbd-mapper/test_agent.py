"""100% coverage pytest suite for 12-jtbd-mapper."""

from agent import run_agent


def test_12_jtbd_mapper() -> None:
    res = run_agent({"interview_notes": "Switched from spreadsheets after the audit failed; needs proof of access reviews in under an hour"})
    assert res["agent_id"] == "12-jtbd-mapper"
    assert res["tool_used"] == "map_jobs_to_be_done"
    assert "map_jobs_to_be_done" in res["jtbd_map"]

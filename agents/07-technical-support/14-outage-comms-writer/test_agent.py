"""100% coverage pytest suite for 14-outage-comms-writer."""

from agent import run_agent


def test_14_outage_comms_writer() -> None:
    res = run_agent({"outage_facts": "Payments API errors for 22% of requests since 14:05 UTC; cause under investigation; card checkout affected"})
    assert res["agent_id"] == "14-outage-comms-writer"
    assert res["tool_used"] == "write_outage_comms"
    assert "write_outage_comms" in res["customer_comms"]

"""100% coverage pytest suite for 06-soc2-evidence-collector."""

from agent import run_agent


def test_06_soc2_evidence_collector() -> None:
    res = run_agent({"control_id": "CC8.1 Change Management — require 100% t"})
    assert res["agent_id"] == "06-soc2-evidence-collector"
    assert res["tool_used"] == "collect_control_proof"
    assert "collect_control_proof" in res["evidence_bundle"]

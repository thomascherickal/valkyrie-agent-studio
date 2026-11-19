"""100% coverage pytest suite for 19-dns-change-verifier."""

from agent import run_agent


def test_19_dns_change_verifier() -> None:
    res = run_agent({"dns_change": "Move api.example.com from the old load balancer to the new one; current TTL 3600; mail records unchanged"})
    assert res["agent_id"] == "19-dns-change-verifier"
    assert res["tool_used"] == "verify_dns_change"
    assert "verify_dns_change" in res["dns_checklist"]

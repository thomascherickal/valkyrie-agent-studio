"""100% coverage pytest suite for 10-rust-port-advisor."""

from agent import run_agent


def test_10_rust_port_advisor() -> None:
    res = run_agent({"profile_stats": "json_validator.py: 68% CPU time, 42ms p9"})
    assert res["agent_id"] == "10-rust-port-advisor"
    assert res["tool_used"] == "estimate_rust_speedup"
    assert "estimate_rust_speedup" in res["port_blueprint"]

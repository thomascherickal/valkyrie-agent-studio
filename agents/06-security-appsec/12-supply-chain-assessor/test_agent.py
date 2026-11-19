"""100% coverage pytest suite for 12-supply-chain-assessor."""

from agent import run_agent


def test_12_supply_chain_assessor() -> None:
    res = run_agent({"dependency_notes": "1,240 transitive packages, 36 maintained by one person, builds pull unpinned actions, images unsigned"})
    assert res["agent_id"] == "12-supply-chain-assessor"
    assert res["tool_used"] == "assess_supply_chain"
    assert "assess_supply_chain" in res["supply_chain_report"]

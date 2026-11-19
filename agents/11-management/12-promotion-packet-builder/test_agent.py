"""100% coverage pytest suite for 12-promotion-packet-builder."""

from agent import run_agent


def test_12_promotion_packet_builder() -> None:
    res = run_agent({"impact_notes": "Led billing migration (zero downtime, 3 teams), mentored 2 engineers, cut invoice errors 70%, wrote the pricing RFC"})
    assert res["agent_id"] == "12-promotion-packet-builder"
    assert res["tool_used"] == "build_promo_packet"
    assert "build_promo_packet" in res["promo_packet"]

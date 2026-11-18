"""100% coverage pytest suite for 01-board-deck-synthesizer."""

from agent import run_agent


def test_01_board_deck_synthesizer() -> None:
    res = run_agent({"quarter_metrics": "ARR $4.8M (+22% QoQ), NRR 118%, Runway 2"})
    assert res["agent_id"] == "01-board-deck-synthesizer"
    assert res["tool_used"] == "build_board_narrative"
    assert "build_board_narrative" in res["board_slides_md"]

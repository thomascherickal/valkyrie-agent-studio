"""100% coverage pytest suite for 11-persona-builder."""

from agent import run_agent


def test_11_persona_builder() -> None:
    res = run_agent({"research_notes": "12 interviews: admins spend Mondays on access requests; 9 of 12 use spreadsheets to track licences"})
    assert res["agent_id"] == "11-persona-builder"
    assert res["tool_used"] == "synthesize_personas"
    assert "synthesize_personas" in res["persona_cards"]

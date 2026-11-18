"""100% coverage pytest suite for 02-1on1-prep-assistant."""

from agent import run_agent


def test_02_1on1_prep_assistant() -> None:
    res = run_agent({"engineer_context": "Led Rust workspace rollout; blocked on C"})
    assert res["agent_id"] == "02-1on1-prep-assistant"
    assert res["tool_used"] == "structure_1on1_agenda"
    assert "structure_1on1_agenda" in res["agenda_md"]

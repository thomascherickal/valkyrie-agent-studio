"""100% coverage pytest suite for 08-cfp-abstract-writer."""

from agent import run_agent


def test_08_cfp_abstract_writer() -> None:
    res = run_agent({"talk_idea": "Zero-GIL AI Agents: Compiling Python Pro"})
    assert res["agent_id"] == "08-cfp-abstract-writer"
    assert res["tool_used"] == "polish_cfp_abstract"
    assert "polish_cfp_abstract" in res["cfp_submission"]

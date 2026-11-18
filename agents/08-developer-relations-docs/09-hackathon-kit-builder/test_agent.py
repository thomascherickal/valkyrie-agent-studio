"""100% coverage pytest suite for 09-hackathon-kit-builder."""

from agent import run_agent


def test_09_hackathon_kit_builder() -> None:
    res = run_agent({"theme": "Build an automated FinOps agent in 4 hou"})
    assert res["agent_id"] == "09-hackathon-kit-builder"
    assert res["tool_used"] == "assemble_kit_manifest"
    assert "assemble_kit_manifest" in res["hackathon_kit"]

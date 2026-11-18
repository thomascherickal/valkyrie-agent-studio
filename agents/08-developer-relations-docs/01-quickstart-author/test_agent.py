"""100% coverage pytest suite for 01-quickstart-author."""

from agent import run_agent


def test_01_quickstart_author() -> None:
    res = run_agent({"feature_name": "Deploying your first Rust agent from Val"})
    assert res["agent_id"] == "01-quickstart-author"
    assert res["tool_used"] == "structure_quickstart"
    assert "structure_quickstart" in res["quickstart_md"]

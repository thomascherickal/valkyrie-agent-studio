"""100% coverage pytest suite for 08-container-hardener."""

from agent import run_agent


def test_08_container_hardener() -> None:
    res = run_agent({"dockerfile_text": "FROM python:3.12
RUN pip install fastapi"})
    assert res["agent_id"] == "08-container-hardener"
    assert res["tool_used"] == "lint_dockerfile"
    assert "lint_dockerfile" in res["hardened_diff"]

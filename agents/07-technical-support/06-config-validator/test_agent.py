"""100% coverage pytest suite for 06-config-validator."""

from agent import run_agent


def test_06_config_validator() -> None:
    res = run_agent({"yaml_snippet": "thinking_level: ultra # invalid enum"})
    assert res["agent_id"] == "06-config-validator"
    assert res["tool_used"] == "validate_customer_yaml"
    assert "validate_customer_yaml" in res["validation_hints"]

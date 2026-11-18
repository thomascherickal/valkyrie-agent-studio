"""Tests for Universal Agent IR schema and YAML serialization."""

import pytest
from pydantic import ValidationError

from valkyrie.ir_schema import AgentIR, dump_ir_to_yaml, load_ir_from_yaml


def test_ir_defaults_to_gemini_4_hydrogen_low() -> None:
    ir = AgentIR(
        id="prd-architect",
        name="PRD Architect",
        role="Product Management",
        description="Drafts PRDs",
        system_prompt="You are a PRD architect.",
    )
    assert ir.model_config_spec.provider == "gemini"
    assert ir.model_config_spec.model == "gemini-4-hydrogen"
    assert ir.model_config_spec.thinking_level == "low"


def test_ir_invalid_id_rejected() -> None:
    with pytest.raises(ValidationError, match="alphanumeric characters and hyphens"):
        AgentIR(
            id="bad_id!",
            name="Bad",
            role="Role",
            description="Desc",
            system_prompt="Prompt",
        )


def test_ir_yaml_roundtrip_and_invalid_yaml() -> None:
    ir = AgentIR(
        id="test-agent",
        name="Test Agent",
        role="QA",
        description="Tests",
        system_prompt="Run tests.",
    )
    dumped = dump_ir_to_yaml(ir)
    loaded = load_ir_from_yaml(dumped)
    assert loaded == ir

    with pytest.raises(ValueError, match="mapping"):
        load_ir_from_yaml("- just a list")


"""Universal Agent Intermediate Representation (IR) schema and YAML validator."""

from __future__ import annotations

from typing import Literal
import yaml
from pydantic import BaseModel, Field, field_validator


class ModelConfig(BaseModel):
    """LLM routing and effort configuration."""

    provider: Literal["gemini", "ollama"] = "gemini"
    model: str = "gemini-4-hydrogen"
    thinking_level: Literal["low", "medium", "high"] = "low"
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, ge=1, le=1_000_000)
    ollama_base_url: str = "http://localhost:11434/v1"
    ollama_model: str = "qwen3.5:latest"


class ToolSpec(BaseModel):
    """Declarative tool definition wired into an agent."""

    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    parameters: dict[str, str] = Field(default_factory=dict)


class GuardrailConfig(BaseModel):
    """Safety, latency, and cost guardrails."""

    max_latency_ms: int = Field(default=5000, ge=100)
    max_cost_usd: float = Field(default=0.05, ge=0.0)
    require_json_output: bool = True
    blocked_patterns: list[str] = Field(default_factory=list)


class AgentIR(BaseModel):
    """Universal Agent Intermediate Representation (agent.ir.yaml)."""

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    role: str = Field(min_length=1)
    version: str = "1.0.0"
    description: str = Field(min_length=1)
    system_prompt: str = Field(min_length=1)
    model_config_spec: ModelConfig = Field(default_factory=ModelConfig)
    tools: list[ToolSpec] = Field(default_factory=list)
    input_schema: dict[str, str] = Field(default_factory=dict)
    output_schema: dict[str, str] = Field(default_factory=dict)
    guardrails: GuardrailConfig = Field(default_factory=GuardrailConfig)
    custom_python_enabled: bool = False

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        """Ensure agent IDs use kebab-case."""
        if not all(ch.isalnum() or ch == "-" for ch in value):
            raise ValueError("Agent id must contain only alphanumeric characters and hyphens")
        return value


def load_ir_from_yaml(yaml_text: str) -> AgentIR:
    """Parse and validate an AgentIR from a YAML string."""
    raw = yaml.safe_load(yaml_text)
    if not isinstance(raw, dict):
        raise ValueError("IR YAML must deserialize to a mapping")
    return AgentIR.model_validate(raw)


def dump_ir_to_yaml(ir: AgentIR) -> str:
    """Serialize an AgentIR instance to YAML."""
    return yaml.safe_dump(ir.model_dump(mode="json"), sort_keys=False)


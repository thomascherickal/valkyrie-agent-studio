"""Tests for plain-English custom agent generator."""

from pathlib import Path
import pytest

from valkyrie.agent_generator import generate_agent_from_english, write_generated_agent
from valkyrie.ir_schema import load_ir_from_yaml
from valkyrie.python_runner import run_custom_python


def test_generate_and_persist_custom_agent(tmp_path: Path) -> None:
    bundle = generate_agent_from_english(
        "Monitor Postgres slow queries and suggest composite indexes",
        role="Data Engineering",
        name="Slow Query Helper",
    )
    assert bundle.agent_id == "slow-query-helper"
    assert bundle.tool_name == "run_slow_query_helper"

    # Validate generated IR YAML and Python code in sandbox
    ir = load_ir_from_yaml(bundle.ir_yaml)
    assert ir.id == "slow-query-helper"
    py_res = run_custom_python(bundle.agent_py, {"task_input": "SELECT * FROM events"})
    assert py_res.ok is True
    assert "run_slow_query_helper" in py_res.output["result"]

    # Persist to disk and verify files
    out_dir = write_generated_agent(bundle, tmp_path)
    assert (out_dir / "agent.ir.yaml").exists()
    assert (out_dir / "agent.py").exists()
    assert (out_dir / "test_agent.py").exists()
    assert (out_dir / "AGENT.md").exists()
    assert (out_dir / "rust" / "Cargo.toml").exists()
    assert (out_dir / "rust" / "src" / "main.rs").exists()


def test_generate_agent_empty_and_punctuation_fallbacks() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        generate_agent_from_english("   ")

    bundle = generate_agent_from_english("!!!")
    assert bundle.agent_id == "custom-agent"

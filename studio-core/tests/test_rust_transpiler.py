"""Tests for Rust deployment transpiler."""

from valkyrie.ir_schema import AgentIR
from valkyrie.rust_transpiler import transpile_ir_to_rust


def test_transpile_ir_to_rust() -> None:
    ir = AgentIR(
        id="prd-architect",
        name="PRD Architect",
        role="Product Management",
        description="Drafts PRDs",
        system_prompt="Draft a PRD.",
    )
    bundle = transpile_ir_to_rust(ir)
    assert bundle.crate_name == "valkyrie_prd_architect"
    assert "tokio" in bundle.cargo_toml
    assert "gemini-4-hydrogen" in bundle.main_rs
    assert "#[tokio::test]" in bundle.main_rs


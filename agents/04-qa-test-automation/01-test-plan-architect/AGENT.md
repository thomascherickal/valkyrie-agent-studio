# Test Plan Architect (`01-test-plan-architect`)

**Role:** QA & Test Automation  
**Tool:** `derive_test_matrix`

## Focused Responsibility
Maps PRD acceptance criteria into risk-weighted test matrices.

## Contract
- **Input (`spec_summary`):** string
- **Output (`test_plan`):** string, `tool_used` (`derive_test_matrix`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_test_plan_architect`)

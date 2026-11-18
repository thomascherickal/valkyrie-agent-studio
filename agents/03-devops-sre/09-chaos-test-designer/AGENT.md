# Chaos Test Designer (`09-chaos-test-designer`)

**Role:** DevOps & SRE  
**Tool:** `design_chaos_drill`

## Focused Responsibility
Defines steady-state hypotheses and blast-radius bounds for fault drills.

## Contract
- **Input (`target_service`):** string
- **Output (`chaos_spec`):** string, `tool_used` (`design_chaos_drill`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_chaos_test_designer`)

# Load Test Modeler (`09-load-test-modeler`)

**Role:** QA & Test Automation  
**Tool:** `build_k6_profile`

## Focused Responsibility
Generates ramped virtual-user profiles and p95 latency thresholds.

## Contract
- **Input (`target_sla`):** string
- **Output (`load_script`):** string, `tool_used` (`build_k6_profile`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_load_test_modeler`)

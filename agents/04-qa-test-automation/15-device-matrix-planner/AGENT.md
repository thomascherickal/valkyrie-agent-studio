# Mobile Device Matrix Planner (`15-device-matrix-planner`)

**Role:** QA & Test Automation
**Tool:** `build_device_matrix`

## Focused Responsibility
Builds a mobile test matrix from usage analytics, risk, and testing capacity.

## Contract
- **Input (`usage_analytics`):** string
- **Output (`device_matrix`):** string, `tool_used` (`build_device_matrix`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_device_matrix_planner`)

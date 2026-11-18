# Regression Selector (`07-regression-selector`)

**Role:** QA & Test Automation  
**Tool:** `map_impacted_tests`

## Focused Responsibility
Selects the minimal impacted test subset from changed file paths.

## Contract
- **Input (`changed_files`):** string
- **Output (`selected_tests`):** string, `tool_used` (`map_impacted_tests`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_regression_selector`)

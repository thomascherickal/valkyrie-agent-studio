# Slowly Changing Dimension Modeler (`15-scd-modeler`)

**Role:** Data Engineering
**Tool:** `model_scd`

## Focused Responsibility
Models slowly changing dimensions with type choice, keys, effective dates, and load logic.

## Contract
- **Input (`dimension_changes`):** string
- **Output (`scd_design`):** string, `tool_used` (`model_scd`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_scd_modeler`)

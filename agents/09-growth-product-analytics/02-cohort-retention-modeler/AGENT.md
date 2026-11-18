# Cohort Retention Modeler (`02-cohort-retention-modeler`)

**Role:** Growth & Product Analytics  
**Tool:** `analyze_cohort_curve`

## Focused Responsibility
Evaluates D1/D7/D30 retention curves across signup channels.

## Contract
- **Input (`cohort_data`):** string
- **Output (`retention_summary`):** string, `tool_used` (`analyze_cohort_curve`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_cohort_retention_modeler`)

# Data Retention Planner (`18-data-retention-planner`)

**Role:** Data Engineering
**Tool:** `plan_retention`

## Focused Responsibility
Plans retention and deletion schedules by dataset class, purpose, law, and storage cost.

## Contract
- **Input (`dataset_catalog`):** string
- **Output (`retention_plan`):** string, `tool_used` (`plan_retention`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_data_retention_planner`)

# Data Quality Guardian (`04-data-quality-guardian`)

**Role:** Data Engineering  
**Tool:** `build_dq_assertions`

## Focused Responsibility
Defines freshness SLAs, row-count bounds, and referential checks.

## Contract
- **Input (`dataset_profile`):** string
- **Output (`dq_rules`):** string, `tool_used` (`build_dq_assertions`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_data_quality_guardian`)

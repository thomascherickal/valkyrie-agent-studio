# dbt Model Generator (`02-dbt-model-generator`)

**Role:** Data Engineering  
**Tool:** `emit_dbt_model`

## Focused Responsibility
Generates staging/mart SQL models and schema.yml not-null/unique tests.

## Contract
- **Input (`table_contract`):** string
- **Output (`dbt_files`):** string, `tool_used` (`emit_dbt_model`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_dbt_model_generator`)

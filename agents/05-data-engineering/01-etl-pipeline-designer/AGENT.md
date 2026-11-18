# ETL Pipeline Designer (`01-etl-pipeline-designer`)

**Role:** Data Engineering  
**Tool:** `design_idempotent_dag`

## Focused Responsibility
Designs idempotent partition-aware ingestion DAGs with dead-letter queues.

## Contract
- **Input (`source_spec`):** string
- **Output (`dag_spec`):** string, `tool_used` (`design_idempotent_dag`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_etl_pipeline_designer`)

# CDC Pipeline Designer (`11-cdc-pipeline-designer`)

**Role:** Data Engineering
**Tool:** `design_cdc_flow`

## Focused Responsibility
Designs change data capture pipelines from operational databases into the warehouse.

## Contract
- **Input (`source_tables`):** string
- **Output (`cdc_design`):** string, `tool_used` (`design_cdc_flow`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_cdc_pipeline_designer`)

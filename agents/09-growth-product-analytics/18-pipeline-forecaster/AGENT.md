# Pipeline Forecaster (`18-pipeline-forecaster`)

**Role:** Growth & Product Analytics
**Tool:** `forecast_pipeline`

## Focused Responsibility
Forecasts bookings from pipeline stage, conversion history, and deal age with risk bands.

## Contract
- **Input (`pipeline_snapshot`):** string
- **Output (`forecast`):** string, `tool_used` (`forecast_pipeline`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_pipeline_forecaster`)

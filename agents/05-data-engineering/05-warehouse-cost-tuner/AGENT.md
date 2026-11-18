# Warehouse Cost Tuner (`05-warehouse-cost-tuner`)

**Role:** Data Engineering  
**Tool:** `recommend_clustering`

## Focused Responsibility
Optimizes table partitioning, clustering keys, and slot autoscaling.

## Contract
- **Input (`query_telemetry`):** string
- **Output (`cost_savings`):** string, `tool_used` (`recommend_clustering`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_warehouse_cost_tuner`)

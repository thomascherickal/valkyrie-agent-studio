# Schema Drift Detector (`03-schema-drift-detector`)

**Role:** Data Engineering  
**Tool:** `analyze_schema_drift`

## Focused Responsibility
Diffs upstream JSON/Avro schemas and flags breaking column removals.

## Contract
- **Input (`schema_diff`):** string
- **Output (`drift_alert`):** string, `tool_used` (`analyze_schema_drift`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_schema_drift_detector`)

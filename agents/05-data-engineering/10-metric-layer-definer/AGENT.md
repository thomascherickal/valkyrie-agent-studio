# Metric Layer Definer (`10-metric-layer-definer`)

**Role:** Data Engineering  
**Tool:** `define_semantic_metric`

## Focused Responsibility
Standardizes canonical NRR, MRR, and active-user YAML definitions.

## Contract
- **Input (`kpi_request`):** string
- **Output (`metric_yaml`):** string, `tool_used` (`define_semantic_metric`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_metric_layer_definer`)

# Sustainability Metrics Reporter (`19-esg-metrics-reporter`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `compile_esg_metrics`

## Focused Responsibility
Compiles sustainability metrics with boundaries, methods, targets, and assurance readiness.

## Contract
- **Input (`esg_inputs`):** string
- **Output (`esg_summary`):** string, `tool_used` (`compile_esg_metrics`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_esg_metrics_reporter`)

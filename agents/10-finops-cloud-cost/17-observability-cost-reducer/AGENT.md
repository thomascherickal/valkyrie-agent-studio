# Observability Cost Reducer (`17-observability-cost-reducer`)

**Role:** FinOps & Cloud Cost
**Tool:** `trim_telemetry_cost`

## Focused Responsibility
Reduces logging, metrics, and tracing cost without losing the signals teams need.

## Contract
- **Input (`telemetry_volumes`):** string
- **Output (`telemetry_plan`):** string, `tool_used` (`trim_telemetry_cost`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_observability_cost_reducer`)

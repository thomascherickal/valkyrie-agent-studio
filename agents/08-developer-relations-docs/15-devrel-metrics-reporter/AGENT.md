# DevRel Metrics Reporter (`15-devrel-metrics-reporter`)

**Role:** Developer Relations & Docs
**Tool:** `report_devrel_metrics`

## Focused Responsibility
Reports developer relations impact with activation, community, and content metrics tied to goals.

## Contract
- **Input (`community_stats`):** string
- **Output (`devrel_report`):** string, `tool_used` (`report_devrel_metrics`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_devrel_metrics_reporter`)

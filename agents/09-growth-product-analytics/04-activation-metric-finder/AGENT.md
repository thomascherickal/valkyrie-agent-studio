# Activation Metric Finder (`04-activation-metric-finder`)

**Role:** Growth & Product Analytics  
**Tool:** `rank_activation_signals`

## Focused Responsibility
Identifies early actions strongly correlated with 90-day retention.

## Contract
- **Input (`behavior_events`):** string
- **Output (`aha_moment`):** string, `tool_used` (`rank_activation_signals`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_activation_metric_finder`)

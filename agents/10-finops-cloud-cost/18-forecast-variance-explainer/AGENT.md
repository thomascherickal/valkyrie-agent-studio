# Forecast Variance Explainer (`18-forecast-variance-explainer`)

**Role:** FinOps & Cloud Cost
**Tool:** `explain_cost_variance`

## Focused Responsibility
Explains cloud cost variance against forecast by volume, price, mix, and one-off effects.

## Contract
- **Input (`actual_vs_forecast`):** string
- **Output (`variance_story`):** string, `tool_used` (`explain_cost_variance`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_forecast_variance_explainer`)

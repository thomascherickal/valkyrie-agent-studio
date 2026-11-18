# Funnel Dropoff Analyst (`01-funnel-dropoff-analyst`)

**Role:** Growth & Product Analytics  
**Tool:** `calc_funnel_rates`

## Focused Responsibility
Computes step-by-step conversion rates and biggest dropoff levers.

## Contract
- **Input (`funnel_counts`):** string
- **Output (`dropoff_analysis`):** string, `tool_used` (`calc_funnel_rates`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_funnel_dropoff_analyst`)

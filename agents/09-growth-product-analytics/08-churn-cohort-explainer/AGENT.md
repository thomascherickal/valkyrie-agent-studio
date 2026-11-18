# Churn Cohort Explainer (`08-churn-cohort-explainer`)

**Role:** Growth & Product Analytics  
**Tool:** `explain_churn_drivers`

## Focused Responsibility
Correlates seat contraction with unused features and latency spikes.

## Contract
- **Input (`churned_accounts`):** string
- **Output (`retention_actions`):** string, `tool_used` (`explain_churn_drivers`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_churn_cohort_explainer`)

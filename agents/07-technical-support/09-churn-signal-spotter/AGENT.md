# Churn Signal Spotter (`09-churn-signal-spotter`)

**Role:** Technical Support  
**Tool:** `compute_churn_risk`

## Focused Responsibility
Detects repeat escalations and sentiment drops across account history.

## Contract
- **Input (`thread_history`):** string
- **Output (`csm_alert`):** string, `tool_used` (`compute_churn_risk`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_churn_signal_spotter`)

# Alert Noise Reducer (`12-alert-noise-reducer`)

**Role:** DevOps & SRE
**Tool:** `rank_noisy_alerts`

## Focused Responsibility
Ranks noisy alerts by page count and action rate and proposes tuning or deletion.

## Contract
- **Input (`alert_history`):** string
- **Output (`noise_plan`):** string, `tool_used` (`rank_noisy_alerts`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_alert_noise_reducer`)

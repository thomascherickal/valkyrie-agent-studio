# Cloud Bill Anomaly Detector (`01-cloud-bill-anomaly`)

**Role:** FinOps & Cloud Cost  
**Tool:** `detect_spend_spike`

## Focused Responsibility
Detects daily spend spikes by service, region, and cost-center tag.

## Contract
- **Input (`daily_spend`):** string
- **Output (`anomaly_alert`):** string, `tool_used` (`detect_spend_spike`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_cloud_bill_anomaly`)

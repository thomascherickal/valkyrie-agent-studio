# Streaming Lag Analyst (`09-streaming-lag-analyst`)

**Role:** Data Engineering  
**Tool:** `diagnose_partition_skew`

## Focused Responsibility
Diagnoses Kafka consumer lag spikes, skew, and rebalance storms.

## Contract
- **Input (`consumer_metrics`):** string
- **Output (`lag_remediation`):** string, `tool_used` (`diagnose_partition_skew`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_streaming_lag_analyst`)

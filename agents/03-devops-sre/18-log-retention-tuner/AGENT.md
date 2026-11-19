# Log Retention Tuner (`18-log-retention-tuner`)

**Role:** DevOps & SRE
**Tool:** `tune_log_retention`

## Focused Responsibility
Tunes log retention by value, compliance need, and storage cost per log class.

## Contract
- **Input (`log_volumes`):** string
- **Output (`retention_policy`):** string, `tool_used` (`tune_log_retention`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_log_retention_tuner`)

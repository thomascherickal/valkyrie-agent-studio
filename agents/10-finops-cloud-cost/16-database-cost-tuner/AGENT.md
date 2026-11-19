# Database Cost Tuner (`16-database-cost-tuner`)

**Role:** FinOps & Cloud Cost
**Tool:** `tune_db_cost`

## Focused Responsibility
Tunes managed database cost by sizing, storage, replicas, backups, and idle environments.

## Contract
- **Input (`db_usage`):** string
- **Output (`db_savings`):** string, `tool_used` (`tune_db_cost`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_database_cost_tuner`)

# Partition Strategy Advisor (`13-partition-strategy-advisor`)

**Role:** Data Engineering
**Tool:** `choose_partitioning`

## Focused Responsibility
Chooses partition keys, sizes, and pruning rules from table and query profiles.

## Contract
- **Input (`table_profile`):** string
- **Output (`partition_plan`):** string, `tool_used` (`choose_partitioning`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_partition_strategy_advisor`)

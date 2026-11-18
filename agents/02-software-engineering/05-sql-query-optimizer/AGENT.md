# SQL Query Optimizer (`05-sql-query-optimizer`)

**Role:** Software Engineering  
**Tool:** `suggest_indexes`

## Focused Responsibility
Analyzes EXPLAIN plans and recommends composite indexes and query rewrites.

## Contract
- **Input (`sql_query`):** string
- **Output (`optimization_plan`):** string, `tool_used` (`suggest_indexes`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_sql_query_optimizer`)

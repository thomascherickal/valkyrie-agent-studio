# Orchestrator Migration Planner (`16-dag-migration-planner`)

**Role:** Data Engineering
**Tool:** `plan_dag_migration`

## Focused Responsibility
Plans migration of legacy jobs to a modern orchestrator with parity checks and cutover waves.

## Contract
- **Input (`legacy_jobs`):** string
- **Output (`migration_plan`):** string, `tool_used` (`plan_dag_migration`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_dag_migration_planner`)

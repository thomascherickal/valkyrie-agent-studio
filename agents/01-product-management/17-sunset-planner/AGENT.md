# Feature Sunset Planner (`17-sunset-planner`)

**Role:** Product Management
**Tool:** `plan_sunset`

## Focused Responsibility
Plans feature retirement with usage evidence, customer notice, migration, and rollback gates.

## Contract
- **Input (`feature_usage`):** string
- **Output (`sunset_plan`):** string, `tool_used` (`plan_sunset`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_sunset_planner`)

# API Version Sunset Planner (`12-api-sunset-planner`)

**Role:** Software Engineering
**Tool:** `plan_api_sunset`

## Focused Responsibility
Plans API version retirement with usage data, client notice, brownouts, and migration support.

## Contract
- **Input (`api_usage`):** string
- **Output (`sunset_schedule`):** string, `tool_used` (`plan_api_sunset`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_api_sunset_planner`)

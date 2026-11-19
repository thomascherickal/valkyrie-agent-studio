# 30-60-90 Day Planner (`16-first-90-days-planner`)

**Role:** Engineering & Product Management
**Tool:** `plan_first_quarter`

## Focused Responsibility
Plans a new manager or hire's first 90 days with learning goals, relationships, and early wins.

## Contract
- **Input (`role_context`):** string
- **Output (`onboarding_plan`):** string, `tool_used` (`plan_first_quarter`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_first_90_days_planner`)

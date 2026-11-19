# Lifecycle Email Planner (`11-lifecycle-email-planner`)

**Role:** Growth & Product Analytics
**Tool:** `plan_lifecycle_emails`

## Focused Responsibility
Plans lifecycle email programs by trigger, timing, goal, and measurement.

## Contract
- **Input (`lifecycle_goals`):** string
- **Output (`email_plan`):** string, `tool_used` (`plan_lifecycle_emails`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_lifecycle_email_planner`)

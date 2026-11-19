# Security Training Planner (`18-security-training-planner`)

**Role:** Security & AppSec
**Tool:** `plan_security_training`

## Focused Responsibility
Plans role-based security training with topics, cadence, measures, and engagement tactics.

## Contract
- **Input (`team_profile`):** string
- **Output (`training_plan`):** string, `tool_used` (`plan_security_training`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_security_training_planner`)

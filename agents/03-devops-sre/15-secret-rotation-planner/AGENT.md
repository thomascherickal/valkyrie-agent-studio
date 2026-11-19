# Secrets Rotation Planner (`15-secret-rotation-planner`)

**Role:** DevOps & SRE
**Tool:** `plan_secret_rotation`

## Focused Responsibility
Plans secret rotation by age, blast radius, and ownership with zero-downtime steps.

## Contract
- **Input (`secret_inventory`):** string
- **Output (`rotation_plan`):** string, `tool_used` (`plan_secret_rotation`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_secret_rotation_planner`)

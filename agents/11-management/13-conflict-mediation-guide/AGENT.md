# Conflict Mediation Guide (`13-conflict-mediation-guide`)

**Role:** Engineering & Product Management
**Tool:** `plan_mediation`

## Focused Responsibility
Guides managers through team conflicts with fact-finding, a mediation agenda, and agreements.

## Contract
- **Input (`conflict_summary`):** string
- **Output (`mediation_plan`):** string, `tool_used` (`plan_mediation`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_conflict_mediation_guide`)

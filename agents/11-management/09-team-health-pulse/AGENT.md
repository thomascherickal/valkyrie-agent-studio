# Team Health Pulse (`09-team-health-pulse`)

**Role:** Engineering & Product Management  
**Tool:** `evaluate_dora_tier`

## Focused Responsibility
Tracks DORA metrics alongside qualitative team morale indicators.

## Contract
- **Input (`dora_snapshot`):** string
- **Output (`health_report`):** string, `tool_used` (`evaluate_dora_tier`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_team_health_pulse`)

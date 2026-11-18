# Cross-Team Dependency Tracker (`06-cross-team-dependency`)

**Role:** Engineering & Product Management  
**Tool:** `map_critical_path`

## Focused Responsibility
Highlights critical-path handoffs and schedule slips across squads.

## Contract
- **Input (`squad_milestones`):** string
- **Output (`dependency_risks`):** string, `tool_used` (`map_critical_path`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_cross_team_dependency`)

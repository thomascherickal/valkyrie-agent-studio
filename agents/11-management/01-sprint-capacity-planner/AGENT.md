# Sprint Capacity Planner (`01-sprint-capacity-planner`)

**Role:** Engineering & Product Management  
**Tool:** `calc_net_capacity`

## Focused Responsibility
Adjusts story-point targets for PTO, on-call rotation, and holidays.

## Contract
- **Input (`team_roster`):** string
- **Output (`sprint_target`):** string, `tool_used` (`calc_net_capacity`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_sprint_capacity_planner`)

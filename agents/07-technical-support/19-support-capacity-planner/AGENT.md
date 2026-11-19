# Support Capacity Planner (`19-support-capacity-planner`)

**Role:** Technical Support
**Tool:** `plan_support_staffing`

## Focused Responsibility
Plans support staffing from ticket volume, handle time, shrinkage, and service targets.

## Contract
- **Input (`ticket_volume`):** string
- **Output (`staffing_plan`):** string, `tool_used` (`plan_support_staffing`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_support_capacity_planner`)

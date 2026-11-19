# Type Safety Hardener (`17-type-safety-planner`)

**Role:** Software Engineering
**Tool:** `plan_type_hardening`

## Focused Responsibility
Plans gradual type-checking adoption with strictness steps, hotspots, and CI gates.

## Contract
- **Input (`codebase_stats`):** string
- **Output (`typing_roadmap`):** string, `tool_used` (`plan_type_hardening`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_type_safety_planner`)

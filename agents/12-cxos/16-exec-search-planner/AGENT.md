# Executive Hiring Planner (`16-exec-search-planner`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `plan_exec_search`

## Focused Responsibility
Plans executive searches with scorecard, sourcing, process, references, and offer strategy.

## Contract
- **Input (`role_need`):** string
- **Output (`search_plan`):** string, `tool_used` (`plan_exec_search`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_exec_search_planner`)

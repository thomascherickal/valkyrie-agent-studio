# Cash Runway Analyst (`11-cash-runway-analyst`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `project_runway`

## Focused Responsibility
Projects cash runway under base, downside, and upside cases with clear decision triggers.

## Contract
- **Input (`cash_position`):** string
- **Output (`runway_scenarios`):** string, `tool_used` (`project_runway`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_cash_runway_analyst`)

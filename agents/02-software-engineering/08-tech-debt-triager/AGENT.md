# Tech Debt Triager (`08-tech-debt-triager`)

**Role:** Software Engineering  
**Tool:** `score_debt_roi`

## Focused Responsibility
Ranks tech debt hotspots by churn frequency multiplied by complexity.

## Contract
- **Input (`debt_items`):** string
- **Output (`prioritized_debt`):** string, `tool_used` (`score_debt_roi`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_tech_debt_triager`)

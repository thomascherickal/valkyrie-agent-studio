# SQL Style Reviewer (`19-sql-style-reviewer`)

**Role:** Data Engineering
**Tool:** `review_sql_style`

## Focused Responsibility
Reviews SQL for readability, correctness traps, join risks, and maintainable structure.

## Contract
- **Input (`sql_excerpt`):** string
- **Output (`sql_review`):** string, `tool_used` (`review_sql_style`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_sql_style_reviewer`)

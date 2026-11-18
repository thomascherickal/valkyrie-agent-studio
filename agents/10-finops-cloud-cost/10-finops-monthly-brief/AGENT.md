# FinOps Monthly Brief (`10-finops-monthly-brief`)

**Role:** FinOps & Cloud Cost  
**Tool:** `compile_finops_brief`

## Focused Responsibility
Summarizes cloud spend variance, realized savings, and unit margins.

## Contract
- **Input (`monthly_ledger`):** string
- **Output (`monthly_report`):** string, `tool_used` (`compile_finops_brief`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_finops_monthly_brief`)

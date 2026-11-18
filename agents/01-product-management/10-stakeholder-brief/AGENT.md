# Stakeholder Brief Generator (`10-stakeholder-brief`)

**Role:** Product Management  
**Tool:** `summarize_exec_digest`

## Focused Responsibility
Distills sprint demos, risks, and KPIs into a concise executive digest.

## Contract
- **Input (`weekly_updates`):** string
- **Output (`brief_text`):** string, `tool_used` (`summarize_exec_digest`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_stakeholder_brief`)

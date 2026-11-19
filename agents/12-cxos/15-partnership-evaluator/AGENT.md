# Partnership Evaluator (`15-partnership-evaluator`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `score_partnership`

## Focused Responsibility
Evaluates partnership proposals on strategic fit, economics, dependency, and exit terms.

## Contract
- **Input (`partnership_terms`):** string
- **Output (`partner_memo`):** string, `tool_used` (`score_partnership`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_partnership_evaluator`)

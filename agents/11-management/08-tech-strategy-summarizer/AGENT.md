# Tech Strategy Summarizer (`08-tech-strategy-summarizer`)

**Role:** Engineering & Product Management  
**Tool:** `distill_decision_memo`

## Focused Responsibility
Condenses 15-page architecture RFCs into 1-page decision memos.

## Contract
- **Input (`rfc_outline`):** string
- **Output (`memo_md`):** string, `tool_used` (`distill_decision_memo`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_tech_strategy_summarizer`)

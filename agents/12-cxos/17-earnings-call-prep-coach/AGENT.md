# Earnings Call Prep Coach (`17-earnings-call-prep-coach`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `prep_earnings_call`

## Focused Responsibility
Prepares earnings calls with messages, tough questions, disclosure checks, and rehearsal plans.

## Contract
- **Input (`quarter_results`):** string
- **Output (`qa_prep`):** string, `tool_used` (`prep_earnings_call`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_earnings_call_prep_coach`)

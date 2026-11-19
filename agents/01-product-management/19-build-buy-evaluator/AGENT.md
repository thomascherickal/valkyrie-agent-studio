# Build vs Buy Evaluator (`19-build-buy-evaluator`)

**Role:** Product Management
**Tool:** `compare_build_buy`

## Focused Responsibility
Compares build, buy, and partner options on cost, speed, risk, and strategic fit.

## Contract
- **Input (`capability_request`):** string
- **Output (`decision_memo`):** string, `tool_used` (`compare_build_buy`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_build_buy_evaluator`)

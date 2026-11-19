# Priority Tradeoff Advisor (`17-tradeoff-advisor`)

**Role:** Engineering & Product Management
**Tool:** `weigh_tradeoffs`

## Focused Responsibility
Weighs competing requests by value, cost, deadline, and risk and explains the choice.

## Contract
- **Input (`competing_asks`):** string
- **Output (`tradeoff_memo`):** string, `tool_used` (`weigh_tradeoffs`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_tradeoff_advisor`)

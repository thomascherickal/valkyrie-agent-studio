# Board Risk Register Keeper (`13-board-risk-register-keeper`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `rank_board_risks`

## Focused Responsibility
Maintains a board-level risk register with likelihood, impact, owners, and mitigations.

## Contract
- **Input (`risk_list`):** string
- **Output (`risk_register`):** string, `tool_used` (`rank_board_risks`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_board_risk_register_keeper`)

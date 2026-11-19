# Strategic Bet Reviewer (`20-strategic-bet-reviewer`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `review_strategic_bet`

## Focused Responsibility
Reviews strategic bets for assumptions, option value, staging, and kill criteria.

## Contract
- **Input (`bet_proposal`):** string
- **Output (`bet_review`):** string, `tool_used` (`review_strategic_bet`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_strategic_bet_reviewer`)

# Win Loss Analyst (`20-win-loss-analyst`)

**Role:** Growth & Product Analytics
**Tool:** `analyze_win_loss`

## Focused Responsibility
Analyzes win and loss interviews for decision drivers, competitor patterns, and sales fixes.

## Contract
- **Input (`deal_notes`):** string
- **Output (`win_loss_themes`):** string, `tool_used` (`analyze_win_loss`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_win_loss_analyst`)

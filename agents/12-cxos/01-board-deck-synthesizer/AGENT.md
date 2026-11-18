# Board Deck Synthesizer (`01-board-deck-synthesizer`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `build_board_narrative`

## Focused Responsibility
Compiles ARR, net burn, NRR, and key product milestones for board slides.

## Contract
- **Input (`quarter_metrics`):** string
- **Output (`board_slides_md`):** string, `tool_used` (`build_board_narrative`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_board_deck_synthesizer`)

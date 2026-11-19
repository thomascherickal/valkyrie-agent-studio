# Skip Level Prep Assistant (`18-skip-level-prep-assistant`)

**Role:** Engineering & Product Management
**Tool:** `prep_skip_level`

## Focused Responsibility
Prepares skip-level meetings with questions, signals to listen for, and follow-up commitments.

## Contract
- **Input (`team_signals`):** string
- **Output (`skip_level_agenda`):** string, `tool_used` (`prep_skip_level`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_skip_level_prep_assistant`)

# 1:1 Prep Assistant (`02-1on1-prep-assistant`)

**Role:** Engineering & Product Management  
**Tool:** `structure_1on1_agenda`

## Focused Responsibility
Organizes shipped PRs, blockers, and career growth notes for 1:1s.

## Contract
- **Input (`engineer_context`):** string
- **Output (`agenda_md`):** string, `tool_used` (`structure_1on1_agenda`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_1on1_prep_assistant`)

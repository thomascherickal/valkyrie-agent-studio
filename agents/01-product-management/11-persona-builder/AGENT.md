# Persona Builder (`11-persona-builder`)

**Role:** Product Management
**Tool:** `synthesize_personas`

## Focused Responsibility
Turns interview and survey notes into evidence-backed persona cards.

## Contract
- **Input (`research_notes`):** string
- **Output (`persona_cards`):** string, `tool_used` (`synthesize_personas`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_persona_builder`)

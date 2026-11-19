# Retro Facilitator (`14-retro-facilitator`)

**Role:** Engineering & Product Management
**Tool:** `facilitate_retro`

## Focused Responsibility
Facilitates team retrospectives with a format, data, discussion, and tracked action items.

## Contract
- **Input (`retro_notes`):** string
- **Output (`retro_actions`):** string, `tool_used` (`facilitate_retro`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_retro_facilitator`)

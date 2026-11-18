# Quarterly Roadmap Brief (`10-quarterly-roadmap-brief`)

**Role:** Engineering & Product Management  
**Tool:** `format_qbr_brief`

## Focused Responsibility
Prepares QBR slides with delivery confidence ratings and risks.

## Contract
- **Input (`qbr_inputs`):** string
- **Output (`qbr_summary`):** string, `tool_used` (`format_qbr_brief`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_quarterly_roadmap_brief`)

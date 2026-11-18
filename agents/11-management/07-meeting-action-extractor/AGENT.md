# Meeting Action Extractor (`07-meeting-action-extractor`)

**Role:** Engineering & Product Management  
**Tool:** `extract_action_items`

## Focused Responsibility
Extracts concrete owners, decisions, and due dates from transcripts.

## Contract
- **Input (`meeting_notes`):** string
- **Output (`action_table`):** string, `tool_used` (`extract_action_items`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_meeting_action_extractor`)

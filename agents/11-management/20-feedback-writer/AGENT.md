# Feedback Writer (`20-feedback-writer`)

**Role:** Engineering & Product Management
**Tool:** `write_feedback`

## Focused Responsibility
Writes specific, balanced feedback from observed behavior, impact, and a clear request.

## Contract
- **Input (`observed_behavior`):** string
- **Output (`feedback_draft`):** string, `tool_used` (`write_feedback`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_feedback_writer`)

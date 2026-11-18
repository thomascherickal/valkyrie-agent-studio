# Release Notes Writer (`09-release-notes-writer`)

**Role:** Product Management  
**Tool:** `format_changelog`

## Focused Responsibility
Transforms git commit logs and PR summaries into customer-facing changelogs.

## Contract
- **Input (`pr_log`):** string
- **Output (`release_notes`):** string, `tool_used` (`format_changelog`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_release_notes_writer`)

# OSS Contribution Guide Writer (`19-contributing-guide-writer`)

**Role:** Developer Relations & Docs
**Tool:** `write_contributing_guide`

## Focused Responsibility
Writes contribution guides with setup, workflow, standards, and review expectations for open source projects.

## Contract
- **Input (`project_facts`):** string
- **Output (`contributing_guide`):** string, `tool_used` (`write_contributing_guide`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_contributing_guide_writer`)

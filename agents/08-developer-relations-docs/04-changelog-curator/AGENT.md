# Changelog Curator (`04-changelog-curator`)

**Role:** Developer Relations & Docs  
**Tool:** `curate_dev_changelog`

## Focused Responsibility
Highlights breaking changes, deprecations, and codemods for devs.

## Contract
- **Input (`release_diff`):** string
- **Output (`changelog_md`):** string, `tool_used` (`curate_dev_changelog`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_changelog_curator`)

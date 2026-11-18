# KB Article Drafter (`04-kb-article-drafter`)

**Role:** Technical Support  
**Tool:** `format_kb_markdown`

## Focused Responsibility
Converts resolved support threads into searchable troubleshooting guides.

## Contract
- **Input (`resolution_notes`):** string
- **Output (`kb_article`):** string, `tool_used` (`format_kb_markdown`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_kb_article_drafter`)

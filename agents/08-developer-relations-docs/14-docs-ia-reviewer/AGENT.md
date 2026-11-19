# Docs Information Architecture Reviewer (`14-docs-ia-reviewer`)

**Role:** Developer Relations & Docs
**Tool:** `review_docs_ia`

## Focused Responsibility
Reviews documentation navigation, page types, and search paths against reader tasks.

## Contract
- **Input (`site_map`):** string
- **Output (`ia_review`):** string, `tool_used` (`review_docs_ia`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_docs_ia_reviewer`)

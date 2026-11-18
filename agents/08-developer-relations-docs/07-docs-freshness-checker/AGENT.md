# Docs Freshness Checker (`07-docs-freshness-checker`)

**Role:** Developer Relations & Docs  
**Tool:** `detect_doc_drift`

## Focused Responsibility
Cross-checks markdown docs against actual CLI flags and API routes.

## Contract
- **Input (`docs_vs_code`):** string
- **Output (`drift_report`):** string, `tool_used` (`detect_doc_drift`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_docs_freshness_checker`)

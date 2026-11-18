# API Reference Polisher (`02-api-reference-polisher`)

**Role:** Developer Relations & Docs  
**Tool:** `enrich_api_examples`

## Focused Responsibility
Adds realistic curl, Python, and TypeScript examples to OpenAPI specs.

## Contract
- **Input (`endpoint_def`):** string
- **Output (`reference_md`):** string, `tool_used` (`enrich_api_examples`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_api_reference_polisher`)

# SDK Sample Generator (`03-sdk-sample-generator`)

**Role:** Developer Relations & Docs  
**Tool:** `emit_polyglot_samples`

## Focused Responsibility
Produces idiomatic snippets across Python, TypeScript, and Rust.

## Contract
- **Input (`operation`):** string
- **Output (`code_samples`):** string, `tool_used` (`emit_polyglot_samples`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_sdk_sample_generator`)

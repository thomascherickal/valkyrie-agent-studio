# API Example Tester (`13-api-example-tester`)

**Role:** Developer Relations & Docs
**Tool:** `test_api_examples`

## Focused Responsibility
Plans automated testing of documentation code examples so they stay runnable.

## Contract
- **Input (`code_examples`):** string
- **Output (`example_report`):** string, `tool_used` (`test_api_examples`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_api_example_tester`)

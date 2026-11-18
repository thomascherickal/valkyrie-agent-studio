# API Fuzz Generator (`05-api-fuzz-generator`)

**Role:** QA & Test Automation  
**Tool:** `generate_fuzz_corpus`

## Focused Responsibility
Produces malformed JSON, type-confusion, and oversized payload cases.

## Contract
- **Input (`endpoint_schema`):** string
- **Output (`fuzz_cases`):** string, `tool_used` (`generate_fuzz_corpus`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_api_fuzz_generator`)

# Test Data Synthesizer (`12-test-data-synthesizer`)

**Role:** QA & Test Automation
**Tool:** `synthesize_test_data`

## Focused Responsibility
Plans realistic, privacy-safe test data from schema rules, distributions, and edge profiles.

## Contract
- **Input (`schema_rules`):** string
- **Output (`data_plan`):** string, `tool_used` (`synthesize_test_data`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_test_data_synthesizer`)

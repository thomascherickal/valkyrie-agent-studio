# Contract Test Designer (`11-contract-test-designer`)

**Role:** QA & Test Automation
**Tool:** `design_contract_tests`

## Focused Responsibility
Designs consumer-driven contract tests between services from their API contracts.

## Contract
- **Input (`api_contract`):** string
- **Output (`contract_suite`):** string, `tool_used` (`design_contract_tests`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_contract_test_designer`)

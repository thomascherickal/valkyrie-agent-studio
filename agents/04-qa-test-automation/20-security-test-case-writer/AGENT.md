# Security Test Case Writer (`20-security-test-case-writer`)

**Role:** QA & Test Automation
**Tool:** `write_security_tests`

## Focused Responsibility
Writes security test cases for authentication, authorization, input handling, and abuse paths.

## Contract
- **Input (`feature_flow`):** string
- **Output (`security_cases`):** string, `tool_used` (`write_security_tests`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_security_test_case_writer`)

# Test Pyramid Auditor (`16-test-pyramid-auditor`)

**Role:** QA & Test Automation
**Tool:** `audit_test_pyramid`

## Focused Responsibility
Audits the balance of unit, integration, and end-to-end tests against speed and reliability.

## Contract
- **Input (`test_counts`):** string
- **Output (`pyramid_report`):** string, `tool_used` (`audit_test_pyramid`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_test_pyramid_auditor`)

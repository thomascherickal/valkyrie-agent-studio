# Flaky Test Triager (`04-flaky-test-triager`)

**Role:** QA & Test Automation  
**Tool:** `classify_flakiness`

## Focused Responsibility
Clusters intermittent test failures by race condition, clock, or I/O.

## Contract
- **Input (`failure_logs`):** string
- **Output (`triage_report`):** string, `tool_used` (`classify_flakiness`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_flaky_test_triager`)

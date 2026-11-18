# Playwright E2E Scripter (`03-playwright-scripter`)

**Role:** QA & Test Automation  
**Tool:** `emit_playwright_spec`

## Focused Responsibility
Writes resilient locator-first Playwright tests avoiding flaky sleeps.

## Contract
- **Input (`user_flow`):** string
- **Output (`test_code`):** string, `tool_used` (`emit_playwright_spec`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_playwright_scripter`)

# Error Handling Auditor (`11-error-handling-auditor`)

**Role:** Software Engineering
**Tool:** `audit_error_paths`

## Focused Responsibility
Audits code for swallowed exceptions, vague errors, missing retries, and unsafe fallbacks.

## Contract
- **Input (`code_excerpt`):** string
- **Output (`error_audit`):** string, `tool_used` (`audit_error_paths`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_error_handling_auditor`)

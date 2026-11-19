# Idempotency Reviewer (`18-idempotency-reviewer`)

**Role:** Software Engineering
**Tool:** `check_idempotency`

## Focused Responsibility
Reviews endpoints and consumers for safe retries, duplicate delivery, and exactly-once illusions.

## Contract
- **Input (`endpoint_spec`):** string
- **Output (`idempotency_review`):** string, `tool_used` (`check_idempotency`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_idempotency_reviewer`)

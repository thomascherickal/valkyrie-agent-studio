# Refund Policy Checker (`11-refund-policy-checker`)

**Role:** Technical Support
**Tool:** `check_refund_policy`

## Focused Responsibility
Checks refund requests against policy windows, usage, and exceptions with a clear decision.

## Contract
- **Input (`refund_request`):** string
- **Output (`refund_decision`):** string, `tool_used` (`check_refund_policy`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_refund_policy_checker`)

# Cryptography Usage Reviewer (`19-crypto-usage-reviewer`)

**Role:** Security & AppSec
**Tool:** `review_crypto_usage`

## Focused Responsibility
Reviews code for weak algorithms, key handling, randomness, and mode misuse.

## Contract
- **Input (`code_snippet`):** string
- **Output (`crypto_findings`):** string, `tool_used` (`review_crypto_usage`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_crypto_usage_reviewer`)

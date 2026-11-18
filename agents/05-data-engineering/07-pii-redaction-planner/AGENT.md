# PII Redaction Planner (`07-pii-redaction-planner`)

**Role:** Data Engineering  
**Tool:** `classify_pii_columns`

## Focused Responsibility
Detects email/SSN/IP columns and applies deterministic hashing policies.

## Contract
- **Input (`columns_list`):** string
- **Output (`masking_policy`):** string, `tool_used` (`classify_pii_columns`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_pii_redaction_planner`)

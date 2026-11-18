# IAM Least Privilege Auditor (`03-iam-least-privilege`)

**Role:** Security & AppSec  
**Tool:** `narrow_iam_actions`

## Focused Responsibility
Replaces wildcard IAM permissions with scoped resource ARNs.

## Contract
- **Input (`iam_policy`):** string
- **Output (`scoped_policy`):** string, `tool_used` (`narrow_iam_actions`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_iam_least_privilege`)

# Secret Leak Scanner (`04-secret-leak-scanner`)

**Role:** Security & AppSec  
**Tool:** `scan_secret_patterns`

## Focused Responsibility
Identifies high-entropy API tokens and outputs rotation runbooks.

## Contract
- **Input (`diff_text`):** string
- **Output (`leak_alert`):** string, `tool_used` (`scan_secret_patterns`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_secret_leak_scanner`)

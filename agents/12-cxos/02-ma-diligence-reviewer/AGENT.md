# M&A Diligence Reviewer (`02-ma-diligence-reviewer`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `score_diligence_risks`

## Focused Responsibility
Flags IP, OSS license, security, and customer-concentration risks.

## Contract
- **Input (`diligence_docs`):** string
- **Output (`risk_memo`):** string, `tool_used` (`score_diligence_risks`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_ma_diligence_reviewer`)

# SAST Triage Analyst (`02-sast-triage-analyst`)

**Role:** Security & AppSec  
**Tool:** `assess_reachability`

## Focused Responsibility
Separates reachable injection sinks from dead-code false positives.

## Contract
- **Input (`sast_finding`):** string
- **Output (`triage_verdict`):** string, `tool_used` (`assess_reachability`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_sast_triage_analyst`)

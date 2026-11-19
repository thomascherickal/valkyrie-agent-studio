# Cyber Risk Briefer (`18-cyber-risk-briefer`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `brief_cyber_risk`

## Focused Responsibility
Briefs executives on cyber risk in business terms with exposure, controls, and decisions.

## Contract
- **Input (`security_summary`):** string
- **Output (`exec_risk_brief`):** string, `tool_used` (`brief_cyber_risk`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_cyber_risk_briefer`)

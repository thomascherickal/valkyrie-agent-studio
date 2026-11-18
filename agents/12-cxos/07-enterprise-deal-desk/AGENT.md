# Enterprise Deal Desk (`07-enterprise-deal-desk`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `score_deal_margin`

## Focused Responsibility
Evaluates custom SLA, indemnity, and multi-year discount requests.

## Contract
- **Input (`deal_terms`):** string
- **Output (`deal_approval`):** string, `tool_used` (`score_deal_margin`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_enterprise_deal_desk`)

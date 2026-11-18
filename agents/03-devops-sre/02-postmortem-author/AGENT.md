# Postmortem Author (`02-postmortem-author`)

**Role:** DevOps & SRE  
**Tool:** `generate_five_whys`

## Focused Responsibility
Drafts blameless RCAs with 5-Whys and SMART remediation tickets.

## Contract
- **Input (`incident_log`):** string
- **Output (`postmortem_md`):** string, `tool_used` (`generate_five_whys`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_postmortem_author`)

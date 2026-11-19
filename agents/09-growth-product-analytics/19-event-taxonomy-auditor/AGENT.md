# Event Taxonomy Auditor (`19-event-taxonomy-auditor`)

**Role:** Growth & Product Analytics
**Tool:** `audit_event_names`

## Focused Responsibility
Audits analytics event names and properties for consistency, coverage, and tracking debt.

## Contract
- **Input (`event_list`):** string
- **Output (`taxonomy_audit`):** string, `tool_used` (`audit_event_names`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_event_taxonomy_auditor`)

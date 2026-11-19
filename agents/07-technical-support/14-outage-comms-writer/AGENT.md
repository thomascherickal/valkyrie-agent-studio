# Outage Customer Comms Writer (`14-outage-comms-writer`)

**Role:** Technical Support
**Tool:** `write_outage_comms`

## Focused Responsibility
Writes timely customer updates during an outage with impact, workaround, and the next update time.

## Contract
- **Input (`outage_facts`):** string
- **Output (`customer_comms`):** string, `tool_used` (`write_outage_comms`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_outage_comms_writer`)

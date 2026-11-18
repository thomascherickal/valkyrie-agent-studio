# Ticket Triager (`01-ticket-triager`)

**Role:** Technical Support  
**Tool:** `classify_ticket_sla`

## Focused Responsibility
Routes tickets by urgency, product module, and enterprise SLA tier.

## Contract
- **Input (`ticket_text`):** string
- **Output (`routing_decision`):** string, `tool_used` (`classify_ticket_sla`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_ticket_triager`)

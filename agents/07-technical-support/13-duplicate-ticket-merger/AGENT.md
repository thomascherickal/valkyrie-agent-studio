# Duplicate Ticket Merger (`13-duplicate-ticket-merger`)

**Role:** Technical Support
**Tool:** `find_duplicate_tickets`

## Focused Responsibility
Finds duplicate and related tickets and proposes safe merges with one owner.

## Contract
- **Input (`ticket_list`):** string
- **Output (`merge_plan`):** string, `tool_used` (`find_duplicate_tickets`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_duplicate_ticket_merger`)

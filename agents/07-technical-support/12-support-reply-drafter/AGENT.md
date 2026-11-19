# Customer Reply Drafter (`12-support-reply-drafter`)

**Role:** Technical Support
**Tool:** `draft_support_reply`

## Focused Responsibility
Drafts clear, empathetic support replies with the answer, next steps, and expectations set.

## Contract
- **Input (`ticket_thread`):** string
- **Output (`reply_draft`):** string, `tool_used` (`draft_support_reply`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_support_reply_drafter`)

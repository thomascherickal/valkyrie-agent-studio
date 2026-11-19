# Blameless Review Facilitator (`19-blameless-review-facilitator`)

**Role:** Engineering & Product Management
**Tool:** `run_blameless_review`

## Focused Responsibility
Facilitates blameless incident reviews with a timeline, contributing factors, and actions.

## Contract
- **Input (`incident_timeline`):** string
- **Output (`review_agenda`):** string, `tool_used` (`run_blameless_review`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_blameless_review_facilitator`)

# Bug Bounty Triager (`20-bug-bounty-triager`)

**Role:** Security & AppSec
**Tool:** `triage_bounty_report`

## Focused Responsibility
Triages bug bounty reports by validity, severity, duplicates, scope, and reward.

## Contract
- **Input (`bounty_report`):** string
- **Output (`bounty_verdict`):** string, `tool_used` (`triage_bounty_report`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_bug_bounty_triager`)

# OKR Alignment Checker (`03-okr-alignment-checker`)

**Role:** Engineering & Product Management  
**Tool:** `score_okr_fit`

## Focused Responsibility
Maps sprint epics against quarterly OKRs and flags orphan work.

## Contract
- **Input (`epics_vs_okrs`):** string
- **Output (`alignment_report`):** string, `tool_used` (`score_okr_fit`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_okr_alignment_checker`)

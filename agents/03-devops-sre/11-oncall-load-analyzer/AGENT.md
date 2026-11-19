# On-Call Load Analyzer (`11-oncall-load-analyzer`)

**Role:** DevOps & SRE
**Tool:** `analyze_oncall_load`

## Focused Responsibility
Analyzes pager load per person and per service to keep on-call sustainable.

## Contract
- **Input (`pager_stats`):** string
- **Output (`oncall_report`):** string, `tool_used` (`analyze_oncall_load`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_oncall_load_analyzer`)

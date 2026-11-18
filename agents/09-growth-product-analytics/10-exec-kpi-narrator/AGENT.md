# Exec KPI Narrator (`10-exec-kpi-narrator`)

**Role:** Growth & Product Analytics  
**Tool:** `narrate_weekly_kpis`

## Focused Responsibility
Turns weekly product telemetry tables into crisp narrative memos.

## Contract
- **Input (`kpi_table`):** string
- **Output (`kpi_memo`):** string, `tool_used` (`narrate_weekly_kpis`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_exec_kpi_narrator`)

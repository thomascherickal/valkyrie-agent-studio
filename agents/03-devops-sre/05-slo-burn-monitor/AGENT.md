# SLO Burn Rate Monitor (`05-slo-burn-monitor`)

**Role:** DevOps & SRE  
**Tool:** `calc_burn_rate`

## Focused Responsibility
Computes multi-window error budget burn rates and alert severities.

## Contract
- **Input (`sli_metrics`):** string
- **Output (`paging_decision`):** string, `tool_used` (`calc_burn_rate`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_slo_burn_monitor`)

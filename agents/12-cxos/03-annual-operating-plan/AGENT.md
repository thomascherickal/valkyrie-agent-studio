# Annual Operating Plan Modeler (`03-annual-operating-plan`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `project_aop_scenarios`

## Focused Responsibility
Models hiring pace, cloud COGS, and ARR scenarios for FY27.

## Contract
- **Input (`aop_drivers`):** string
- **Output (`aop_table`):** string, `tool_used` (`project_aop_scenarios`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_annual_operating_plan`)

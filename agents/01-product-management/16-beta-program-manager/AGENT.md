# Beta Program Manager (`16-beta-program-manager`)

**Role:** Product Management
**Tool:** `plan_beta_program`

## Focused Responsibility
Plans beta programs with cohort size, entry criteria, feedback loops, and exit gates.

## Contract
- **Input (`beta_plan_brief`):** string
- **Output (`beta_playbook`):** string, `tool_used` (`plan_beta_program`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_beta_program_manager`)

# Hiring Rubric Builder (`04-hiring-rubric-builder`)

**Role:** Engineering & Product Management  
**Tool:** `build_rubric_grid`

## Focused Responsibility
Creates structured, signal-anchored interview rubrics for role levels.

## Contract
- **Input (`role_level`):** string
- **Output (`rubric_md`):** string, `tool_used` (`build_rubric_grid`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_hiring_rubric_builder`)

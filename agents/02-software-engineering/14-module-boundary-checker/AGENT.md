# Module Boundary Checker (`14-module-boundary-checker`)

**Role:** Software Engineering
**Tool:** `check_module_boundaries`

## Focused Responsibility
Checks dependency graphs for cycles, layer violations, and hidden coupling between modules.

## Contract
- **Input (`dependency_graph`):** string
- **Output (`boundary_report`):** string, `tool_used` (`check_module_boundaries`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_module_boundary_checker`)

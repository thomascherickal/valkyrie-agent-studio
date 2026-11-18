# Org Design Modeler (`09-org-design-modeler`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `analyze_org_topology`

## Focused Responsibility
Evaluates manager span-of-control and platform vs stream-aligned pods.

## Contract
- **Input (`org_chart`):** string
- **Output (`org_recommendations`):** string, `tool_used` (`analyze_org_topology`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_org_design_modeler`)

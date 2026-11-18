# PRD Architect (`01-prd-architect`)

**Role:** Product Management  
**Tool:** `extract_requirements`

## Focused Responsibility
Converts feature briefs into structured PRDs with goals, non-goals, and acceptance criteria.

## Contract
- **Input (`feature_brief`):** string
- **Output (`prd_markdown`):** string, `tool_used` (`extract_requirements`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_prd_architect`)

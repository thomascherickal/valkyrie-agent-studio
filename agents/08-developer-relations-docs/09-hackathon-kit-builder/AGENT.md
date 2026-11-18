# Hackathon Kit Builder (`09-hackathon-kit-builder`)

**Role:** Developer Relations & Docs  
**Tool:** `assemble_kit_manifest`

## Focused Responsibility
Packages starter prompts, sample datasets, and judging rubrics.

## Contract
- **Input (`theme`):** string
- **Output (`hackathon_kit`):** string, `tool_used` (`assemble_kit_manifest`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_hackathon_kit_builder`)

# AI Transformation Advisor (`05-ai-transformation-advisor`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `rank_ai_roi`

## Focused Responsibility
Ranks internal workflows by automation ROI and compliance safety.

## Contract
- **Input (`workflow_catalog`):** string
- **Output (`rollout_roadmap`):** string, `tool_used` (`rank_ai_roi`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_ai_transformation_advisor`)

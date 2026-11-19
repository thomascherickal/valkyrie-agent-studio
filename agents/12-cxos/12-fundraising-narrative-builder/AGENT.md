# Fundraising Narrative Builder (`12-fundraising-narrative-builder`)

**Role:** C-Suite & Executives (CxOs)
**Tool:** `build_fundraise_story`

## Focused Responsibility
Builds investor narratives from traction, market, team, and use of funds with proof points.

## Contract
- **Input (`company_facts`):** string
- **Output (`investor_narrative`):** string, `tool_used` (`build_fundraise_story`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_fundraising_narrative_builder`)

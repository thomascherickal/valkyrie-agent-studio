# Referral Program Designer (`14-referral-program-designer`)

**Role:** Growth & Product Analytics
**Tool:** `design_referral`

## Focused Responsibility
Designs referral programs with rewards, triggers, fraud limits, and break-even math.

## Contract
- **Input (`referral_brief`):** string
- **Output (`referral_design`):** string, `tool_used` (`design_referral`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_referral_program_designer`)

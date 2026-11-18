# Pricing & Packaging Modeler (`07-pricing-modeler`)

**Role:** Product Management  
**Tool:** `simulate_unit_margin`

## Focused Responsibility
Models gross margin and ARPA across seat-based and usage-based pricing tiers.

## Contract
- **Input (`tier_assumptions`):** string
- **Output (`margin_report`):** string, `tool_used` (`simulate_unit_margin`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_pricing_modeler`)

# Supply Chain Risk Assessor (`12-supply-chain-assessor`)

**Role:** Security & AppSec
**Tool:** `assess_supply_chain`

## Focused Responsibility
Assesses software supply chain risk across dependencies, build systems, and release signing.

## Contract
- **Input (`dependency_notes`):** string
- **Output (`supply_chain_report`):** string, `tool_used` (`assess_supply_chain`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_supply_chain_assessor`)

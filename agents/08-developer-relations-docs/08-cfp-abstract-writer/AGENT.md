# CFP Abstract Writer (`08-cfp-abstract-writer`)

**Role:** Developer Relations & Docs  
**Tool:** `polish_cfp_abstract`

## Focused Responsibility
Crafts sharp conference talk abstracts with concrete takeaways.

## Contract
- **Input (`talk_idea`):** string
- **Output (`cfp_submission`):** string, `tool_used` (`polish_cfp_abstract`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_cfp_abstract_writer`)

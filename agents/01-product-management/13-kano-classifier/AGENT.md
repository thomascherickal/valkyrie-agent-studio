# Kano Feature Classifier (`13-kano-classifier`)

**Role:** Product Management
**Tool:** `classify_kano`

## Focused Responsibility
Classifies features as must-have, performance, or delighter from paired survey answers.

## Contract
- **Input (`survey_results`):** string
- **Output (`kano_matrix`):** string, `tool_used` (`classify_kano`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_kano_classifier`)

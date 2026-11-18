# Voice of Customer Synthesizer (`05-voice-of-customer`)

**Role:** Product Management  
**Tool:** `cluster_verbatims`

## Focused Responsibility
Clusters NPS verbatims and support themes by frequency and churn risk.

## Contract
- **Input (`feedback_batch`):** string
- **Output (`top_themes`):** string, `tool_used` (`cluster_verbatims`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_voice_of_customer`)

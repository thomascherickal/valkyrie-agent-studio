# Perf Review Synthesizer (`05-perf-review-synthesizer`)

**Role:** Engineering & Product Management  
**Tool:** `synthesize_feedback`

## Focused Responsibility
Synthesizes peer feedback and shipped artifacts into balanced reviews.

## Contract
- **Input (`feedback_notes`):** string
- **Output (`review_draft`):** string, `tool_used` (`synthesize_feedback`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_perf_review_synthesizer`)

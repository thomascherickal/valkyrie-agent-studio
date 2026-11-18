# API Error Explainer (`07-api-error-explainer`)

**Role:** Technical Support  
**Tool:** `explain_api_error`

## Focused Responsibility
Translates raw HTTP 4xx/5xx error payloads into plain-English fixes.

## Contract
- **Input (`error_payload`):** string
- **Output (`fix_guidance`):** string, `tool_used` (`explain_api_error`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_api_error_explainer`)

# Pricing Page Reviewer (`17-pricing-page-reviewer`)

**Role:** Growth & Product Analytics
**Tool:** `review_pricing_page`

## Focused Responsibility
Reviews pricing pages for clarity, anchoring, plan fit, objections, and conversion risks.

## Contract
- **Input (`page_copy`):** string
- **Output (`pricing_review`):** string, `tool_used` (`review_pricing_page`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_pricing_page_reviewer`)

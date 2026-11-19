# Promotion Packet Builder (`12-promotion-packet-builder`)

**Role:** Engineering & Product Management
**Tool:** `build_promo_packet`

## Focused Responsibility
Builds promotion packets from impact evidence mapped to level expectations and peer signal.

## Contract
- **Input (`impact_notes`):** string
- **Output (`promo_packet`):** string, `tool_used` (`build_promo_packet`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_promotion_packet_builder`)

# Rust Port Advisor (`10-rust-port-advisor`)

**Role:** Software Engineering  
**Tool:** `estimate_rust_speedup`

## Focused Responsibility
Profiles CPU-bound Python hotspots and plans zero-GIL PyO3/Tokio ports.

## Contract
- **Input (`profile_stats`):** string
- **Output (`port_blueprint`):** string, `tool_used` (`estimate_rust_speedup`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_rust_port_advisor`)

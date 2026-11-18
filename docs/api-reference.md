# API Reference (`studio-core`)

FastAPI application defined in `studio-core/valkyrie/api_server.py`.

## Endpoints
| Method / Protocol | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Returns `{"status": "ok", "default_model": "gemini-4-hydrogen", "thinking_level": "low"}`. |
| `GET` | `/api/agents` | Scans `agents/` and returns all 12 roles and 120 focused agent IDs. |
| `POST` | `/api/agents/run` | Validates `ir_yaml` (`AgentIR`), runs either `run_custom_python` (if enabled) or `LLMRouter.invoke`, and evaluates output via `evaluate_agent_output`. |
| `POST` | `/api/agents/deploy-rust` | Validates `ir_yaml` and returns `{crate_name, cargo_toml, main_rs, estimated_speedup}` from `transpile_ir_to_rust`. |
| `WS` | `/ws/traces` | Accepts WebSocket connections and streams `CommandCentre` agent trace JSON (`agent_id`, `state`, `steps`). |

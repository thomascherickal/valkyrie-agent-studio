# API Reference (`studio-core`)

FastAPI application defined in `studio-core/valkyrie/api_server.py`. Routers live beside it: `agent_impl_routes.py` (code editor), `agent_generator_routes.py` (custom agents), `command_centre_routes.py` (traces) and `provider_routes.py` (keys).

## Endpoints
| Method / Protocol | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Returns `{"status": "ok", "default_model": "gemini-4-hydrogen", "thinking_level": "low"}`. |
| `GET` | `/api/agents` | Scans `agents/` and returns all 12 roles and 240 focused agent IDs (20 per role). |
| `POST` | `/api/agents/run` | Validates `ir_yaml` (`AgentIR`), re-reads `.env`, then runs the model (`LLMRouter.invoke`), custom Python, or one of an agent's Python versions (`role_id`, `agent_id`, `impl`). Add `code` to run the editor's unsaved text instead of the saved version. Sandboxed code can call `model(prompt)`. Output is evaluated by `evaluate_agent_output`. |
| `POST` | `/api/agents/deploy-rust` | Validates `ir_yaml` and returns `{crate_name, cargo_toml, main_rs, estimated_speedup}` from `transpile_ir_to_rust`. The crate is built from the agent's definition, not from edited Python. |
| `GET/PUT/DELETE` | `/api/agents/{role}/{agent}/implementations/{impl}` | Read, save an edit to, or revert one Python version (or delete a saved one). |
| `POST` | `/api/agents/{role}/{agent}/implementations`, `/check` | Save a new version next to the built-in three, or run code once with the sample to find errors. |
| `GET` | `/api/agents/{role}/{agent}/fields`, `/explanation` | The extra data fields the agent needs, and a bulleted explanation. |
| `POST` | `/api/agents/create-from-prompt` | Generates a custom agent from English and saves it. Regenerating an id drops its old edits. |
| `GET/DELETE` | `/api/agents/custom`, `/api/agents/custom/{id}` | List saved custom agents, or delete one with its edits. |
| `GET` | `/api/providers` | For each provider: the variable that holds its key and whether a key is set. Never returns a key. |
| `POST` | `/api/providers/reload` | Re-reads `.env` so a pasted key is used without a restart. Returns the names that changed. |
| `GET/POST` | `/api/command-centre/traces`, `/start/{id}`, `/stop/{id}`, `/admin/stop-all` | Command Centre state and controls. |
| `WS` | `/ws/traces` | Sends the shared Command Centre trace list on connect and again on every change, until the client leaves. |

## Model helper settings
`model(prompt)` uses Gemini by default. Set `VALKYRIE_MODEL_PROVIDER` (`gemini`, `ollama`, `openrouter`, `opencode`) and `VALKYRIE_MODEL_ID` (needed for `openrouter` and `opencode`). With no key, `model()` returns `None` and Hybrid versions fall back to their drafted report.

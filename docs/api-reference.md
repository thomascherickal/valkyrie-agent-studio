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
| `GET/DELETE` | `/api/trace/events?after=<id>&run=<run>` | The step-by-step trace: every step of every run and action, with secrets removed. `last_id` says where to continue. `DELETE` clears the pane's memory; the JSONL log file (`logs/trace.jsonl`, or `VALKYRIE_LOG_DIR`) is kept. |
| `WS` | `/ws/trace?after=<id>` | Streams each new trace step as it happens, so the Command Centre trace log is live. |
| `WS` | `/ws/traces` | Sends the shared Command Centre trace list on connect and again on every change, until the client leaves. |

## Provider fallback and tracing
A model run asks **Gemini 4 Hydrogen** first. If it fails (error, rate limit, empty answer), the **OpenCode free models** (`big-pickle`, `deepseek-v4.1-flash-free`, `mimo-v2.6-flash-free`) are tried, then the **OpenRouter free models** (`openrouter/free`, `google/gemma-4-31b-it:free`). A provider with no key is skipped (and the skip is traced). If every provider with a key fails, the run returns `502` listing what each said. With no keys at all, the offline simulation answers. The response carries `provider` and `model` so you can see who answered. Override the free lists with `VALKYRIE_OPENCODE_MODELS` and `VALKYRIE_OPENROUTER_MODELS`.

Every run records its steps: `run.start`, `env`, `ir`, `code`, `prompt`, `route`, each `provider.attempt` / `provider.fail` / `provider.ok`, `fallback`, `sandbox.start` / `sandbox.end`, each pipeline `stage`, `result`, `eval` and `run.done` (or `run.error`). Button actions (save, revert, check, create, delete, key reload, start, stop) are recorded under the run `system`. Keys never reach the trace: key values, `key=` parameters and bearer tokens are replaced with `***`, and Gemini's key travels in a header, not in the URL.

## Model helper settings
`model(prompt)` uses Gemini by default. Set `VALKYRIE_MODEL_PROVIDER` (`gemini`, `ollama`, `openrouter`, `opencode`) and `VALKYRIE_MODEL_ID` (needed for `openrouter` and `opencode`). With no key, `model()` returns `None` and Hybrid versions fall back to their drafted report.

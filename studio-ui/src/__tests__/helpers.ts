import { vi } from "vitest";
import { implRoute, resetApi, runRoute } from "./fakeApi";
import { ok } from "./http";

export { fail, ok } from "./http";
export { originalOf, seedSaved } from "./fakeApi";

export function stubFetch(handler: (path: string, init?: RequestInit) => unknown) {
  resetApi();
  const f = vi.fn(async (url: string, init?: RequestInit) => handler(url.replace("http://localhost:8000", ""), init));
  vi.stubGlobal("fetch", f);
  return f;
}

/** An empty trace log, for tests that are about something else. */
export const noTraceEvents = { events: [], last_id: 0, log_file: "/tmp/trace.jsonl" };

/** stubFetch that answers the trace log's request with an empty log and hands everything else to `handler`. */
export function stubTraces(handler: (path: string, init?: RequestInit) => unknown) {
  return stubFetch((path, init) => (path.startsWith("/api/trace/events") ? ok(noTraceEvents) : handler(path, init)));
}

/** A WebSocket that never connects, so tests do not depend on a real socket. */
export function silentSocket() {
  vi.stubGlobal("WebSocket", class { onopen = null; onmessage = null; onclose = null; onerror = null; close() {} });
}

const entry = (id: string, label: string, model: string, effort: string | null = null) =>
  ({ id, label, env_var: `${id.toUpperCase()}_API_KEY`, key_set: false, preview: "", model, effort });
/** What GET /api/secrets returns with no keys set. */
export const secretsState = {
  env_file: ".env", env_path: "/home/me/.local/share/valkyrie-studio/.env",
  providers: [], fallback: [{ provider: "gemini", models: ["gemini-4-hydrogen"] }, { provider: "opencode", models: ["big-pickle"] }],
  secrets: [entry("gemini", "Gemini", "gemini-4-hydrogen", "low"), entry("openrouter", "OpenRouter", "openrouter/free"), entry("opencode", "OpenCode", "big-pickle")],
  default_provider: "gemini", default_providers: ["gemini", "openrouter", "opencode", "ollama"], efforts: ["low", "medium", "high"], simulated: true,
};
export const modelCatalog = {
  models: [{ id: "big-pickle", label: "Big Pickle", free: true }, { id: "gpt-5", label: "GPT-5", free: false }], source: "live", note: "", efforts: [],
};

const check = (impl: string, label: string, problems: unknown[] = [], warnings: string[] = []) =>
  ({ impl, label, ok: problems.length === 0, runs: 6, problems, warnings });
const versions = [["rules", "Rules"], ["pipeline", "Pipeline"], ["hybrid", "Hybrid (model + rules)"]];
/** What POST .../verify returns when every version passes. */
export const verifyPass = { agent: "Gen Agent", ok: true, checks: versions.map(([i, l]) => check(i, l)), problem_count: 0, warning_count: 0 };
export const verifyFail = {
  agent: "Gen Agent", ok: false, problem_count: 2, warning_count: 0,
  checks: [
    check("rules", "Rules", [{ stage: "run", payload: "no data", message: "KeyError: 'x' (line 2)", line: 2 }, { stage: "blocked", payload: null, message: "Forbidden construct: open(", line: null }]),
    check("pipeline", "Pipeline"), check("hybrid", "Hybrid (model + rules)"),
  ],
};
export const verifiedAgent = {
  id: "verified-copy", name: "Verified Copy", description: "Does things", tool: "do_things", input_key: "profile_stats", output_key: "port_blueprint",
  sample: "a sample", role_id: "custom-agents", edits_copied: false,
};

export function polyfillDialog() {
  HTMLDialogElement.prototype.showModal = function () { this.setAttribute("open", ""); };
  HTMLDialogElement.prototype.close = function () { this.removeAttribute("open"); };
}

/** A promise you resolve by hand, to land a reply after the screen has gone. */
export function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((r) => { resolve = r; });
  return { promise, resolve };
}

export const bundle = {
  agent_id: "gen-1", name: "Gen Agent", role: "x", description: "Does gen things", tool_name: "gen_tool",
  ir_yaml: "IR", agent_py: "PY", test_agent_py: "TEST", agent_md: "MD", main_rs: "RS",
};
export const llmRun = {
  mode: "llm", model: "gemini-4-hydrogen", thinking_level: "low", content: "hello", input_tokens: 1,
  output_tokens: 2, cost_usd: 0.5, eval_passed: true, eval_reasons: [],
};
export const deployed = { crate_name: "crate-x", cargo_toml: "", main_rs: "fn main(){}", estimated_speedup: "10x" };
export const health = { status: "ok", default_model: "gemini-4-hydrogen", thinking_level: "low" };

export function appRoutes(path: string, init?: RequestInit) {
  const found = implRoute(path, init) ?? runRoute(path, init);
  if (found) return found;
  if (path === "/health") return ok(health);
  if (path === "/api/command-centre/traces") return ok({ traces: [] });
  if (path.startsWith("/api/trace/events")) return ok(noTraceEvents);
  if (path.endsWith("/verify")) return ok(verifyPass);
  if (path.endsWith("/save-verified")) return ok(verifiedAgent);
  if (path === "/api/secrets") return ok(secretsState);
  if (path.startsWith("/api/secrets/") && path.endsWith("/models")) return ok(modelCatalog);
  if (path === "/api/agents/run") return ok(llmRun);
  if (path === "/api/agents/deploy-rust") return ok(deployed);
  if (path === "/api/agents/create-from-prompt") return ok(bundle);
  if (path === "/api/agents/custom") return ok({ agents: [] });
  return ok({});
}

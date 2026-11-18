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
  if (path === "/api/agents/run") return ok(llmRun);
  if (path === "/api/agents/deploy-rust") return ok(deployed);
  if (path === "/api/agents/create-from-prompt") return ok(bundle);
  if (path === "/api/agents/custom") return ok({ agents: [] });
  return ok({});
}

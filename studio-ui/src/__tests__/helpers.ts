import { vi } from "vitest";

export const ok = (data: unknown) => ({ ok: true, json: async () => data });
export const fail = (status = 500, detail?: string) => ({
  ok: false,
  status,
  json: detail === undefined ? async () => { throw new Error("no body"); } : async () => ({ detail }),
});

/** Saved edits by "role/agent". Cleared by every stubFetch, so each test starts pristine. */
const edits = new Map<string, string>();

export const originalOf = (roleId: string, agentId: string) => `# original ${roleId}/${agentId}`;

/** A stateful stand-in for the /code endpoints. A PUT of the text "FAIL" answers 400. */
export function codeRoute(path: string, init?: RequestInit) {
  const m = path.match(/^\/api\/agents\/([^/]+)\/([^/]+)\/code$/);
  if (!m) return undefined;
  const [, role, agent] = m;
  const key = `${role}/${agent}`;
  const original = originalOf(role, agent);
  if (init?.method === "PUT") {
    const { code } = JSON.parse(init.body as string);
    if (code === "FAIL") return fail(400, "Code is not allowed");
    if (code === original) edits.delete(key);
    else edits.set(key, code);
  } else if (init?.method === "DELETE") edits.delete(key);
  const code = edits.get(key) ?? original;
  return ok({ role_id: role, agent_id: agent, original, code, edited: edits.has(key) });
}

export function stubFetch(handler: (path: string, init?: RequestInit) => unknown) {
  edits.clear();
  const f = vi.fn(async (url: string, init?: RequestInit) => handler(url.replace("http://localhost:8000", ""), init));
  vi.stubGlobal("fetch", f);
  return f;
}

export function polyfillDialog() {
  HTMLDialogElement.prototype.showModal = function () { this.setAttribute("open", ""); };
  HTMLDialogElement.prototype.close = function () { this.removeAttribute("open"); };
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
  const code = codeRoute(path, init);
  if (code) return code;
  if (path === "/health") return ok(health);
  if (path === "/api/command-centre/traces") return ok({ traces: [] });
  if (path === "/api/agents/run") return ok(llmRun);
  if (path === "/api/agents/deploy-rust") return ok(deployed);
  if (path === "/api/agents/create-from-prompt") return ok(bundle);
  if (path === "/api/agents/custom") return ok({ agents: [] });
  return ok({});
}

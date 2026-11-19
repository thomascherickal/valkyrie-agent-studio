import { afterEach, describe, expect, it, vi } from "vitest";
import * as api from "../api/client";
import { fail, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

describe("api client", () => {
  it("returns json on success and POSTs bodies", async () => {
    const f = stubFetch(() => ok({ a: 1 }));
    expect(await api.getHealth()).toEqual({ a: 1 });
    await api.runAgent("ir", "p", { task_input: "p" }, null);
    await api.deployRust("ir");
    await api.createFromPrompt("p", "");
    await api.createFromPrompt("p", "n");
    await api.listTraces();
    await api.startAgent("a");
    await api.stopAgent("a");
    await api.stopAll();
    const bodies = f.mock.calls.map((c) => c[1]?.body);
    expect(bodies[1]).toContain("task_input");
    expect(bodies[3]).toContain('"name":null');
    expect(bodies[4]).toContain('"name":"n"');
  });
  it("sends unsaved code only when asked, and calls delete and the provider endpoints", async () => {
    const f = stubFetch(() => ok({}));
    const target = { roleId: "r", agentId: "a", impl: "rules" };
    await api.runAgent("ir", "p", {}, target);
    await api.runAgent("ir", "p", {}, { ...target, code: "" });
    await api.runAgent("ir", "p", {}, { ...target, code: "x = 1" });
    const body = (i: number) => JSON.parse(f.mock.calls[i][1]!.body as string);
    expect(body(0)).not.toHaveProperty("code");
    expect(body(1).code).toBe("");
    expect(body(2)).toMatchObject({ role_id: "r", agent_id: "a", impl: "rules", code: "x = 1" });
    f.mockClear();
    await api.deleteCustomAgent("mine");
    await api.getProviders();
    await api.reloadProviders();
    expect(f.mock.calls.map(([u, i]) => `${i?.method ?? "GET"} ${u.replace("http://localhost:8000", "")}`)).toEqual([
      "DELETE /api/agents/custom/mine", "GET /api/providers", "POST /api/providers/reload",
    ]);
  });
  it("uses detail, status fallback, and offline message", async () => {
    stubFetch(() => fail(400, "bad thing"));
    await expect(api.getHealth()).rejects.toThrow("bad thing");
    stubFetch(() => fail(500, ""));
    await expect(api.getHealth()).rejects.toThrow("The API returned 500.");
    stubFetch(() => fail(500));
    await expect(api.getHealth()).rejects.toThrow("The API returned 500.");
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new Error("down")));
    await expect(api.getHealth()).rejects.toThrow("Can't reach the Valkyrie API");
    expect(new api.ApiError("x")).toBeInstanceOf(Error);
  });
  it("buildIr always pins the default model", () => {
    const spec = { id: "i", name: "n", role: "r", description: "d", systemPrompt: "s" };
    const ir = JSON.parse(api.buildIr(spec, { provider: "ollama", thinkingLevel: "high", hostedModel: "" }, true));
    expect(ir.model_config_spec).toEqual({ provider: "ollama", model: "gemini-4-hydrogen", thinking_level: "high" });
    for (const provider of ["openrouter", "opencode"] as const) {
      const hosted = JSON.parse(api.buildIr(spec, { provider, thinkingLevel: "low", hostedModel: "acme/free" }, false));
      expect(hosted.model_config_spec).toEqual({ provider, model: "acme/free", thinking_level: "low" });
    }
    expect(ir.custom_python_enabled).toBe(true);
  });
});

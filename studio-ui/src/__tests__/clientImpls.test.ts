import { afterEach, describe, expect, it, vi } from "vitest";
import * as api from "../api/client";
import { ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const BASE = "http://localhost:8000/api/agents/r1/a1";
const lastCall = (f: ReturnType<typeof stubFetch>) => f.mock.calls[f.mock.calls.length - 1] as [string, RequestInit | undefined];
const json = { "Content-Type": "application/json" };

describe("api client: running", () => {
  it("runAgent without a target sends only the model request", async () => {
    const f = stubFetch(() => ok({}));
    await api.runAgent("ir", "p", { k: "v" }, null);
    const [url, init] = lastCall(f);
    expect(url).toBe("http://localhost:8000/api/agents/run");
    expect(init).toMatchObject({ method: "POST", headers: json });
    expect(JSON.parse(init!.body as string)).toEqual({ ir_yaml: "ir", prompt: "p", payload: { k: "v" } });
  });
  it("runAgent with a target adds role_id, agent_id and impl, and no custom_python", async () => {
    const f = stubFetch(() => ok({}));
    await api.runAgent("ir", "p", { k: "v" }, { roleId: "r1", agentId: "a1", impl: "pipeline" });
    expect(JSON.parse(lastCall(f)[1]!.body as string)).toEqual({
      ir_yaml: "ir", prompt: "p", payload: { k: "v" }, role_id: "r1", agent_id: "a1", impl: "pipeline",
    });
  });
});

describe("api client: implementations", () => {
  it("listImpls, getImpl, getFields and getExplanation are plain GETs", async () => {
    const f = stubFetch(() => ok({ x: 1 }));
    const urls = [`${BASE}/implementations`, `${BASE}/implementations/hybrid`, `${BASE}/fields`, `${BASE}/explanation`];
    const results = await Promise.all([
      api.listImpls("r1", "a1"), api.getImpl("r1", "a1", "hybrid"), api.getFields("r1", "a1"), api.getExplanation("r1", "a1"),
    ]);
    expect(results).toEqual(urls.map(() => ({ x: 1 })));
    expect(f.mock.calls.map(([u]) => u)).toEqual(urls);
    expect(f.mock.calls.every(([, init]) => init === undefined)).toBe(true);
  });
  it("saveImpl PUTs the code", async () => {
    const f = stubFetch(() => ok({}));
    await api.saveImpl("r1", "a1", "rules", "x = 1");
    const [url, init] = lastCall(f);
    expect(url).toBe(`${BASE}/implementations/rules`);
    expect(init).toMatchObject({ method: "PUT", headers: json, body: JSON.stringify({ code: "x = 1" }) });
  });
  it("removeImpl DELETEs without a body", async () => {
    const f = stubFetch(() => ok({ deleted: "saved-x" }));
    expect(await api.removeImpl("r1", "a1", "saved-x")).toEqual({ deleted: "saved-x" });
    const [url, init] = lastCall(f);
    expect(url).toBe(`${BASE}/implementations/saved-x`);
    expect(init).toEqual({ method: "DELETE" });
  });
  it("createImpl and checkCode POST JSON", async () => {
    const f = stubFetch(() => ok({}));
    await api.createImpl("r1", "a1", "Mine", "y = 2");
    let [url, init] = lastCall(f);
    expect(url).toBe(`${BASE}/implementations`);
    expect(init).toMatchObject({ method: "POST", headers: json, body: JSON.stringify({ name: "Mine", code: "y = 2" }) });
    await api.checkCode("r1", "a1", "z = 3");
    [url, init] = lastCall(f);
    expect(url).toBe(`${BASE}/check`);
    expect(init).toMatchObject({ method: "POST", headers: json, body: JSON.stringify({ code: "z = 3" }) });
  });
});

import { afterEach, describe, expect, it, vi } from "vitest";
import * as api from "../api/client";
import { ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());
const info = { role_id: "r", agent_id: "a", original: "o", code: "c", edited: false };

describe("agent code client", () => {
  it("GETs, PUTs JSON and DELETEs the code endpoint", async () => {
    const f = stubFetch(() => ok(info));
    expect(await api.getAgentCode("r", "a")).toEqual(info);
    await api.saveAgentCode("r", "a", "new");
    await api.revertAgentCode("r", "a");
    const [get, put, del] = f.mock.calls;
    expect(get).toEqual(["http://localhost:8000/api/agents/r/a/code", undefined]);
    expect(put[0]).toBe("http://localhost:8000/api/agents/r/a/code");
    expect(put[1]).toEqual({ method: "PUT", headers: { "Content-Type": "application/json" }, body: '{"code":"new"}' });
    expect(del[1]).toEqual({ method: "DELETE" });
  });
  it("runAgent sends the payload and passes custom python through", async () => {
    const f = stubFetch(() => ok({}));
    await api.runAgent("ir", "Feature brief: x", "code", { feature_brief: "x" });
    await api.runAgent("ir", "p", null, {});
    const bodies = f.mock.calls.map((c) => JSON.parse(c[1]!.body as string));
    expect(bodies[0]).toEqual({ ir_yaml: "ir", prompt: "Feature brief: x", custom_python: "code", payload: { feature_brief: "x" } });
    expect(bodies[1].custom_python).toBeNull();
  });
});

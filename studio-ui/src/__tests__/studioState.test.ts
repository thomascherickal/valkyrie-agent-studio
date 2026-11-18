import { describe, expect, it } from "vitest";
import { addCustomAgent, CUSTOM_ROLE, DEFAULT_PYTHON, draftFor, findAgent } from "../components/studioState";

const a = (id: string) => ({ id, name: id, description: "d", tool: "t", inputKey: "i", outputKey: "o", sampleInput: "s" });
const roles = [{ id: "r", name: "R", agents: [a("x")] }];

describe("studioState", () => {
  it("draftFor uses default or supplied python", () => {
    expect(draftFor(a("x")).pythonCode).toBe(DEFAULT_PYTHON);
    expect(draftFor(a("x"), "code").pythonCode).toBe("code");
    expect(draftFor(a("x")).systemPrompt).toBe("You are x. d");
  });
  it("findAgent", () => {
    expect(findAgent(roles, "r", "x").agent.id).toBe("x");
  });
  it("addCustomAgent creates then replaces by id", () => {
    const first = addCustomAgent(roles, a("c"));
    expect(first[first.length - 1]).toEqual({ ...CUSTOM_ROLE, agents: [a("c")] });
    const second = addCustomAgent(first, { ...a("c"), name: "new" });
    const custom = second.filter((r) => r.id === CUSTOM_ROLE.id);
    expect(custom).toHaveLength(1);
    expect(custom[0].agents).toEqual([{ ...a("c"), name: "new" }]);
    const third = addCustomAgent(first, a("d"));
    expect(third[third.length - 1].agents).toHaveLength(2);
  });
});

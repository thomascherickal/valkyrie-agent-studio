import { describe, expect, it } from "vitest";
import {
  addCustomAgent, CUSTOM_ROLE, customBlueprint, draftFor, findAgent, labelFor, payloadOf, promptOf, restoreCustomAgents,
} from "../components/studioState";

const a = (id: string) => ({ id, name: id, description: "d", tool: "t", inputKey: "i", outputKey: "o", sampleInput: "s" });
const roles = [{ id: "r", name: "R", agents: [a("x")] }];

describe("studioState", () => {
  it("draftFor builds fields from the agent and starts without code", () => {
    const d = draftFor(a("x"));
    expect(d.pythonCode).toBe("");
    expect(d.codeInfo).toBeNull();
    expect(d.fields).toEqual([{ key: "i", value: "s", custom: false }]);
    expect(d.systemPrompt).toBe("You are x. d");
  });
  it("labelFor, payloadOf and promptOf skip blank names and trim", () => {
    expect(labelFor("feature_brief")).toBe("Feature brief");
    const fields = [
      { key: "feature_brief", value: "a", custom: false },
      { key: "  extra_note ", value: "b", custom: true },
      { key: "  ", value: "dropped", custom: true },
    ];
    expect(payloadOf(fields)).toEqual({ feature_brief: "a", extra_note: "b" });
    expect(promptOf(fields)).toBe("Feature brief: a\nExtra note: b");
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
  it("restoreCustomAgents turns saved agents into blueprints, and leaves roles alone when none are saved", () => {
    expect(restoreCustomAgents(roles, [])).toBe(roles);
    const saved = { id: "s", name: "Saved", description: "does s", tool: "run_s" };
    const restored = restoreCustomAgents(roles, [saved]);
    expect(restored[restored.length - 1].agents).toEqual([customBlueprint(saved)]);
    expect(customBlueprint(saved)).toEqual({ ...saved, inputKey: "task_input", outputKey: "result", sampleInput: "does s" });
  });
});

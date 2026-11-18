import { describe, expect, it } from "vitest";
import type { ImplCode, ImplMeta } from "../api/types";
import {
  addCustomAgent, CUSTOM_ROLE, customBlueprint, draftFor, findAgent, labelFor, MODEL, payloadOf, promptOf, restoreCustomAgents, toField,
  withMeta, type DataField,
} from "../components/studioState";

const a = (id: string) => ({ id, name: id, description: "d", tool: "t", inputKey: "i", outputKey: "o", sampleInput: "s" });
const roles = [{ id: "r", name: "R", agents: [a("x")] }];

describe("studioState drafts and fields", () => {
  it("draftFor builds the main field from the agent and starts empty", () => {
    const d = draftFor(a("x"));
    expect(d.fields).toEqual([{ key: "i", value: "s", custom: false, label: "I", kind: "longtext" }]);
    expect(d).toMatchObject({ systemPrompt: "You are x. d", runWith: MODEL, editing: "rules", impls: null, fieldsLoaded: false, codes: {}, texts: {} });
  });
  it("toField starts a box from the playbook example", () => {
    expect(toField({ key: "budget", label: "Budget", kind: "number", example: "100" })).toEqual({
      key: "budget", value: "100", custom: false, label: "Budget", kind: "number",
    });
  });
  it("withMeta keeps null, and updates only the matching implementation", () => {
    const info: ImplCode = { role_id: "r", agent_id: "x", impl: "pipeline", label: "Pipeline", kind: "builtin", edited: true, original: "o", code: "c" };
    expect(withMeta(null, info)).toBeNull();
    const list: ImplMeta[] = [
      { id: "rules", label: "Rules", kind: "builtin", edited: false },
      { id: "pipeline", label: "Pipeline", kind: "builtin", edited: false },
    ];
    expect(withMeta(list, info)).toEqual([list[0], { ...list[1], edited: true }]);
  });
  it("labelFor, payloadOf and promptOf skip blank names and trim", () => {
    expect(labelFor("feature_brief")).toBe("Feature brief");
    const f = (key: string, value: string, custom: boolean): DataField => ({ key, value, custom, label: "", kind: "text" });
    const fields = [f("feature_brief", "a", false), f("  extra_note ", "b", true), f("  ", "dropped", true)];
    expect(payloadOf(fields)).toEqual({ feature_brief: "a", extra_note: "b" });
    expect(promptOf(fields)).toBe("Feature brief: a\nExtra note: b");
  });
});

describe("studioState catalog helpers", () => {
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

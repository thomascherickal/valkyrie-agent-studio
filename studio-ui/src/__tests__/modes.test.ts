import { describe, expect, it } from "vitest";
import { MODE_TABS, TAB_LABELS } from "../components/modes";

describe("modes", () => {
  it("each level reveals more tabs", () => {
    expect(MODE_TABS.beginner).toEqual(["run", "about", "create"]);
    expect(MODE_TABS.advanced).toEqual(["run", "about", "create", "design", "code", "secrets"]);
    expect(Object.keys(MODE_TABS)).toEqual(["beginner", "advanced"]); // there is no Intermediate mode
  });
  it("About is in every mode, and every tab has a label", () => {
    for (const tabs of Object.values(MODE_TABS)) {
      expect(tabs).toContain("about");
      expect(tabs.map((t) => TAB_LABELS[t]).every(Boolean)).toBe(true);
    }
    expect(TAB_LABELS.about).toBe("About this agent");
    expect(TAB_LABELS.code).toBe("Python");
  });
});

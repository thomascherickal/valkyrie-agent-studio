import { describe, expect, it } from "vitest";
import { ALL_TABS, TAB_LABELS } from "../components/modes";

describe("modes", () => {
  it("exposes all studio tabs with labels", () => {
    expect(ALL_TABS).toEqual(["run", "about", "create", "design", "code", "secrets"]);
    expect(ALL_TABS.map((t) => TAB_LABELS[t]).every(Boolean)).toBe(true);
    expect(TAB_LABELS.about).toBe("About this agent");
    expect(TAB_LABELS.code).toBe("Python");
  });
});

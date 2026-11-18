import { fireEvent, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { DataField } from "../components/studioState";
import { mountRun } from "./Harness";

afterEach(() => vi.unstubAllGlobals());

const field = (key: string, kind: DataField["kind"], value = "v"): DataField => ({ key, value, custom: false, label: key.toUpperCase(), kind });
const input = (name: string) => screen.getByLabelText(name) as HTMLInputElement & HTMLTextAreaElement;

describe("RunPanel fields", () => {
  it("loads the agent's own fields after the main input", async () => {
    mountRun();
    await screen.findByLabelText("Audience");
    expect(input("Feature brief").tagName).toBe("TEXTAREA");
    expect(input("Feature brief").value).toBe("sample");
    expect(input("Audience").tagName).toBe("INPUT");
    expect(input("Audience").value).toBe("engineers");
    expect(input("Audience").inputMode).toBe("text");
    expect(input("Budget").inputMode).toBe("decimal");
    expect(input("Budget").value).toBe("100");
  });
  it("shows text and number as inputs, and longtext and list as textareas of different heights", () => {
    mountRun({
      fieldsLoaded: true, impls: [],
      fields: [field("t", "text"), field("n", "number"), field("l", "longtext"), field("li", "list")],
    });
    expect([input("T"), input("N")].map((e) => e.tagName)).toEqual(["INPUT", "INPUT"]);
    expect([input("L"), input("LI")].map((e) => e.tagName)).toEqual(["TEXTAREA", "TEXTAREA"]);
    expect([input("L").rows, input("LI").rows]).toEqual([4, 3]);
  });
  it("edits a field's value", () => {
    mountRun({ fieldsLoaded: true, impls: [], fields: [field("t", "text", "a")] });
    fireEvent.change(input("T"), { target: { value: "b" } });
    expect(input("T").value).toBe("b");
  });
  it("adds, edits and removes your own fields", () => {
    mountRun({ fieldsLoaded: true, impls: [], fields: [field("t", "text", "a")] });
    fireEvent.click(screen.getByRole("button", { name: "Add field" }));
    fireEvent.click(screen.getByRole("button", { name: "Add field" }));
    fireEvent.change(input("Field name 2"), { target: { value: "note" } });
    fireEvent.change(input("Value of field 2"), { target: { value: "hi" } });
    expect(input("Field name 2").value).toBe("note");
    expect(input("Value of field 2").value).toBe("hi");
    expect(screen.getAllByRole("button", { name: "Remove" })).toHaveLength(2);
    fireEvent.click(screen.getAllByRole("button", { name: "Remove" })[1]);
    expect(screen.getAllByRole("button", { name: "Remove" })).toHaveLength(1);
    expect(input("Field name 2").value).toBe("note");
    expect(input("T").value).toBe("a");
  });
});

describe("RunPanel run with", () => {
  it("offers the model and one option per implementation, marking edited ones", async () => {
    mountRun();
    await screen.findByRole("option", { name: "Python: Rules" });
    expect(screen.getAllByRole("option").map((o) => o.textContent)).toEqual([
      "Gemini 4 Hydrogen (model)", "Python: Rules", "Python: Pipeline", "Python: Hybrid",
    ]);
  });
  it("marks an edited implementation", () => {
    mountRun({ impls: [{ id: "rules", label: "Rules", kind: "builtin", edited: true }], fieldsLoaded: true });
    expect(screen.getByRole("option", { name: "Python: Rules (edited)" })).toBeTruthy();
  });
  it("lists only the model before the implementations load", () => {
    mountRun({ fieldsLoaded: true, impls: null });
    expect(screen.getAllByRole("option")).toHaveLength(1);
  });
  it("choosing one changes what Run executes", async () => {
    mountRun();
    await screen.findByRole("option", { name: "Python: Pipeline" });
    fireEvent.change(screen.getByLabelText("Run with"), { target: { value: "pipeline" } });
    expect(screen.getByTestId("state").textContent).toBe("rules|pipeline");
    await waitFor(() => expect((screen.getByLabelText("Run with") as HTMLSelectElement).value).toBe("pipeline"));
  });
});

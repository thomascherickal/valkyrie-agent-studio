import { fireEvent, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { ImplCode } from "../api/types";
import { calls, mountRun } from "./Harness";

afterEach(() => vi.unstubAllGlobals());

const body = (f: Parameters<typeof calls>[0]) => JSON.parse(calls(f, "POST", "/run")[0][1]!.body as string);
const runButton = () => screen.getByRole("button", { name: "Run agent" });
const code = (text: string): ImplCode => ({ role_id: "r1", agent_id: "a1", impl: "rules", label: "Rules", kind: "builtin", edited: false, original: "o", code: text });

describe("RunPanel running", () => {
  it("runs the model with a prompt and a payload keyed by every field", async () => {
    const { f } = mountRun();
    await screen.findByLabelText("Audience");
    fireEvent.click(screen.getByRole("button", { name: "Add field" }));
    fireEvent.change(screen.getByLabelText("Field name 4"), { target: { value: "note" } });
    fireEvent.change(screen.getByLabelText("Value of field 4"), { target: { value: "hi" } });
    fireEvent.click(screen.getByRole("button", { name: "Add field" })); // left unnamed: not sent
    fireEvent.click(runButton());
    expect(screen.getByRole("status").textContent).toBe("Running…");
    expect(runButton().hasAttribute("disabled")).toBe(true);
    await screen.findByText("Eval passed");
    const sent = body(f);
    expect(sent.ir_yaml).toBe("IR");
    expect(sent.prompt).toBe("Feature brief: sample\nAudience: engineers\nBudget: 100\nNote: hi");
    expect(sent.payload).toEqual({ feature_brief: "sample", audience: "engineers", budget: "100", note: "hi" });
    expect(sent).not.toHaveProperty("role_id");
    expect(sent).not.toHaveProperty("impl");
  });
  it("runs an implementation and sends role_id, agent_id and impl", async () => {
    const { f } = mountRun();
    await screen.findByRole("option", { name: "Python: Hybrid" });
    fireEvent.change(screen.getByLabelText("Run with"), { target: { value: "hybrid" } });
    fireEvent.click(runButton());
    await screen.findByText("Python · hybrid");
    expect(body(f)).toMatchObject({ role_id: "r1", agent_id: "a1", impl: "hybrid" });
    expect(screen.getByText(/"agent_id": "a1"/)).toBeTruthy();
  });
  it("reports a failed run and shows it", async () => {
    const { report } = mountRun({ fieldsLoaded: true, impls: [] });
    fireEvent.change(screen.getByLabelText("Feature brief"), { target: { value: "BOOM" } });
    fireEvent.click(runButton());
    await screen.findByText("Run blew up");
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "model", stage: "run", message: "Run blew up" });
  });
  it("reports the implementation that failed", async () => {
    const { report } = mountRun({ fieldsLoaded: true, impls: [], runWith: "pipeline", fields: [
      { key: "k", value: "BOOM", custom: false, label: "K", kind: "text" },
    ] });
    fireEvent.click(runButton());
    await screen.findByRole("alert");
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "pipeline", stage: "run", message: "Run blew up" });
  });
});

describe("RunPanel unsaved-edits hint", () => {
  const hint = /unsaved edits to this version/;
  const setup = (runWith: string, text: string) =>
    mountRun({ fieldsLoaded: true, impls: [], runWith, codes: { rules: code("a") }, texts: { rules: text } });
  it("shows when the selected implementation has edits that are not saved", () => {
    setup("rules", "b");
    expect(screen.getByText(hint)).toBeTruthy();
  });
  it("is hidden when the text matches the saved code", () => {
    setup("rules", "a");
    expect(screen.queryByText(hint)).toBeNull();
  });
  it("is hidden when running the model", () => {
    setup("model", "b");
    expect(screen.queryByText(hint)).toBeNull();
  });
  it("is hidden when the implementation has not been opened", () => {
    setup("pipeline", "b");
    expect(screen.queryByText(hint)).toBeNull();
  });
});

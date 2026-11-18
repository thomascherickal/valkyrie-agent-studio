import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { RunPanel } from "../components/RunPanel";
import { agent, Held } from "./Harness";
import { fail, llmRun, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());
const mount = (initial = {}) =>
  render(<Held initial={initial} render={(d, c) => <RunPanel agent={agent} ir="IR" draft={d} onChange={c} />} />);
const body = (f: ReturnType<typeof stubFetch>) => JSON.parse(f.mock.calls[0][1]!.body as string);
const run = () => fireEvent.click(screen.getByText("Run Agent A"));

describe("RunPanel", () => {
  it("shows the sample in a labelled box, edits it and runs", async () => {
    const f = stubFetch(() => ok(llmRun));
    mount();
    expect(screen.queryByText(/Python override is on/)).toBeNull();
    const box = screen.getByLabelText("Feature brief") as HTMLTextAreaElement;
    expect(box.value).toBe("sample");
    fireEvent.change(box, { target: { value: "hi" } });
    run();
    expect(screen.getByRole("status").textContent).toBe("Running…");
    await screen.findByText("Eval passed");
    expect(body(f)).toEqual({ ir_yaml: "IR", prompt: "Feature brief: hi", custom_python: null, payload: { feature_brief: "hi" } });
  });
  it("adds, edits and removes extra fields; blank names are dropped", async () => {
    const f = stubFetch(() => ok(llmRun));
    mount();
    fireEvent.click(screen.getByText("Add field"));
    fireEvent.click(screen.getByText("Add field"));
    fireEvent.change(screen.getByLabelText("Field name 2"), { target: { value: " extra_note " } });
    fireEvent.change(screen.getByLabelText("Value of field 2"), { target: { value: "more" } });
    fireEvent.change(screen.getByLabelText("Value of field 3"), { target: { value: "orphan" } });
    run();
    await screen.findByText("Eval passed");
    expect(body(f).payload).toEqual({ feature_brief: "sample", extra_note: "more" });
    expect(body(f).prompt).toBe("Feature brief: sample\nExtra note: more");
    fireEvent.click(screen.getAllByText("Remove")[0]);
    expect(screen.queryByLabelText("Field name 3")).toBeNull();
    expect((screen.getByLabelText("Value of field 2") as HTMLTextAreaElement).value).toBe("orphan");
  });
  it("sends the override code and shows the hint", async () => {
    const f = stubFetch(() => ok(llmRun));
    mount({ pythonEnabled: true, pythonCode: "def run_agent(p): pass" });
    expect(screen.getByText(/Python override is on/)).toBeTruthy();
    run();
    await screen.findByText("Eval passed");
    expect(body(f).custom_python).toBe("def run_agent(p): pass");
  });
  it("blocks a run when the override is on but the code is blank", () => {
    const f = stubFetch(() => ok(llmRun));
    mount({ pythonEnabled: true, pythonCode: "  " });
    run();
    expect(screen.getByRole("alert").textContent).toMatch(/has not loaded/);
    expect(f).not.toHaveBeenCalled();
  });
  it("shows API errors", async () => {
    stubFetch(() => fail(500));
    mount();
    run();
    await waitFor(() => expect(screen.getByRole("alert").textContent).toBe("The API returned 500."));
  });
});

import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { RunPanel } from "../components/RunPanel";
import { fail, llmRun, ok, stubFetch } from "./helpers";

const agent = { id: "a", name: "Agent A", description: "", tool: "", inputKey: "", outputKey: "", sampleInput: "sample" };
afterEach(() => vi.unstubAllGlobals());

describe("RunPanel", () => {
  it("runs and shows the result, no override hint", async () => {
    const f = stubFetch(() => ok(llmRun));
    render(<RunPanel agent={agent} ir="IR" customPython={null} />);
    expect(screen.queryByText(/Python override is on/)).toBeNull();
    fireEvent.change(screen.getByLabelText("Test Prompt"), { target: { value: "hi" } });
    fireEvent.click(screen.getByText("Run agent"));
    expect(screen.getByRole("status").textContent).toBe("Running…");
    await screen.findByText("Eval passed");
    expect(JSON.parse(f.mock.calls[0][1]!.body as string)).toMatchObject({ ir_yaml: "IR", prompt: "hi", custom_python: null });
  });
  it("shows python override hint and errors", async () => {
    stubFetch(() => fail(500));
    render(<RunPanel agent={agent} ir="IR" customPython="code" />);
    expect(screen.getByText(/Python override is on/)).toBeTruthy();
    fireEvent.click(screen.getByText("Run agent"));
    await waitFor(() => expect(screen.getByRole("alert").textContent).toBe("The API returned 500."));
  });
});

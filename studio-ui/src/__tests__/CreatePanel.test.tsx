import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { CreatePanel } from "../components/CreatePanel";
import { bundle, fail, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

describe("CreatePanel", () => {
  it("creates, notifies, and switches file tabs", async () => {
    const f = stubFetch(() => ok(bundle));
    const onCreated = vi.fn();
    render(<CreatePanel onCreated={onCreated} />);
    fireEvent.change(screen.getByLabelText("Plain-English Agent Description"), { target: { value: "do it" } });
    fireEvent.change(screen.getByLabelText("Custom Agent Name"), { target: { value: "Nm" } });
    fireEvent.click(screen.getByText("Create agent"));
    expect(screen.getByRole("status").textContent).toBe("Creating…");
    await screen.findByText(/Created Gen Agent/);
    expect(onCreated).toHaveBeenCalledWith(bundle);
    expect(JSON.parse(f.mock.calls[0][1]!.body as string)).toEqual({ prompt: "do it", name: "Nm" });
    const pre = () => screen.getByLabelText("File contents").textContent;
    expect(pre()).toBe("IR");
    for (const [label, text] of [["agent.py", "PY"], ["test_agent.py", "TEST"], ["AGENT.md", "MD"], ["main.rs", "RS"]]) {
      fireEvent.click(screen.getByText(label));
      expect(pre()).toBe(text);
    }
    fireEvent.click(screen.getByText("agent.ir.yaml"));
    expect(pre()).toBe("IR");
  });
  it("shows errors without notifying", async () => {
    stubFetch(() => fail(422, "nope"));
    const onCreated = vi.fn();
    render(<CreatePanel onCreated={onCreated} />);
    fireEvent.click(screen.getByText("Create agent"));
    await screen.findByText("nope");
    expect(onCreated).not.toHaveBeenCalled();
  });
});

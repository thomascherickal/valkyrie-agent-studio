import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { TracePanel } from "../components/TracePanel";
import { fail, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

describe("TracePanel", () => {
  it("shows empty message, then traces, and actions POST then refresh", async () => {
    let traces: unknown[] = [];
    const f = stubFetch((p) => (p.endsWith("/traces") ? ok({ traces }) : ok({})));
    render(<TracePanel agentId="ag" online />);
    await screen.findByText("No agents have run yet.");
    traces = [{ agent_id: "ag", state: "running", steps: ["a", "b"] }];
    for (const [label, path] of [
      ["Start agent", "/start/ag"], ["Stop agent", "/stop/ag"], ["Stop all", "/admin/stop-all"],
    ]) {
      f.mockClear();
      fireEvent.click(screen.getByText(label));
      await waitFor(() => expect(f).toHaveBeenCalledTimes(2));
      expect(f.mock.calls[0][0]).toContain(path);
      expect(f.mock.calls[0][1]!.method).toBe("POST");
      expect(f.mock.calls[1][0]).toContain("/traces");
    }
    expect(screen.getByText("a → b")).toBeTruthy();
    expect(screen.queryByText("No agents have run yet.")).toBeNull();
  });
  it("reloads when the API comes online", async () => {
    let up = false;
    const f = stubFetch(() => (up ? ok({ traces: [{ agent_id: "ag", state: "running", steps: ["x"] }] }) : fail(500)));
    const { rerender } = render(<TracePanel agentId="ag" online={false} />);
    await screen.findByRole("alert");
    up = true;
    rerender(<TracePanel agentId="ag" online />);
    await screen.findByText("x");
    expect(f).toHaveBeenCalledTimes(2);
  });
  it("shows errors", async () => {
    stubFetch(() => fail(500));
    render(<TracePanel agentId="ag" online />);
    await screen.findByRole("alert");
  });
});

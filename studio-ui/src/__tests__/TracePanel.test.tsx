import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type { Problem } from "../api/types";
import { TracePanel } from "../components/TracePanel";
import { fail, ok, silentSocket, stubTraces } from "./helpers";

beforeEach(silentSocket);
afterEach(() => vi.unstubAllGlobals());

const none: Problem[] = [];
const props = { agentId: "ag", problems: none, onClearProblems: () => {} };

describe("TracePanel", () => {
  it("shows empty message, then traces, and actions POST then refresh", async () => {
    let traces: unknown[] = [];
    const f = stubTraces((p) => (p.endsWith("/traces") ? ok({ traces }) : ok({})));
    render(<TracePanel {...props} online />);
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
    const f = stubTraces(() => (up ? ok({ traces: [{ agent_id: "ag", state: "running", steps: ["x"] }] }) : fail(500)));
    const { rerender } = render(<TracePanel {...props} online={false} />);
    await screen.findByRole("alert");
    up = true;
    rerender(<TracePanel {...props} online />);
    await screen.findByText("x");
    expect(f.mock.calls.filter(([url]) => url.endsWith("/traces"))).toHaveLength(2);
  });
  it("shows errors", async () => {
    stubTraces(() => fail(500));
    render(<TracePanel {...props} online />);
    await screen.findByRole("alert");
  });
});

describe("TracePanel problems", () => {
  const problem = (id: number, stage: Problem["stage"], message: string): Problem =>
    ({ id, at: "10:00:00", agent: "Agent A", impl: "rules", stage, message });
  const section = () => within(screen.getByRole("region", { name: "Problems" }));

  it("says there are none, with a zero count and no Clear button", async () => {
    stubTraces(() => ok({ traces: [] }));
    render(<TracePanel {...props} online />);
    expect(section().getByText("No errors from checking, saving or running.")).toBeTruthy();
    expect(section().getByRole("heading").textContent).toBe("Problems 0");
    expect(section().queryByRole("button", { name: "Clear problems" })).toBeNull();
    await screen.findByText("No agents have run yet.");
  });
  it("lists each problem with its stage, agent, implementation, time and message, and clears them", async () => {
    stubTraces(() => ok({ traces: [] }));
    const onClear = vi.fn();
    render(<TracePanel {...props} online problems={[problem(2, "check", "line 3 bad"), problem(1, "save", "not allowed")]} onClearProblems={onClear} />);
    expect(section().getByRole("heading").textContent).toBe("Problems 2");
    const items = section().getAllByRole("alert");
    expect(items).toHaveLength(2);
    expect(items[0].textContent).toBe("check · Agent A · rules 10:00:00line 3 bad");
    expect(items[1].textContent).toContain("save");
    expect(items[1].textContent).toContain("not allowed");
    expect(section().queryByText("No errors from checking, saving or running.")).toBeNull();
    fireEvent.click(section().getByRole("button", { name: "Clear problems" }));
    expect(onClear).toHaveBeenCalledTimes(1);
    await screen.findByText("No agents have run yet.");
  });
});

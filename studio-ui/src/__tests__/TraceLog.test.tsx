import { act, fireEvent, render, screen, within } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type { TraceEvent } from "../api/types";
import { SHOWN, TraceLog } from "../components/TraceLog";
import { fail, ok, stubFetch } from "./helpers";

class Socket {
  static all: Socket[] = [];
  onopen: (() => void) | null = null;
  onmessage: ((e: { data: string }) => void) | null = null;
  onclose: (() => void) | null = null;
  onerror: (() => void) | null = null;
  closed = false;
  constructor(public url: string) {
    Socket.all.push(this);
  }
  close() {
    this.closed = true;
  }
  push(events: TraceEvent[]) {
    this.onmessage!({ data: JSON.stringify({ events }) });
  }
}

const ev = (id: number, over: Partial<TraceEvent> = {}): TraceEvent => ({
  id, at: `2026-11-19T10:00:0${id % 10}.000+00:00`, run: "r1", agent: "Roadmap", stage: `stage-${id}`, message: `message ${id}`,
  status: "info", ms: id * 10, detail: {}, ...over,
});
const page = (events: TraceEvent[]) => ok({ events, last_id: events.length ? events[events.length - 1].id : 0, log_file: "/repo/logs/trace.jsonl" });

beforeEach(() => {
  Socket.all = [];
  vi.stubGlobal("WebSocket", Socket);
});
afterEach(() => {
  vi.useRealTimers();
  vi.unstubAllGlobals();
});
const steps = () => within(screen.getByRole("list", { name: "Steps" }));

describe("TraceLog", () => {
  it("is empty until a step is recorded, then lists every step newest first with its detail one click away", async () => {
    stubFetch(() => page([ev(1), ev(2, { status: "ok", detail: { provider: "gemini", tokens: 5 } })]));
    render(<TraceLog online />);
    await screen.findByText("message 2");
    expect(Socket.all[0].url).toBe("ws://localhost:8000/ws/trace?after=2");
    expect(steps().getAllByRole("listitem").map((li) => li.textContent?.includes("stage-2"))).toEqual([true, false]);
    expect(screen.getByRole("heading", { name: "Trace log 2" })).toBeTruthy();
    expect(screen.getByText("/repo/logs/trace.jsonl")).toBeTruthy();
    fireEvent.click(screen.getByText("message 2"));
    expect(screen.getByLabelText("Detail of step 2").textContent).toContain('"provider": "gemini"');
    expect(screen.queryByLabelText("Detail of step 1")).toBeNull(); // a step with no detail has nothing to open
    act(() => Socket.all[0].onopen!());
    expect(screen.getByRole("status").textContent).toContain("Live");
    act(() => Socket.all[0].push([ev(3, { status: "error", message: "it failed" })]));
    expect(steps().getAllByRole("listitem")[0].textContent).toContain("it failed");
    expect(screen.getByRole("heading", { name: "Trace log 3" })).toBeTruthy();
  });

  it("says so when there is nothing yet and when the filters hide everything", async () => {
    stubFetch(() => page([]));
    render(<TraceLog online />);
    await screen.findByText(/No steps yet/);
    expect((screen.getByRole("button", { name: "Clear" }) as HTMLButtonElement).disabled).toBe(true);
    expect((screen.getByRole("button", { name: "Copy" }) as HTMLButtonElement).disabled).toBe(true);
    act(() => Socket.all[0].push([ev(1, { status: "ok" })]));
    fireEvent.change(screen.getByLabelText("Status"), { target: { value: "error" } });
    expect(screen.getByText("No steps match these filters.")).toBeTruthy();
    expect(screen.getByRole("option", { name: "All" })).toBeTruthy();
  });

  it("filters by run and by status, and copies what is shown", async () => {
    stubFetch(() => page([ev(1, { run: "a1", agent: "Alpha" }), ev(2, { run: "b2", agent: "Beta", status: "error" }), ev(3, { run: "b2", agent: "Beta", status: "ok" })]));
    const writeText = vi.fn();
    vi.stubGlobal("navigator", { clipboard: { writeText } });
    render(<TraceLog online />);
    await screen.findByText("message 3");
    expect(screen.getAllByRole("option").map((o) => o.textContent)).toEqual(["All runs", "Beta · b2", "Alpha · a1", "All", "error", "warn", "ok", "info"]);
    fireEvent.change(screen.getByLabelText("Run"), { target: { value: "b2" } });
    expect(steps().getAllByRole("listitem")).toHaveLength(2);
    fireEvent.change(screen.getByLabelText("Status"), { target: { value: "error" } });
    expect(steps().getAllByRole("listitem")).toHaveLength(1);
    fireEvent.click(screen.getByRole("button", { name: "Copy" }));
    expect(writeText).toHaveBeenCalledWith("2026-11-19T10:00:02.000+00:00 b2 ERROR stage-2 message 2");
  });

  it("copying without clipboard access does nothing, and Clear empties the pane through the API", async () => {
    const f = stubFetch((p, init) => (init?.method === "DELETE" ? ok({ cleared: 1 }) : page([ev(1)])));
    render(<TraceLog online />);
    await screen.findByText("message 1");
    fireEvent.click(screen.getByRole("button", { name: "Copy" })); // jsdom has no clipboard: must not throw
    fireEvent.click(screen.getByRole("button", { name: "Clear" }));
    await screen.findByText(/No steps yet/);
    expect(f.mock.calls.some(([url, init]) => url.endsWith("/api/trace/events") && init?.method === "DELETE")).toBe(true);
  });

  it("shows only the latest steps when there are many, and says where the rest is", async () => {
    stubFetch(() => page(Array.from({ length: SHOWN + 5 }, (_, i) => ev(i + 1))));
    render(<TraceLog online />);
    await screen.findByText(`message ${SHOWN + 5}`);
    expect(steps().getAllByRole("listitem")).toHaveLength(SHOWN);
    expect(screen.getByText(`Showing the latest ${SHOWN} of ${SHOWN + 5}. The log file has all of them.`)).toBeTruthy();
  });
});

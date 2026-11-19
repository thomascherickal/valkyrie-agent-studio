import { act, render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { TracePanel } from "../components/TracePanel";
import { ok, stubTraces } from "./helpers";

class FakeSocket {
  static all: FakeSocket[] = [];
  onmessage: ((e: { data: string }) => void) | null = null;
  onclose: (() => void) | null = null;
  onerror: (() => void) | null = null;
  closed = false;
  constructor(public url: string) {
    FakeSocket.all.push(this);
  }
  close() {
    this.closed = true;
  }
  send(traces: unknown) {
    this.onmessage!({ data: JSON.stringify({ traces }) });
  }
}

const stateSockets = () => FakeSocket.all.filter((s) => s.url.endsWith("/ws/traces"));

beforeEach(() => {
  FakeSocket.all = [];
  vi.stubGlobal("WebSocket", FakeSocket);
});
afterEach(() => vi.unstubAllGlobals());

const props = { agentId: "ag", problems: [], onClearProblems: () => {} };
const trace = (state: string, steps: string[]) => [{ agent_id: "ag", state, steps }];

describe("live traces", () => {
  it("shows what the socket sends as it changes, and falls back to the REST list when it closes", async () => {
    stubTraces(() => ok({ traces: trace("stopped", ["from rest"]) }));
    render(<TracePanel {...props} online />);
    await screen.findByText("from rest");
    const socket = stateSockets()[0];
    expect(socket.url).toBe("ws://localhost:8000/ws/traces");
    act(() => socket.send(trace("running", ["a", "b"])));
    expect(screen.getByText("a → b")).toBeTruthy();
    expect(screen.queryByText("from rest")).toBeNull();
    act(() => socket.send(trace("running", ["a", "b", "c"])));
    expect(screen.getByText("a → b → c")).toBeTruthy();
    act(() => socket.onclose!());
    expect(screen.getByText("from rest")).toBeTruthy();
    act(() => socket.send([]));
    expect(screen.getByText("No agents have run yet.")).toBeTruthy();
    act(() => socket.onerror!());
    expect(screen.getByText("from rest")).toBeTruthy();
  });
  it("does not connect until the API is online, and closes the socket when the panel goes away", async () => {
    stubTraces(() => ok({ traces: [] }));
    const { rerender, unmount } = render(<TracePanel {...props} online={false} />);
    expect(stateSockets()).toHaveLength(0);
    rerender(<TracePanel {...props} online />);
    expect(stateSockets()).toHaveLength(1);
    unmount();
    expect(stateSockets()[0].closed).toBe(true);
    expect(stateSockets()[0].onclose).toBeNull();
  });
});

import { act, render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type { TraceEvent } from "../api/types";
import { MAX_EVENTS, POLL_MS, useTraceEvents } from "../hooks/useTraceEvents";
import { deferred, fail, ok, stubFetch } from "./helpers";

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
}

const ev = (id: number): TraceEvent => ({ id, at: "t", run: "r", agent: "a", stage: "s", message: `m${id}`, status: "info", ms: 0, detail: {} });
const page = (events: TraceEvent[]) => ok({ events, last_id: events.length ? events[events.length - 1].id : 0, log_file: "log.jsonl" });

function Probe({ online = true }: { online?: boolean }) {
  const { events, live, logFile } = useTraceEvents(online);
  return <p>{`${events.map((e) => e.id).join(",")}|${live ? "live" : "polling"}|${logFile}|${events.length}`}</p>;
}
const text = () => screen.getByText(/\|/).textContent;
const listCalls = (f: ReturnType<typeof stubFetch>) => f.mock.calls.map(([url]) => url.replace("http://localhost:8000", "")).filter((u) => u.startsWith("/api/trace/events"));

beforeEach(() => {
  Socket.all = [];
  vi.stubGlobal("WebSocket", Socket);
});
afterEach(() => {
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

describe("useTraceEvents", () => {
  it("does nothing while the API is offline", () => {
    const f = stubFetch(() => page([]));
    render(<Probe online={false} />);
    expect(f).not.toHaveBeenCalled();
    expect(Socket.all).toHaveLength(0);
    expect(text()).toBe("|polling||0");
  });

  it("keeps only the newest MAX_EVENTS", async () => {
    stubFetch(() => page(Array.from({ length: MAX_EVENTS + 20 }, (_, i) => ev(i + 1))));
    render(<Probe />);
    await vi.waitFor(() => expect(text()!.endsWith(`|${MAX_EVENTS}`)).toBe(true));
    expect(text()!.startsWith("21,22")).toBe(true);
  });

  it("falls back to polling from the last id when the socket closes, and stops when it goes away", async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    let calls = 0;
    const f = stubFetch(() => (++calls === 1 ? page([ev(1)]) : calls === 2 ? fail(500) : page([ev(2), ev(3)])));
    const { unmount } = render(<Probe />);
    await vi.waitFor(() => expect(Socket.all).toHaveLength(1));
    act(() => Socket.all[0].onclose!());
    expect(Socket.all[0].onclose).toBeNull(); // a second close or error cannot start a second poll
    expect(text()).toBe("1|polling|log.jsonl|1");
    await act(() => vi.advanceTimersByTimeAsync(10)); // the first poll fails: the pane keeps what it has
    expect(text()).toBe("1|polling|log.jsonl|1");
    await act(() => vi.advanceTimersByTimeAsync(POLL_MS + 50));
    expect(text()).toBe("1,2,3|polling|log.jsonl|3");
    expect(listCalls(f).slice(-2)).toEqual(["/api/trace/events?after=1", "/api/trace/events?after=1"]);
    unmount();
    const before = f.mock.calls.length;
    await act(() => vi.advanceTimersByTimeAsync(POLL_MS * 3));
    expect(f.mock.calls.length).toBe(before);
  });

  it("still connects when the first load fails, and closes the socket when it goes away", async () => {
    stubFetch(() => fail(500));
    const { unmount } = render(<Probe />);
    await vi.waitFor(() => expect(Socket.all).toHaveLength(1));
    expect(Socket.all[0].url).toBe("ws://localhost:8000/ws/trace?after=0");
    act(() => Socket.all[0].onopen!());
    expect(text()).toBe("|live||0");
    act(() => Socket.all[0].onerror!());
    expect(text()).toBe("|polling||0");
    unmount();
    const other = render(<Probe />);
    await vi.waitFor(() => expect(Socket.all).toHaveLength(2));
    other.unmount();
    expect(Socket.all[1].closed).toBe(true);
    expect(Socket.all[1].onclose).toBeNull();
  });

  it("does not open a socket if it goes away while the first load is still running", async () => {
    const slow = deferred<unknown>();
    stubFetch(() => slow.promise);
    const { unmount } = render(<Probe />);
    unmount();
    slow.resolve(page([ev(1)]));
    await act(async () => { await slow.promise; });
    expect(Socket.all).toHaveLength(0);
  });

  it("does not poll again if it goes away while a poll is running", async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    const slow = deferred<unknown>();
    let calls = 0;
    const f = stubFetch(() => (++calls === 1 ? page([]) : slow.promise));
    const { unmount } = render(<Probe />);
    await vi.waitFor(() => expect(Socket.all).toHaveLength(1));
    act(() => Socket.all[0].onclose!());
    await act(() => vi.advanceTimersByTimeAsync(10)); // the poll is waiting for its answer
    unmount();
    slow.resolve(page([ev(9)]));
    await act(async () => { await slow.promise; });
    const before = f.mock.calls.length;
    await act(() => vi.advanceTimersByTimeAsync(POLL_MS * 3));
    expect(f.mock.calls.length).toBe(before);
  });
});

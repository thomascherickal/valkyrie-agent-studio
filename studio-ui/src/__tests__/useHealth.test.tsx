import { act, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { HEALTH_MAX_DELAY_MS, HEALTH_MAX_TRIES, HEALTH_RETRY_MS, retryDelay, useHealth } from "../hooks/useHealth";
import { Titlebar } from "../components/Titlebar";
import { fail, ok, stubFetch } from "./helpers";

afterEach(() => {
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

function Probe() {
  const { state, gaveUp, retry } = useHealth();
  return <Titlebar health={state} theme="system" onTheme={() => {}} onDeploy={() => {}} gaveUp={gaveUp} onRetry={retry} />;
}

describe("health retry", () => {
  it("waits longer after each failure, up to a cap", () => {
    expect([0, 1, 2, 3].map(retryDelay)).toEqual([1500, 3000, 6000, 12000]);
    expect(retryDelay(4)).toBe(HEALTH_MAX_DELAY_MS);
    expect(retryDelay(10)).toBe(HEALTH_MAX_DELAY_MS);
    expect(HEALTH_MAX_TRIES).toBe(3); // the studio stops after three retries
  });
  it("stops after the cap, offers Retry, and starts over once the API is back", async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    let up = false;
    const f = stubFetch((p) => (up ? ok({ status: "ok", default_model: "m", thinking_level: "low" }) : fail(500)));
    render(<Probe />);
    expect(screen.queryByRole("button", { name: "Retry connection" })).toBeNull();
    for (let i = 0; i < HEALTH_MAX_TRIES + 2; i++) await act(() => vi.advanceTimersByTimeAsync(HEALTH_MAX_DELAY_MS)); // one retry at a time
    const tries = f.mock.calls.length;
    expect(tries).toBe(HEALTH_MAX_TRIES + 1); // the first check, then HEALTH_MAX_TRIES retries
    await act(() => vi.advanceTimersByTimeAsync(HEALTH_MAX_DELAY_MS * 3));
    expect(f.mock.calls.length).toBe(tries); // no more retries
    up = true;
    fireEvent.click(screen.getByRole("button", { name: "Retry connection" }));
    await screen.findByText("m · low thinking");
    expect(screen.queryByRole("button", { name: "Retry connection" })).toBeNull();
  });
  it("first retry comes after HEALTH_RETRY_MS", async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    const f = stubFetch(() => fail(500));
    render(<Probe />);
    await act(() => vi.advanceTimersByTimeAsync(10));
    expect(f).toHaveBeenCalledTimes(1);
    await act(() => vi.advanceTimersByTimeAsync(HEALTH_RETRY_MS + 50));
    expect(f).toHaveBeenCalledTimes(2);
  });
});

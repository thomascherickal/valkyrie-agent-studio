import { renderHook } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import type { AsyncState } from "../hooks/useAsync";
import { useReported } from "../hooks/useReported";

describe("useReported", () => {
  it("reports an error once, with the agent, implementation and stage", () => {
    const report = vi.fn();
    const error: AsyncState<unknown> = { kind: "error", message: "bad" };
    const { rerender } = renderHook(({ s }) => useReported(s, report, "Agent A", "rules", "save"), { initialProps: { s: error } });
    rerender({ s: error });
    expect(report).toHaveBeenCalledTimes(1);
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "rules", stage: "save", message: "bad" });
  });
  it("ignores every other state", () => {
    const report = vi.fn();
    const states: AsyncState<unknown>[] = [{ kind: "idle" }, { kind: "loading" }, { kind: "done", data: 1 }];
    const { rerender } = renderHook(({ s }) => useReported(s, report, "A", "x", "run"), { initialProps: { s: states[0] } });
    for (const s of states) rerender({ s });
    expect(report).not.toHaveBeenCalled();
  });
});

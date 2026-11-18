import { act, renderHook } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { useAsync } from "../hooks/useAsync";

describe("useAsync", () => {
  it("goes idle, done, reset, error", async () => {
    const { result } = renderHook(() => useAsync(async (x: number) => { if (x < 0) throw new Error("neg"); return x; }));
    expect(result.current.state.kind).toBe("idle");
    let v: unknown;
    await act(async () => { v = await result.current.run(2); });
    expect(v).toBe(2);
    expect(result.current.state).toEqual({ kind: "done", data: 2 });
    act(() => result.current.reset());
    expect(result.current.state.kind).toBe("idle");
    await act(async () => { v = await result.current.run(-1); });
    expect(v).toBeUndefined();
    expect(result.current.state).toEqual({ kind: "error", message: "neg" });
  });
});

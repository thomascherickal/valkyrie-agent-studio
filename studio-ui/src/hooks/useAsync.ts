import { useCallback, useState } from "react";

export type AsyncState<R> =
  | { kind: "idle" }
  | { kind: "loading" }
  | { kind: "done"; data: R }
  | { kind: "error"; message: string };

/** Wraps an async call in idle/loading/done/error state. `run` resolves to the data, or undefined on error. */
export function useAsync<A extends unknown[], R>(fn: (...args: A) => Promise<R>) {
  const [state, setState] = useState<AsyncState<R>>({ kind: "idle" });

  const run = useCallback(
    async (...args: A) => {
      setState({ kind: "loading" });
      try {
        const data = await fn(...args);
        setState({ kind: "done", data });
        return data;
      } catch (error) {
        setState({ kind: "error", message: (error as Error).message });
        return undefined;
      }
    },
    [fn],
  );

  const reset = useCallback(() => setState({ kind: "idle" }), []);

  return { state, run, reset };
}

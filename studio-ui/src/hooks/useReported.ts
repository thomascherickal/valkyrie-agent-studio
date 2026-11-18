import { useEffect } from "react";
import type { Problem } from "../api/types";
import type { AsyncState } from "./useAsync";

export type Report = (problem: Omit<Problem, "id" | "at">) => void;

/** Sends a failed async call to the trace pane, once per failure. */
export function useReported(state: AsyncState<unknown>, report: Report, agent: string, impl: string, stage: Problem["stage"]) {
  useEffect(() => {
    if (state.kind === "error") report({ agent, impl, stage, message: state.message });
  }, [state]);
}

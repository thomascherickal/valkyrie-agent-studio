import React from "react";
import type { AsyncState } from "../hooks/useAsync";

/** Shows the loading and error states of an async call; renders nothing otherwise. */
export function AsyncNotice({ state, working = "Working…" }: { state: AsyncState<unknown>; working?: string }) {
  if (state.kind === "loading") return <p role="status" className="notice">{working}</p>;
  if (state.kind === "error") return <p role="alert" className="notice notice-error">{state.message}</p>;
  return null;
}

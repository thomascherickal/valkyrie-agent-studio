import React, { useEffect } from "react";
import { listTraces, startAgent, stopAgent, stopAll } from "../api/client";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

// Module scope keeps the function identity stable, so useAsync's `run` does not change between renders.
const refresh = async (action?: () => Promise<unknown>) => {
  if (action) await action();
  return (await listTraces()).traces;
};

/** `online` flips true when the API starts answering, which reloads the list after an early failure. */
export function TracePanel({ agentId, online }: { agentId: string; online: boolean }) {
  const { state, run } = useAsync(refresh);
  useEffect(() => {
    run();
  }, [run, online]);

  return (
    <aside className="traces" aria-label="Command Centre">
      <h2>Command Centre</h2>
      <div className="actions">
        <button type="button" onClick={() => run(() => startAgent(agentId))}>Start agent</button>
        <button type="button" onClick={() => run(() => stopAgent(agentId))}>Stop agent</button>
        <button type="button" className="danger" onClick={() => run(stopAll)}>Stop all</button>
      </div>
      <AsyncNotice state={state} working="Loading traces…" />
      {state.kind === "done" && state.data.length === 0 && <p className="empty">No agents have run yet.</p>}
      {state.kind === "done" && (
        <ul aria-label="Agent traces">
          {state.data.map((t) => (
            <li key={t.agent_id}>
              <strong>{t.agent_id}</strong> <span className="badge" data-state={t.state}>{t.state}</span>
              <span className="steps">{t.steps.join(" → ")}</span>
            </li>
          ))}
        </ul>
      )}
    </aside>
  );
}

import React, { useEffect } from "react";
import { listTraces, startAgent, stopAgent, stopAll } from "../api/client";
import type { Problem } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { useTraceStream } from "../hooks/useTraceStream";
import { AsyncNotice } from "./AsyncNotice";

// Module scope keeps the function identity stable, so useAsync's `run` does not change between renders.
const refresh = async (action?: () => Promise<unknown>) => {
  if (action) await action();
  return (await listTraces()).traces;
};

interface TracePanelProps {
  agentId: string;
  /** Flips true when the API starts answering, which reloads the list after an early failure. */
  online: boolean;
  /** Errors from checking, saving and running agents, newest first. */
  problems: Problem[];
  onClearProblems: () => void;
}

export function TracePanel({ agentId, online, problems, onClearProblems }: TracePanelProps) {
  const { state, run } = useAsync(refresh);
  const live = useTraceStream(online);
  const traces = live ?? (state.kind === "done" ? state.data : null);
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
      <section aria-label="Problems" className="problems">
        <h3>
          Problems <span className="count">{problems.length}</span>
        </h3>
        {problems.length === 0 ? (
          <p className="empty">No errors from checking, saving or running.</p>
        ) : (
          <>
            <ul>
              {problems.map((p) => (
                <li key={p.id} role="alert">
                  <strong>{p.stage}</strong> · {p.agent} · {p.impl} <span className="steps">{p.at}</span>
                  <span className="notice-error">{p.message}</span>
                </li>
              ))}
            </ul>
            <button type="button" onClick={onClearProblems}>Clear problems</button>
          </>
        )}
      </section>
      <AsyncNotice state={state} working="Loading traces…" />
      {traces && traces.length === 0 && <p className="empty">No agents have run yet.</p>}
      {traces && (
        <ul aria-label="Agent traces">
          {traces.map((t) => (
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

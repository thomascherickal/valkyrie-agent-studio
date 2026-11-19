import React, { useMemo, useState } from "react";
import type { TraceEvent } from "../api/types";
import { useTraceEvents } from "../hooks/useTraceEvents";

export const SHOWN = 300;
const STATUSES = ["all", "error", "warn", "ok", "info"] as const;

const line = (e: TraceEvent) => `${e.at} ${e.run} ${e.status.toUpperCase()} ${e.stage} ${e.message}`;

/** One step: a summary line, and the full recorded detail when there is any. */
function Step({ e }: { e: TraceEvent }) {
  const summary = (
    <>
      <span className="ms">{e.ms}ms</span> <span className="badge" data-status={e.status}>{e.status}</span> <strong>{e.stage}</strong>{" "}
      <span className="what">{e.message}</span>
    </>
  );
  return Object.keys(e.detail).length === 0 ? (
    <div className="step">{summary}</div>
  ) : (
    <details className="step">
      <summary>{summary}</summary>
      <pre aria-label={`Detail of step ${e.id}`}>{JSON.stringify(e.detail, null, 2)}</pre>
    </details>
  );
}

/** Every step of every run, newest first, with the run and status filters. Details expand in place. */
export function TraceLog({ online }: { online: boolean }) {
  const { events, live, logFile, clear } = useTraceEvents(online);
  const [run, setRun] = useState("all");
  const [status, setStatus] = useState<(typeof STATUSES)[number]>("all");

  const runs = useMemo(() => {
    const seen = new Map<string, string>();
    for (const e of events) if (!seen.has(e.run)) seen.set(e.run, `${e.agent} · ${e.run}`);
    return [...seen].reverse();
  }, [events]);

  const matching = events.filter((e) => (run === "all" || e.run === run) && (status === "all" || e.status === status));
  const shown = matching.slice(-SHOWN).reverse();

  return (
    <section aria-label="Trace log" className="trace-log">
      <h3>
        Trace log <span className="count">{events.length}</span>
      </h3>
      <p className="hint" role="status">
        {live ? "Live" : "Polling"}
        {logFile && <> · also written to <code>{logFile}</code></>}
      </p>
      <div className="actions">
        <label>
          Run
          <select aria-label="Run" value={run} onChange={(e) => setRun(e.target.value)}>
            <option value="all">All runs</option>
            {runs.map(([id, label]) => (
              <option key={id} value={id}>{label}</option>
            ))}
          </select>
        </label>
        <label>
          Status
          <select aria-label="Status" value={status} onChange={(e) => setStatus(e.target.value as typeof status)}>
            {STATUSES.map((s) => (
              <option key={s} value={s}>{s === "all" ? "All" : s}</option>
            ))}
          </select>
        </label>
        <button type="button" onClick={() => navigator.clipboard?.writeText(matching.map(line).join("\n"))} disabled={matching.length === 0}>
          Copy
        </button>
        <button type="button" className="danger" onClick={clear} disabled={events.length === 0}>
          Clear
        </button>
      </div>
      {events.length === 0 && <p className="empty">No steps yet. Run an agent and every step shows up here.</p>}
      {events.length > 0 && matching.length === 0 && <p className="empty">No steps match these filters.</p>}
      <ol aria-label="Steps" className="steps-list">
        {shown.map((e) => (
          <li key={e.id} data-status={e.status}>
            <Step e={e} />
          </li>
        ))}
      </ol>
      {matching.length > SHOWN && <p className="hint">Showing the latest {SHOWN} of {matching.length}. The log file has all of them.</p>}
    </section>
  );
}

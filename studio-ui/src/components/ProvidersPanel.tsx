import React, { useEffect } from "react";
import { getProviders, reloadProviders } from "../api/client";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

export function ProvidersPanel() {
  const status = useAsync(getProviders);
  const reload = useAsync(reloadProviders);
  useEffect(() => {
    status.run();
  }, [status.run]);

  const latest = reload.state.kind === "done" ? reload.state.data : status.state.kind === "done" ? status.state.data : null;
  const changed = reload.state.kind === "done" ? reload.state.data.changed ?? [] : null;

  return (
    <div className="stack">
      <p>
        Model keys live in <code>{latest?.env_path ?? ".env"}</code>, one <code>NAME=value</code> per line.
        The studio shows whether a key is set, never the key. Without a key, runs are simulated.
      </p>
      <AsyncNotice state={status.state} working="Checking keys…" />
      {latest && (
        <ul aria-label="Providers" className="providers">
          {latest.providers.map((p) => (
            <li key={p.id}>
              <strong>{p.id}</strong> <code>{p.env_var}</code>{" "}
              <span className="badge" data-state={p.key_set ? "running" : "stopped"}>{p.key_set ? "key found" : "no key"}</span>
            </li>
          ))}
        </ul>
      )}
      {latest && (
        <>
          <h3>If a provider fails, the next one answers</h3>
          <ol aria-label="Fallback order">
            {latest.fallback.map((f) => (
              <li key={f.provider}>
                <strong>{f.provider}</strong>: {f.models.join(", ")}
              </li>
            ))}
          </ol>
          <p className="hint">OpenCode and OpenRouter use their free models. A provider with no key is skipped, and every step is shown in the Command Centre trace log.</p>
        </>
      )}
      <div className="actions">
        <button type="button" className="primary" disabled={reload.state.kind === "loading"} onClick={() => reload.run()}>
          Reload .env
        </button>
        {changed && (
          <span className="hint" role="status">
            {changed.length === 0 ? "No changes." : `Updated: ${changed.join(", ")}.`}
          </span>
        )}
      </div>
      <AsyncNotice state={reload.state} working="Reloading…" />
    </div>
  );
}

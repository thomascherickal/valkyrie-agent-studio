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
        Model keys live in the <code>{latest?.env_file ?? ".env"}</code> file at the top of the repo, one <code>NAME=value</code> per line.
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

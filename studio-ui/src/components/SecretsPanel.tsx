import React, { useEffect, useState } from "react";
import { getSecrets, reloadProviders, setDefaultProvider } from "../api/client";
import type { SecretEntry, SecretsState } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";
import { SecretCard } from "./SecretCard";

/** Where you keep the keys for Gemini, OpenRouter and OpenCode. Keys are optional: without one, output is simulated. */
export function SecretsPanel() {
  const load = useAsync(getSecrets);
  const reload = useAsync(reloadProviders);
  const choose = useAsync(setDefaultProvider);
  const [data, setData] = useState<SecretsState | null>(null);

  useEffect(() => {
    load.run().then((state) => state && setData(state));
  }, [load.run]);

  const saved = (entry: SecretEntry) =>
    setData((prev) => {
      const secrets = prev!.secrets.map((s) => (s.id === entry.id ? entry : s)); // cards exist only once the data has loaded
      return { ...prev!, secrets, simulated: !secrets.some((s) => s.key_set) };
    });
  const onReload = () => reload.run().then(() => load.run().then((state) => state && setData(state)));
  const onDefault = (provider: string) => choose.run(provider).then((state) => state && setData(state));
  const changed = reload.state.kind === "done" ? reload.state.data.changed ?? [] : null;

  return (
    <div className="stack">
      <p>
        Keys are saved in <code>{data?.env_path ?? ".env"}</code> and are only ever shown as their first 10 characters. Every key is optional.
      </p>
      <AsyncNotice state={load.state} working="Loading…" />
      {data?.simulated && (
        <p role="status" className="notice notice-warn">
          No API keys are set, so every answer is simulated offline. Add a key below to use a real model.
        </p>
      )}
      {data && (
        <>
          <label>
            Default provider
            <select aria-label="Default provider" value={data.default_provider} onChange={(e) => onDefault(e.target.value)}>
              {data.default_providers.map((p) => (
                <option key={p} value={p}>{p}</option>
              ))}
            </select>
          </label>
          <AsyncNotice state={choose.state} working="Saving…" />
          {data.secrets.map((entry) => (
            <SecretCard key={entry.id} entry={entry} efforts={data.efforts} onSaved={saved} />
          ))}
          <h3>If a provider fails, the next one answers</h3>
          <ol aria-label="Fallback order">
            {data.fallback.map((f) => (
              <li key={f.provider}>
                <strong>{f.provider}</strong>: {f.models.join(", ")}
              </li>
            ))}
          </ol>
          <p className="hint">OpenCode and OpenRouter use their free models. A provider with no key is skipped, and every step is shown in the Command Centre trace log.</p>
        </>
      )}
      <div className="actions">
        <button type="button" disabled={reload.state.kind === "loading"} onClick={onReload}>Reload .env</button>
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

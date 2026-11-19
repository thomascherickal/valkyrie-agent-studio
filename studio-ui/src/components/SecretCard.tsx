import React, { useEffect, useState } from "react";
import { getSecretModels, saveSecret, testSecretKey } from "../api/client";
import type { SecretEntry } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

interface SecretCardProps {
  entry: SecretEntry;
  efforts: string[];
  onSaved: (entry: SecretEntry) => void;
}

/** One provider: its masked key, model and effort drop downs, Save, and Test Key with the result and likely causes. */
export function SecretCard({ entry, efforts, onSaved }: SecretCardProps) {
  const { id, label } = entry;
  const [typed, setTyped] = useState<string | null>(null); // null: showing the saved key's masked preview
  const [model, setModel] = useState(entry.model);
  const [effort, setEffort] = useState(entry.effort);
  const models = useAsync(getSecretModels);
  const save = useAsync(saveSecret);
  const test = useAsync(testSecretKey);

  useEffect(() => {
    models.run(id);
  }, [id, models.run, entry.key_set]); // the list is longer once a Gemini key is saved

  const catalog = models.state.kind === "done" ? models.state.data : null;
  const options = catalog?.models ?? [];
  const shown = options.some((m) => m.id === model) ? options : [{ id: model, label: model, free: false }, ...options];
  const changed = (typed !== null && typed !== "") || model !== entry.model || effort !== entry.effort;

  const persist = async (body: { key?: string; model?: string; effort?: string }) => {
    const saved = await save.run(id, body);
    if (saved) {
      setTyped(null);
      setModel(saved.model);
      setEffort(saved.effort);
      onSaved(saved);
    }
  };
  const onSave = () =>
    persist({
      ...(typed ? { key: typed } : {}),
      ...(model !== entry.model ? { model } : {}),
      ...(effort !== null && effort !== entry.effort ? { effort } : {}),
    });
  const result = test.state.kind === "done" ? test.state.data : null;

  return (
    <section aria-label={`${label} secrets`} className="secret-card">
      <h3>
        {label} <span className="badge" data-state={entry.key_set ? "running" : "stopped"}>{entry.key_set ? "key set" : "no key"}</span>
      </h3>
      <label>
        API key
        <input
          aria-label={`${label} API key`}
          type={typed === null ? "text" : "password"}
          autoComplete="off"
          spellCheck={false}
          placeholder={`Paste your ${label} key (optional)`}
          value={typed ?? entry.preview}
          onFocus={() => typed === null && setTyped("")}
          onBlur={() => typed === "" && setTyped(null)}
          onChange={(e) => setTyped(e.target.value)}
        />
      </label>
      <label>
        Model
        <select aria-label={`${label} model`} value={model} onChange={(e) => setModel(e.target.value)}>
          {shown.map((m) => (
            <option key={m.id} value={m.id}>{m.free ? `${m.id} (free)` : m.id}</option>
          ))}
        </select>
      </label>
      {effort !== null && (
        <label>
          Effort
          <select aria-label={`${label} effort`} value={effort} onChange={(e) => setEffort(e.target.value)}>
            {efforts.map((level) => (
              <option key={level} value={level}>{level}</option>
            ))}
          </select>
        </label>
      )}
      {catalog?.note && <p className="hint">{catalog.note}</p>}
      <div className="actions">
        <button type="button" className="primary" disabled={!changed || save.state.kind === "loading"} onClick={onSave}>Save</button>
        <button type="button" disabled={test.state.kind === "loading"} onClick={() => test.run(id, { ...(typed ? { key: typed } : {}), model })}>Test Key</button>
        {entry.key_set && <button type="button" className="danger" disabled={save.state.kind === "loading"} onClick={() => persist({ key: "" })}>Remove key</button>}
      </div>
      <AsyncNotice state={save.state} working="Saving…" />
      <AsyncNotice state={test.state} working="Testing the key…" />
      {result?.ok && <p role="status" className="test-ok">Test Succeeded</p>}
      {result && !result.ok && (
        <div role="alert" className="test-fail">
          <strong>Test Failed</strong>
          <p>{result.message}</p>
          <ul aria-label="Likely causes">
            {result.causes.map((cause) => (
              <li key={cause}>{cause}</li>
            ))}
          </ul>
        </div>
      )}
    </section>
  );
}

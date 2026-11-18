import React, { useState } from "react";
import { runAgent } from "../api/client";
import type { AgentBlueprint } from "../data/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";
import { RunReadout } from "./RunReadout";
import { labelFor, payloadOf, promptOf, type DataField, type Draft } from "./studioState";

interface RunPanelProps {
  agent: AgentBlueprint;
  ir: string;
  draft: Draft;
  onChange: (patch: Partial<Draft>) => void;
}

export function RunPanel({ agent, ir, draft, onChange }: RunPanelProps) {
  const { state, run } = useAsync(runAgent);
  const [blocked, setBlocked] = useState("");
  const { fields } = draft;

  const setField = (i: number, patch: Partial<DataField>) =>
    onChange({ fields: fields.map((f, j) => (j === i ? { ...f, ...patch } : f)) });

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (draft.pythonEnabled && draft.pythonCode.trim() === "") {
      setBlocked("Your Python override is on, but its code has not loaded. Open the Python tab, or turn the override off.");
      return;
    }
    setBlocked("");
    run(ir, promptOf(fields), draft.pythonEnabled ? draft.pythonCode : null, payloadOf(fields));
  };

  return (
    <form onSubmit={submit} className="stack">
      {fields.map((f, i) =>
        f.custom ? (
          <div className="row field" key={i}>
            <input aria-label={`Field name ${i + 1}`} placeholder="Field name" value={f.key} onChange={(e) => setField(i, { key: e.target.value })} />
            <textarea aria-label={`Value of field ${i + 1}`} rows={2} value={f.value} onChange={(e) => setField(i, { value: e.target.value })} />
            <button type="button" onClick={() => onChange({ fields: fields.filter((_, j) => j !== i) })}>
              Remove
            </button>
          </div>
        ) : (
          <label key={i}>
            {labelFor(f.key)}
            <textarea aria-label={labelFor(f.key)} rows={4} value={f.value} onChange={(e) => setField(i, { value: e.target.value })} />
          </label>
        ),
      )}
      <div className="actions">
        <button type="button" onClick={() => onChange({ fields: [...fields, { key: "", value: "", custom: true }] })}>
          Add field
        </button>
        <button type="submit" className="primary" disabled={state.kind === "loading"}>
          Run {agent.name}
        </button>
        {draft.pythonEnabled && <span className="hint">Python override is on. The model is skipped.</span>}
      </div>
      {blocked && <p role="alert" className="notice notice-error">{blocked}</p>}
      <AsyncNotice state={state} working="Running…" />
      {state.kind === "done" && <RunReadout result={state.data} />}
    </form>
  );
}

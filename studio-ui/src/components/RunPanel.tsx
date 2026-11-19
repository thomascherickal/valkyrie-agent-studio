import React from "react";
import { runAgent } from "../api/client";
import type { AgentBlueprint } from "../data/types";
import { useAgentData } from "../hooks/useAgentData";
import { useAsync } from "../hooks/useAsync";
import { useReported, type Report } from "../hooks/useReported";
import { AsyncNotice } from "./AsyncNotice";
import { RunReadout } from "./RunReadout";
import { MODEL, payloadOf, promptOf, type DataField, type Draft, type Patch } from "./studioState";

interface RunPanelProps {
  agent: AgentBlueprint;
  roleId: string;
  ir: string;
  draft: Draft;
  onChange: (patch: Patch) => void;
  report: Report;
}

export function RunPanel({ agent, roleId, ir, draft, onChange, report }: RunPanelProps) {
  const { state, run } = useAsync(runAgent);
  useAgentData(roleId, agent.id, draft, onChange);
  useReported(state, report, agent.name, draft.runWith, "run");
  const { fields, runWith } = draft;
  const usingImpl = runWith !== MODEL;
  const opened = draft.codes[runWith];
  const unsaved = usingImpl && opened !== undefined && draft.texts[runWith] !== opened.code;

  const setField = (i: number, patch: Partial<DataField>) =>
    onChange((d) => ({ fields: d.fields.map((f, j) => (j === i ? { ...f, ...patch } : f)) }));

  // `code` is what is in the editor, to run it without saving. Left out, the saved version runs.
  const start = (code?: string) =>
    run(ir, promptOf(fields), payloadOf(fields), usingImpl ? { roleId, agentId: agent.id, impl: runWith, code } : null);
  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    start();
  };

  return (
    <form onSubmit={submit} className="stack">
      <label>
        Run with
        <select aria-label="Run with" value={runWith} onChange={(e) => onChange({ runWith: e.target.value })}>
          <option value={MODEL}>Gemini 4 Hydrogen (model)</option>
          {(draft.impls ?? []).map((i) => (
            <option key={i.id} value={i.id}>
              Python: {i.label}{i.edited ? " (edited)" : ""}
            </option>
          ))}
        </select>
      </label>
      {fields.map((f, i) =>
        f.custom ? (
          <div className="row field" key={i}>
            <input aria-label={`Field name ${i + 1}`} placeholder="Field name" value={f.key} onChange={(e) => setField(i, { key: e.target.value })} />
            <textarea aria-label={`Value of field ${i + 1}`} rows={2} value={f.value} onChange={(e) => setField(i, { value: e.target.value })} />
            <button type="button" onClick={() => onChange((d) => ({ fields: d.fields.filter((_, j) => j !== i) }))}>
              Remove
            </button>
          </div>
        ) : (
          <label key={i}>
            {f.label}
            {f.kind === "text" || f.kind === "number" ? (
              <input
                aria-label={f.label}
                inputMode={f.kind === "number" ? "decimal" : "text"}
                value={f.value}
                onChange={(e) => setField(i, { value: e.target.value })}
              />
            ) : (
              <textarea aria-label={f.label} rows={f.kind === "list" ? 3 : 4} value={f.value} onChange={(e) => setField(i, { value: e.target.value })} />
            )}
          </label>
        ),
      )}
      <div className="actions">
        <button type="button" onClick={() => onChange((d) => ({ fields: [...d.fields, { key: "", value: "", custom: true, label: "", kind: "text" }] }))}>
          Add field
        </button>
        <button type="submit" className="primary" disabled={state.kind === "loading"}>
          Run agent
        </button>
        {unsaved && (
          <button type="button" onClick={() => start(draft.texts[runWith])} disabled={state.kind === "loading"}>
            Run with my unsaved edits
          </button>
        )}
        {unsaved && <span className="hint">You have unsaved edits to this version. Run agent uses the saved one.</span>}
      </div>
      <AsyncNotice state={state} working="Running…" />
      {state.kind === "done" && <RunReadout result={state.data} />}
    </form>
  );
}

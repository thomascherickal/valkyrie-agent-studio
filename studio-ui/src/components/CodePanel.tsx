import React, { useEffect, useRef } from "react";
import { checkCode, getImpl, removeImpl, saveImpl } from "../api/client";
import type { ImplCode } from "../api/types";
import { useAgentData } from "../hooks/useAgentData";
import { useAsync } from "../hooks/useAsync";
import { useReported, type Report } from "../hooks/useReported";
import { AsyncNotice } from "./AsyncNotice";
import { NewImplForm } from "./NewImplForm";
import { MODEL, withMeta, type Draft, type Patch } from "./studioState";

interface CodePanelProps {
  roleId: string;
  agentId: string;
  agentName: string;
  draft: Draft;
  onChange: (patch: Patch) => void;
  report: Report;
}

export function CodePanel({ roleId, agentId, agentName, draft, onChange, report }: CodePanelProps) {
  useAgentData(roleId, agentId, draft, onChange);
  const load = useAsync(getImpl);
  const save = useAsync(saveImpl);
  const remove = useAsync(removeImpl);
  const check = useAsync(checkCode);
  const live = useRef(true);
  const { impls, editing, codes, texts } = draft;
  const current = codes[editing];
  const text = texts[editing] ?? "";

  // A reply that lands after you moved to another agent must not touch that agent's draft.
  const adopt = (info?: ImplCode) => {
    if (info && live.current) {
      onChange((d) => ({
        codes: { ...d.codes, [info.impl]: info },
        texts: { ...d.texts, [info.impl]: info.code },
        impls: withMeta(d.impls, info),
      }));
    }
  };

  useEffect(() => {
    live.current = true;
    return () => {
      live.current = false;
    };
  }, []);

  // Open the selected implementation once the list is known and its code has not been loaded yet.
  useEffect(() => {
    if (impls !== null && current === undefined) load.run(roleId, agentId, editing).then(adopt);
  }, [impls === null, editing]);

  useReported(save.state, report, agentName, editing, "save");
  useReported(remove.state, report, agentName, editing, "save");
  useEffect(() => {
    if (check.state.kind === "done" && !check.state.data.ok) {
      report({ agent: agentName, impl: editing, stage: "check", message: check.state.data.error! });
    }
  }, [check.state]);

  const onSave = () =>
    save.run(roleId, agentId, editing, text).then((info) => {
      adopt(info);
      if (info) check.run(roleId, agentId, info.code); // run it once, so runtime errors show up too
    });
  const onRevert = () => remove.run(roleId, agentId, editing).then((res) => adopt(res as ImplCode | undefined));
  const onDelete = () =>
    remove.run(roleId, agentId, editing).then((res) => {
      if (res && live.current) {
        onChange((d) => ({
          impls: d.impls!.filter((m) => m.id !== editing),
          editing: "rules",
          runWith: d.runWith === editing ? MODEL : d.runWith,
        }));
      }
    });
  const onCreated = (info: ImplCode) =>
    onChange((d) => ({
      impls: [...d.impls!, { id: info.impl, label: info.label, kind: info.kind, edited: false }],
      codes: { ...d.codes, [info.impl]: info },
      texts: { ...d.texts, [info.impl]: info.code },
      editing: info.impl,
    }));

  const unsaved = current !== undefined && text !== current.code;
  const canRevert = current?.kind === "builtin" && (current.edited || text !== current.original);
  const status =
    current === undefined ? "" : unsaved ? "Unsaved changes" : current.kind === "saved" ? "Saved implementation" : current.edited ? "Edited and saved" : "Original";
  const result = check.state.kind === "done" ? check.state.data : null;

  return (
    <div className="stack">
      <div role="group" aria-label="Implementations" className="chips">
        {(impls ?? []).map((i) => (
          <button key={i.id} type="button" aria-pressed={i.id === editing} onClick={() => onChange({ editing: i.id })}>
            {i.label}{i.edited ? " (edited)" : ""}
          </button>
        ))}
      </div>
      <textarea
        aria-label="Python Source"
        className="code"
        rows={18}
        spellCheck={false}
        readOnly={current === undefined}
        value={text}
        onChange={(e) => onChange((d) => ({ texts: { ...d.texts, [editing]: e.target.value } }))}
      />
      <div className="actions">
        <button type="button" className="primary" disabled={!unsaved || save.state.kind === "loading"} onClick={onSave}>
          Save changes
        </button>
        {current?.kind === "saved" ? (
          <button type="button" className="danger" disabled={remove.state.kind === "loading"} onClick={onDelete}>
            Delete this implementation
          </button>
        ) : (
          <button type="button" disabled={!canRevert || remove.state.kind === "loading"} onClick={onRevert}>
            Revert to original
          </button>
        )}
        <button type="button" disabled={current === undefined || check.state.kind === "loading"} onClick={() => check.run(roleId, agentId, text)}>
          Check for errors
        </button>
        <span className="hint" role="status">{status}</span>
      </div>
      <AsyncNotice state={load.state} working="Loading the code…" />
      <AsyncNotice state={save.state} working="Saving…" />
      <AsyncNotice state={remove.state} working="Working…" />
      <AsyncNotice state={check.state} working="Checking…" />
      {result && result.ok && <p role="status" className="notice">No errors. The code ran once with the sample input.</p>}
      {result && !result.ok && <p role="alert" className="notice notice-error">{result.error}</p>}
      {result && result.warnings.map((w) => <p key={w} className="notice">{w}</p>)}
      <NewImplForm roleId={roleId} agentId={agentId} agentName={agentName} code={text} disabled={current === undefined} onCreated={onCreated} report={report} />
      {current && current.kind === "builtin" && (
        <details>
          <summary>Original code (always kept; never changed)</summary>
          <pre aria-label="Original code">{current.original}</pre>
        </details>
      )}
      <p className="hint">
        Define <code>run_agent(payload)</code> and return a dict. The payload holds your data fields, keyed by name. You can import{" "}
        <code>typing</code>, <code>re</code>, <code>json</code> and <code>math</code>. Errors are listed in the Command Centre.
      </p>
    </div>
  );
}

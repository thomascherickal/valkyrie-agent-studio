import React, { useEffect, useRef } from "react";
import { getAgentCode, revertAgentCode, saveAgentCode } from "../api/client";
import type { AgentCode } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";
import type { Draft } from "./studioState";

interface CodePanelProps {
  roleId: string;
  agentId: string;
  draft: Draft;
  onChange: (patch: Partial<Draft>) => void;
}

export function CodePanel({ roleId, agentId, draft, onChange }: CodePanelProps) {
  const load = useAsync(getAgentCode);
  const save = useAsync(saveAgentCode);
  const revert = useAsync(revertAgentCode);
  const live = useRef(true);
  const info = draft.codeInfo;

  // A reply that lands after you moved to another agent must not overwrite that agent's draft.
  const adopt = (next?: AgentCode) => {
    if (next && live.current) onChange({ codeInfo: next, pythonCode: next.code });
  };

  // Load once per agent. The draft keeps the text, so switching tabs does not lose unsaved edits.
  useEffect(() => {
    live.current = true;
    if (draft.codeInfo === null) load.run(roleId, agentId).then(adopt);
    return () => {
      live.current = false;
    };
  }, [roleId, agentId]);

  const unsaved = info !== null && draft.pythonCode !== info.code;
  const canRevert = info !== null && (info.edited || draft.pythonCode !== info.original);
  const status = info === null ? "" : unsaved ? "Unsaved changes" : info.edited ? "Edited and saved" : "Original";

  return (
    <div className="stack">
      <label className="check">
        <input type="checkbox" checked={draft.pythonEnabled} onChange={(e) => onChange({ pythonEnabled: e.target.checked })} />
        Run my Python instead of the model
      </label>
      <textarea
        aria-label="Python Source"
        className="code"
        rows={16}
        spellCheck={false}
        readOnly={info === null}
        value={draft.pythonCode}
        onChange={(e) => onChange({ pythonCode: e.target.value })}
      />
      <div className="actions">
        <button
          type="button"
          className="primary"
          disabled={!unsaved || save.state.kind === "loading"}
          onClick={() => save.run(roleId, agentId, draft.pythonCode).then(adopt)}
        >
          Save changes
        </button>
        <button
          type="button"
          disabled={!canRevert || revert.state.kind === "loading"}
          onClick={() => revert.run(roleId, agentId).then(adopt)}
        >
          Revert to original
        </button>
        <span className="hint" role="status">{status}</span>
      </div>
      <AsyncNotice state={load.state} working="Loading the code…" />
      <AsyncNotice state={save.state} working="Saving…" />
      <AsyncNotice state={revert.state} working="Reverting…" />
      {info && (
        <details>
          <summary>Original code (kept as it was; never changed)</summary>
          <pre aria-label="Original code">{info.original}</pre>
        </details>
      )}
      <p className="hint">
        Define <code>run_agent(payload)</code> and return a dict. The payload holds your data fields, keyed by name. Only{" "}
        <code>typing</code> can be imported, and os, subprocess, open, eval and exec are blocked.
      </p>
    </div>
  );
}

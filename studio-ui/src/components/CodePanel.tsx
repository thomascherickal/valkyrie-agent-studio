import React from "react";
import type { Draft } from "./studioState";

interface CodePanelProps {
  draft: Draft;
  onChange: (patch: Partial<Draft>) => void;
}

export function CodePanel({ draft, onChange }: CodePanelProps) {
  return (
    <div className="stack">
      <label className="check">
        <input
          type="checkbox"
          checked={draft.pythonEnabled}
          onChange={(e) => onChange({ pythonEnabled: e.target.checked })}
        />
        Run my Python instead of the model
      </label>
      {draft.pythonEnabled && (
        <>
          <textarea
            aria-label="Python Source"
            className="code"
            rows={10}
            spellCheck={false}
            value={draft.pythonCode}
            onChange={(e) => onChange({ pythonCode: e.target.value })}
          />
          <p className="hint">
            Define <code>run_agent(payload)</code> and return a dict. The task arrives as{" "}
            <code>payload["task_input"]</code>. Imports of os and subprocess, open, eval and exec are blocked.
          </p>
        </>
      )}
    </div>
  );
}

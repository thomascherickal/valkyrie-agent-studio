import React, { useState } from "react";
import { runAgent } from "../api/client";
import type { AgentBlueprint } from "../data/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";
import { RunReadout } from "./RunReadout";

interface RunPanelProps {
  agent: AgentBlueprint;
  ir: string;
  customPython: string | null;
}

export function RunPanel({ agent, ir, customPython }: RunPanelProps) {
  const [prompt, setPrompt] = useState(agent.sampleInput);
  const { state, run } = useAsync(runAgent);

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    run(ir, prompt, customPython);
  };

  return (
    <form onSubmit={submit} className="stack">
      <label>
        Task for {agent.name}
        <textarea aria-label="Test Prompt" rows={4} value={prompt} onChange={(e) => setPrompt(e.target.value)} />
      </label>
      <div className="actions">
        <button type="submit" className="primary" disabled={state.kind === "loading"}>
          Run agent
        </button>
        {customPython !== null && <span className="hint">Python override is on. The model is skipped.</span>}
      </div>
      <AsyncNotice state={state} working="Running…" />
      {state.kind === "done" && <RunReadout result={state.data} />}
    </form>
  );
}

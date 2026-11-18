import React, { useState } from "react";
import { createFromPrompt } from "../api/client";
import type { GeneratedBundle } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

const FILES: { label: string; pick: (b: GeneratedBundle) => string }[] = [
  { label: "agent.ir.yaml", pick: (b) => b.ir_yaml },
  { label: "agent.py", pick: (b) => b.agent_py },
  { label: "test_agent.py", pick: (b) => b.test_agent_py },
  { label: "AGENT.md", pick: (b) => b.agent_md },
  { label: "main.rs", pick: (b) => b.main_rs },
];

export function CreatePanel({ onCreated }: { onCreated: (bundle: GeneratedBundle) => void }) {
  const [description, setDescription] = useState("");
  const [name, setName] = useState("");
  const [file, setFile] = useState(0);
  const { state, run } = useAsync(createFromPrompt);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const bundle = await run(description, name);
    if (bundle) {
      setFile(0);
      onCreated(bundle);
    }
  };

  return (
    <form onSubmit={submit} className="stack">
      <label>
        What should the agent do?
        <textarea
          aria-label="Plain-English Agent Description"
          rows={4}
          placeholder="Summarize cloud billing spikes every morning"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </label>
      <label>
        Name (optional)
        <input aria-label="Custom Agent Name" value={name} onChange={(e) => setName(e.target.value)} />
      </label>
      <div className="actions">
        <button type="submit" className="primary" disabled={state.kind === "loading"}>
          Create agent
        </button>
      </div>
      <AsyncNotice state={state} working="Creating…" />
      {state.kind === "done" && (
        <section className="readout" aria-label="Generated files">
          <p className="hint">Created {state.data.name}. It is now under Custom Agents.</p>
          <div role="group" aria-label="Files" className="chips">
            {FILES.map((f, i) => (
              <button key={f.label} type="button" aria-pressed={i === file} onClick={() => setFile(i)}>
                {f.label}
              </button>
            ))}
          </div>
          <pre aria-label="File contents">{FILES[file].pick(state.data)}</pre>
        </section>
      )}
    </form>
  );
}

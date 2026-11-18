import React, { useState } from "react";
import { createImpl } from "../api/client";
import type { ImplCode } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { useReported, type Report } from "../hooks/useReported";
import { AsyncNotice } from "./AsyncNotice";

interface NewImplFormProps {
  roleId: string;
  agentId: string;
  agentName: string;
  /** The code in the editor, which becomes the new implementation. */
  code: string;
  disabled: boolean;
  onCreated: (info: ImplCode) => void;
  report: Report;
}

/** Saves the editor's code as a new implementation next to the built-in ones, which are never replaced. */
export function NewImplForm({ roleId, agentId, agentName, code, disabled, onCreated, report }: NewImplFormProps) {
  const [name, setName] = useState("");
  const { state, run } = useAsync(createImpl);
  useReported(state, report, agentName, name, "save");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const info = await run(roleId, agentId, name, code);
    if (info) {
      setName("");
      onCreated(info);
    }
  };

  return (
    <form onSubmit={submit} className="row field">
      <input aria-label="New implementation name" placeholder="Name for a new implementation" value={name} onChange={(e) => setName(e.target.value)} />
      <button type="submit" disabled={disabled || name.trim() === "" || state.kind === "loading"}>
        Save as new implementation
      </button>
      <AsyncNotice state={state} working="Saving…" />
    </form>
  );
}

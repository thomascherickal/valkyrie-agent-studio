import React, { useEffect, useId, useRef, useState } from "react";
import { saveVerified } from "../api/client";
import type { VerifiedAgent } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

interface SaveVerifiedDialogProps {
  open: boolean;
  roleId: string;
  agentId: string;
  agentName: string;
  onClose: () => void;
  onSaved: (agent: VerifiedAgent) => void;
}

/** A modal box that asks for a name and saves a verified copy of the agent, with its edits, under Custom Agents. */
export function SaveVerifiedDialog({ open, roleId, agentId, agentName, onClose, onSaved }: SaveVerifiedDialogProps) {
  const ref = useRef<HTMLDialogElement>(null);
  const titleId = useId();
  const [name, setName] = useState("");
  const save = useAsync(saveVerified);

  useEffect(() => {
    const dialog = ref.current!;
    if (open && !dialog.open) {
      setName(`${agentName} (verified)`);
      save.reset();
      dialog.showModal();
    } else if (!open && dialog.open) dialog.close();
  }, [open]);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const saved = await save.run(roleId, agentId, name.trim());
    if (saved) onSaved(saved);
  };

  return (
    <dialog ref={ref} aria-labelledby={titleId} onCancel={onClose} className="deploy">
      <h2 id={titleId}>Save the verified agent</h2>
      <form onSubmit={submit} className="stack">
        <p className="hint">It is saved in Custom Agents (the built-in categories are read only), with your edits to its Python.</p>
        <label>
          Agent name
          <input aria-label="Agent name" autoFocus value={name} maxLength={60} onChange={(e) => setName(e.target.value)} />
        </label>
        <AsyncNotice state={save.state} working="Verifying and saving…" />
        <div className="actions">
          <button type="submit" className="primary" disabled={name.trim() === "" || save.state.kind === "loading"}>Save</button>
          <button type="button" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </dialog>
  );
}

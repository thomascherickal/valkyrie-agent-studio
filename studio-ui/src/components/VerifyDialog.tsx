import React, { useEffect, useId, useRef, useState } from "react";
import { verifyAgent } from "../api/client";
import type { VerifiedAgent, VerifyProblem } from "../api/types";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";
import { SaveVerifiedDialog } from "./SaveVerifiedDialog";

interface VerifyDialogProps {
  open: boolean;
  roleId: string;
  agentId: string;
  agentName: string;
  onClose: () => void;
  /** Called when you choose to continue to Deploy to Rust. */
  onDeploy: () => void;
  onSaved: (agent: VerifiedAgent) => void;
}

const where = (p: VerifyProblem) => [p.payload && `on ${p.payload}`, p.line && `line ${p.line}`].filter(Boolean).join(", ");

/** Checks every Python version before Deploy to Rust. Problems block. A pass shows a warning and the choices. */
export function VerifyDialog({ open, roleId, agentId, agentName, onClose, onDeploy, onSaved }: VerifyDialogProps) {
  const ref = useRef<HTMLDialogElement>(null);
  const titleId = useId();
  const [naming, setNaming] = useState(false);
  const verify = useAsync(verifyAgent);

  useEffect(() => {
    const dialog = ref.current!;
    if (open && !dialog.open) {
      setNaming(false);
      dialog.showModal();
      verify.run(roleId, agentId);
    } else if (!open && dialog.open) dialog.close();
  }, [open]);

  const result = verify.state.kind === "done" ? verify.state.data : null;
  const proceed = () => {
    onClose();
    onDeploy();
  };
  const saved = (agent: VerifiedAgent) => {
    setNaming(false);
    onClose();
    onSaved(agent);
  };

  return (
    <>
      <dialog ref={ref} aria-labelledby={titleId} onCancel={onClose} className="deploy">
        <h2 id={titleId}>Verify {agentName} before deploying</h2>
        <AsyncNotice state={verify.state} working="Checking every Python version…" />
        {result && !result.ok && (
          <>
            <p role="alert" className="notice notice-error">{result.problem_count} problem(s) found. Fix them, then deploy.</p>
            <ul aria-label="Problems found">
              {result.checks.filter((c) => !c.ok).map((c) => (
                <li key={c.impl}>
                  <strong>{c.label}</strong>
                  <ul>
                    {c.problems.map((p, i) => (
                      <li key={i}>{p.message} <span className="hint">({p.stage}{where(p) && `, ${where(p)}`})</span></li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>
          </>
        )}
        {result?.ok && (
          <>
            <p role="status" className="test-ok">
              All {result.checks.length} versions passed, each on {result.checks[0].runs} kinds of input.
            </p>
            {result.warning_count > 0 && (
              <ul aria-label="Warnings">
                {result.checks.flatMap((c) => c.warnings.map((w) => <li key={`${c.impl}-${w}`}>{c.label}: {w}</li>))}
              </ul>
            )}
            <p className="notice notice-warn" role="note">
              Warning: Deploy to Rust builds the crate from the agent's definition (name, description and tool). The Python versions checked here are not part of the Rust crate.
            </p>
          </>
        )}
        <div className="actions">
          {result?.ok && <button type="button" className="primary" autoFocus onClick={proceed}>Continue and deploy to Rust</button>}
          {result?.ok && <button type="button" onClick={() => setNaming(true)}>Save verified agent…</button>}
          <button type="button" onClick={onClose}>{result?.ok ? "Cancel" : "Close"}</button>
        </div>
      </dialog>
      <SaveVerifiedDialog open={open && naming} roleId={roleId} agentId={agentId} agentName={agentName} onClose={() => setNaming(false)} onSaved={saved} />
    </>
  );
}

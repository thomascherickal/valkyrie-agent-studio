import React, { useEffect, useId, useRef } from "react";
import type { DeployResult } from "../api/types";
import type { AsyncState } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

interface DeployDialogProps {
  state: AsyncState<DeployResult>;
  onClose: () => void;
}

export function DeployDialog({ state, onClose }: DeployDialogProps) {
  const ref = useRef<HTMLDialogElement>(null);
  const titleId = useId();
  const isOpen = state.kind !== "idle";

  useEffect(() => {
    const dialog = ref.current!;
    if (isOpen && !dialog.open) dialog.showModal();
    else if (!isOpen && dialog.open) dialog.close();
  }, [isOpen]);

  return (
    <dialog ref={ref} aria-labelledby={titleId} onCancel={onClose} className="deploy">
      <h2 id={titleId}>{state.kind === "done" ? `Deployed to Rust: ${state.data.crate_name}` : "Deploy to Rust"}</h2>
      <p className="hint">
        The crate is built from the agent's definition (name, description and tool). It does not include Python you wrote or edited.
      </p>
      <AsyncNotice state={state} working="Building the Rust crate…" />
      {state.kind === "done" && (
        <>
          <p>Benchmark: {state.data.estimated_speedup}</p>
          <pre aria-label="main.rs">{state.data.main_rs}</pre>
        </>
      )}
      <button type="button" autoFocus onClick={onClose}>
        Close
      </button>
    </dialog>
  );
}

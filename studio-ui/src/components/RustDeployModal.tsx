import React, { useEffect, useId, useRef } from "react";

interface RustDeployModalProps {
  isOpen: boolean;
  crateName: string;
  speedup: string;
  onClose: () => void;
}

export function RustDeployModal({ isOpen, crateName, speedup, onClose }: RustDeployModalProps) {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const titleId = useId();

  useEffect(() => {
    const dialog = dialogRef.current!;
    if (isOpen && !dialog.open) {
      dialog.showModal();
    } else if (!isOpen && dialog.open) {
      dialog.close();
    }
  }, [isOpen]);

  return (
    <dialog ref={dialogRef} aria-labelledby={titleId} onCancel={onClose}>
      <h2 id={titleId}>Deployed to Rust: {crateName}</h2>
      <p>Benchmark: {speedup}</p>
      <form method="dialog">
        <button type="button" autoFocus onClick={onClose}>
          Close
        </button>
      </form>
    </dialog>
  );
}

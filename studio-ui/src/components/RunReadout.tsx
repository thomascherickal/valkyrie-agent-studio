import React from "react";
import type { RunResult } from "../api/types";

/** The readout for one run: which engine answered, what it cost, whether the eval gate passed. */
export function RunReadout({ result }: { result: RunResult }) {
  if (result.mode === "python") {
    return (
      <section className="readout" aria-label="Result">
        <ul className="chips">
          <li>{result.impl ? `Python · ${result.impl}` : "Python override"}</li>
          <li>{result.latency_ms} ms</li>
        </ul>
        <pre>{JSON.stringify(result.output, null, 2)}</pre>
      </section>
    );
  }
  return (
    <section className="readout" aria-label="Result">
      <ul className="chips">
        <li>{result.model} · {result.thinking_level}</li>
        <li>{result.input_tokens} in / {result.output_tokens} out</li>
        <li>${result.cost_usd.toFixed(6)}</li>
        <li data-ok={result.eval_passed}>{result.eval_passed ? "Eval passed" : "Eval failed"}</li>
      </ul>
      {result.eval_reasons.map((reason) => (
        <p key={reason} className="notice notice-error">{reason}</p>
      ))}
      <pre>{result.content}</pre>
    </section>
  );
}

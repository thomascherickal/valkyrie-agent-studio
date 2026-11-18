import React, { useEffect } from "react";
import { getExplanation } from "../api/client";
import { useAsync } from "../hooks/useAsync";
import { AsyncNotice } from "./AsyncNotice";

/** What the agent does, the data it needs, how each Python version works, and what you still have to add. */
export function AboutPanel({ roleId, agentId }: { roleId: string; agentId: string }) {
  const { state, run } = useAsync(getExplanation);
  useEffect(() => {
    run(roleId, agentId);
  }, [roleId, agentId]);

  return (
    <div className="stack about">
      <AsyncNotice state={state} working="Loading…" />
      {state.kind === "done" &&
        state.data.sections.map((s) => (
          <section key={s.heading}>
            <h3>{s.heading}</h3>
            <ul>
              {s.bullets.map((b) => (
                <li key={b}>{b}</li>
              ))}
            </ul>
          </section>
        ))}
    </div>
  );
}

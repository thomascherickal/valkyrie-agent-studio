import React from "react";
import type { AgentBlueprint } from "../data/types";

export function AgentSummary({ roleName, agent }: { roleName: string; agent: AgentBlueprint }) {
  return (
    <section className="summary" aria-label="Selected agent">
      <p className="role">{roleName}</p>
      <h2>{agent.name}</h2>
      <p className="description">{agent.description}</p>
      <dl>
        <div>
          <dt>Tool</dt>
          <dd><code>{agent.tool}</code></dd>
        </div>
        <div>
          <dt>Takes</dt>
          <dd><code>{agent.inputKey}</code></dd>
        </div>
        <div>
          <dt>Returns</dt>
          <dd><code>{agent.outputKey}</code></dd>
        </div>
      </dl>
    </section>
  );
}

import React, { useState } from "react";
import type { AgentBlueprint } from "../data/types";

interface AgentSummaryProps {
  roleName: string;
  agent: AgentBlueprint;
  /** Given only for agents you created: shows a Delete button that asks once before deleting. */
  onDelete?: () => void;
}

export function AgentSummary({ roleName, agent, onDelete }: AgentSummaryProps) {
  const [asking, setAsking] = useState(false);
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
      {onDelete && !asking && (
        <button type="button" className="danger" onClick={() => setAsking(true)}>
          Delete agent
        </button>
      )}
      {onDelete && asking && (
        <div className="actions" role="group" aria-label="Confirm delete">
          <span>Delete {agent.name} and its saved edits?</span>
          <button type="button" className="danger" onClick={onDelete}>
            Yes, delete
          </button>
          <button type="button" onClick={() => setAsking(false)}>
            Cancel
          </button>
        </div>
      )}
    </section>
  );
}

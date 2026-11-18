import React from "react";
import type { AgentBlueprint } from "../data/agentCatalog";

interface AgentDocsViewerProps {
  roleName: string;
  agent: AgentBlueprint;
}

export function AgentDocsViewer({ roleName, agent }: AgentDocsViewerProps) {
  return (
    <section className="panel-card" aria-label="Agent Documentation and Demo Preview">
      <h3>
        {agent.name} ({agent.id})
      </h3>
      <p>
        <strong>Role:</strong> {roleName} | <strong>Tool:</strong> <code>{agent.tool}</code>
      </p>
      <p>{agent.description}</p>
      <pre>{`In (${agent.inputKey}): ${agent.sampleInput}\nOut (${agent.outputKey}): [${agent.tool}] Verified`}</pre>
    </section>
  );
}

import React from "react";

export interface AgentTraceItem {
  agentId: string;
  state: "running" | "stopped";
  steps: string[];
}

interface CommandCentreProps {
  traces: AgentTraceItem[];
  onStart: (agentId: string) => void;
  onStop: (agentId: string) => void;
  onAdminStopAll: () => void;
}

export function CommandCentre({ traces, onStart, onStop, onAdminStopAll }: CommandCentreProps) {
  return (
    <section aria-label="Command Centre">
      <h2>Command Centre</h2>
      <div>
        <button type="button" onClick={() => onStart("01-prd-architect")}>
          Start Selected Agent
        </button>
        <button type="button" onClick={() => onStop("01-prd-architect")}>
          Stop Selected Agent
        </button>
        <button type="button" onClick={onAdminStopAll}>
          Admin: Stop All Agents
        </button>
      </div>
      <ul aria-label="Visual Agent Traces">
        {traces.map((t) => (
          <li key={t.agentId}>
            <strong>{t.agentId}</strong> [{t.state}] — Trace: {t.steps.join(" -> ")}
          </li>
        ))}
      </ul>
    </section>
  );
}


import React from "react";

export interface AgentConfigState {
  name: string;
  model: string;
  thinkingLevel: "low" | "medium" | "high";
  provider: "gemini" | "ollama";
  systemPrompt: string;
}

interface VisualAgentCanvasProps {
  config: AgentConfigState;
  onChange: (next: AgentConfigState) => void;
}

export function VisualAgentCanvas({ config, onChange }: VisualAgentCanvasProps) {
  return (
    <section aria-label="Visual Agent Builder">
      <h2>Visual Agent Builder: {config.name}</h2>
      <label>
        Provider
        <select
          value={config.provider}
          onChange={(e) =>
            onChange({ ...config, provider: e.target.value as "gemini" | "ollama" })
          }
        >
          <option value="gemini">Gemini 4 Hydrogen</option>
          <option value="ollama">Local Ollama (qwen3.5:latest)</option>
        </select>
      </label>
      <label>
        Thinking Effort
        <select
          value={config.thinkingLevel}
          onChange={(e) =>
            onChange({ ...config, thinkingLevel: e.target.value as "low" | "medium" | "high" })
          }
        >
          <option value="low">Low (Default)</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </label>
      <label>
        System Prompt
        <textarea
          value={config.systemPrompt}
          onChange={(e) => onChange({ ...config, systemPrompt: e.target.value })}
        />
      </label>
    </section>
  );
}


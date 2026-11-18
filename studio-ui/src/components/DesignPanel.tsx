import React from "react";
import { HOSTED_PROVIDERS } from "../api/client";
import { DEFAULT_MODEL } from "../api/config";
import type { Provider, ThinkingLevel } from "../api/types";
import type { Draft } from "./studioState";

interface DesignPanelProps {
  draft: Draft;
  onChange: (patch: Partial<Draft>) => void;
}

export function DesignPanel({ draft, onChange }: DesignPanelProps) {
  const { settings } = draft;
  return (
    <div className="stack">
      <label>
        System prompt
        <textarea
          aria-label="System Prompt"
          rows={6}
          value={draft.systemPrompt}
          onChange={(e) => onChange({ systemPrompt: e.target.value })}
        />
      </label>
      <div className="row">
        <label>
          Provider
          <select
            aria-label="Provider"
            value={settings.provider}
            onChange={(e) => onChange({ settings: { ...settings, provider: e.target.value as Provider } })}
          >
            <option value="gemini">Gemini 4 Hydrogen</option>
            <option value="ollama">Local Ollama (qwen3.5)</option>
            <option value="openrouter">OpenRouter (free models)</option>
            <option value="opencode">OpenCode (free tier)</option>
          </select>
        </label>
        {HOSTED_PROVIDERS.includes(settings.provider) && (
          <label>
            Model ID
            <input
              aria-label="Model ID"
              placeholder="Model ID from the provider"
              value={settings.hostedModel}
              onChange={(e) => onChange({ settings: { ...settings, hostedModel: e.target.value } })}
            />
          </label>
        )}
        <label>
          Thinking level
          <select
            aria-label="Thinking Level"
            value={settings.thinkingLevel}
            onChange={(e) => onChange({ settings: { ...settings, thinkingLevel: e.target.value as ThinkingLevel } })}
          >
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </label>
      </div>
      <p className="hint">
        Requests ask for {DEFAULT_MODEL} unless you pick another provider. Start the API with GEMINI_API_KEY,
        OPENROUTER_API_KEY or OPENCODE_API_KEY set. Without a key, runs are simulated. Ollama runs offline and
        needs no key.
      </p>
    </div>
  );
}

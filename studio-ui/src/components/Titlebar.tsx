import React from "react";
import type { Health } from "../api/types";
import type { AsyncState } from "../hooks/useAsync";
import type { ThemeMode } from "../theme/ThemeProvider";

interface TitlebarProps {
  health: AsyncState<Health>;
  theme: ThemeMode;
  onTheme: (mode: ThemeMode) => void;
  onDeploy: () => void;
  /** True once the studio stopped retrying the API. Shows a button that starts over. */
  gaveUp?: boolean;
  onRetry?: () => void;
}

function statusText(health: AsyncState<Health>) {
  if (health.kind === "done") return `${health.data.default_model} · ${health.data.thinking_level} thinking`;
  if (health.kind === "error") return "API offline";
  return "Connecting to API…";
}

export function Titlebar({ health, theme, onTheme, onDeploy, gaveUp, onRetry }: TitlebarProps) {
  return (
    <header className="titlebar">
      <h1>Valkyrie Studio</h1>
      <p className="api-status" data-state={health.kind} role="status">
        {statusText(health)}
      </p>
      {gaveUp && (
        <button type="button" onClick={onRetry}>
          Retry connection
        </button>
      )}
      <label>
        Theme
        <select aria-label="Theme Mode" value={theme} onChange={(e) => onTheme(e.target.value as ThemeMode)}>
          <option value="system">System</option>
          <option value="light">Light</option>
          <option value="dark">Dark</option>
        </select>
      </label>
      <button type="button" className="primary" onClick={onDeploy}>
        Deploy to Rust
      </button>
    </header>
  );
}

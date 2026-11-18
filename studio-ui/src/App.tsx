import React, { useState } from "react";
import { useTheme, ThemeMode } from "./theme/ThemeProvider";
import { AGENT_CATALOG } from "./data/agentCatalog";
import { SidebarRoleTree } from "./components/SidebarRoleTree";
import { VisualAgentCanvas, AgentConfigState } from "./components/VisualAgentCanvas";
import { CustomPythonEditor } from "./components/CustomPythonEditor";
import { AgentDocsViewer } from "./components/AgentDocsViewer";
import { SandboxTestConsole } from "./components/SandboxTestConsole";
import { RustDeployModal } from "./components/RustDeployModal";
import { SubscriptionSwitcher, SubscriptionProvider } from "./components/SubscriptionSwitcher";
import { CommandCentre, AgentTraceItem } from "./components/CommandCentre";

export type ExperienceMode = "beginner" | "intermediate" | "advanced";

export function App() {
  const { theme, setThemeMode } = useTheme();
  const [mode, setMode] = useState<ExperienceMode>("beginner");
  const [selectedRoleId, setSelectedRoleId] = useState(AGENT_CATALOG[0].id);
  const [selectedAgentId, setSelectedAgentId] = useState(AGENT_CATALOG[0].agents[0].id);

  const activeRole = AGENT_CATALOG.find((r) => r.id === selectedRoleId)!;
  const activeAgent = activeRole.agents.find((a) => a.id === selectedAgentId)!;

  const [config, setConfig] = useState<AgentConfigState>({
    name: activeAgent.name,
    model: "gemini-4-hydrogen",
    thinkingLevel: "low",
    provider: "gemini",
    systemPrompt: `You are ${activeAgent.name}. ${activeAgent.description}`,
  });
  const [pythonEnabled, setPythonEnabled] = useState(false);
  const [pythonCode, setPythonCode] = useState(`def run_agent(payload):\n    return {"tool": "${activeAgent.tool}", "data": payload}`);
  const [deployOpen, setDeployOpen] = useState(false);
  const [subscription, setSubscription] = useState<SubscriptionProvider>("gemini_free");
  const [traces, setTraces] = useState<AgentTraceItem[]>([
    { agentId: activeAgent.id, state: "running", steps: ["init", activeAgent.tool, "gemini-4-hydrogen:low"] },
  ]);

  const handleSelectAgent = (roleId: string, agentId: string) => {
    setSelectedRoleId(roleId);
    setSelectedAgentId(agentId);
    const role = AGENT_CATALOG.find((r) => r.id === roleId)!;
    const agent = role.agents.find((a) => a.id === agentId)!;
    setConfig((prev) => ({ ...prev, name: agent.name, systemPrompt: `You are ${agent.name}. ${agent.description}` }));
  };

  return (
    <div className="studio-shell">
      <header className="studio-titlebar">
        <h1>Valkyrie AI Agent Studio (Desktop · 120 Agents)</h1>
        <label>
          Theme
          <select aria-label="Theme Mode" value={theme} onChange={(e) => setThemeMode(e.target.value as ThemeMode)}>
            <option value="system">System</option>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </label>
        <label>
          Experience Mode
          <select aria-label="Experience Mode" value={mode} onChange={(e) => setMode(e.target.value as ExperienceMode)}>
            <option value="beginner">Beginner Mode</option>
            <option value="intermediate">Intermediate Mode</option>
            <option value="advanced">Advanced Mode</option>
          </select>
        </label>
        <button type="button" onClick={() => setDeployOpen(true)}>
          Deploy to Rust
        </button>
      </header>
      <SidebarRoleTree roles={AGENT_CATALOG} selectedAgentId={selectedAgentId} onSelectAgent={handleSelectAgent} />
      <main className="studio-workspace">
        <div className="workspace-grid">
          <VisualAgentCanvas config={config} onChange={setConfig} />
          <AgentDocsViewer roleName={activeRole.name} agent={activeAgent} />
        </div>
        {mode !== "beginner" && <CustomPythonEditor code={pythonCode} enabled={pythonEnabled} onToggle={setPythonEnabled} onChange={setPythonCode} />}
        <div className="workspace-grid">
          <SubscriptionSwitcher selected={subscription} onSelect={setSubscription} />
          <SandboxTestConsole model={config.provider === "gemini" ? config.model : "qwen3.5:latest"} thinkingLevel={config.thinkingLevel} onRun={(p) => `[${activeAgent.tool}] ${p}`} />
        </div>
        {mode === "advanced" && (
          <CommandCentre
            traces={traces}
            onStart={(id) => setTraces([{ agentId: id, state: "running", steps: ["init", "running"] }])}
            onStop={(id) => setTraces([{ agentId: id, state: "stopped", steps: ["init", "stopped"] }])}
            onAdminStopAll={() => setTraces((prev) => prev.map((t) => ({ ...t, state: "stopped", steps: [...t.steps, "admin_stop"] })))}
          />
        )}
      </main>
      <RustDeployModal isOpen={deployOpen} crateName={`valkyrie_${selectedAgentId.replace(/-/g, "_")}`} speedup="14.2x lower p99 latency, 0ms GIL pause" onClose={() => setDeployOpen(false)} />
    </div>
  );
}

import React, { useEffect, useState } from "react";
import { buildIr, deployRust, getHealth } from "./api/client";
import type { GeneratedBundle } from "./api/types";
import { AgentBrowser } from "./components/AgentBrowser";
import { AgentSummary } from "./components/AgentSummary";
import { CodePanel } from "./components/CodePanel";
import { CreatePanel } from "./components/CreatePanel";
import { DeployDialog } from "./components/DeployDialog";
import { DesignPanel } from "./components/DesignPanel";
import { MODE_TABS, type ExperienceMode, type TabId } from "./components/modes";
import { RunPanel } from "./components/RunPanel";
import { addCustomAgent, draftFor, findAgent, type Draft } from "./components/studioState";
import { Tabs } from "./components/Tabs";
import { Titlebar } from "./components/Titlebar";
import { TracePanel } from "./components/TracePanel";
import { AGENT_CATALOG } from "./data/agentCatalog";
import { useAsync } from "./hooks/useAsync";
import { useTheme } from "./theme/ThemeProvider";

export type { ExperienceMode } from "./components/modes";

export const HEALTH_RETRY_MS = 1500;

export function App() {
  const { theme, setThemeMode } = useTheme();
  const [roles, setRoles] = useState(AGENT_CATALOG);
  const [mode, setMode] = useState<ExperienceMode>("beginner");
  const [tab, setTab] = useState<TabId>("run");
  const [selection, setSelection] = useState({ roleId: AGENT_CATALOG[0].id, agentId: AGENT_CATALOG[0].agents[0].id });
  const { role, agent } = findAgent(roles, selection.roleId, selection.agentId);
  const [draft, setDraft] = useState<Draft>(() => draftFor(agent));

  const health = useAsync(getHealth);
  const deploy = useAsync(deployRust);
  // Check the API right away, then retry until it answers: the desktop app starts it and it needs a moment.
  // ponytail: retries forever at a fixed interval. Add a cap or backoff if offline noise matters.
  useEffect(() => {
    if (health.state.kind === "done" || health.state.kind === "loading") return;
    const timer = setTimeout(health.run, health.state.kind === "idle" ? 0 : HEALTH_RETRY_MS);
    return () => clearTimeout(timer);
  }, [health.state.kind, health.run]);

  const tabs = MODE_TABS[mode];
  const active = tabs.includes(tab) ? tab : "run";
  const patchDraft = (patch: Partial<Draft>) => setDraft((prev) => ({ ...prev, ...patch }));

  const ir = buildIr(
    { id: agent.id, name: agent.name, role: role.name, description: agent.description, systemPrompt: draft.systemPrompt },
    draft.settings,
    draft.pythonEnabled,
  );

  const select = (roleId: string, agentId: string) => {
    setSelection({ roleId, agentId });
    setDraft(draftFor(findAgent(roles, roleId, agentId).agent));
  };

  const onCreated = (b: GeneratedBundle) => {
    const created = {
      id: b.agent_id,
      name: b.name,
      description: b.description,
      tool: b.tool_name,
      inputKey: "task_input",
      outputKey: "result",
      sampleInput: b.description,
    };
    setRoles((prev) => addCustomAgent(prev, created));
    setSelection({ roleId: "custom-agents", agentId: created.id });
    setDraft(draftFor(created, b.agent_py));
  };

  return (
    <div className="shell">
      <Titlebar
        health={health.state}
        theme={theme}
        onTheme={setThemeMode}
        mode={mode}
        onMode={setMode}
        onDeploy={() => deploy.run(ir)}
      />
      <AgentBrowser roles={roles} selectedAgentId={agent.id} onSelect={select} />
      <main className="workspace">
        <AgentSummary roleName={role.name} agent={agent} />
        <Tabs tabs={tabs} active={active} onChange={setTab} />
        <div role="tabpanel" id="panel" aria-labelledby={`tab-${active}`} className="panel">
          {active === "run" && (
            <RunPanel key={agent.id} agent={agent} ir={ir} customPython={draft.pythonEnabled ? draft.pythonCode : null} />
          )}
          {active === "create" && <CreatePanel onCreated={onCreated} />}
          {active === "design" && <DesignPanel draft={draft} onChange={patchDraft} />}
          {active === "code" && <CodePanel draft={draft} onChange={patchDraft} />}
        </div>
      </main>
      <TracePanel agentId={agent.id} online={health.state.kind === "done"} />
      <DeployDialog state={deploy.state} onClose={deploy.reset} />
    </div>
  );
}

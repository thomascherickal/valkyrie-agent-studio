import React, { useEffect, useState } from "react";
import { buildIr, deleteCustomAgent, deployRust, listCustomAgents } from "./api/client";
import type { GeneratedBundle, Problem } from "./api/types";
import { AboutPanel } from "./components/AboutPanel";
import { AgentBrowser } from "./components/AgentBrowser";
import { AgentSummary } from "./components/AgentSummary";
import { CodePanel } from "./components/CodePanel";
import { CreatePanel } from "./components/CreatePanel";
import { DeployDialog } from "./components/DeployDialog";
import { DesignPanel } from "./components/DesignPanel";
import { SecretsPanel } from "./components/SecretsPanel";
import { MODE_TABS, type ExperienceMode, type TabId } from "./components/modes";
import { RunPanel } from "./components/RunPanel";
import { addCustomAgent, customBlueprint, draftFor, findAgent, MODEL, removeCustomAgent, restoreCustomAgents, type Draft, type Patch } from "./components/studioState";
import { Tabs } from "./components/Tabs";
import { Titlebar } from "./components/Titlebar";
import { TracePanel } from "./components/TracePanel";
import { AGENT_CATALOG } from "./data/agentCatalog";
import { useAsync } from "./hooks/useAsync";
import { useHealth } from "./hooks/useHealth";
import type { Report } from "./hooks/useReported";
import { useTheme } from "./theme/ThemeProvider";

export type { ExperienceMode } from "./components/modes";

export { HEALTH_RETRY_MS } from "./hooks/useHealth";

export function App() {
  const { theme, setThemeMode } = useTheme();
  const [roles, setRoles] = useState(AGENT_CATALOG);
  const [mode, setMode] = useState<ExperienceMode>("beginner");
  const [tab, setTab] = useState<TabId>("run");
  const [selection, setSelection] = useState({ roleId: AGENT_CATALOG[0].id, agentId: AGENT_CATALOG[0].agents[0].id });
  const { role, agent } = findAgent(roles, selection.roleId, selection.agentId);
  const [draft, setDraft] = useState<Draft>(() => draftFor(agent));

  const health = useHealth();
  const deploy = useAsync(deployRust);

  // Agents created in earlier sessions come back from the API once it is online.
  const saved = useAsync(listCustomAgents);
  const online = health.state.kind === "done";
  useEffect(() => {
    if (online) saved.run().then((res) => res && setRoles((prev) => restoreCustomAgents(prev, res.agents)));
  }, [online, saved.run]);

  const tabs = MODE_TABS[mode];
  const active = tabs.includes(tab) ? tab : "run";
  const patchDraft = (patch: Patch) => setDraft((prev) => ({ ...prev, ...(typeof patch === "function" ? patch(prev) : patch) }));

  // Errors from checking, saving and running show in the trace pane. Newest first, at most 50.
  const [problems, setProblems] = useState<Problem[]>([]);
  const report: Report = (p) =>
    setProblems((prev) => [{ ...p, id: (prev[0]?.id ?? 0) + 1, at: new Date().toLocaleTimeString() }, ...prev].slice(0, 50));

  const ir = buildIr(
    { id: agent.id, name: agent.name, role: role.name, description: agent.description, systemPrompt: draft.systemPrompt },
    draft.settings,
    draft.runWith !== MODEL,
  );

  const select = (roleId: string, agentId: string) => {
    setSelection({ roleId, agentId });
    setDraft(draftFor(findAgent(roles, roleId, agentId).agent));
  };

  const onDelete = async () => {
    const res = await deleteCustomAgent(agent.id).catch((e: Error) => report({ agent: agent.name, impl: "-", stage: "save", message: e.message }));
    if (!res) return;
    const rest = removeCustomAgent(roles, agent.id);
    setRoles(rest);
    select(rest[0].id, rest[0].agents[0].id);
  };

  const onCreated = (b: GeneratedBundle) => {
    const created = customBlueprint({ id: b.agent_id, name: b.name, description: b.description, tool: b.tool_name });
    setRoles((prev) => addCustomAgent(prev, created));
    setSelection({ roleId: "custom-agents", agentId: created.id });
    setDraft(draftFor(created));
  };

  return (
    <div className="shell">
      <Titlebar
        health={health.state}
        gaveUp={health.gaveUp}
        onRetry={health.retry}
        theme={theme}
        onTheme={setThemeMode}
        mode={mode}
        onMode={setMode}
        onDeploy={() => deploy.run(ir)}
      />
      <AgentBrowser roles={roles} selectedAgentId={agent.id} onSelect={select} />
      <main className="workspace">
        <AgentSummary roleName={role.name} agent={agent} onDelete={selection.roleId === "custom-agents" ? onDelete : undefined} />
        <Tabs tabs={tabs} active={active} onChange={setTab} />
        <div role="tabpanel" id="panel" aria-labelledby={`tab-${active}`} className="panel">
          {active === "run" && (
            <RunPanel key={agent.id} agent={agent} roleId={selection.roleId} ir={ir} draft={draft} onChange={patchDraft} report={report} />
          )}
          {active === "about" && <AboutPanel key={agent.id} roleId={selection.roleId} agentId={agent.id} />}
          {active === "secrets" && <SecretsPanel />}
          {active === "create" && <CreatePanel onCreated={onCreated} />}
          {active === "design" && <DesignPanel draft={draft} onChange={patchDraft} />}
          {active === "code" && (
            <CodePanel
              key={agent.id}
              roleId={selection.roleId}
              agentId={agent.id}
              agentName={agent.name}
              draft={draft}
              onChange={patchDraft}
              report={report}
            />
          )}
        </div>
      </main>
      <TracePanel agentId={agent.id} online={online} problems={problems} onClearProblems={() => setProblems([])} />
      <DeployDialog state={deploy.state} onClose={deploy.reset} />
    </div>
  );
}

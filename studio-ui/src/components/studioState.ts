import { DEFAULT_SETTINGS } from "../api/client";
import type { ModelSettings } from "../api/types";
import type { AgentBlueprint, RoleCatalog } from "../data/types";

export interface Draft {
  systemPrompt: string;
  settings: ModelSettings;
  pythonEnabled: boolean;
  pythonCode: string;
}

export const CUSTOM_ROLE = { id: "custom-agents", name: "Custom Agents" };

export const DEFAULT_PYTHON = `def run_agent(payload):
    text = str(payload.get("task_input", ""))
    return {"result": text.upper()}
`;

export const draftFor = (agent: AgentBlueprint, pythonCode?: string): Draft => ({
  systemPrompt: `You are ${agent.name}. ${agent.description}`,
  settings: DEFAULT_SETTINGS,
  pythonEnabled: false,
  pythonCode: pythonCode ?? DEFAULT_PYTHON,
});

export const findAgent = (roles: RoleCatalog[], roleId: string, agentId: string) => {
  const role = roles.find((r) => r.id === roleId)!;
  return { role, agent: role.agents.find((a) => a.id === agentId)! };
};

/** Adds (or replaces, by id) an agent in the "Custom Agents" role, creating the role on first use. */
export function addCustomAgent(roles: RoleCatalog[], agent: AgentBlueprint): RoleCatalog[] {
  const existing = roles.find((r) => r.id === CUSTOM_ROLE.id)?.agents ?? [];
  const agents = [...existing.filter((a) => a.id !== agent.id), agent];
  return [...roles.filter((r) => r.id !== CUSTOM_ROLE.id), { ...CUSTOM_ROLE, agents }];
}

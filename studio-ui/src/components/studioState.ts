import { DEFAULT_SETTINGS } from "../api/client";
import type { AgentCode, ModelSettings, SavedAgent } from "../api/types";
import type { AgentBlueprint, RoleCatalog } from "../data/types";

/** One data box on the Run tab. The agent's own input is fixed; extra fields are named by the user. */
export interface DataField {
  key: string;
  value: string;
  custom: boolean;
}

export interface Draft {
  systemPrompt: string;
  settings: ModelSettings;
  pythonEnabled: boolean;
  /** The editor's text. Empty until the agent's code has loaded. */
  pythonCode: string;
  /** What the API last returned for this agent, or null before it has loaded. */
  codeInfo: AgentCode | null;
  fields: DataField[];
}

export const CUSTOM_ROLE = { id: "custom-agents", name: "Custom Agents" };

export const draftFor = (agent: AgentBlueprint): Draft => ({
  systemPrompt: `You are ${agent.name}. ${agent.description}`,
  settings: DEFAULT_SETTINGS,
  pythonEnabled: false,
  pythonCode: "",
  codeInfo: null,
  fields: [{ key: agent.inputKey, value: agent.sampleInput, custom: false }],
});

/** "feature_brief" becomes "Feature brief". */
export const labelFor = (key: string) => key.replace(/_/g, " ").replace(/^./, (c) => c.toUpperCase());

const named = (fields: DataField[]) => fields.filter((f) => f.key.trim() !== "");

/** The payload the agent's run_agent(payload) receives, keyed by field name. */
export const payloadOf = (fields: DataField[]) => Object.fromEntries(named(fields).map((f) => [f.key.trim(), f.value]));

/** The model's prompt: one labelled line per field. */
export const promptOf = (fields: DataField[]) => named(fields).map((f) => `${labelFor(f.key.trim())}: ${f.value}`).join("\n");

export const findAgent = (roles: RoleCatalog[], roleId: string, agentId: string) => {
  const role = roles.find((r) => r.id === roleId)!;
  return { role, agent: role.agents.find((a) => a.id === agentId)! };
};

export const customBlueprint = (a: SavedAgent): AgentBlueprint => ({
  ...a,
  inputKey: "task_input",
  outputKey: "result",
  sampleInput: a.description,
});

/** Puts agents saved by the API back into the "Custom Agents" role. */
export const restoreCustomAgents = (roles: RoleCatalog[], saved: SavedAgent[]) =>
  saved.reduce((acc, a) => addCustomAgent(acc, customBlueprint(a)), roles);

/** Adds (or replaces, by id) an agent in the "Custom Agents" role, creating the role on first use. */
export function addCustomAgent(roles: RoleCatalog[], agent: AgentBlueprint): RoleCatalog[] {
  const existing = roles.find((r) => r.id === CUSTOM_ROLE.id)?.agents ?? [];
  const agents = [...existing.filter((a) => a.id !== agent.id), agent];
  return [...roles.filter((r) => r.id !== CUSTOM_ROLE.id), { ...CUSTOM_ROLE, agents }];
}

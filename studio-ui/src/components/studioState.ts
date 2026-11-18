import { DEFAULT_SETTINGS } from "../api/client";
import type { FieldSpec, ImplCode, ImplMeta, ModelSettings, SavedAgent } from "../api/types";
import type { AgentBlueprint, RoleCatalog } from "../data/types";

/**
 * One data box on the Run tab: the agent's main input, one for each extra piece of data the agent needs
 * (from its playbook), and any you add yourself (custom, with a name you choose).
 */
export interface DataField {
  key: string;
  value: string;
  custom: boolean;
  label: string;
  kind: FieldSpec["kind"];
}

/** An agent's playbook field, as a box that starts with the agent's worked example. */
export const toField = (f: FieldSpec): DataField => ({ key: f.key, value: f.example, custom: false, label: f.label, kind: f.kind });

export const MODEL = "model";

export interface Draft {
  systemPrompt: string;
  settings: ModelSettings;
  /** What Run executes: MODEL, or the id of one of the agent's Python implementations. */
  runWith: string;
  fields: DataField[];
  /** True once the agent's own data fields have been added after its main input. */
  fieldsLoaded: boolean;
  /** The agent's implementations, or null until they have loaded. */
  impls: ImplMeta[] | null;
  /** Which implementation the Python tab is showing. */
  editing: string;
  /** What the API last returned for each implementation opened so far. */
  codes: Record<string, ImplCode>;
  /** The editor's text for each implementation opened so far. Unsaved edits live here. */
  texts: Record<string, string>;
}

/** A change to the draft: the fields to set, or a function of the latest draft (for replies that arrive later). */
export type Patch = Partial<Draft> | ((draft: Draft) => Partial<Draft>);

/** Updates one implementation's `edited` flag in the list, after a save or revert. */
export const withMeta = (impls: ImplMeta[] | null, info: ImplCode) =>
  impls === null ? null : impls.map((m) => (m.id === info.impl ? { ...m, edited: info.edited } : m));

export const CUSTOM_ROLE = { id: "custom-agents", name: "Custom Agents" };

export const draftFor = (agent: AgentBlueprint): Draft => ({
  systemPrompt: `You are ${agent.name}. ${agent.description}`,
  settings: DEFAULT_SETTINGS,
  runWith: MODEL,
  fields: [{ key: agent.inputKey, value: agent.sampleInput, custom: false, label: labelFor(agent.inputKey), kind: "longtext" }],
  fieldsLoaded: false,
  impls: null,
  editing: "rules",
  codes: {},
  texts: {},
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

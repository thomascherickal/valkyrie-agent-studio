import { BASE_URL, DEFAULT_MODEL, DEFAULT_THINKING } from "./config";
import type {
  AgentSpec,
  DeployResult,
  GeneratedBundle,
  Health,
  ModelSettings,
  Provider,
  RunResult,
  SavedAgent,
  Trace,
} from "./types";

export const DEFAULT_SETTINGS: ModelSettings = { provider: "gemini", thinkingLevel: DEFAULT_THINKING, hostedModel: "" };
export const HOSTED_PROVIDERS: Provider[] = ["openrouter", "opencode"];

export class ApiError extends Error {}

async function send<T>(path: string, init?: RequestInit): Promise<T> {
  let res: Response;
  try {
    res = await fetch(BASE_URL + path, init);
  } catch {
    throw new ApiError(`Can't reach the Valkyrie API at ${BASE_URL}. Start it with "make run-gui".`);
  }
  if (!res.ok) {
    const body = await res.json().catch(() => ({ detail: "" }));
    throw new ApiError(body.detail || `The API returned ${res.status}.`);
  }
  return res.json();
}

const get = <T>(path: string) => send<T>(path);
const post = <T>(path: string, body: unknown = {}) =>
  send<T>(path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });

/** Builds the IR the API validates. JSON is valid YAML, so no YAML library is needed. */
export function buildIr(spec: AgentSpec, settings: ModelSettings, customPython: boolean): string {
  return JSON.stringify({
    id: spec.id,
    name: spec.name,
    role: spec.role,
    description: spec.description,
    system_prompt: spec.systemPrompt,
    model_config_spec: {
      provider: settings.provider,
      model: HOSTED_PROVIDERS.includes(settings.provider) ? settings.hostedModel : DEFAULT_MODEL,
      thinking_level: settings.thinkingLevel,
    },
    output_schema: { result: "string" },
    custom_python_enabled: customPython,
  });
}

export const getHealth = () => get<Health>("/health");

export const runAgent = (irYaml: string, prompt: string, customPython: string | null) =>
  post<RunResult>("/api/agents/run", {
    ir_yaml: irYaml,
    prompt,
    custom_python: customPython,
    payload: { task_input: prompt },
  });

export const deployRust = (irYaml: string) => post<DeployResult>("/api/agents/deploy-rust", { ir_yaml: irYaml });

export const createFromPrompt = (prompt: string, name: string) =>
  post<GeneratedBundle>("/api/agents/create-from-prompt", { prompt, name: name || null });

export const listCustomAgents = () => get<{ agents: SavedAgent[] }>("/api/agents/custom");

export const listTraces =() => get<{ traces: Trace[] }>("/api/command-centre/traces");
export const startAgent = (id: string) => post<Trace>(`/api/command-centre/start/${id}`);
export const stopAgent = (id: string) => post<Trace>(`/api/command-centre/stop/${id}`);
export const stopAll = () => post<{ stopped: number }>("/api/command-centre/admin/stop-all");

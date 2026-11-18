export type Provider = "gemini" | "ollama" | "openrouter" | "opencode";
export type ThinkingLevel = "low" | "medium" | "high";

export interface ModelSettings {
  provider: Provider;
  thinkingLevel: ThinkingLevel;
  /** Model ID to request from OpenRouter or OpenCode, which host many models. Unused for Gemini and Ollama. */
  hostedModel: string;
}

export interface AgentSpec {
  id: string;
  name: string;
  role: string;
  description: string;
  systemPrompt: string;
}

export interface Health {
  status: string;
  default_model: string;
  thinking_level: string;
}

export type RunResult =
  | { mode: "python"; impl?: string; output: Record<string, unknown>; latency_ms: number; cost_usd: number }
  | {
      mode: "llm";
      model: string;
      thinking_level: string;
      content: string;
      input_tokens: number;
      output_tokens: number;
      cost_usd: number;
      eval_passed: boolean;
      eval_reasons: string[];
    };

export interface DeployResult {
  crate_name: string;
  cargo_toml: string;
  main_rs: string;
  estimated_speedup: string;
}

/** One of an agent's Python implementations: a built-in (rules, pipeline, hybrid) or one you saved. */
export interface ImplMeta {
  id: string;
  label: string;
  kind: "builtin" | "saved";
  edited: boolean;
}

/** An implementation's code: the untouched original (empty for saved ones) and the code in use. */
export interface ImplCode {
  role_id: string;
  agent_id: string;
  impl: string;
  label: string;
  kind: ImplMeta["kind"];
  edited: boolean;
  original: string;
  code: string;
}

/** The outcome of loading and running code once with the agent's own sample. */
export interface CheckResult {
  ok: boolean;
  error: string | null;
  line: number | null;
  warnings: string[];
}

/** One extra piece of data an agent needs, with a worked example to start from. */
export interface FieldSpec {
  key: string;
  label: string;
  kind: "text" | "longtext" | "number" | "list";
  example: string;
}

export interface Explanation {
  title: string;
  sections: { heading: string; bullets: string[] }[];
  words: number;
}

/** Something that went wrong, shown in the trace pane. */
export interface Problem {
  id: number;
  at: string;
  agent: string;
  impl: string;
  stage: "check" | "save" | "run";
  message: string;
}

/** Which implementation Run should execute. */
export interface RunTarget {
  roleId: string;
  agentId: string;
  impl: string;
}

/** An agent saved by the API under Custom Agents. */
export interface SavedAgent {
  id: string;
  name: string;
  description: string;
  tool: string;
}

export interface GeneratedBundle {
  agent_id: string;
  name: string;
  role: string;
  description: string;
  tool_name: string;
  ir_yaml: string;
  agent_py: string;
  test_agent_py: string;
  agent_md: string;
  main_rs: string;
}

export interface Trace {
  agent_id: string;
  state: string;
  steps: string[];
}

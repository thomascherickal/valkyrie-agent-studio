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
  | { mode: "python"; output: Record<string, unknown>; latency_ms: number; cost_usd: number }
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

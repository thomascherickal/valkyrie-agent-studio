import type { Providers } from "./types";

/** One provider in the Secrets tab. The key is only ever shown as `preview`: its first 10 characters, then asterisks. */
export interface SecretEntry {
  id: "gemini" | "openrouter" | "opencode";
  label: string;
  env_var: string;
  key_set: boolean;
  preview: string;
  model: string;
  /** Gemini's thinking level. Null for the other providers. */
  effort: string | null;
}

export interface SecretsState extends Providers {
  secrets: SecretEntry[];
  default_provider: string;
  default_providers: string[];
  efforts: string[];
  /** True when no provider has a key, so every answer is simulated. */
  simulated: boolean;
}

export interface ModelOption {
  id: string;
  label: string;
  free: boolean;
}

export interface ModelCatalog {
  models: ModelOption[];
  source: "live" | "built-in";
  note: string;
  efforts: string[];
}

/** The result of Test Key. `causes` lists the likely reasons when it failed. */
export interface KeyTestResult {
  ok: boolean;
  status: number | null;
  ms: number;
  provider: string;
  model: string;
  message: string;
  causes: string[];
}

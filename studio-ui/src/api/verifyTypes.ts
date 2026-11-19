/** Something wrong with one Python version of an agent, found by Verify. */
export interface VerifyProblem {
  stage: "syntax" | "blocked" | "run" | "result";
  /** Which input it happened on (for example "no data" or "very long text"). Null for syntax and blocked code. */
  payload: string | null;
  message: string;
  line: number | null;
}

export interface VersionCheck {
  impl: string;
  label: string;
  ok: boolean;
  /** How many different inputs the version was run with. */
  runs: number;
  problems: VerifyProblem[];
  warnings: string[];
}

export interface VerifyResult {
  agent: string;
  ok: boolean;
  checks: VersionCheck[];
  problem_count: number;
  warning_count: number;
}

/** A verified copy saved under Custom Agents. */
export interface VerifiedAgent {
  id: string;
  name: string;
  description: string;
  tool: string;
  input_key: string;
  output_key: string;
  sample: string;
  role_id: string;
  edits_copied: boolean;
}

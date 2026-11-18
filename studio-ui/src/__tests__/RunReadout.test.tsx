import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { RunResult } from "../api/types";
import { RunReadout } from "../components/RunReadout";
import { llmRun } from "./helpers";

describe("RunReadout", () => {
  it("python mode", () => {
    render(<RunReadout result={{ mode: "python", output: { result: "X" }, latency_ms: 7, cost_usd: 0 }} />);
    expect(screen.getByText("Python override")).toBeTruthy();
    expect(screen.getByText("7 ms")).toBeTruthy();
    expect(screen.getByText(/"result": "X"/)).toBeTruthy();
  });
  it("llm passed", () => {
    render(<RunReadout result={llmRun as RunResult} />);
    expect(screen.getByText("Eval passed")).toBeTruthy();
    expect(screen.getByText("$0.500000")).toBeTruthy();
    expect(screen.getByText("gemini-4-hydrogen · low")).toBeTruthy();
    expect(screen.getByText("1 in / 2 out")).toBeTruthy();
  });
  it("llm failed with reasons", () => {
    render(<RunReadout result={{ ...llmRun, eval_passed: false, eval_reasons: ["too short", "no cite"] } as RunResult} />);
    expect(screen.getByText("Eval failed")).toBeTruthy();
    expect(screen.getByText("too short")).toBeTruthy();
    expect(screen.getByText("no cite")).toBeTruthy();
  });
});

import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import { buildIr } from "../api/client";
import { ThemeProvider } from "../theme/ThemeProvider";
import { appRoutes, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());

describe("default model requirement", () => {
  it("every request asks for gemini-4-hydrogen / gemini / low", async () => {
    const f = stubFetch(appRoutes);
    render(<ThemeProvider><App /></ThemeProvider>);
    await screen.findByText("gemini-4-hydrogen · low thinking");
    expect(f.mock.calls.some((c) => String(c[0]).endsWith("/health"))).toBe(true);
    fireEvent.click(screen.getByRole("button", { name: "Run agent" }));
    await screen.findByText("Eval passed");
    fireEvent.click(screen.getByRole("button", { name: "Deploy to Rust" }));
    await screen.findByText(/Deployed to Rust/);
    const bodies = f.mock.calls.map((c) => c[1]?.body).filter((b): b is string => typeof b === "string" && b.includes("ir_yaml"));
    expect(bodies.length).toBeGreaterThanOrEqual(2);
    for (const b of bodies) {
      const cfg = JSON.parse(JSON.parse(b).ir_yaml).model_config_spec;
      expect(cfg).toEqual({ provider: "gemini", model: "gemini-4-hydrogen", thinking_level: "low" });
    }
  });
  it("buildIr keeps the model even for ollama", () => {
    const spec = { id: "i", name: "n", role: "r", description: "d", systemPrompt: "s" };
    const ir = JSON.parse(buildIr(spec, { provider: "ollama", thinkingLevel: "low", hostedModel: "" }, false));
    expect(ir.model_config_spec.model).toBe("gemini-4-hydrogen");
  });
});

import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import { ThemeProvider } from "../theme/ThemeProvider";
import { appRoutes, ok, originalOf, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());

const ROLE = "01-product-management";
const PRD = originalOf(ROLE, "01-prd-architect");
const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const tab = (name: string) => fireEvent.click(screen.getByText(name, { selector: "[role=tab]" }));
const edit = (v: string) => fireEvent.change(source(), { target: { value: v } });
const urls = (f: ReturnType<typeof stubFetch>) => f.mock.calls.map((c) => String(c[0]));

function openPython(routes: typeof appRoutes = appRoutes) {
  const f = stubFetch(routes);
  render(<ThemeProvider><App /></ThemeProvider>);
  fireEvent.change(screen.getByLabelText("Experience Mode"), { target: { value: "advanced" } });
  tab("Python");
  return f;
}

describe("App Python editor", () => {
  it("saves an edit with a PUT, and an unsaved edit survives switching tabs", async () => {
    const f = openPython();
    await waitFor(() => expect(source().value).toBe(PRD));
    edit("x = 1");
    fireEvent.click(screen.getByRole("button", { name: "Save changes" }));
    await screen.findByText("Edited and saved");
    expect(f.mock.calls.find((c) => c[1]?.method === "PUT")![0]).toContain(`/api/agents/${ROLE}/01-prd-architect/code`);
    edit("y = 2");
    tab("Run");
    tab("Python");
    expect(source().value).toBe("y = 2");
    expect(screen.getByText("Unsaved changes")).toBeTruthy();
    expect(urls(f).filter((u) => u.endsWith("/code"))).toHaveLength(2); // one GET, one PUT: no reload
  });
  it("selecting another agent loads that agent's own code", async () => {
    const f = openPython();
    await waitFor(() => expect(source().value).toBe(PRD));
    edit("mine");
    fireEvent.click(screen.getByRole("button", { name: /Roadmap Prioritizer/ }));
    const next = originalOf(ROLE, "02-roadmap-prioritizer");
    await waitFor(() => expect(source().value).toBe(next));
    expect(urls(f)).toContain(`http://localhost:8000/api/agents/${ROLE}/02-roadmap-prioritizer/code`);
  });
  it("a custom agent uses the custom-agents role id", async () => {
    const saved = [{ id: "billing-watch", name: "Billing Watch", description: "Watches billing", tool: "t" }];
    const f = openPython((p, i) => (p === "/api/agents/custom" ? ok({ agents: saved }) : appRoutes(p, i)));
    fireEvent.click(await screen.findByRole("button", { name: "Billing Watch" }));
    await waitFor(() => expect(source().value).toBe(originalOf("custom-agents", "billing-watch")));
    expect(urls(f)).toContain("http://localhost:8000/api/agents/custom-agents/billing-watch/code");
  });
  it("runs the edited code with a payload keyed by the agent's input", async () => {
    const f = openPython();
    await waitFor(() => expect(source().value).toBe(PRD));
    fireEvent.click(screen.getByRole("checkbox"));
    edit("def run_agent(p): return p");
    tab("Run");
    fireEvent.click(screen.getByRole("button", { name: "Run PRD Architect" }));
    await screen.findByText("Eval passed");
    const body = JSON.parse(f.mock.calls.find((c) => String(c[0]).endsWith("/run"))![1]!.body as string);
    expect(body.custom_python).toBe("def run_agent(p): return p");
    expect(Object.keys(body.payload)).toEqual(["feature_brief"]);
    expect(body.prompt).toMatch(/^Feature brief: Add SSO/);
  });
});

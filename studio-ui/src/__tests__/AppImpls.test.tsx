import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import { ThemeProvider } from "../theme/ThemeProvider";
import { calls } from "./Harness";
import { appRoutes, ok, originalOf, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());

const ROLE = "01-product-management";
const PRD = originalOf(ROLE, "01-prd-architect");
const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const tab = (name: string) => fireEvent.click(screen.getByText(name, { selector: "[role=tab]" }));
const edit = (v: string) => fireEvent.change(source(), { target: { value: v } });
const runWith = () => screen.getByLabelText("Run with") as HTMLSelectElement;

function mount(routes: typeof appRoutes = appRoutes) {
  const f = stubFetch(routes);
  render(<ThemeProvider><App /></ThemeProvider>);
  return f;
}

describe("App Python tab", () => {
  it("is visible at Advanced, and an unsaved edit survives switching tabs without reloading", async () => {
    const f = mount();
    tab("Python");
    await waitFor(() => expect(source().value).toBe(PRD));
    edit("y = 2");
    tab("Run");
    tab("Python");
    expect(source().value).toBe("y = 2");
    expect(screen.getByText("Unsaved changes")).toBeTruthy();
    expect(calls(f, "GET", "/implementations/rules")).toHaveLength(1);
  });
  it("selecting another agent loads that agent's own code and resets the draft", async () => {
    const f = mount();
    tab("Python");
    await waitFor(() => expect(source().value).toBe(PRD));
    edit("mine");
    fireEvent.click(screen.getByRole("button", { name: /Roadmap Prioritizer/ }));
    await waitFor(() => expect(source().value).toBe(originalOf(ROLE, "02-roadmap-prioritizer")));
    expect(f.mock.calls.map((c) => String(c[0]))).toContain(`http://localhost:8000/api/agents/${ROLE}/02-roadmap-prioritizer/implementations/rules`);
  });
  it("a custom agent uses the custom-agents role id", async () => {
    const saved = [{ id: "billing-watch", name: "Billing Watch", description: "Watches billing", tool: "t" }];
    const f = mount((p, i) => (p === "/api/agents/custom" ? ok({ agents: saved }) : appRoutes(p, i)));
    fireEvent.click(await screen.findByRole("button", { name: "Billing Watch" }));
    tab("Python");
    await waitFor(() => expect(source().value).toBe(originalOf("custom-agents", "billing-watch")));
    expect(f.mock.calls.map((c) => String(c[0]))).toContain("http://localhost:8000/api/agents/custom-agents/billing-watch/implementations/rules");
  });
});

describe("App running with an implementation", () => {
  it("sends role_id, agent_id, impl and a payload for every field, and turns the Python flag on", async () => {
    const f = mount();
    await screen.findByRole("option", { name: "Python: Pipeline" });
    await screen.findByLabelText("Budget");
    fireEvent.change(runWith(), { target: { value: "pipeline" } });
    fireEvent.click(screen.getByRole("button", { name: "Run agent" }));
    await screen.findByText("Python · pipeline");
    const body = JSON.parse(calls(f, "POST", "/run")[0][1]!.body as string);
    expect(body).toMatchObject({ role_id: ROLE, agent_id: "01-prd-architect", impl: "pipeline" });
    expect(Object.keys(body.payload)).toEqual(["feature_brief", "audience", "budget"]);
    expect(body.prompt).toMatch(/^Feature brief: Add SSO/);
    expect(JSON.parse(body.ir_yaml).custom_python_enabled).toBe(true);
  });
  it("runs the model without a target, and with the Python flag off", async () => {
    const f = mount();
    await screen.findByLabelText("Budget");
    fireEvent.click(screen.getByRole("button", { name: "Run agent" }));
    await screen.findByText("Eval passed");
    const body = JSON.parse(calls(f, "POST", "/run")[0][1]!.body as string);
    expect(body.impl).toBeUndefined();
    expect(JSON.parse(body.ir_yaml).custom_python_enabled).toBe(false);
  });
  it("selecting another agent goes back to the model with that agent's own fields", async () => {
    mount();
    await screen.findByRole("option", { name: "Python: Rules" });
    fireEvent.change(runWith(), { target: { value: "rules" } });
    fireEvent.click(screen.getByRole("button", { name: /Roadmap Prioritizer/ }));
    await waitFor(() => expect(runWith().value).toBe("model"));
    await screen.findByRole("option", { name: "Python: Rules" });
    expect(screen.getAllByLabelText("Budget")).toHaveLength(1);
  });
});

describe("App About tab", () => {
  it("shows the explanation for the agent, and reloads for another", async () => {
    const f = mount(appRoutes);
    tab("About this agent");
    expect(await screen.findByRole("heading", { name: "What it does" })).toBeTruthy();
    expect(screen.getByText("Lists risks")).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: /Roadmap Prioritizer/ }));
    await waitFor(() => expect(calls(f, "GET", "/02-roadmap-prioritizer/explanation")).toHaveLength(1));
    expect(await screen.findByText("Lists risks")).toBeTruthy();
  });
});

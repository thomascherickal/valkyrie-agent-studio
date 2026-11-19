import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import type { AgentBlueprint, RoleCatalog } from "../data/types";
import { AgentSummary } from "../components/AgentSummary";
import { removeCustomAgent } from "../components/studioState";
import { ThemeProvider } from "../theme/ThemeProvider";
import { appRoutes, fail, ok, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());

const blueprint = (id: string): AgentBlueprint => ({ id, name: id, description: "d", tool: "t", inputKey: "i", outputKey: "o", sampleInput: "" });

describe("removeCustomAgent", () => {
  const roles: RoleCatalog[] = [
    { id: "01", name: "One", agents: [blueprint("a")] },
    { id: "custom-agents", name: "Custom Agents", agents: [blueprint("x"), blueprint("y")] },
  ];
  it("removes one agent, and the role when it was the last", () => {
    expect(removeCustomAgent(roles, "x")[1].agents.map((a) => a.id)).toEqual(["y"]);
    expect(removeCustomAgent(removeCustomAgent(roles, "x"), "y").map((r) => r.id)).toEqual(["01"]);
  });
});

describe("AgentSummary delete", () => {
  it("has no Delete button unless it can delete, and asks once before deleting", () => {
    const { rerender } = render(<AgentSummary roleName="R" agent={blueprint("x")} />);
    expect(screen.queryByRole("button", { name: "Delete agent" })).toBeNull();
    const onDelete = vi.fn();
    rerender(<AgentSummary roleName="R" agent={blueprint("x")} onDelete={onDelete} />);
    fireEvent.click(screen.getByRole("button", { name: "Delete agent" }));
    fireEvent.click(screen.getByRole("button", { name: "Cancel" }));
    expect(onDelete).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole("button", { name: "Delete agent" }));
    expect(screen.getByText("Delete x and its saved edits?")).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: "Yes, delete" }));
    expect(onDelete).toHaveBeenCalledTimes(1);
  });
});

async function createAgent() {
  fireEvent.click(screen.getByText("Create agent", { selector: "[role=tab]" }));
  fireEvent.click(screen.getByText("Create agent", { selector: "button[type=submit]" }));
  await screen.findByText(/Created Gen Agent/);
}
const mount = () => render(<ThemeProvider><App /></ThemeProvider>);

describe("deleting a created agent in the app", () => {
  it("removes it from the list and selects the first agent", async () => {
    const f = stubFetch(appRoutes);
    mount();
    await createAgent();
    fireEvent.click(screen.getByRole("button", { name: "Delete agent" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, delete" }));
    await vi.waitFor(() => expect(screen.queryByRole("heading", { name: "Gen Agent" })).toBeNull());
    expect(screen.queryByText("Custom Agents", { selector: "summary" })).toBeNull();
    const del = f.mock.calls.find(([, init]) => init?.method === "DELETE")!;
    expect(del[0]).toBe("http://localhost:8000/api/agents/custom/gen-1");
    expect(screen.queryByRole("button", { name: "Delete agent" })).toBeNull(); // a built-in agent cannot be deleted
  });
  it("keeps the agent and lists a problem when the API refuses", async () => {
    stubFetch((p, init) => (init?.method === "DELETE" ? fail(404, "No custom agent gen-1") : appRoutes(p, init)));
    mount();
    await createAgent();
    fireEvent.click(screen.getByRole("button", { name: "Delete agent" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, delete" }));
    await screen.findByText("No custom agent gen-1");
    expect(screen.getByRole("heading", { name: "Gen Agent" })).toBeTruthy();
  });
  it("shows the Providers tab only at Advanced", () => {
    stubFetch((p, init) => (p === "/api/providers" ? ok({ env_file: ".env", env_path: ".env", providers: [], fallback: [] }) : appRoutes(p, init)));
    mount();
    expect(screen.queryByRole("tab", { name: "Providers" })).toBeNull();
    fireEvent.change(screen.getByLabelText("Experience Mode"), { target: { value: "advanced" } });
    fireEvent.click(screen.getByRole("tab", { name: "Providers" }));
    expect(screen.getByRole("button", { name: "Reload .env" })).toBeTruthy();
  });
});

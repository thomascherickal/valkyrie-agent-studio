import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { SecretsPanel } from "../components/SecretsPanel";
import { fail, modelCatalog, ok, secretsState, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const saved = { ...secretsState.secrets[0], key_set: true, preview: "AQ.Ab8RN6j" + "*".repeat(20) };

function routes(overrides: Record<string, (init?: RequestInit) => unknown> = {}) {
  return (path: string, init?: RequestInit) => {
    const key = `${init?.method ?? "GET"} ${path}`;
    if (overrides[key]) return overrides[key](init);
    if (path.endsWith("/models")) return ok(modelCatalog);
    return ok(secretsState);
  };
}

describe("SecretsPanel", () => {
  it("shows where keys are kept, a warning that output is simulated, the default provider, a card for each provider and the fallback order", async () => {
    stubFetch(routes());
    render(<SecretsPanel />);
    await screen.findByRole("region", { name: "Gemini secrets" });
    expect(screen.getByText("/home/me/.local/share/valkyrie-studio/.env")).toBeTruthy();
    expect(screen.getByRole("status").textContent).toContain("every answer is simulated");
    expect(screen.getAllByRole("region").map((r) => r.getAttribute("aria-label"))).toEqual(["Gemini secrets", "OpenRouter secrets", "OpenCode secrets"]);
    expect(within(screen.getByLabelText("Default provider")).getAllByRole("option").map((o) => o.textContent)).toEqual(["gemini", "openrouter", "opencode", "ollama"]);
    expect(screen.getByRole("list", { name: "Fallback order" }).textContent).toBe("gemini: gemini-4-hydrogenopencode: big-pickle");
  });

  it("drops the warning as soon as a key is saved, and keeps working when it is removed again", async () => {
    stubFetch(routes({ "PUT /api/secrets/gemini": (init) => ok(JSON.parse(init!.body as string).key === "" ? secretsState.secrets[0] : saved) }));
    render(<SecretsPanel />);
    await screen.findByRole("region", { name: "Gemini secrets" });
    const card = within(screen.getByRole("region", { name: "Gemini secrets" }));
    fireEvent.focus(card.getByLabelText("Gemini API key"));
    fireEvent.change(card.getByLabelText("Gemini API key"), { target: { value: "AQ.typed" } });
    fireEvent.click(card.getByRole("button", { name: "Save" }));
    await waitFor(() => expect(screen.queryByText(/every answer is simulated/)).toBeNull());
    expect((card.getByLabelText("Gemini API key") as HTMLInputElement).value).toBe(saved.preview);
    fireEvent.click(card.getByRole("button", { name: "Remove key" }));
    await screen.findByText(/every answer is simulated/);
  });

  it("saves the default provider", async () => {
    const f = stubFetch(routes({ "PUT /api/secrets/default-provider": () => ok({ ...secretsState, default_provider: "openrouter" }) }));
    render(<SecretsPanel />);
    await screen.findByRole("region", { name: "Gemini secrets" });
    fireEvent.change(screen.getByLabelText("Default provider"), { target: { value: "openrouter" } });
    await waitFor(() => expect((screen.getByLabelText("Default provider") as HTMLSelectElement).value).toBe("openrouter"));
    const put = f.mock.calls.find(([url, init]) => init?.method === "PUT" && String(url).endsWith("/default-provider"))!;
    expect(JSON.parse(put[1]!.body as string)).toEqual({ provider: "openrouter" });
  });

  it("Reload .env re-reads the file, reports what changed and refreshes the keys shown", async () => {
    let loads = 0;
    stubFetch(routes({
      "GET /api/secrets": () => ok(++loads === 1 ? secretsState : { ...secretsState, secrets: [saved, ...secretsState.secrets.slice(1)], simulated: false }),
      "POST /api/providers/reload": () => ok({ ...secretsState, changed: ["GEMINI_API_KEY"] }),
    }));
    render(<SecretsPanel />);
    await screen.findByText(/every answer is simulated/);
    fireEvent.click(screen.getByRole("button", { name: "Reload .env" }));
    await screen.findByText("Updated: GEMINI_API_KEY.");
    await waitFor(() => expect(screen.queryByText(/every answer is simulated/)).toBeNull());
    expect(screen.getByText("key set")).toBeTruthy();
  });

  it("says when a reload changed nothing", async () => {
    stubFetch(routes({ "POST /api/providers/reload": () => ok(secretsState) })); // no `changed` list
    render(<SecretsPanel />);
    await screen.findByRole("region", { name: "Gemini secrets" });
    fireEvent.click(screen.getByRole("button", { name: "Reload .env" }));
    await screen.findByText("No changes.");
  });

  it("reports an API that cannot be reached and still offers Reload", async () => {
    stubFetch(() => fail(500));
    render(<SecretsPanel />);
    await screen.findByRole("alert");
    expect(screen.getByText(/only ever shown as their first 10 characters/)).toBeTruthy();
    expect(screen.getByRole("button", { name: "Reload .env" })).toBeTruthy();
  });
});

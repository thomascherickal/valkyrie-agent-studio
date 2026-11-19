import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { ProvidersPanel } from "../components/ProvidersPanel";
import { fail, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const status = (keySet: boolean[], changed?: string[]) => ({
  env_file: ".env",
  env_path: "/home/me/.local/share/valkyrie-studio/.env",
  providers: ["gemini", "openrouter", "opencode"].map((id, i) => ({ id, env_var: `${id.toUpperCase()}_API_KEY`, key_set: keySet[i] })),
  fallback: [
    { provider: "gemini", models: ["gemini-4-hydrogen"] },
    { provider: "opencode", models: ["big-pickle", "mimo-free"] },
    { provider: "openrouter", models: ["openrouter/free"] },
  ],
  ...(changed && { changed }),
});

describe("ProvidersPanel", () => {
  it("shows which keys are set, and a reload picks up a key you just pasted", async () => {
    let keys = [false, false, false];
    const f = stubFetch((p) => ok(p.endsWith("/reload") ? status([true, false, false], ["GEMINI_API_KEY"]) : status(keys)));
    render(<ProvidersPanel />);
    await screen.findByText("OPENROUTER_API_KEY");
    expect(screen.getAllByText("no key")).toHaveLength(3);
    expect(screen.getByText("/home/me/.local/share/valkyrie-studio/.env")).toBeTruthy();
    expect(screen.getByRole("list", { name: "Fallback order" }).textContent).toBe("gemini: gemini-4-hydrogenopencode: big-pickle, mimo-freeopenrouter: openrouter/free");
    keys = [true, false, false];
    fireEvent.click(screen.getByRole("button", { name: "Reload .env" }));
    await screen.findByText("Updated: GEMINI_API_KEY.");
    expect(screen.getByText("key found")).toBeTruthy();
    expect(f.mock.calls[f.mock.calls.length - 1][1]!.method).toBe("POST");
  });
  it("says when nothing changed", async () => {
    stubFetch((p) => ok(status([false, false, false]))  /* a reload reply without a `changed` list also means no changes */);
    render(<ProvidersPanel />);
    fireEvent.click(await screen.findByRole("button", { name: "Reload .env" }));
    await screen.findByText("No changes.");
  });
  it("reports an API that cannot be reached", async () => {
    stubFetch(() => fail(500));
    render(<ProvidersPanel />);
    await screen.findByRole("alert");
    expect(screen.getByText(/never the key/)).toBeTruthy();
  });
});

import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import { ThemeProvider } from "../theme/ThemeProvider";
import { appRoutes, fail, ok, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());
const mount = () => render(<ThemeProvider><App /></ThemeProvider>);

const saved = [
  { id: "billing-watch", name: "Billing Watch", description: "Watches billing", tool: "run_billing_watch" },
  { id: "iam-audit", name: "IAM Audit", description: "Audits IAM", tool: "run_iam_audit" },
];

describe("agents saved by earlier sessions", () => {
  it("come back under Custom Agents once the API is online, and can be opened", async () => {
    stubFetch((p) => (p === "/api/agents/custom" ? ok({ agents: saved }) : appRoutes(p)));
    mount();
    await screen.findByText("Custom Agents", { selector: "summary" });
    fireEvent.click(await screen.findByRole("button", { name: "Billing Watch" }));
    expect(screen.getByRole("heading", { name: "Billing Watch" })).toBeTruthy();
    expect(screen.getByText("Watches billing", { selector: ".description" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "IAM Audit" })).toBeTruthy();
  });

  it("are skipped quietly when the list cannot be loaded", async () => {
    stubFetch((p) => (p === "/api/agents/custom" ? fail(500) : appRoutes(p)));
    mount();
    await screen.findByText("gemini-4-hydrogen · low thinking");
    await vi.waitFor(() => expect(fetch).toHaveBeenCalledWith(expect.stringContaining("/api/agents/custom"), undefined));
    expect(screen.queryByText("Custom Agents", { selector: "summary" })).toBeNull();
    expect(screen.getByRole("heading", { name: "PRD Architect" })).toBeTruthy();
  });
});

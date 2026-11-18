import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import { ThemeProvider } from "../theme/ThemeProvider";
import { appRoutes, fail, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());
const mount = () => render(<ThemeProvider><App /></ThemeProvider>);
const mode = (v: string) => fireEvent.change(screen.getByLabelText("Experience Mode"), { target: { value: v } });
const tabs = () => screen.getAllByRole("tab").map((t) => t.textContent);

describe("App modes and tabs", () => {
  it("gates tabs by mode and falls back to Run", () => {
    stubFetch(appRoutes);
    mount();
    expect(tabs()).toEqual(["Run", "Create agent"]);
    mode("intermediate");
    expect(tabs()).toEqual(["Run", "Create agent", "Design"]);
    mode("advanced");
    expect(tabs()).toEqual(["Run", "Create agent", "Design", "Python"]);
    fireEvent.click(screen.getByText("Python"));
    fireEvent.click(screen.getByRole("checkbox"));
    expect(screen.getByLabelText("Python Source")).toBeTruthy();
    mode("beginner");
    expect(screen.getByText("Run agent")).toBeTruthy();
    mode("advanced");
    fireEvent.click(screen.getByText("Design"));
    fireEvent.change(screen.getByLabelText("System Prompt"), { target: { value: "custom" } });
    expect((screen.getByLabelText("System Prompt") as HTMLTextAreaElement).value).toBe("custom");
    fireEvent.click(screen.getByText("Run", { selector: "[role=tab]" }));
    expect(screen.getByText(/Python override is on/)).toBeTruthy();
  });
  it("shows API offline", async () => {
    stubFetch((p) => (p === "/health" ? fail(500) : appRoutes(p)));
    mount();
    await screen.findByText("API offline");
  });
});

describe("App flow", () => {
  it("selecting an agent resets the draft", () => {
    stubFetch(appRoutes);
    mount();
    mode("intermediate");
    fireEvent.click(screen.getByText("Design"));
    fireEvent.change(screen.getByLabelText("System Prompt"), { target: { value: "edited" } });
    const other = screen.getAllByRole("button").find((b) => b.getAttribute("aria-current") === "false")!;
    fireEvent.click(other);
    expect((screen.getByLabelText("System Prompt") as HTMLTextAreaElement).value).toMatch(/^You are /);
  });
  it("create adds a custom agent and selects it; deploy opens dialog", async () => {
    stubFetch(appRoutes);
    mount();
    fireEvent.click(screen.getByText("Create agent", { selector: "[role=tab]" }));
    fireEvent.click(screen.getByText("Create agent", { selector: "button[type=submit]" }));
    await screen.findByText(/Created Gen Agent/);
    expect(screen.getByText("Custom Agents", { selector: "summary" })).toBeTruthy();
    expect(screen.getByRole("heading", { name: "Gen Agent" })).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: "Deploy to Rust" }));
    await screen.findByText("Deployed to Rust: crate-x");
    fireEvent.click(screen.getByText("Close"));
    await waitFor(() => expect(document.querySelector("dialog")!.open).toBe(false));
  });
});

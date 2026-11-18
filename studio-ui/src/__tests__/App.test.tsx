import { act, fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { App } from "../App";
import { ThemeProvider } from "../theme/ThemeProvider";

describe("Valkyrie AI Agent Studio Desktop UI", () => {
  it("exercises 120-agent catalog, theme modes, experience modes, native dialog, and command centre", () => {
    HTMLDialogElement.prototype.showModal = function () {
      this.setAttribute("open", "");
    };
    HTMLDialogElement.prototype.close = function () {
      this.removeAttribute("open");
    };

    const meta = document.createElement("meta");
    meta.setAttribute("name", "color-scheme");
    meta.setAttribute("content", "light dark");
    document.head.appendChild(meta);

    render(
      <ThemeProvider>
        <App />
      </ThemeProvider>
    );

    // Theme modes (dark, light, system) + storage event sync
    const themeSelect = screen.getByLabelText("Theme Mode");
    fireEvent.change(themeSelect, { target: { value: "dark" } });
    expect(meta.getAttribute("content")).toBe("dark");
    fireEvent.change(themeSelect, { target: { value: "light" } });
    expect(meta.getAttribute("content")).toBe("light");
    fireEvent.change(themeSelect, { target: { value: "system" } });
    expect(meta.getAttribute("content")).toBe("light dark");

    act(() => {
      window.dispatchEvent(new StorageEvent("storage", { key: "color-scheme", newValue: "dark" }));
      window.dispatchEvent(new StorageEvent("storage", { key: "color-scheme", newValue: "light" }));
      window.dispatchEvent(new StorageEvent("storage", { key: "color-scheme", newValue: null }));
      window.dispatchEvent(new StorageEvent("storage", { key: "other", newValue: "x" }));
    });

    // Search and select from 120-agent catalog
    const search = screen.getByPlaceholderText("Search 120 agents...");
    fireEvent.change(search, { target: { value: "Rust Port" } });
    fireEvent.click(screen.getByRole("button", { name: "Rust Port Advisor" }));

    // Visual builder
    fireEvent.change(screen.getByLabelText("Provider"), { target: { value: "ollama" } });
    fireEvent.change(screen.getByLabelText("Thinking Effort"), { target: { value: "high" } });
    fireEvent.change(screen.getByLabelText("System Prompt"), { target: { value: "Updated prompt" } });

    // Intermediate mode -> Custom Python editor
    const modeSelect = screen.getByLabelText("Experience Mode");
    fireEvent.change(modeSelect, { target: { value: "intermediate" } });
    fireEvent.click(screen.getByLabelText("Enable Custom Python Override"));
    fireEvent.change(screen.getByLabelText("Python Source"), { target: { value: "def run_agent(p): return p" } });

    // Subscription switcher + Sandbox test
    fireEvent.change(screen.getByLabelText("Subscription Provider"), { target: { value: "openrouter_free" } });
    fireEvent.change(screen.getByLabelText("Test Prompt"), { target: { value: "hello" } });
    fireEvent.click(screen.getByRole("button", { name: "Run Sandbox Test" }));
    expect(screen.getByText(/\[estimate_rust_speedup\] hello/)).toBeTruthy();

    // Advanced mode -> Command Centre
    fireEvent.change(modeSelect, { target: { value: "advanced" } });
    fireEvent.click(screen.getByRole("button", { name: "Start Selected Agent" }));
    fireEvent.click(screen.getByRole("button", { name: "Stop Selected Agent" }));
    fireEvent.click(screen.getByRole("button", { name: "Admin: Stop All Agents" }));

    // Native <dialog> Rust deploy modal
    const dialog = document.querySelector("dialog")!;
    fireEvent.click(screen.getByRole("button", { name: "Deploy to Rust" }));
    expect(dialog.hasAttribute("open")).toBe(true);
    fireEvent.click(screen.getByRole("button", { name: "Close" }));
    expect(dialog.hasAttribute("open")).toBe(false);
  });
});

import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { CodePanel } from "../components/CodePanel";
import { DesignPanel } from "../components/DesignPanel";
import { draftFor } from "../components/studioState";

const draft = draftFor({ id: "a", name: "A", description: "d", tool: "", inputKey: "", outputKey: "", sampleInput: "" });

describe("DesignPanel", () => {
  it("reports provider, thinking and prompt changes", () => {
    const onChange = vi.fn();
    render(<DesignPanel draft={draft} onChange={onChange} />);
    fireEvent.change(screen.getByLabelText("Provider"), { target: { value: "ollama" } });
    expect(onChange).toHaveBeenLastCalledWith({ settings: { provider: "ollama", thinkingLevel: "low", hostedModel: "" } });
    fireEvent.change(screen.getByLabelText("Thinking Level"), { target: { value: "high" } });
    expect(onChange).toHaveBeenLastCalledWith({ settings: { provider: "gemini", thinkingLevel: "high", hostedModel: "" } });
    expect(screen.queryByLabelText("Model ID")).toBeNull();
    fireEvent.change(screen.getByLabelText("System Prompt"), { target: { value: "new" } });
    expect(onChange).toHaveBeenLastCalledWith({ systemPrompt: "new" });
    expect(screen.getByText(/gemini-4-hydrogen/)).toBeTruthy();
  });
});

describe("DesignPanel hosted providers", () => {
  it("offers OpenRouter and OpenCode and asks for a model ID", () => {
    const onChange = vi.fn();
    const { rerender } = render(<DesignPanel draft={draft} onChange={onChange} />);
    expect(screen.getByRole("option", { name: /OpenRouter/ })).toBeTruthy();
    expect(screen.getByRole("option", { name: /OpenCode/ })).toBeTruthy();
    fireEvent.change(screen.getByLabelText("Provider"), { target: { value: "openrouter" } });
    expect(onChange).toHaveBeenLastCalledWith({ settings: { ...draft.settings, provider: "openrouter" } });

    const hosted = { ...draft, settings: { ...draft.settings, provider: "opencode" as const } };
    rerender(<DesignPanel draft={hosted} onChange={onChange} />);
    fireEvent.change(screen.getByLabelText("Model ID"), { target: { value: "acme/free" } });
    expect(onChange).toHaveBeenLastCalledWith({ settings: { ...hosted.settings, hostedModel: "acme/free" } });
  });
});

describe("CodePanel", () => {
  it("hides editor until enabled, then edits", () => {
    const onChange = vi.fn();
    const { rerender } = render(<CodePanel draft={draft} onChange={onChange} />);
    expect(screen.queryByLabelText("Python Source")).toBeNull();
    fireEvent.click(screen.getByRole("checkbox"));
    expect(onChange).toHaveBeenLastCalledWith({ pythonEnabled: true });
    rerender(<CodePanel draft={{ ...draft, pythonEnabled: true }} onChange={onChange} />);
    fireEvent.change(screen.getByLabelText("Python Source"), { target: { value: "x=1" } });
    expect(onChange).toHaveBeenLastCalledWith({ pythonCode: "x=1" });
  });
});

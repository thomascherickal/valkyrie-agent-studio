import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { AgentBrowser } from "../components/AgentBrowser";

const a = (id: string, name: string) => ({ id, name, description: "", tool: "", inputKey: "", outputKey: "", sampleInput: "" });
const roles = [
  { id: "r1", name: "Alpha", agents: [a("a1", "Writer"), a("a2", "Reader")] },
  { id: "r2", name: "Beta", agents: [a("b1", "Coder")] },
];

describe("AgentBrowser", () => {
  it("opens only the selected role and selects agents", () => {
    const onSelect = vi.fn();
    const { container } = render(<AgentBrowser roles={roles} selectedAgentId="b1" onSelect={onSelect} />);
    const [d1, d2] = Array.from(container.querySelectorAll("details"));
    expect(d1.open).toBe(false);
    expect(d2.open).toBe(true);
    fireEvent.click(screen.getByText("Writer"));
    expect(onSelect).toHaveBeenCalledWith("r1", "a1");
    expect(screen.getByText("Coder").getAttribute("aria-current")).toBe("true");
  });
  it("filters, opens matches, and shows empty state", () => {
    const { container } = render(<AgentBrowser roles={roles} selectedAgentId="b1" onSelect={vi.fn()} />);
    const search = screen.getByLabelText("Search agents");
    fireEvent.change(search, { target: { value: " read " } });
    expect(container.querySelectorAll("details")).toHaveLength(1);
    expect(container.querySelector("details")!.open).toBe(true);
    fireEvent.change(search, { target: { value: "zzz" } });
    expect(screen.getByText(/No agent matches/)).toBeTruthy();
  });
});

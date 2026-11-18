import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { AgentSummary } from "../components/AgentSummary";
import { AsyncNotice } from "../components/AsyncNotice";
import { MODE_TABS } from "../components/modes";
import { Tabs } from "../components/Tabs";

describe("small components", () => {
  it("AgentSummary", () => {
    render(<AgentSummary roleName="Role" agent={{ id: "i", name: "Nm", description: "Desc", tool: "tl", inputKey: "ik", outputKey: "ok", sampleInput: "" }} />);
    expect(screen.getByText("tl")).toBeTruthy();
    expect(screen.getByText("Role")).toBeTruthy();
  });
  it("AsyncNotice states", () => {
    const { container, rerender } = render(<AsyncNotice state={{ kind: "idle" }} />);
    expect(container.innerHTML).toBe("");
    rerender(<AsyncNotice state={{ kind: "loading" }} />);
    expect(screen.getByRole("status").textContent).toBe("Working…");
    rerender(<AsyncNotice state={{ kind: "loading" }} working="Busy" />);
    expect(screen.getByRole("status").textContent).toBe("Busy");
    rerender(<AsyncNotice state={{ kind: "error", message: "boom" }} />);
    expect(screen.getByRole("alert").textContent).toBe("boom");
    rerender(<AsyncNotice state={{ kind: "done", data: 1 }} />);
    expect(container.innerHTML).toBe("");
  });
  it("Tabs", () => {
    const onChange = vi.fn();
    render(<Tabs tabs={MODE_TABS.advanced} active="design" onChange={onChange} />);
    expect(screen.getAllByRole("tab")).toHaveLength(5);
    expect(screen.getByText("Design").getAttribute("aria-selected")).toBe("true");
    fireEvent.click(screen.getByText("Python"));
    expect(onChange).toHaveBeenCalledWith("code");
  });
});

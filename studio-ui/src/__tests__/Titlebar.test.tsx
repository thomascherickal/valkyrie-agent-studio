import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { Titlebar } from "../components/Titlebar";
import type { AsyncState } from "../hooks/useAsync";
import type { Health } from "../api/types";
import { health } from "./helpers";

const setup = (state: AsyncState<Health>) => {
  const p = { onTheme: vi.fn(), onMode: vi.fn(), onDeploy: vi.fn() };
  render(<Titlebar health={state} theme="system" mode="beginner" {...p} />);
  return p;
};

describe("Titlebar", () => {
  it.each([
    [{ kind: "idle" }, "Connecting to API…"],
    [{ kind: "loading" }, "Connecting to API…"],
    [{ kind: "error", message: "x" }, "API offline"],
    [{ kind: "done", data: health }, "gemini-4-hydrogen · low thinking"],
  ] as [AsyncState<Health>, string][])("shows %j status", (state, text) => {
    setup(state);
    expect(screen.getByRole("status").textContent).toBe(text);
  });
  it("fires callbacks", () => {
    const p = setup({ kind: "idle" });
    fireEvent.change(screen.getByLabelText("Experience Mode"), { target: { value: "advanced" } });
    fireEvent.change(screen.getByLabelText("Theme Mode"), { target: { value: "dark" } });
    fireEvent.click(screen.getByText("Deploy to Rust"));
    expect(p.onMode).toHaveBeenCalledWith("advanced");
    expect(p.onTheme).toHaveBeenCalledWith("dark");
    expect(p.onDeploy).toHaveBeenCalled();
  });
});

import { render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { AboutPanel } from "../components/AboutPanel";
import { appRoutes, fail, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

describe("AboutPanel", () => {
  it("shows the explanation's bullets under their headings", async () => {
    const f = stubFetch(appRoutes);
    render(<AboutPanel roleId="r1" agentId="a1" />);
    expect(screen.getByText("Loading…")).toBeTruthy();
    expect(await screen.findByRole("heading", { name: "What it does" })).toBeTruthy();
    expect(screen.getByRole("heading", { name: "Data it needs" })).toBeTruthy();
    expect(screen.getAllByRole("listitem").map((li) => li.textContent)).toEqual(["Writes PRDs", "Lists risks", "Audience"]);
    expect(f.mock.calls[0][0]).toBe("http://localhost:8000/api/agents/r1/a1/explanation");
  });
  it("loads again for another agent", async () => {
    const f = stubFetch(appRoutes);
    const { rerender } = render(<AboutPanel roleId="r1" agentId="a1" />);
    await screen.findByText("Writes PRDs");
    rerender(<AboutPanel roleId="r2" agentId="b2" />);
    await screen.findByText("Writes PRDs");
    expect(f.mock.calls.map(([u]) => u)).toEqual([
      "http://localhost:8000/api/agents/r1/a1/explanation", "http://localhost:8000/api/agents/r2/b2/explanation",
    ]);
  });
  it("shows an error instead of sections", async () => {
    stubFetch(() => fail(500, "no explanation"));
    render(<AboutPanel roleId="r1" agentId="a1" />);
    expect((await screen.findByRole("alert")).textContent).toBe("no explanation");
    expect(screen.queryByRole("heading")).toBeNull();
  });
});

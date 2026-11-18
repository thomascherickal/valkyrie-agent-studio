import { fireEvent, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { calls, mountCode, status } from "./Harness";
import { appRoutes, fail, originalOf, seedSaved } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const button = (name: string) => screen.getByRole("button", { name }) as HTMLButtonElement;
const edit = (v: string) => fireEvent.change(source(), { target: { value: v } });
const ORIGINAL = originalOf("r1", "a1");
const ready = () => waitFor(() => expect(source().value).toBe(ORIGINAL));

describe("CodePanel revert (built-ins)", () => {
  it("is disabled while the code is the original, and there is no Delete", async () => {
    mountCode();
    await ready();
    expect(button("Revert to original").disabled).toBe(true);
    expect(screen.queryByRole("button", { name: /Delete/ })).toBeNull();
  });
  it("reverts unsaved edits to the original", async () => {
    const { f } = mountCode();
    await ready();
    edit("x = 1");
    expect(button("Revert to original").disabled).toBe(false);
    fireEvent.click(button("Revert to original"));
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    expect(calls(f, "DELETE", "/implementations/rules")).toHaveLength(1);
    expect(status()).toBe("Original");
  });
  it("reverts a saved edit, even when the editor already matches it", async () => {
    mountCode();
    await ready();
    edit("x = 1");
    fireEvent.click(button("Save changes"));
    await screen.findByText("Edited and saved");
    expect(button("Revert to original").disabled).toBe(false);
    fireEvent.click(button("Revert to original"));
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    expect(status()).toBe("Original");
    expect(button("Rules")).toBeTruthy(); // no longer marked (edited)
  });
  it("reports a failed revert", async () => {
    const { report } = mountCode(undefined, (p, i) => (i?.method === "DELETE" ? fail(500, "cannot revert") : appRoutes(p, i)));
    await ready();
    edit("x = 1");
    fireEvent.click(button("Revert to original"));
    await screen.findByText("cannot revert");
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "rules", stage: "save", message: "cannot revert" });
    expect(source().value).toBe("x = 1");
  });
});

describe("CodePanel saved implementations", () => {
  /** Routes that put a saved implementation "Mine" in the fake API before the first request, optionally failing DELETE. */
  const routes = (failDelete = false) => {
    let seeded = false;
    return (p: string, i?: RequestInit) => {
      if (!seeded) seeded = !!seedSaved("r1", "a1", "Mine", "mine = 1");
      return failDelete && i?.method === "DELETE" ? fail(500, "cannot delete") : appRoutes(p, i);
    };
  };
  const openMine = async (initial?: Parameters<typeof mountCode>[0], failDelete = false) => {
    const view = mountCode(initial, routes(failDelete));
    fireEvent.click(await screen.findByRole("button", { name: "Mine" }));
    await waitFor(() => expect(source().value).toBe("mine = 1"));
    return view;
  };
  it("shows Delete instead of Revert, no original code, and edits through Save", async () => {
    await openMine();
    expect(status()).toBe("Saved implementation");
    expect(screen.queryByRole("button", { name: "Revert to original" })).toBeNull();
    expect(screen.queryByLabelText("Original code")).toBeNull();
    edit("mine = 2");
    expect(status()).toBe("Unsaved changes");
    fireEvent.click(button("Save changes"));
    await waitFor(() => expect(status()).toBe("Saved implementation"));
  });
  it("Delete removes it and goes back to Rules; Run keeps its choice when it was another", async () => {
    const { f } = await openMine({ runWith: "pipeline" });
    fireEvent.click(button("Delete this implementation"));
    await waitFor(() => expect(screen.queryByRole("button", { name: "Mine" })).toBeNull());
    expect(calls(f, "DELETE", "/implementations/saved-mine")).toHaveLength(1);
    expect(screen.getByTestId("state").textContent).toBe("rules|pipeline");
    expect(button("Rules").getAttribute("aria-pressed")).toBe("true");
  });
  it("Delete resets Run to the model when it was running that implementation", async () => {
    await openMine({ runWith: "saved-mine" });
    expect(screen.getByTestId("state").textContent).toBe("saved-mine|saved-mine");
    fireEvent.click(button("Delete this implementation"));
    await waitFor(() => expect(screen.getByTestId("state").textContent).toBe("rules|model"));
  });
  it("reports a failed delete and keeps the implementation", async () => {
    const { report } = await openMine(undefined, true);
    fireEvent.click(button("Delete this implementation"));
    await screen.findByText("cannot delete");
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "saved-mine", stage: "save", message: "cannot delete" });
    expect(button("Mine")).toBeTruthy();
  });
});

import { fireEvent, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { calls, mountCode, status } from "./Harness";
import { appRoutes, originalOf, seedSaved } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const nameBox = () => screen.getByLabelText("New implementation name") as HTMLInputElement;
const create = () => screen.getByRole("button", { name: "Save as new implementation" }) as HTMLButtonElement;
const type = (name: string) => fireEvent.change(nameBox(), { target: { value: name } });
const ready = () => waitFor(() => expect(source().value).toBe(originalOf("r1", "a1")));

describe("Save as new implementation", () => {
  it("needs a name, and the code to be loaded", async () => {
    mountCode();
    type("Early");
    expect(create().disabled).toBe(true); // code not loaded yet
    await ready();
    expect(create().disabled).toBe(false);
    type("   ");
    expect(create().disabled).toBe(true);
    type("");
    expect(create().disabled).toBe(true);
  });
  it("creates it from the editor's code and switches to it", async () => {
    const { f, report } = mountCode();
    await ready();
    fireEvent.change(source(), { target: { value: "copy = 1" } });
    type("My Copy");
    fireEvent.click(create());
    await waitFor(() => expect(screen.getByRole("button", { name: "My Copy" }).getAttribute("aria-pressed")).toBe("true"));
    expect(JSON.parse(calls(f, "POST", "/implementations")[0][1]!.body as string)).toEqual({ name: "My Copy", code: "copy = 1" });
    expect(source().value).toBe("copy = 1");
    expect(status()).toBe("Saved implementation");
    expect(nameBox().value).toBe("");
    expect(screen.getByTestId("state").textContent).toBe("saved-my-copy|model");
    expect(screen.getByRole("button", { name: "Delete this implementation" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "Rules" }).getAttribute("aria-pressed")).toBe("false");
    expect(report).not.toHaveBeenCalled();
    expect(calls(f, "GET", "/implementations/saved-my-copy")).toHaveLength(0); // already known: not reloaded
  });
  it("reports a duplicate name (409) and keeps the form", async () => {
    let seeded = false;
    const { report } = mountCode(undefined, (p, i) => {
      if (!seeded) seeded = !!seedSaved("r1", "a1", "Mine", "x");
      return appRoutes(p, i);
    });
    await ready();
    type("Mine");
    fireEvent.click(create());
    await screen.findByText("That name is already used");
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "Mine", stage: "save", message: "That name is already used" });
    expect(nameBox().value).toBe("Mine");
    expect(screen.getAllByRole("button", { name: "Mine" })).toHaveLength(1);
    expect(screen.getByTestId("state").textContent).toBe("rules|model");
  });
});

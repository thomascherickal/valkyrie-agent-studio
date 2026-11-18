import { fireEvent, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { calls, mountCode, status } from "./Harness";
import { appRoutes, fail, ok, originalOf } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const button = (name: string) => screen.getByRole("button", { name }) as HTMLButtonElement;
const edit = (v: string) => fireEvent.change(source(), { target: { value: v } });
const ORIGINAL = originalOf("r1", "a1");

describe("CodePanel loading", () => {
  it("loads the list, then the selected implementation's code", async () => {
    const { f } = mountCode();
    expect(source().readOnly).toBe(true);
    expect(button("Check for errors").disabled).toBe(true);
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    expect(source().readOnly).toBe(false);
    expect(["Rules", "Pipeline", "Hybrid"].map((n) => button(n).getAttribute("aria-pressed"))).toEqual(["true", "false", "false"]);
    expect(calls(f, "GET", "/implementations")).toHaveLength(1);
    expect(calls(f, "GET", "/implementations/rules")).toHaveLength(1);
    expect(screen.getByLabelText("Original code").textContent).toBe(ORIGINAL);
    expect(status()).toBe("Original");
  });
  it("picking another implementation loads it, and going back does not reload", async () => {
    const { f } = mountCode();
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    fireEvent.click(button("Pipeline"));
    await waitFor(() => expect(source().value).toBe(originalOf("r1", "a1", "pipeline")));
    expect(button("Pipeline").getAttribute("aria-pressed")).toBe("true");
    fireEvent.click(button("Rules"));
    expect(source().value).toBe(ORIGINAL);
    expect(calls(f, "GET", "/implementations/rules")).toHaveLength(1);
    expect(calls(f, "GET", "/implementations/pipeline")).toHaveLength(1);
  });
  it("shows the error and stays read-only when the code cannot be loaded", async () => {
    mountCode(undefined, (p, i) => (p.endsWith("/implementations/rules") ? fail(500, "no code") : appRoutes(p, i)));
    await screen.findByText("no code");
    expect(source().readOnly).toBe(true);
    expect(source().value).toBe("");
    expect(screen.queryByLabelText("Original code")).toBeNull();
  });
  it("shows no implementations until the list arrives, and none when it fails", async () => {
    const { f } = mountCode(undefined, (p, i) => (p.endsWith("/implementations") ? fail(500, "no list") : appRoutes(p, i)));
    await waitFor(() => expect(calls(f, "GET", "/implementations")).toHaveLength(1));
    expect(screen.queryByRole("button", { name: "Rules" })).toBeNull();
    expect(calls(f, "GET", "/implementations/rules")).toHaveLength(0);
  });
});

describe("CodePanel editing", () => {
  it("an edit shows Unsaved changes and enables Save", async () => {
    mountCode();
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    expect(button("Save changes").disabled).toBe(true);
    edit("x = 1");
    expect(status()).toBe("Unsaved changes");
    expect(button("Save changes").disabled).toBe(false);
  });
  it("Save PUTs the code, then checks it, and marks the implementation edited", async () => {
    const { f } = mountCode();
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    edit("x = 1");
    fireEvent.click(button("Save changes"));
    await screen.findByText(/No errors/);
    expect(JSON.parse(calls(f, "PUT", "/implementations/rules")[0][1]!.body as string)).toEqual({ code: "x = 1" });
    expect(JSON.parse(calls(f, "POST", "/check")[0][1]!.body as string)).toEqual({ code: "x = 1" });
    expect(status()).toBe("Edited and saved");
    expect(button("Rules (edited)")).toBeTruthy();
    expect(button("Save changes").disabled).toBe(true);
  });
  it("a failed save is reported, not checked, and keeps the edit", async () => {
    const { f, report } = mountCode();
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    edit("FAIL");
    fireEvent.click(button("Save changes"));
    await screen.findByText("Code is not allowed");
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "rules", stage: "save", message: "Code is not allowed" });
    expect(calls(f, "POST", "/check")).toHaveLength(0);
    expect(source().value).toBe("FAIL");
    expect(status()).toBe("Unsaved changes");
  });
});

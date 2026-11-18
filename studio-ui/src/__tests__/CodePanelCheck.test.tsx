import { fireEvent, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { calls, mountCode, status } from "./Harness";
import { appRoutes, ok, originalOf } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const button = (name: string) => screen.getByRole("button", { name }) as HTMLButtonElement;
const edit = (v: string) => fireEvent.change(source(), { target: { value: v } });
const ready = () => waitFor(() => expect(source().value).toBe(originalOf("r1", "a1")));

describe("CodePanel Check for errors", () => {
  it("success shows a notice and sends the editor's text", async () => {
    const { f, report } = mountCode();
    await ready();
    edit("fine = 1");
    fireEvent.click(button("Check for errors"));
    await screen.findByText(/No errors/);
    expect(JSON.parse(calls(f, "POST", "/check")[0][1]!.body as string)).toEqual({ code: "fine = 1" });
    expect(screen.queryByRole("alert")).toBeNull();
    expect(report).not.toHaveBeenCalled();
  });
  it("failure shows an alert and goes to the report", async () => {
    const { report } = mountCode();
    await ready();
    edit("BOOM");
    fireEvent.click(button("Check for errors"));
    expect((await screen.findByRole("alert")).textContent).toBe("BOOM happened");
    expect(screen.queryByText(/No errors/)).toBeNull();
    expect(report).toHaveBeenCalledWith({ agent: "Agent A", impl: "rules", stage: "check", message: "BOOM happened" });
  });
  it("a save whose code fails the check reports the check, and the save still stands", async () => {
    const { report } = mountCode();
    await ready();
    edit("BOOM");
    fireEvent.click(button("Save changes"));
    await screen.findByText("BOOM happened");
    expect(status()).toBe("Edited and saved");
    expect(report).toHaveBeenCalledTimes(1);
    expect(report.mock.calls[0][0].stage).toBe("check");
  });
  it("lists warnings", async () => {
    mountCode(undefined, (p, i) =>
      p.endsWith("/check") ? ok({ ok: true, error: null, line: null, warnings: ["unused import", "slow loop"] }) : appRoutes(p, i));
    await ready();
    fireEvent.click(button("Check for errors"));
    await screen.findByText("unused import");
    expect(screen.getByText("slow loop")).toBeTruthy();
    expect(screen.getByText(/No errors/)).toBeTruthy();
  });
  it("shows Checking… while it runs", async () => {
    mountCode();
    await ready();
    fireEvent.click(button("Check for errors"));
    expect(screen.getByText("Checking…")).toBeTruthy();
    expect(button("Check for errors").disabled).toBe(true);
    await screen.findByText(/No errors/);
  });
});

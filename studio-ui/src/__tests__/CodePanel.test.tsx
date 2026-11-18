import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { CodePanel } from "../components/CodePanel";
import { draftFor } from "../components/studioState";
import { agent, Held } from "./Harness";
import { appRoutes, fail, ok, originalOf, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());
const ORIGINAL = originalOf("r", "a1");
const mount = (initial = {}) =>
  render(<Held initial={initial} render={(d, c) => <CodePanel roleId="r" agentId="a1" draft={d} onChange={c} />} />);
const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const type = (v: string) => fireEvent.change(source(), { target: { value: v } });
const button = (name: string) => screen.getByRole("button", { name }) as HTMLButtonElement;
const status = () => screen.getByRole("status").textContent;
const methods = (f: ReturnType<typeof stubFetch>) => f.mock.calls.map((c) => c[1]?.method ?? "GET");
const loaded = () => waitFor(() => expect(source().value).toBe(ORIGINAL));

describe("CodePanel loading", () => {
  it("is read-only until the code loads, then shows it and the original", async () => {
    stubFetch(appRoutes);
    mount();
    expect(source().readOnly).toBe(true);
    expect(source().value).toBe("");
    await loaded();
    expect(source().readOnly).toBe(false);
    expect(screen.getByLabelText("Original code").textContent).toBe(ORIGINAL);
    expect(screen.getByLabelText("Original code").closest("details")).toBeTruthy();
    expect(status()).toBe("Original");
    expect(button("Revert to original").disabled).toBe(true);
    expect(button("Save changes").disabled).toBe(true);
  });
  it("does not reload when the draft already has its code", () => {
    const f = stubFetch(appRoutes);
    const codeInfo = { role_id: "r", agent_id: "a1", original: "o", code: "c", edited: false };
    mount({ codeInfo, pythonCode: "c" });
    expect(f).not.toHaveBeenCalled();
    expect(source().value).toBe("c");
  });
  it("shows an alert when loading fails", async () => {
    stubFetch(() => fail(500));
    mount();
    await waitFor(() => expect(screen.getByRole("alert").textContent).toBe("The API returned 500."));
    expect(status()).toBe("");
  });
  it("ignores a reply that arrives after unmount", async () => {
    let release!: (v: unknown) => void;
    stubFetch(() => new Promise((r) => (release = r)));
    const onChange = vi.fn();
    const { unmount } = render(<CodePanel roleId="r" agentId="a1" draft={draftFor(agent)} onChange={onChange} />);
    unmount();
    release(ok({ role_id: "r", agent_id: "a1", original: "o", code: "c", edited: false }));
    await new Promise((r) => setTimeout(r, 10));
    expect(onChange).not.toHaveBeenCalled();
  });
  it("toggles the override", async () => {
    stubFetch(appRoutes);
    mount();
    await loaded();
    fireEvent.click(screen.getByRole("checkbox"));
    expect((screen.getByRole("checkbox") as HTMLInputElement).checked).toBe(true);
  });
});

describe("CodePanel editing", () => {
  it("saves an edit with a PUT and reverts it with a DELETE", async () => {
    const f = stubFetch(appRoutes);
    mount();
    await loaded();
    type("x = 1");
    expect(status()).toBe("Unsaved changes");
    expect(button("Save changes").disabled).toBe(false);
    expect(button("Revert to original").disabled).toBe(false);
    fireEvent.click(button("Save changes"));
    await waitFor(() => expect(status()).toBe("Edited and saved"));
    expect(methods(f)).toEqual(["GET", "PUT"]);
    expect(JSON.parse(f.mock.calls[1][1]!.body as string)).toEqual({ code: "x = 1" });
    expect(button("Save changes").disabled).toBe(true);
    expect(screen.getByLabelText("Original code").textContent).toBe(ORIGINAL);
    fireEvent.click(button("Revert to original"));
    await waitFor(() => expect(status()).toBe("Original"));
    expect(methods(f)).toEqual(["GET", "PUT", "DELETE"]);
    expect(source().value).toBe(ORIGINAL);
    expect(button("Revert to original").disabled).toBe(true);
  });
  it("reverts an unsaved buffer that differs from the original", async () => {
    const f = stubFetch(appRoutes);
    mount();
    await loaded();
    type("scratch");
    fireEvent.click(button("Revert to original"));
    await waitFor(() => expect(source().value).toBe(ORIGINAL));
    expect(methods(f)).toEqual(["GET", "DELETE"]);
    expect(status()).toBe("Original");
  });
  it("shows the API's reason when a save is rejected", async () => {
    stubFetch(appRoutes);
    mount();
    await loaded();
    type("FAIL");
    fireEvent.click(button("Save changes"));
    await waitFor(() => expect(screen.getByRole("alert").textContent).toBe("Code is not allowed"));
    expect(status()).toBe("Unsaved changes");
    expect(source().value).toBe("FAIL");
  });
});

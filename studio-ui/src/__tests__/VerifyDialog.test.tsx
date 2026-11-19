import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { VerifyDialog } from "../components/VerifyDialog";
import { fail, ok, polyfillDialog, stubFetch, verifiedAgent, verifyFail, verifyPass } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());

function setup(routes: (path: string, init?: RequestInit) => unknown = (p) => ok(p.endsWith("/save-verified") ? verifiedAgent : verifyPass), open = true) {
  const f = stubFetch(routes);
  const props = { roleId: "r1", agentId: "a1", agentName: "Gen Agent", onClose: vi.fn(), onDeploy: vi.fn(), onSaved: vi.fn() };
  const view = render(<VerifyDialog open={open} {...props} />);
  return { f, props, rerender: (o: boolean) => view.rerender(<VerifyDialog open={o} {...props} />) };
}
const dialogs = () => Array.from(document.querySelectorAll("dialog"));
const calls = (f: ReturnType<typeof stubFetch>, suffix: string) => f.mock.calls.filter(([url]) => String(url).endsWith(suffix));

describe("VerifyDialog", () => {
  it("does nothing until it is opened", () => {
    const { f } = setup(undefined, false);
    expect(f).not.toHaveBeenCalled();
    expect(dialogs().every((d) => !d.open)).toBe(true);
  });

  it("checks the agent when opened and, when everything passes, warns and offers to deploy or save", async () => {
    const { f, props } = setup();
    expect(screen.getByRole("heading", { name: "Verify Gen Agent before deploying" })).toBeTruthy();
    expect(await screen.findByText("All 3 versions passed, each on 6 kinds of input.")).toBeTruthy();
    expect(calls(f, "/api/agents/r1/a1/verify")[0][1]!.method).toBe("POST");
    expect(screen.getByRole("note").textContent).toContain("Deploy to Rust builds the crate from the agent's definition");
    expect(screen.queryByRole("list", { name: "Problems found" })).toBeNull();
    fireEvent.click(screen.getByRole("button", { name: "Continue and deploy to Rust" }));
    expect(props.onClose).toHaveBeenCalledTimes(1);
    expect(props.onDeploy).toHaveBeenCalledTimes(1);
  });

  it("lists warnings such as missing example data without blocking", async () => {
    const warned = { ...verifyPass, warning_count: 1, checks: [{ ...verifyPass.checks[0], warnings: ["No example data for: Owner"] }, ...verifyPass.checks.slice(1)] };
    setup(() => ok(warned));
    const list = await screen.findByRole("list", { name: "Warnings" });
    expect(list.textContent).toBe("Rules: No example data for: Owner");
    expect(screen.getByRole("button", { name: "Continue and deploy to Rust" })).toBeTruthy();
  });

  it("blocks when a version has problems, naming the version, the input and the line, with no way to deploy", async () => {
    const { props } = setup(() => ok(verifyFail));
    expect((await screen.findByRole("alert")).textContent).toBe("2 problem(s) found. Fix them, then deploy.");
    const list = within(screen.getByRole("list", { name: "Problems found" }));
    expect(list.getByText("Rules")).toBeTruthy();
    expect(list.getByText("(run, on no data, line 2)")).toBeTruthy();
    expect(list.getByText("(blocked)")).toBeTruthy(); // no input and no line to name
    expect(list.queryByText("Pipeline")).toBeNull(); // versions that passed are not listed
    expect(screen.queryByRole("button", { name: "Continue and deploy to Rust" })).toBeNull();
    expect(screen.queryByRole("button", { name: "Save verified agent…" })).toBeNull();
    fireEvent.click(screen.getByRole("button", { name: "Close" }));
    expect(props.onClose).toHaveBeenCalled();
    expect(props.onDeploy).not.toHaveBeenCalled();
  });

  it("shows an API error and can only be closed, and Escape closes it", async () => {
    const { props } = setup(() => fail(500, "The API is down"));
    expect((await screen.findByRole("alert")).textContent).toBe("The API is down");
    expect(screen.queryByRole("button", { name: "Continue and deploy to Rust" })).toBeNull();
    fireEvent(dialogs()[0], new Event("cancel"));
    expect(props.onClose).toHaveBeenCalledTimes(1);
  });

  it("checks again each time it is opened", async () => {
    const { f, rerender } = setup();
    await screen.findByText(/versions passed/);
    rerender(false);
    expect(dialogs().every((d) => !d.open)).toBe(true);
    rerender(true);
    await waitFor(() => expect(calls(f, "/verify")).toHaveLength(2));
  });
});

describe("saving the verified agent", () => {
  async function openName(routes?: Parameters<typeof setup>[0]) {
    const s = setup(routes);
    await screen.findByText(/versions passed/);
    fireEvent.click(screen.getByRole("button", { name: "Save verified agent…" }));
    return s;
  }

  it("asks for a name in its own box, suggests one, and saves with the name you type", async () => {
    const { f, props } = await openName();
    const input = screen.getByLabelText("Agent name") as HTMLInputElement;
    expect(input.value).toBe("Gen Agent (verified)");
    expect(screen.getByText(/saved in Custom Agents/)).toBeTruthy();
    fireEvent.change(input, { target: { value: "  Mine  " } });
    fireEvent.click(screen.getByRole("button", { name: "Save" }));
    await waitFor(() => expect(props.onSaved).toHaveBeenCalledWith(verifiedAgent));
    expect(JSON.parse(calls(f, "/api/agents/r1/a1/save-verified")[0][1]!.body as string)).toEqual({ name: "Mine" });
    expect(props.onClose).toHaveBeenCalled();
  });

  it("will not save an empty name", async () => {
    await openName();
    fireEvent.change(screen.getByLabelText("Agent name"), { target: { value: "   " } });
    expect((screen.getByRole("button", { name: "Save" }) as HTMLButtonElement).disabled).toBe(true);
  });

  it("shows why a save was refused, and Cancel returns to the verified result", async () => {
    const { props } = await openName((p, init) => (init?.method === "POST" && p.endsWith("/save-verified") ? fail(409, "A custom agent named gen already exists.") : ok(verifyPass)));
    fireEvent.click(screen.getByRole("button", { name: "Save" }));
    expect((await screen.findByText("A custom agent named gen already exists.")).getAttribute("role")).toBe("alert");
    expect(props.onSaved).not.toHaveBeenCalled();
    fireEvent.click(within(dialogs()[1]).getByRole("button", { name: "Cancel" }));
    await waitFor(() => expect(dialogs()[1].open).toBe(false));
    expect(dialogs()[0].open).toBe(true);
    expect(screen.getByRole("button", { name: "Continue and deploy to Rust" })).toBeTruthy();
  });

  it("Escape in the name box closes only that box", async () => {
    const { props } = await openName();
    const nameDialog = dialogs()[1];
    expect(nameDialog.open).toBe(true);
    fireEvent(nameDialog, new Event("cancel"));
    await waitFor(() => expect(nameDialog.open).toBe(false));
    expect(props.onClose).not.toHaveBeenCalled();
  });
});

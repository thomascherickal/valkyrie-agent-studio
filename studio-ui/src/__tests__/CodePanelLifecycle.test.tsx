import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { CodePanel } from "../components/CodePanel";
import type { ImplCode } from "../api/types";
import { draftFor } from "../components/studioState";
import { agent } from "./Harness";
import { appRoutes, deferred, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const info = (code: string, kind: ImplCode["kind"] = "builtin"): ImplCode =>
  ({ role_id: "r1", agent_id: "a1", impl: "rules", label: "Rules", kind, edited: false, original: "o", code });
const metas = [{ id: "rules", label: "Rules", kind: "builtin" as const, edited: false }];

/** Mounts with the list already known, so the panel asks for the code straight away. */
function mountBare(over: Partial<ReturnType<typeof draftFor>> = {}) {
  const onChange = vi.fn();
  const draft = { ...draftFor(agent), impls: metas, fieldsLoaded: true, ...over };
  const view = render(<CodePanel roleId="r1" agentId="a1" agentName="Agent A" draft={draft} onChange={onChange} report={vi.fn()} />);
  return { onChange, ...view };
}

describe("CodePanel after it has gone", () => {
  it("drops a code reply that lands after unmount", async () => {
    const slow = deferred<unknown>();
    const f = stubFetch(() => slow.promise);
    const { onChange, unmount } = mountBare();
    await waitFor(() => expect(f).toHaveBeenCalledTimes(1));
    unmount();
    slow.resolve(ok(info("late")));
    await new Promise((r) => setTimeout(r, 10));
    expect(onChange).not.toHaveBeenCalled();
  });
  it("adopts the reply while it is mounted", async () => {
    stubFetch(() => ok(info("fresh")));
    const { onChange } = mountBare();
    await waitFor(() => expect(onChange).toHaveBeenCalledTimes(1));
    const patch = onChange.mock.calls[0][0](draftFor(agent));
    expect(patch.texts).toEqual({ rules: "fresh" });
    expect(patch.codes.rules.code).toBe("fresh");
    expect(patch.impls).toBeNull(); // withMeta keeps a missing list missing
  });
  it("drops a save reply that lands after unmount", async () => {
    const slow = deferred<unknown>();
    const f = stubFetch((p, i) => (i?.method === "PUT" ? slow.promise : appRoutes(p, i)));
    const { onChange, unmount } = mountBare({ codes: { rules: info("a") }, texts: { rules: "b" } });
    fireEvent.click(screen.getByRole("button", { name: "Save changes" }));
    await waitFor(() => expect(f).toHaveBeenCalledTimes(1));
    unmount();
    slow.resolve(ok(info("b")));
    await new Promise((r) => setTimeout(r, 10));
    expect(onChange).not.toHaveBeenCalled();
  });
  it("drops a delete reply that lands after unmount", async () => {
    const slow = deferred<unknown>();
    const f = stubFetch(() => slow.promise);
    const saved = info("a", "saved");
    const { onChange, unmount } = mountBare({ codes: { rules: saved }, texts: { rules: "a" } });
    fireEvent.click(screen.getByRole("button", { name: "Delete this implementation" }));
    await waitFor(() => expect(f).toHaveBeenCalledTimes(1));
    unmount();
    slow.resolve(ok({ deleted: "rules" }));
    await new Promise((r) => setTimeout(r, 10));
    expect(onChange).not.toHaveBeenCalled();
  });
});

import { fireEvent, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { ImplCode } from "../api/types";
import { calls, mountRun } from "./Harness";

afterEach(() => vi.unstubAllGlobals());

const saved: ImplCode = { role_id: "r1", agent_id: "a1", impl: "rules", label: "Rules", kind: "builtin", edited: false, original: "o", code: "saved" };
const sent = (f: Parameters<typeof calls>[0]) => JSON.parse(calls(f, "POST", "/run")[0][1]!.body as string);

describe("Run with my unsaved edits", () => {
  it("sends the editor's text as `code`, and the plain Run button still runs the saved version", async () => {
    const { f } = mountRun({ fieldsLoaded: true, impls: [], runWith: "rules", codes: { rules: saved }, texts: { rules: "edited text" } });
    fireEvent.click(screen.getByRole("button", { name: "Run with my unsaved edits" }));
    await screen.findByText("Python · rules");
    expect(sent(f)).toMatchObject({ impl: "rules", code: "edited text" });
    f.mockClear();
    fireEvent.click(screen.getByRole("button", { name: "Run agent" }));
    await screen.findByText("Python · rules");
    expect(sent(f)).not.toHaveProperty("code");
  });
  it("is only offered when there is something unsaved", () => {
    mountRun({ fieldsLoaded: true, impls: [], runWith: "rules", codes: { rules: saved }, texts: { rules: "saved" } });
    expect(screen.queryByRole("button", { name: "Run with my unsaved edits" })).toBeNull();
  });
});

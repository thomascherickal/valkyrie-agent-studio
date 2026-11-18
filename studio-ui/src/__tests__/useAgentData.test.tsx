import { render, renderHook, screen, waitFor } from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { draftFor, type Draft } from "../components/studioState";
import { useAgentData } from "../hooks/useAgentData";
import { FIELDS } from "./fakeApi";
import { agent, Held } from "./Harness";
import { appRoutes, deferred, fail, ok, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const fresh = () => draftFor(agent);
type Fn = (d: Draft) => Partial<Draft>;
const patches = (onChange: ReturnType<typeof vi.fn>) => onChange.mock.calls.map(([p]) => p);
const fieldsPatch = (onChange: ReturnType<typeof vi.fn>) => patches(onChange).find((p) => typeof p === "function") as Fn;
const keys = (p: Partial<Draft>) => p.fields!.map((f) => f.key);

function Probe() {
  return <Held render={(d, c) => { useAgentData("r1", "a1", d, c); return <p>{d.fields.map((f) => f.key).join(",")}</p>; }} />;
}

describe("useAgentData", () => {
  it("loads the implementations and the data fields once", async () => {
    const f = stubFetch(appRoutes);
    const onChange = vi.fn();
    renderHook(() => useAgentData("r1", "a1", fresh(), onChange));
    await waitFor(() => expect(onChange).toHaveBeenCalledTimes(2));
    const plain = patches(onChange).find((p) => typeof p !== "function");
    expect(plain.impls.map((m: { id: string }) => m.id)).toEqual(["rules", "pipeline", "hybrid"]);
    const patch = fieldsPatch(onChange)(fresh());
    expect(keys(patch)).toEqual(["feature_brief", "audience", "budget"]);
    expect(patch.fieldsLoaded).toBe(true);
    expect(patch.fields![1]).toEqual({ key: "audience", value: "engineers", custom: false, label: "Audience", kind: "text" });
    expect(f).toHaveBeenCalledTimes(2);
  });
  it("puts the agent's fields after the main one and before custom ones", async () => {
    stubFetch(appRoutes);
    const onChange = vi.fn();
    renderHook(() => useAgentData("r1", "a1", fresh(), onChange));
    await waitFor(() => expect(onChange).toHaveBeenCalledTimes(2));
    const custom = { key: "mine", value: "", custom: true, label: "", kind: "text" as const };
    const d = { ...fresh(), fields: [...fresh().fields, custom] };
    expect(keys(fieldsPatch(onChange)(d))).toEqual(["feature_brief", "audience", "budget", "mine"]);
  });
  it("the fields patch is a no-op once fieldsLoaded is set", async () => {
    stubFetch(appRoutes);
    const onChange = vi.fn();
    renderHook(() => useAgentData("r1", "a1", fresh(), onChange));
    await waitFor(() => expect(onChange).toHaveBeenCalledTimes(2));
    expect(fieldsPatch(onChange)({ ...fresh(), fieldsLoaded: true })).toEqual({});
  });
  it("does not reload what the draft already has", async () => {
    const f = stubFetch(appRoutes);
    const onChange = vi.fn();
    renderHook(() => useAgentData("r1", "a1", { ...fresh(), impls: [], fieldsLoaded: true }, onChange));
    await new Promise((r) => setTimeout(r, 10));
    expect(f).not.toHaveBeenCalled();
    expect(onChange).not.toHaveBeenCalled();
  });
  it("adds nothing when a failed call returns no data", async () => {
    const f = stubFetch(() => fail(500, "down"));
    const onChange = vi.fn();
    renderHook(() => useAgentData("r1", "a1", fresh(), onChange));
    await waitFor(() => expect(f).toHaveBeenCalledTimes(2));
    await new Promise((r) => setTimeout(r, 10));
    expect(onChange).not.toHaveBeenCalled();
  });
  it("ignores replies that land after unmount", async () => {
    const slow = deferred<unknown>();
    const f = stubFetch(() => slow.promise);
    const onChange = vi.fn();
    const { unmount } = renderHook(() => useAgentData("r1", "a1", fresh(), onChange));
    await waitFor(() => expect(f).toHaveBeenCalledTimes(2));
    unmount();
    slow.resolve(ok({ implementations: [], fields: FIELDS }));
    await new Promise((r) => setTimeout(r, 10));
    expect(onChange).not.toHaveBeenCalled();
  });
  it("strict-mode double mount does not duplicate the fields", async () => {
    const f = stubFetch(appRoutes);
    render(<React.StrictMode><Probe /></React.StrictMode>);
    await screen.findByText("feature_brief,audience,budget");
    await new Promise((r) => setTimeout(r, 20));
    expect(screen.getByText("feature_brief,audience,budget")).toBeTruthy();
    expect(f.mock.calls.length).toBeGreaterThan(2); // it did load twice
  });
});

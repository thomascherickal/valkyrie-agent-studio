import React, { useState } from "react";
import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { SecretEntry } from "../api/types";
import { SecretCard } from "../components/SecretCard";
import { fail, modelCatalog, ok, secretsState, stubFetch } from "./helpers";

afterEach(() => vi.unstubAllGlobals());

const gemini = secretsState.secrets[0] as SecretEntry;
const opencode = secretsState.secrets[2] as SecretEntry;
const withKey = (e: SecretEntry): SecretEntry => ({ ...e, key_set: true, preview: "AQ.Ab8RN6j" + "*".repeat(20) });
const efforts = ["low", "medium", "high"];
/** Holds the entry like the Secrets panel does: when the card saves, the new entry comes back down as the prop. */
function Host({ start, onSaved = () => {} }: { start: SecretEntry; onSaved?: (e: SecretEntry) => void }) {
  const [entry, setEntry] = useState(start);
  return <SecretCard entry={entry} efforts={efforts} onSaved={(e) => { setEntry(e); onSaved(e); }} />;
}
const bodyOf = (f: ReturnType<typeof stubFetch>, method: string, suffix: string) => {
  const call = f.mock.calls.find(([url, init]) => (init?.method ?? "GET") === method && String(url).endsWith(suffix))!;
  return JSON.parse(call[1]!.body as string);
};

describe("SecretCard", () => {
  it("shows the provider, its models with free ones marked, the effort levels for Gemini only, and a hint from the catalog", async () => {
    stubFetch((p) => ok(p.endsWith("/models") ? { ...modelCatalog, note: "Showing the built-in models." } : {}));
    const { unmount } = render(<SecretCard entry={opencode} efforts={efforts} onSaved={() => {}} />);
    await screen.findByRole("option", { name: "big-pickle (free)" });
    expect(screen.getByRole("option", { name: "gpt-5" })).toBeTruthy();
    expect(screen.getByText("Showing the built-in models.")).toBeTruthy();
    expect(screen.getByText("no key")).toBeTruthy();
    expect(screen.queryByLabelText("OpenCode effort")).toBeNull();
    unmount();
    render(<SecretCard entry={gemini} efforts={efforts} onSaved={() => {}} />);
    expect(screen.getAllByRole("option", { name: /^(low|medium|high)$/ }).map((o) => o.textContent)).toEqual(efforts);
    expect((screen.getByLabelText("Gemini effort") as HTMLSelectElement).value).toBe("low");
  });

  it("keeps a model that is not in the list selectable, even when the list cannot be loaded", async () => {
    stubFetch(() => fail(500));
    render(<SecretCard entry={{ ...opencode, model: "my-own-slug" }} efforts={efforts} onSaved={() => {}} />);
    await waitFor(() => expect(screen.getByRole("option", { name: "my-own-slug" })).toBeTruthy());
    expect((screen.getByLabelText("OpenCode model") as HTMLSelectElement).value).toBe("my-own-slug");
  });

  it("shows a saved key as its first 10 characters then asterisks, and typing replaces it with a hidden field", async () => {
    stubFetch(() => ok(modelCatalog));
    render(<SecretCard entry={withKey(gemini)} efforts={efforts} onSaved={() => {}} />);
    const key = screen.getByLabelText("Gemini API key") as HTMLInputElement;
    expect(key.value).toBe("AQ.Ab8RN6j" + "*".repeat(20));
    expect(key.type).toBe("text");
    expect(screen.getByText("key set")).toBeTruthy();
    fireEvent.focus(key);
    expect(key.value).toBe("");
    expect(key.type).toBe("password");
    fireEvent.blur(key); // nothing typed: back to the preview
    expect(key.value).toBe("AQ.Ab8RN6j" + "*".repeat(20));
    expect(key.type).toBe("text");
    fireEvent.focus(key);
    fireEvent.change(key, { target: { value: "AQ.new-secret" } });
    fireEvent.blur(key); // something typed: it stays
    expect(key.value).toBe("AQ.new-secret");
    expect(key.type).toBe("password");
    await screen.findByRole("option", { name: "gpt-5" });
  });

  it("saves only what changed, then shows the saved preview and tells the parent", async () => {
    const saved = { ...withKey(gemini), model: "gpt-5", effort: "high" };
    const f = stubFetch((p, init) => (init?.method === "PUT" ? ok(saved) : ok(modelCatalog)));
    const onSaved = vi.fn();
    render(<Host start={gemini} onSaved={onSaved} />);
    await screen.findByRole("option", { name: "gpt-5" });
    const saveButton = screen.getByRole("button", { name: "Save" }) as HTMLButtonElement;
    expect(saveButton.disabled).toBe(true); // nothing changed yet
    fireEvent.focus(screen.getByLabelText("Gemini API key"));
    fireEvent.change(screen.getByLabelText("Gemini API key"), { target: { value: "AQ.typed" } });
    fireEvent.change(screen.getByLabelText("Gemini model"), { target: { value: "gpt-5" } });
    fireEvent.change(screen.getByLabelText("Gemini effort"), { target: { value: "high" } });
    fireEvent.click(saveButton);
    await waitFor(() => expect(onSaved).toHaveBeenCalledWith(saved));
    expect(bodyOf(f, "PUT", "/api/secrets/gemini")).toEqual({ key: "AQ.typed", model: "gpt-5", effort: "high" });
    expect((screen.getByLabelText("Gemini API key") as HTMLInputElement).value).toBe(saved.preview);
  });

  it("saves just the model when only the model changed, and reports a refused save", async () => {
    let refuse = false;
    const f = stubFetch((p, init) => (init?.method === "PUT" ? (refuse ? fail(400, "Effort applies to Gemini") : ok({ ...opencode, model: "gpt-5" })) : ok(modelCatalog)));
    render(<Host start={opencode} />);
    await screen.findByRole("option", { name: "gpt-5" });
    fireEvent.change(screen.getByLabelText("OpenCode model"), { target: { value: "gpt-5" } });
    fireEvent.click(screen.getByRole("button", { name: "Save" }));
    await waitFor(() => expect(bodyOf(f, "PUT", "/api/secrets/opencode")).toEqual({ model: "gpt-5" }));
    refuse = true;
    fireEvent.change(screen.getByLabelText("OpenCode model"), { target: { value: "big-pickle" } });
    fireEvent.click(screen.getByRole("button", { name: "Save" }));
    expect((await screen.findByRole("alert")).textContent).toBe("Effort applies to Gemini");
  });

  it("removes a key by saving an empty one, and offers that only when a key is set", async () => {
    const f = stubFetch((p, init) => (init?.method === "PUT" ? ok(opencode) : ok(modelCatalog)));
    const onSaved = vi.fn();
    const { rerender } = render(<SecretCard entry={opencode} efforts={efforts} onSaved={onSaved} />);
    expect(screen.queryByRole("button", { name: "Remove key" })).toBeNull();
    rerender(<SecretCard entry={withKey(opencode)} efforts={efforts} onSaved={onSaved} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove key" }));
    await waitFor(() => expect(onSaved).toHaveBeenCalledWith(opencode));
    expect(bodyOf(f, "PUT", "/api/secrets/opencode")).toEqual({ key: "" });
  });

  it("Test Key shows a green Test Succeeded for a working key, using the typed key and the chosen model", async () => {
    const f = stubFetch((p) => ok(p.endsWith("/test") ? { ok: true, status: 200, ms: 90, provider: "opencode", model: "gpt-5", message: "The key works.", causes: [] } : modelCatalog));
    render(<SecretCard entry={opencode} efforts={efforts} onSaved={() => {}} />);
    await screen.findByRole("option", { name: "gpt-5" });
    fireEvent.focus(screen.getByLabelText("OpenCode API key"));
    fireEvent.change(screen.getByLabelText("OpenCode API key"), { target: { value: "oc_typed" } });
    fireEvent.change(screen.getByLabelText("OpenCode model"), { target: { value: "gpt-5" } });
    fireEvent.click(screen.getByRole("button", { name: "Test Key" }));
    const success = await screen.findByText("Test Succeeded");
    expect(success.getAttribute("role")).toBe("status");
    expect(bodyOf(f, "POST", "/api/secrets/opencode/test")).toEqual({ key: "oc_typed", model: "gpt-5" });
    expect(screen.queryByText("Test Failed")).toBeNull();
  });

  it("Test Key shows a red Test Failed with the provider's message and the likely causes below the button", async () => {
    const causes = ["The key is invalid, expired or revoked.", "The key belongs to a different provider."];
    const f = stubFetch((p) => ok(p.endsWith("/test") ? { ok: false, status: 401, ms: 40, provider: "opencode", model: "big-pickle", message: "Invalid credential", causes } : modelCatalog));
    render(<SecretCard entry={withKey(opencode)} efforts={efforts} onSaved={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: "Test Key" }));
    const alert = await screen.findByRole("alert");
    expect(within(alert).getByText("Test Failed")).toBeTruthy();
    expect(within(alert).getByText("Invalid credential")).toBeTruthy();
    expect(within(within(alert).getByRole("list", { name: "Likely causes" })).getAllByRole("listitem").map((li) => li.textContent)).toEqual(causes);
    expect(bodyOf(f, "POST", "/api/secrets/opencode/test")).toEqual({ model: "big-pickle" }); // no typed key: the saved one is used
    expect(screen.queryByText("Test Succeeded")).toBeNull();
  });
});

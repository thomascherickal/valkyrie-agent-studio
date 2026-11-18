import { act, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import { ThemeProvider, useTheme } from "../theme/ThemeProvider";

function Probe() {
  const { theme, setThemeMode } = useTheme();
  return (
    <>
      <p data-testid="t">{theme}</p>
      {(["dark", "light", "system"] as const).map((m) => (
        <button key={m} onClick={() => setThemeMode(m)}>{m}</button>
      ))}
    </>
  );
}
const storage = (key: string, newValue: string | null) =>
  act(() => { window.dispatchEvent(new StorageEvent("storage", { key, newValue })); });
const shown = () => screen.getByTestId("t").textContent;

afterEach(() => { document.head.innerHTML = ""; localStorage.clear(); });

describe("ThemeProvider", () => {
  it("updates meta and storage for each mode", () => {
    const meta = document.createElement("meta");
    meta.setAttribute("name", "color-scheme");
    document.head.appendChild(meta);
    render(<ThemeProvider><Probe /></ThemeProvider>);
    fireEvent.click(screen.getByText("dark"));
    expect(meta.getAttribute("content")).toBe("dark");
    expect(localStorage.getItem("color-scheme")).toBe("dark");
    fireEvent.click(screen.getByText("light"));
    expect(meta.getAttribute("content")).toBe("light");
    fireEvent.click(screen.getByText("system"));
    expect(meta.getAttribute("content")).toBe("light dark");
    expect(localStorage.getItem("color-scheme")).toBeNull();
  });
  it("works without a meta tag", () => {
    render(<ThemeProvider><Probe /></ThemeProvider>);
    fireEvent.click(screen.getByText("dark"));
    expect(shown()).toBe("dark");
  });
  it("syncs from storage events", () => {
    render(<ThemeProvider><Probe /></ThemeProvider>);
    storage("color-scheme", "dark");
    expect(shown()).toBe("dark");
    storage("color-scheme", "light");
    expect(shown()).toBe("light");
    storage("color-scheme", "bogus");
    expect(shown()).toBe("system");
    storage("color-scheme", "dark");
    storage("other", "light");
    expect(shown()).toBe("dark");
    storage("color-scheme", null);
    expect(shown()).toBe("system");
  });
});

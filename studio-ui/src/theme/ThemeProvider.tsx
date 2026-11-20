import React, { createContext, useContext, useEffect, useState } from "react";

export type ThemeMode = "system" | "light" | "dark";

interface ThemeContextValue {
  theme: ThemeMode;
  setThemeMode: (mode: ThemeMode) => void;
}

const ThemeContext = createContext<ThemeContextValue>(null!);

function applyColorSchemeMeta(mode: ThemeMode) {
  const content = mode === "system" ? "light dark" : mode;
  const meta = document.querySelector('meta[name="color-scheme"]');
  if (meta) {
    meta.setAttribute("content", content);
  }
  document.documentElement.style.colorScheme = content;
  if (mode === "system") {
    document.documentElement.removeAttribute("data-theme");
    localStorage.removeItem("color-scheme");
  } else {
    document.documentElement.setAttribute("data-theme", mode);
    localStorage.setItem("color-scheme", mode);
  }
  const tauri = (window as unknown as { __TAURI_INTERNALS__?: { invoke?: (cmd: string, args?: Record<string, unknown>) => Promise<unknown> } }).__TAURI_INTERNALS__;
  if (tauri?.invoke) {
    tauri.invoke("set_window_theme", { mode }).catch(() => {});
  }
}

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<ThemeMode>("system");

  const setThemeMode = (mode: ThemeMode) => {
    setTheme(mode);
    applyColorSchemeMeta(mode);
  };

  useEffect(() => {
    const onStorage = (e: StorageEvent) => {
      if (e.key === "color-scheme") {
        setTheme(e.newValue === "light" || e.newValue === "dark" ? e.newValue : "system");
      }
    };
    window.addEventListener("storage", onStorage);
    return () => window.removeEventListener("storage", onStorage);
  }, []);

  return <ThemeContext.Provider value={{ theme, setThemeMode }}>{children}</ThemeContext.Provider>;
}

export function useTheme() {
  return useContext(ThemeContext);
}

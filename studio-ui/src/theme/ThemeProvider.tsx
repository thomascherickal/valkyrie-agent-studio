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
  if (mode === "system") {
    localStorage.removeItem("color-scheme");
  } else {
    localStorage.setItem("color-scheme", mode);
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

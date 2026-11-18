import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    globals: true,
    // Full-app tests take a few seconds under coverage; leave room for a slower machine.
    testTimeout: 20_000,
    coverage: {
      provider: "v8",
      include: ["src/components/**", "src/theme/**", "src/api/**", "src/hooks/**", "src/App.tsx"],
      exclude: ["src/api/types.ts", "src/api/config.ts"],
      thresholds: {
        lines: 100,
        branches: 100,
        functions: 100,
        statements: 100,
      },
    },
  },
});


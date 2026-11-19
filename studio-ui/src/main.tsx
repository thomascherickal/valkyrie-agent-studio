import React from "react";
import ReactDOM from "react-dom/client";
import "./styles/tokens.css";
import "./styles/layout.css";
import "./styles/controls.css";
import "./styles/panels.css";
import "./styles/about-deploy.css";
import { App } from "./App";
import { ThemeProvider } from "./theme/ThemeProvider";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ThemeProvider>
      <App />
    </ThemeProvider>
  </React.StrictMode>
);

import React, { useState } from "react";

interface SandboxTestConsoleProps {
  model: string;
  thinkingLevel: string;
  onRun: (prompt: string) => string;
}

export function SandboxTestConsole({ model, thinkingLevel, onRun }: SandboxTestConsoleProps) {
  const [prompt, setPrompt] = useState("");
  const [output, setOutput] = useState("");

  const handleRun = () => {
    setOutput(onRun(prompt));
  };

  return (
    <section aria-label="Sandbox Test Console">
      <div>
        Engine: {model} ({thinkingLevel})
      </div>
      <input
        type="text"
        aria-label="Test Prompt"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button type="button" onClick={handleRun}>
        Run Sandbox Test
      </button>
      {output && <output>{output}</output>}
    </section>
  );
}


import React from "react";

interface CustomPythonEditorProps {
  code: string;
  enabled: boolean;
  onToggle: (enabled: boolean) => void;
  onChange: (code: string) => void;
}

export function CustomPythonEditor({ code, enabled, onToggle, onChange }: CustomPythonEditorProps) {
  return (
    <section aria-label="Custom Python Editor">
      <label>
        <input
          type="checkbox"
          checked={enabled}
          onChange={(e) => onToggle(e.target.checked)}
        />
        Enable Custom Python Override
      </label>
      {enabled && (
        <textarea
          aria-label="Python Source"
          value={code}
          onChange={(e) => onChange(e.target.value)}
        />
      )}
    </section>
  );
}


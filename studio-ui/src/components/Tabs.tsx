import React from "react";
import { TAB_LABELS, type TabId } from "./modes";

interface TabsProps {
  tabs: TabId[];
  active: TabId;
  onChange: (tab: TabId) => void;
}

export function Tabs({ tabs, active, onChange }: TabsProps) {
  return (
    <div role="tablist" aria-label="Workspace" className="tabs">
      {tabs.map((id) => (
        <button
          key={id}
          type="button"
          role="tab"
          id={`tab-${id}`}
          aria-selected={id === active}
          aria-controls="panel"
          onClick={() => onChange(id)}
        >
          {TAB_LABELS[id]}
        </button>
      ))}
    </div>
  );
}

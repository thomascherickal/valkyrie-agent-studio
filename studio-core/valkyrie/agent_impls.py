"""The three built-in Python implementations of every agent, rendered from versioned templates and playbooks.

The original of each implementation is always reproducible: it is the template plus the agent's playbook,
both in the repo, and nothing here ever writes to them. User edits live elsewhere (see agent_impl_routes).
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Any

from valkyrie.impl_hybrid import TEMPLATE as HYBRID
from valkyrie.impl_pipeline import TEMPLATE as PIPELINE
from valkyrie.profiles import PROFILES
from valkyrie.impl_rules import TEMPLATE as RULES
from valkyrie.ir_schema import load_ir_from_yaml
from valkyrie.playbooks import PLAYBOOKS
from valkyrie.storage import REPO, agents_dir, custom_agents_dir

CUSTOM_ROLE_ID = "custom-agents"
VARIANTS: dict[str, tuple[str, str]] = {
    "rules": ("Rules", RULES),
    "pipeline": ("Pipeline", PIPELINE),
    "hybrid": ("Hybrid (model + rules)", HYBRID),
}
_ID = re.compile(r"[a-z0-9-]+")
_STOP = set("the a an and or of to for with by from into in on at as is are be this that it its their your".split())


@dataclass(frozen=True)
class AgentSpec:
    """What the templates need to know about one agent."""

    role_id: str
    agent_id: str
    name: str
    role: str
    description: str
    tool: str
    input_key: str
    output_key: str
    sample: str


def agent_dir(role_id: str, agent_id: str) -> Path:
    """The agent's directory. Raises ValueError for a bad id and LookupError when there is no such agent."""
    if not (_ID.fullmatch(role_id) and _ID.fullmatch(agent_id)):
        raise ValueError("Invalid agent id")
    base = custom_agents_dir() if role_id == CUSTOM_ROLE_ID else agents_dir() / role_id
    path = base / agent_id
    if not (path / "agent.ir.yaml").is_file():
        raise LookupError(f"No agent {agent_id} in {role_id}")
    return path


def load_spec(role_id: str, agent_id: str) -> AgentSpec:
    folder = agent_dir(role_id, agent_id)
    ir = load_ir_from_yaml((folder / "agent.ir.yaml").read_text())
    input_key = next(iter(ir.input_schema), "task_input")
    sample_file = folder / "sample_data.json"
    sample = str(json.loads(sample_file.read_text()).get(input_key, "")) if sample_file.is_file() else ""
    return AgentSpec(
        role_id=role_id,
        agent_id=agent_id,
        name=ir.name,
        role=ir.role,
        description=ir.description,
        tool=ir.tools[0].name if ir.tools else "run_agent",
        input_key=input_key,
        output_key=next(iter(ir.output_schema), "result"),
        sample=sample,
    )


def parse_profile(text: str) -> dict[str, list[str]]:
    """'goals:goal,aim|risks:risk,blocker' becomes {'goals': ['goal', 'aim'], 'risks': ['risk', 'blocker']}."""
    facets: dict[str, list[str]] = {}
    for part in text.split("|"):
        name, _, words = part.partition(":")
        facets[name.strip()] = [w.strip() for w in words.split(",") if w.strip()]
    return facets


def derive_facets(spec: AgentSpec) -> dict[str, list[str]]:
    """Starter facets for an agent with no authored profile, taken from its own description."""
    words = re.findall(r"[a-z][a-z-]{3,}", f"{spec.name} {spec.description}".lower())
    main = list(dict.fromkeys(w for w in words if w not in _STOP))[:8]
    return {
        "main points": main,
        "risks": ["risk", "issue", "problem", "blocker", "error", "fail", "concern"],
        "next actions": ["should", "need", "todo", "action", "next", "must", "plan", "will"],
    }


def facets_for(spec: AgentSpec) -> dict[str, list[str]]:
    profile = PROFILES.get(f"{spec.role_id}/{spec.agent_id}")
    return parse_profile(profile) if profile else derive_facets(spec)


def parse_playbook(entry: dict[str, Any]) -> dict[str, Any]:
    """Turn the compact authored strings into the structures the templates use."""
    fields = []
    for line in entry["fields"]:
        key, label, kind, example = line.split("|", 3)
        fields.append({"key": key, "label": label, "kind": kind, "example": example})
    metrics = []
    for line in entry.get("metrics", []):
        name, formula, fmt = line.split("|", 2)
        metrics.append({"name": name, "formula": formula, "format": fmt})
    return {"fields": fields, "sections": [list(s) for s in entry["sections"]], "metrics": metrics}


def derive_playbook(spec: AgentSpec) -> dict[str, Any]:
    """A general-purpose playbook for an agent you created yourself, built from its own description."""
    return parse_playbook({
        "fields": [
            "context|Context and constraints|longtext|",
            "owner|Owner|text|",
            "deadline|Deadline|text|",
        ],
        "sections": [
            ["What was asked", "Request: {input}", f"Purpose of this agent: {spec.description}"],
            ["Context", "*{context}", "Write down the people, systems and dates involved before acting on the result."],
            ["Next steps", "Owner: {owner}", "Deadline: {deadline}", "Review the result with the owner before acting on it."],
        ],
    })


def playbook_for(spec: AgentSpec) -> dict[str, Any]:
    entry = PLAYBOOKS.get(f"{spec.role_id}/{spec.agent_id}")
    return parse_playbook(entry) if entry else derive_playbook(spec)


def render(spec: AgentSpec, variant: str) -> str:
    """The original source of one implementation."""
    literal = json.dumps(
        {
            "agent_id": spec.agent_id,
            "name": spec.name,
            "role": spec.role,
            "tool": spec.tool,
            "input_key": spec.input_key,
            "output_key": spec.output_key,
            "description": spec.description,
            **playbook_for(spec),
            "facets": facets_for(spec),
        },
        indent=4,
        ensure_ascii=False,
    )
    template = VARIANTS[variant][1]
    return template.replace("__SPEC__", literal).replace("__NAME__", spec.name).replace("__ROLE__", spec.role)

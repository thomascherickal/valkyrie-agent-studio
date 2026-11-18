"""Plain-English custom agent generator producing IR YAML, Python, tests, docs, and Rust."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re

from valkyrie.ir_schema import AgentIR, GuardrailConfig, ModelConfig, ToolSpec, dump_ir_to_yaml
from valkyrie.llm_router import LLMRouter
from valkyrie.rust_transpiler import transpile_ir_to_rust


@dataclass(frozen=True)
class GeneratedAgentBundle:
    """Complete set of generated implementation files for a custom agent."""

    agent_id: str
    name: str
    role: str
    description: str
    tool_name: str
    ir_yaml: str
    agent_py: str
    test_agent_py: str
    agent_md: str
    sample_data_json: str
    demo_svg: str
    cargo_toml: str
    main_rs: str


def _slugify(text: str) -> str:
    words = re.findall(r"[a-z0-9]+", text.lower())[:4]
    return "-".join(words) if words else "custom-agent"


def _derive_tool_name(agent_id: str) -> str:
    return f"run_{agent_id.replace('-', '_')}"


def generate_agent_from_english(
    prompt: str,
    role: str = "Custom Agents",
    name: str | None = None,
    router: LLMRouter | None = None,
) -> GeneratedAgentBundle:
    """Use the configured LLM router to synthesize a complete agent blueprint from English."""
    cleaned = prompt.strip()
    if not cleaned:
        raise ValueError("Plain-English agent description must not be empty")

    llm = router or LLMRouter()
    llm_res = llm.invoke(
        ModelConfig(),
        "Summarize the agent role and primary capability concisely.",
        cleaned,
    )

    agent_id = _slugify(name or cleaned)
    display_name = name.strip() if name and name.strip() else " ".join(w.capitalize() for w in agent_id.split("-"))
    tool_name = _derive_tool_name(agent_id)

    ir = AgentIR(
        id=agent_id,
        name=display_name,
        role=role,
        description=cleaned,
        system_prompt=f"You are {display_name} ({role}). {cleaned} Summary: {llm_res.content}",
        tools=[ToolSpec(name=tool_name, description=cleaned, parameters={"task_input": "string"})],
        input_schema={"task_input": "string"},
        output_schema={"result": "string"},
        guardrails=GuardrailConfig(),
    )
    ir_yaml = dump_ir_to_yaml(ir)
    rust_bundle = transpile_ir_to_rust(ir)

    agent_py = (
        f'"""{display_name} ({role}) — generated from plain-English spec."""\n\n'
        f"def {tool_name}(task_input: str) -> str:\n"
        f'    return f"[{tool_name}] {{task_input.strip()}}"\n\n\n'
        f"def run_agent(payload: dict) -> dict:\n"
        f'    raw = str(payload.get("task_input", ""))\n'
        f'    return {{"agent_id": "{agent_id}", "tool_used": "{tool_name}", "result": {tool_name}(raw)}}\n'
    )
    test_agent_py = (
        f'"""Tests for generated agent {agent_id}."""\n\n'
        f"from agent import run_agent\n\n\n"
        f"def test_{agent_id.replace('-', '_')}() -> None:\n"
        f'    out = run_agent({{"task_input": "verify"}})\n'
        f'    assert out["agent_id"] == "{agent_id}"\n'
        f'    assert "{tool_name}" in out["result"]\n'
    )
    agent_md = (
        f"# {display_name} (`{agent_id}`)\n\n"
        f"**Role:** {role}  \n**Tool:** `{tool_name}`\n\n"
        f"## Description\n{cleaned}\n"
    )
    sample_data_json = json.dumps({"task_input": f"Sample request for {display_name}"}, indent=2)
    demo_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="120" viewBox="0 0 480 120">'
        f'<rect width="480" height="120" fill="#0b1120" rx="8"/>'
        f'<text x="16" y="40" fill="#38bdf8" font-family="monospace" font-size="13">{display_name}</text>'
        f'<text x="16" y="75" fill="#4ade80" font-family="monospace" font-size="11">[{tool_name}] Ready</text>'
        f"</svg>"
    )
    return GeneratedAgentBundle(
        agent_id=agent_id,
        name=display_name,
        role=role,
        description=cleaned,
        tool_name=tool_name,
        ir_yaml=ir_yaml,
        agent_py=agent_py,
        test_agent_py=test_agent_py,
        agent_md=agent_md,
        sample_data_json=sample_data_json,
        demo_svg=demo_svg,
        cargo_toml=rust_bundle.cargo_toml,
        main_rs=rust_bundle.main_rs,
    )


def write_generated_agent(bundle: GeneratedAgentBundle, target_dir: Path) -> Path:
    """Persist all generated implementation files into target_dir/<agent_id>."""
    agent_dir = target_dir / bundle.agent_id
    (agent_dir / "rust" / "src").mkdir(parents=True, exist_ok=True)
    (agent_dir / "agent.ir.yaml").write_text(bundle.ir_yaml)
    (agent_dir / "agent.py").write_text(bundle.agent_py)
    (agent_dir / "test_agent.py").write_text(bundle.test_agent_py)
    (agent_dir / "AGENT.md").write_text(bundle.agent_md)
    (agent_dir / "sample_data.json").write_text(bundle.sample_data_json)
    (agent_dir / "demo.svg").write_text(bundle.demo_svg)
    (agent_dir / "rust" / "Cargo.toml").write_text(bundle.cargo_toml)
    (agent_dir / "rust" / "src" / "main.rs").write_text(bundle.main_rs)
    return agent_dir

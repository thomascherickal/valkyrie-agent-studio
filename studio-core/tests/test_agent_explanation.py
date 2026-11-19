"""Tests for the plain-language explanation of every agent."""

from pathlib import Path

from valkyrie.agent_explanation import explanation
from valkyrie.agent_impls import load_spec, playbook_for
from valkyrie.playbooks import PLAYBOOKS

AGENTS = Path(__file__).resolve().parents[2] / "agents"
KEYS = sorted(f"{p.parent.parent.name}/{p.parent.name}" for p in AGENTS.glob("*/*/agent.ir.yaml"))


def test_explanations_are_detailed_bullets_for_every_agent() -> None:
    headings = ["What this agent does", "Data you provide", "Figures it calculates", "Rules implementation",
                "Pipeline implementation", "Hybrid implementation", "What you need to add"]
    for key in KEYS:
        spec = load_spec(*key.split("/"))
        info = explanation(spec)
        assert [s["heading"] for s in info["sections"]] == headings, key
        bullets = [b for s in info["sections"] for b in s["bullets"]]
        assert len(bullets) >= 14 and info["words"] >= 250 and info["words"] == sum(len(b.split()) for b in bullets), key
        assert len(info["sections"][1]["bullets"]) == len(playbook_for(spec)["fields"]) + 2, key  # a bullet per data field


def test_role_notes_tell_each_role_what_to_connect_and_long_samples_are_shortened() -> None:
    finops = explanation(load_spec("10-finops-cloud-cost", "01-cloud-bill-anomaly"))["sections"][-1]["bullets"]
    assert any("billing exports" in b for b in finops)
    spec = load_spec("01-product-management", "01-prd-architect")
    long = spec.__class__(**{**spec.__dict__, "sample": "x" * 300})
    assert explanation(long)["sections"][0]["bullets"][1].count("...") == 1
    figures = explanation(load_spec("01-product-management", "02-roadmap-prioritizer"))["sections"][2]["bullets"]
    assert figures[0].startswith("RICE score = reach * impact")
    none = [e for k in KEYS if not PLAYBOOKS[k].get("metrics") for e in [explanation(load_spec(*k.split("/")))]][0]
    assert none["sections"][2]["bullets"] == ["This agent calculates no figures. Its output is the written deliverable."]

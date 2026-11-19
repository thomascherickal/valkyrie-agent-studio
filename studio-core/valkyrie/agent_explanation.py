"""A plain-language, bulleted explanation of each agent: what it does, the data it needs, and how each version works."""

from __future__ import annotations

from valkyrie.agent_impls import AgentSpec, playbook_for
from valkyrie.impl_notes import GENERIC_NOTES, ROLE_NOTES


def explanation(spec: AgentSpec) -> dict[str, object]:
    """A plain-language, bulleted explanation: what the agent does, the data it needs, how each version works."""
    book = playbook_for(spec)
    sample = spec.sample if len(spec.sample) <= 140 else spec.sample[:137] + "..."
    titles = ", ".join(s[0] for s in book["sections"])
    field_bullets = [
        f"{f['label']} ({'a number' if f['kind'] == 'number' else f['kind']})"
        + (f", for example: \"{f['example']}\"" if f["example"] else "")
        for f in book["fields"]
    ]
    figure_bullets = [f"{m['name']} = {m['formula']}" for m in book["metrics"]]
    sections: list[tuple[str, list[str]]] = [
        ("What this agent does", [
            f"{spec.name} ({spec.role}): {spec.description}",
            f"Its main input is \"{spec.input_key}\" (for example: \"{sample}\"). It returns \"{spec.output_key}\", "
            f"the tool name \"{spec.tool}\", the figures it calculated, what data is still missing, and a confidence score.",
            f"The deliverable has these sections: {titles}.",
        ]),
        ("Data you provide", [
            *field_bullets,
            "Each field is prefilled with an example so the agent runs straight away. Replace the examples with your real data.",
            "A field you leave blank is listed under \"Data still needed\", and every line that depends on it is left out of the report.",
        ]),
        ("Figures it calculates", figure_bullets or ["This agent calculates no figures. Its output is the written deliverable."]),
        ("Rules implementation", [
            "Fills the playbook with your data: the same input always gives the same report.",
            "Fast, offline and the easiest to read and change.",
        ]),
        ("Pipeline implementation", [
            "Runs six checked stages (validate, calculate, draft, coverage, review, compose) and reports what each did.",
            "Also scans your free-text input for the topics this agent looks for, and adds review notes for thin sections.",
        ]),
        ("Hybrid implementation", [
            "Drafts with the playbook, builds a prompt (role, required sections, your data, the draft) and calls call_model(prompt).",
            "Until you implement call_model it returns the draft and marks model_used false. A review step flags a dropped section or a changed figure.",
        ]),
        ("What you need to add", [
            *ROLE_NOTES.get(spec.role_id, GENERIC_NOTES),
            "Replace the guidance lines with your own standards and thresholds where they differ from the defaults.",
            "Implement call_model in the hybrid version with your own model and key, and keep the review step.",
            "Try a change: edit the code, Save changes, then Run with that implementation. Revert to original undoes it.",
        ]),
    ]
    out = [{"heading": heading, "bullets": bullets} for heading, bullets in sections]
    words = sum(len(b.split()) for s in out for b in s["bullets"])  # type: ignore[attr-defined]
    return {"title": spec.name, "sections": out, "words": words}

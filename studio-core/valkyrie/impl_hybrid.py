"""Template for the `hybrid` implementation: the playbook drafts, a model polishes, a review step checks."""

from valkyrie.impl_common import COMMON

DOC = r'''"""__NAME__ (__ROLE__): hybrid implementation.

The finished deliverable, optionally written by a model, always checked against your data.
  1. draft     fill the playbook with your data (as the rules implementation does).
  2. prompt    build a prompt: the role, the playbook as the required structure, your data and the draft.
  3. model     call `call_model(prompt)`. This is the part YOU must implement.
  4. fallback  until `call_model` returns text, the draft is the answer and `model_used` is False.
  5. review    check the answer keeps every section title and every calculated figure.

The sandbox has no network, so `call_model` returns None here. To use a real model, implement it in your own runtime
(for example Gemini 4 Hydrogen with thinking level low, key from your .env), keep the prompt, and keep `review` so an
answer that drops a section or changes a number is caught.

TODO(you): implement call_model, tune the prompt in build_prompt, and add your own checks in review.
"""
'''

BODY = r'''

def call_model(prompt: str) -> str | None:
    """TODO(you): send `prompt` to your model and return its text. Return None to use the drafted report."""
    return None


def build_prompt(values: dict[str, str], draft: str) -> str:
    structure = "\n".join("- " + block[0] for block in SPEC["sections"])
    data = "\n".join("- " + f["label"] + ": " + (values[f["key"]] or "(not supplied)") for f in SPEC["fields"])
    return (
        "You are " + SPEC["name"] + ", an agent for " + SPEC["role"] + ".\n" + SPEC["description"]
        + "\n\nWrite the " + SPEC["output_key"] + " as markdown with exactly these sections:\n" + structure
        + "\n\nMain input (" + SPEC["input_key"] + "):\n" + values["input"] + "\n\nData supplied:\n" + data
        + "\n\nDraft to improve. Keep every figure exactly as drafted:\n" + draft
    )


def review(answer: str, metrics: dict[str, str]) -> list[str]:
    problems = []
    low = answer.lower()
    for block in SPEC["sections"]:
        if block[0].lower() not in low:
            problems.append("The answer dropped the section: " + block[0])
    for name, figure in metrics.items():
        if figure not in answer:
            problems.append("The answer changed or dropped " + name + " (" + figure + ")")
    return problems


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    values = collect(payload)
    metrics = compute_metrics(values)
    missing, invalid = missing_fields(values), invalid_numbers(values)
    draft = render_report(build_sections(values), metrics, missing, invalid)
    prompt = build_prompt(values, draft)
    answer = call_model(prompt)
    model_used = answer is not None
    if answer is None:
        answer = draft
    problems = review(answer, metrics)
    done = completeness(missing, invalid)
    return {
        "agent_id": SPEC["agent_id"],
        "role": SPEC["role"],
        "tool_used": SPEC["tool"],
        "implementation": "hybrid",
        SPEC["output_key"]: answer,
        "model_used": model_used,
        "prompt": prompt,
        "review": problems,
        "metrics": metrics,
        "missing": missing,
        "completeness": done,
        "confidence": round(0.35 + 0.5 * done + (0.15 if model_used and not problems else 0), 2),
    }
'''

TEMPLATE = DOC + COMMON + BODY

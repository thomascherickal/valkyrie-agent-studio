"""Template for the `pipeline` implementation: validate, calculate, draft, check coverage, review, compose."""

from valkyrie.impl_common import COMMON

DOC = r'''"""__NAME__ (__ROLE__): pipeline implementation.

The same finished deliverable, produced in checked stages. Each stage reports what it did in `stages`.
  1. validate   read every field; flag blanks and numbers that cannot be read.
  2. calculate  compute the figures from your number fields.
  3. draft      fill the playbook sections with your data.
  4. coverage   scan your free-text input for the topics this agent looks for (SPEC["facets"]).
  5. review     flag thin sections, uncovered topics and unreadable numbers.
  6. compose    write the report with an "Input coverage" section and a "Review notes" section.

Choose it when you want the deliverable plus an audit trail of what was and was not covered.

TODO(you): add your own review rules in `review`, and the keywords your inputs use in SPEC["facets"].
"""
'''

BODY = r'''

def coverage(text: str) -> dict[str, bool]:
    low = text.lower()
    return {facet: any(w in low for w in words) for facet, words in SPEC["facets"].items()}


def review(sections: list[tuple[str, list[str]]], covered: dict[str, bool], invalid: list[str]) -> list[str]:
    notes = [title + ": only " + str(len(lines)) + " line(s). Supply more data." for title, lines in sections if len(lines) < 2]
    notes += ["Your input does not mention: " + facet for facet, hit in covered.items() if not hit]
    notes += ["Unreadable number in: " + label for label in invalid]
    return notes


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    stages: list[dict[str, Any]] = []
    values = collect(payload)
    missing, invalid = missing_fields(values), invalid_numbers(values)
    stages.append({"stage": "validate", "items": len(SPEC["fields"]) - len(missing), "problems": len(missing) + len(invalid)})
    metrics = compute_metrics(values)
    stages.append({"stage": "calculate", "items": len(metrics)})
    sections = build_sections(values)
    stages.append({"stage": "draft", "items": sum(len(lines) for _, lines in sections)})
    covered = coverage(values["input"])
    stages.append({"stage": "coverage", "items": sum(1 for hit in covered.values() if hit)})
    notes = review(sections, covered, invalid)
    stages.append({"stage": "review", "items": len(notes)})

    report = render_report(sections, metrics, missing, invalid)
    report += "\n\n## Input coverage\n" + "\n".join("- " + f + ": " + ("mentioned" if hit else "not mentioned") for f, hit in covered.items())
    if notes:
        report += "\n\n## Review notes\n" + "\n".join("- " + n for n in notes)
    stages.append({"stage": "compose", "items": len(report.splitlines())})
    done = completeness(missing, invalid)
    return {
        "agent_id": SPEC["agent_id"],
        "role": SPEC["role"],
        "tool_used": SPEC["tool"],
        "implementation": "pipeline",
        SPEC["output_key"]: report,
        "metrics": metrics,
        "missing": missing,
        "coverage": covered,
        "review": notes,
        "stages": stages,
        "completeness": done,
        "confidence": round(0.3 + 0.5 * done + 0.2 * (sum(covered.values()) / max(1, len(covered))), 2),
    }
'''

TEMPLATE = DOC + COMMON + BODY

"""Template for the `rules` implementation: fill the agent's playbook with your data. Deterministic, no model."""

from valkyrie.impl_common import COMMON

DOC = r'''"""__NAME__ (__ROLE__): rules implementation.

A finished deliverable from your data, with no model and no guessing.

How it works
  1. Read the main input and each data field from the payload.
  2. Fill every section of the playbook: lines that need data you did not supply are dropped.
  3. Calculate the figures (SPEC["metrics"]) from your number fields.
  4. List the data still needed, and score how complete your data is.

Deterministic and offline, so it is the easiest to read and to change. It applies the playbook as written and does
not interpret free text, so its quality is the quality of the data you give it and the rules in SPEC["sections"].

TODO(you): edit SPEC["sections"] to match your standards, and add the thresholds and decisions your team uses.
"""
'''

BODY = r'''

def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    values = collect(payload)
    metrics = compute_metrics(values)
    missing = missing_fields(values)
    invalid = invalid_numbers(values)
    done = completeness(missing, invalid)
    return {
        "agent_id": SPEC["agent_id"],
        "role": SPEC["role"],
        "tool_used": SPEC["tool"],
        "implementation": "rules",
        SPEC["output_key"]: render_report(build_sections(values), metrics, missing, invalid),
        "metrics": metrics,
        "missing": missing,
        "completeness": done,
        "confidence": round(0.4 + 0.55 * done, 2),
    }
'''

TEMPLATE = DOC + COMMON + BODY

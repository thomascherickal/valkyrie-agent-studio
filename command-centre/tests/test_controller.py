"""100% coverage tests for standalone command-centre module."""

import pytest

from valkyrie_cc import FleetController


def test_fleet_controller_lifecycle_and_admin() -> None:
    fc = FleetController()
    s1 = fc.start("01-prd-architect")
    assert s1.status == "running"

    fc.record_step("01-prd-architect", "tool:extract_requirements")
    assert "tool:extract_requirements" in s1.traces

    with pytest.raises(KeyError, match="not started"):
        fc.record_step("missing-agent", "noop")

    fc.start("02-pr-code-reviewer")
    fc.stop("01-prd-architect")
    assert fc.summary() == {"total": 2, "running": 1, "stopped": 1}

    assert fc.admin_stop_all() == 1
    assert fc.summary() == {"total": 2, "running": 0, "stopped": 2}


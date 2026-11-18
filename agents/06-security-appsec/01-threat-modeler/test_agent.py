"""100% coverage pytest suite for 01-threat-modeler."""

from agent import run_agent


def test_01_threat_modeler() -> None:
    res = run_agent({"architecture_desc": "Desktop Electron UI -> Local FastAPI -> "})
    assert res["agent_id"] == "01-threat-modeler"
    assert res["tool_used"] == "run_stride_analysis"
    assert "run_stride_analysis" in res["threat_matrix"]

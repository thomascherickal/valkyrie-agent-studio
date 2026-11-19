"""100% coverage pytest suite for 15-device-matrix-planner."""

from agent import run_agent


def test_15_device_matrix_planner() -> None:
    res = run_agent({"usage_analytics": "iOS 62% (17, 16), Android 38% (14, 13, 12); top 5 devices cover 41%; 4 devices in the lab"})
    assert res["agent_id"] == "15-device-matrix-planner"
    assert res["tool_used"] == "build_device_matrix"
    assert "build_device_matrix" in res["device_matrix"]

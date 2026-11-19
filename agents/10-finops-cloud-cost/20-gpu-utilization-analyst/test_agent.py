"""100% coverage pytest suite for 20-gpu-utilization-analyst."""

from agent import run_agent


def test_20_gpu_utilization_analyst() -> None:
    res = run_agent({"gpu_metrics": "64 GPUs, average utilization 31%, jobs queue for 3 hours at peak, 22% of GPU-hours are idle between jobs"})
    assert res["agent_id"] == "20-gpu-utilization-analyst"
    assert res["tool_used"] == "analyze_gpu_use"
    assert "analyze_gpu_use" in res["gpu_plan"]
